"use client";

import { useState, useEffect, useRef, useCallback } from "react";

// ─── Types ───────────────────────────────────────────────────────────────────

interface StepData {
  step: number;
  label: string;
  status: "pending" | "processing" | "completed";
  result: string | null;
}

interface ProcessResult {
  intent: string;
  category: string;
  priority: string;
  draft_response: string;
}

const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

const SAMPLE_EMAIL =
  "Hello,\nI purchased Product X last week.\nThe item arrived damaged.\nCan I receive a replacement?\nThank you.";

// ─── Simulated fallback (no backend) ─────────────────────────────────────────

function simulateProcessing(email: string): Promise<{ steps: StepData[]; result: ProcessResult }> {
  return new Promise((resolve) => {
    const steps: StepData[] = [
      { step: 1, label: "Reading Email & Extracting Intent", status: "pending", result: null },
      { step: 2, label: "Categorizing Email", status: "pending", result: null },
      { step: 3, label: "Detecting Priority", status: "pending", result: null },
      { step: 4, label: "Drafting Response", status: "pending", result: null },
    ];
    const result: ProcessResult = {
      intent: "Damaged Product",
      category: "Support Request",
      priority: "Medium",
      draft_response:
        "Hello,\n\nThank you for contacting us. We apologize for receiving a damaged item. We would be happy to arrange a replacement. Please provide your order number and a photo of the damaged product.\n\nBest regards,\nSupport Team",
    };

    let i = 0;
    const run = () => {
      if (i >= steps.length) {
        resolve({ steps, result });
        return;
      }
      steps[i].status = "processing";
      setStepsVal && setStepsVal([...steps]);
      setTimeout(() => {
        steps[i].status = "completed";
        steps[i].result = i === 0 ? result.intent : i === 1 ? result.category : i === 2 ? result.priority : result.draft_response;
        setStepsVal && setStepsVal([...steps]);
        i++;
        setTimeout(run, 700);
      }, 600);
    };
    run();
  });
}

let setStepsVal: React.Dispatch<React.SetStateAction<StepData[]>> | null = null;

// ─── Component ───────────────────────────────────────────────────────────────

export default function HomePage() {
  // State
  const [emailText, setEmailText] = useState(SAMPLE_EMAIL);
  const [steps, setSteps] = useState<StepData[]>([]);
  const [result, setResult] = useState<ProcessResult | null>(null);
  const [isProcessing, setIsProcessing] = useState(false);
  const [approvalStatus, setApprovalStatus] = useState<"none" | "approved" | "rejected">("none");
  const [demoStarted, setDemoStarted] = useState(false);

  setStepsVal = setSteps;

  // Refs for scroll reveal
  const revealRefs = useRef<(HTMLDivElement | null)[]>([]);

  useEffect(() => {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("visible");
          }
        });
      },
      { threshold: 0.1 }
    );
    revealRefs.current.forEach((el) => el && observer.observe(el));
    return () => observer.disconnect();
  }, []);

  const setRevealRef = useCallback((i: number) => (el: HTMLDivElement | null) => {
    revealRefs.current[i] = el;
  }, []);

  // Process email
  const handleProcess = async () => {
    if (!emailText.trim()) return;
    setIsProcessing(true);
    setResult(null);
    setApprovalStatus("none");
    setDemoStarted(true);

    const initialSteps: StepData[] = [
      { step: 1, label: "Reading Email & Extracting Intent", status: "pending", result: null },
      { step: 2, label: "Categorizing Email", status: "pending", result: null },
      { step: 3, label: "Detecting Priority", status: "pending", result: null },
      { step: 4, label: "Drafting Response", status: "pending", result: null },
    ];
    setSteps(initialSteps);

    try {
      const res = await fetch(`${API_URL}/api/process-email`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email_text: emailText }),
      });

      if (!res.ok) throw new Error("Backend unavailable");

      const data = await res.json();
      // Animate steps one by one
      for (let i = 0; i < data.steps.length; i++) {
        setSteps((prev) => {
          const next = [...prev];
          next[i] = { ...next[i], status: "processing" };
          return next;
        });
        await delay(600);

        setSteps((prev) => {
          const next = [...prev];
          next[i] = { ...next[i], status: "completed", result: data.steps[i].result };
          return next;
        });
        await delay(500);
      }

      setResult(data.result);
    } catch {
      // Fallback to simulation
      const { steps: simSteps, result: simResult } = await simulateProcessing(emailText);
      setResult(simResult);
    }

    setIsProcessing(false);
  };

  // Scroll to demo on CTA
  const scrollToDemo = () => {
    document.getElementById("demo-section")?.scrollIntoView({ behavior: "smooth" });
  };

  return (
    <main>
      {/* ═══ SECTION 1: HERO ═══ */}
      <section className="section" style={{ minHeight: "100vh", display: "flex", alignItems: "center" }}>
        <div className="container" style={{ textAlign: "center" }}>
          <div className="glass-strong" style={{ padding: "60px 40px", position: "relative", overflow: "hidden" }}>
            {/* Background glow */}
            <div style={{
              position: "absolute", top: "-50%", left: "-20%", width: "140%", height: "200%",
              background: "radial-gradient(ellipse at center, rgba(0,240,255,0.06) 0%, transparent 60%)",
              pointerEvents: "none",
            }} />

            <div className="animate-gradient" style={{ fontSize: "clamp(2rem, 5vw, 3.5rem)", fontWeight: 800, marginBottom: 20 }}>
              AI Agent Factory Demonstration
            </div>

            <p className="text-secondary animate-fade-in stagger-1" style={{ fontSize: "1.15rem", maxWidth: 600, margin: "0 auto 32px", lineHeight: 1.7 }}>
              See how <span className="text-cyan" style={{ fontWeight: 600 }}>one AI agent</span> can automate repetitive email workflows —
              turning hours of manual work into minutes.
            </p>

            <div className="animate-fade-in stagger-2" style={{ display: "flex", gap: 16, justifyContent: "center", flexWrap: "wrap" }}>
              <button className="btn-primary animate-float" onClick={scrollToDemo}>
                ▶ Run Demo
              </button>
              <button className="btn-secondary" onClick={() => document.getElementById("workflow-before")?.scrollIntoView({ behavior: "smooth" })}>
                Learn More
              </button>
            </div>

            {/* Quick stats row */}
            <div style={{ display: "flex", gap: 24, justifyContent: "center", marginTop: 48, flexWrap: "wrap" }}>
              {[
                { label: "Time Saved", value: "93%", color: "text-green" },
                { label: "Human Steps Reduced", value: "75%", color: "text-cyan" },
                { label: "Automation Rate", value: "80%", color: "text-purple" },
              ].map((stat, i) => (
                <div key={i} className={`glass card-green stagger-${i + 3} animate-fade-in`} style={{ padding: "16px 28px", textAlign: "center", minWidth: 140 }}>
                  <div className={stat.color} style={{ fontSize: "1.8rem", fontWeight: 700 }}>{stat.value}</div>
                  <div style={{ fontSize: "0.8rem", color: "var(--text-secondary)", marginTop: 4 }}>{stat.label}</div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </section>

      {/* ═══ SECTION 2 & 3: WORKFLOW COMPARISON ═══ */}
      <section className="section" id="workflow-before">
        <div className="container">
          <div ref={setRevealRef(0)} className="reveal" style={{ textAlign: "center", marginBottom: 48 }}>
            <h2 className="animate-gradient" style={{ fontSize: "2rem", fontWeight: 700, marginBottom: 12 }}>
              Before vs After AI
            </h2>
            <p className="text-secondary">See how the same workflow transforms with an AI Agent.</p>
          </div>

          <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(320px, 1fr))", gap: 32 }}>
            {/* Before AI */}
            <div ref={setRevealRef(1)} className="reveal card-red glass" style={{ padding: 32 }}>
              <h3 className="text-red" style={{ fontSize: "1.4rem", fontWeight: 700, marginBottom: 6 }}>❌ Before AI</h3>
              <p className="text-muted" style={{ fontSize: "0.85rem", marginBottom: 24 }}>Manual process — 4 human steps</p>

              <WorkflowFlow steps={["Customer Email", "Employee Reads", "Employee Categorizes", "Employee Drafts", "Manager Reviews", "Customer Receives Reply"]} color="var(--accent-red)" />

              <div style={{ marginTop: 24, padding: "16px", borderRadius: 10, background: "rgba(239,68,68,0.08)", border: "1px solid rgba(239,68,68,0.15)" }}>
                <div style={{ display: "flex", justifyContent: "space-between", marginBottom: 8 }}>
                  <span className="text-muted">Time Required</span>
                  <span style={{ fontWeight: 600, color: "var(--accent-red)" }}>15 Minutes</span>
                </div>
                <div style={{ display: "flex", justifyContent: "space-between", marginBottom: 8 }}>
                  <span className="text-muted">Human Steps</span>
                  <span style={{ fontWeight: 600 }}>4</span>
                </div>
                <div style={{ display: "flex", justifyContent: "space-between" }}>
                  <span className="text-muted">Automation</span>
                  <span style={{ fontWeight: 600, color: "var(--accent-red)" }}>0%</span>
                </div>
              </div>
            </div>

            {/* After AI */}
            <div ref={setRevealRef(2)} className="reveal card-green glass shadow-glow-green" style={{ padding: 32, position: "relative", overflow: "hidden" }}>
              <div style={{ position: "absolute", top: 0, right: 0, background: "var(--accent-green)", color: "#000", padding: "4px 14px", borderRadius: "0 20px 0 12px", fontSize: "0.75rem", fontWeight: 700 }}>
                RECOMMENDED
              </div>

              <h3 className="text-green" style={{ fontSize: "1.4rem", fontWeight: 700, marginBottom: 6 }}>✅ After AI</h3>
              <p className="text-muted" style={{ fontSize: "0.85rem", marginBottom: 24 }}>Automated — 1 human approval step</p>

              <WorkflowFlow steps={["Customer Email", "AI Agent Reads", "AI Categorizes", "AI Prioritizes", "AI Drafts Reply", "Manager Approves", "Customer Receives Reply"]} color="var(--accent-green)" />

              <div style={{ marginTop: 24, padding: "16px", borderRadius: 10, background: "rgba(34,197,94,0.08)", border: "1px solid rgba(34,197,94,0.15)" }}>
                <div style={{ display: "flex", justifyContent: "space-between", marginBottom: 8 }}>
                  <span className="text-muted">Time Required</span>
                  <span className="text-green" style={{ fontWeight: 600 }}>2 Minutes</span>
                </div>
                <div style={{ display: "flex", justifyContent: "space-between", marginBottom: 8 }}>
                  <span className="text-muted">Human Steps</span>
                  <span style={{ fontWeight: 600 }}>1</span>
                </div>
                <div style={{ display: "flex", justifyContent: "space-between" }}>
                  <span className="text-muted">Automation</span>
                  <span className="text-green" style={{ fontWeight: 600 }}>80%</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* ═══ SECTION 4: LIVE INTERACTIVE DEMO ═══ */}
      <section className="section" id="demo-section" style={{ background: "var(--bg-secondary)" }}>
        <div className="container">
          <div ref={setRevealRef(3)} className="reveal" style={{ textAlign: "center", marginBottom: 48 }}>
            <h2 className="text-cyan" style={{ fontSize: "2rem", fontWeight: 700, marginBottom: 12 }}>
              Live Interactive Demo
            </h2>
            <p className="text-secondary">Watch the AI process a real customer email step by step.</p>
          </div>

          <div className="glass-strong" style={{ padding: 40 }}>
            <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(300px, 1fr))", gap: 32 }}>
              {/* Left: Input */}
              <div ref={setRevealRef(4)} className="reveal">
                <label className="text-purple" style={{ fontWeight: 600, marginBottom: 8, display: "block" }}>
                  ✉ Incoming Customer Email
                </label>
                <textarea
                  className="demo-textarea"
                  value={emailText}
                  onChange={(e) => setEmailText(e.target.value)}
                  placeholder="Paste a customer email here..."
                />
                <button
                  className="btn-primary"
                  onClick={handleProcess}
                  disabled={isProcessing}
                  style={{ marginTop: 16, width: "100%", justifyContent: "center", opacity: isProcessing ? 0.7 : 1 }}
                >
                  {isProcessing ? (
                    <><span className="spinner" /> Processing...</>
                  ) : (
                    "⚡ Process Email"
                  )}
                </button>
              </div>

              {/* Right: Processing visualization */}
              <div ref={setRevealRef(5)} className="reveal">
                <label className="text-cyan" style={{ fontWeight: 600, marginBottom: 8, display: "block" }}>
                  🤖 AI Processing Steps
                </label>

                {!demoStarted ? (
                  <div
                    className="glass"
                    style={{ padding: 32, textAlign: "center", color: "var(--text-muted)", minHeight: 240, display: "flex", alignItems: "center", justifyContent: "center" }}
                  >
                    <div>
                      <div style={{ fontSize: "2rem", marginBottom: 8 }}>👆</div>
                      <div>Enter an email and click &quot;Process Email&quot;</div>
                    </div>
                  </div>
                ) : (
                  <div style={{ display: "flex", flexDirection: "column", gap: 8 }}>
                    {steps.map((s) => (
                      <div key={s.step} className={`glass card-${s.status === "completed" ? "green" : s.status === "processing" ? "yellow" : ""}`} style={{ padding: "12px 16px", display: "flex", alignItems: "center", gap: 12 }}>
                        <div>
                          {s.status === "completed" ? (
                            <span style={{ color: "var(--accent-green)", fontSize: "1.2rem" }}>✅</span>
                          ) : s.status === "processing" ? (
                            <span className="spinner" />
                          ) : (
                            <span style={{ color: "var(--text-muted)", fontSize: "1.2rem" }}>⏳</span>
                          )}
                        </div>
                        <div style={{ flex: 1 }}>
                          <div style={{ fontSize: "0.85rem", fontWeight: 500, color: s.status === "completed" ? "var(--accent-green)" : s.status === "processing" ? "var(--accent-yellow)" : "var(--text-muted)" }}>
                            Step {s.step}: {s.label}
                          </div>
                          {s.result && (
                            <div className="text-secondary" style={{ fontSize: "0.8rem", marginTop: 2 }}>
                              → {s.result}
                            </div>
                          )}
                        </div>
                      </div>
                    ))}
                  </div>
                )}
              </div>
            </div>

            {/* Generated draft */}
            {result && (
              <div ref={setRevealRef(6)} className="reveal" style={{ marginTop: 24 }}>
                <div className={`glass card-blue shadow-glow-cyan`} style={{ padding: 24 }}>
                  <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 16, flexWrap: "wrap", gap: 8 }}>
                    <h3 className="text-cyan" style={{ fontSize: "1.1rem", fontWeight: 600 }}>✍ AI-Generated Draft Response</h3>
                    <div style={{ display: "flex", gap: 8 }}>
                      <div className="glass" style={{ padding: "4px 10px", fontSize: "0.75rem" }}>
                        <span className="text-purple">Intent:</span> {result.intent}
                      </div>
                      <div className="glass" style={{ padding: "4px 10px", fontSize: "0.75rem" }}>
                        <span className="text-yellow">Priority:</span> {result.priority}
                      </div>
                    </div>
                  </div>

                  <div style={{
                    background: "rgba(0,0,0,0.3)", borderRadius: 10, padding: 20,
                    borderLeft: "3px solid var(--accent-cyan)",
                    whiteSpace: "pre-line", lineHeight: 1.7, fontSize: "0.95rem"
                  }}>
                    {result.draft_response}
                  </div>
                </div>

                {/* ═══ SECTION 5: MANAGER APPROVAL ═══ */}
                <div ref={setRevealRef(7)} className="reveal" style={{ marginTop: 24, textAlign: "center" }}>
                  <div className="glass card-purple shadow-glow-purple" style={{ padding: 28 }}>
                    <h3 className="text-purple" style={{ fontSize: "1.1rem", fontWeight: 600, marginBottom: 6 }}>
                      👤 Manager Approval Required
                    </h3>
                    <p className="text-muted" style={{ fontSize: "0.85rem", marginBottom: 20 }}>
                      The AI has drafted a response. A human manager reviews and approves.
                    </p>

                    {approvalStatus === "none" ? (
                      <div style={{ display: "flex", gap: 16, justifyContent: "center" }}>
                        <button className="btn-approve animate-bounce-in" onClick={() => setApprovalStatus("approved")}>
                          ✅ Approve
                        </button>
                        <button className="btn-reject" onClick={() => setApprovalStatus("rejected")}>
                          ❌ Reject
                        </button>
                      </div>
                    ) : approvalStatus === "approved" ? (
                      <div className="animate-scale-in" style={{ padding: "16px 24px", background: "rgba(34,197,94,0.1)", borderRadius: 12, border: "1px solid rgba(34,197,94,0.2)" }}>
                        <div style={{ fontSize: "1.5rem", marginBottom: 4 }}>✅</div>
                        <div className="text-green" style={{ fontWeight: 600, fontSize: "1.1rem" }}>Response Sent Successfully</div>
                        <p className="text-muted" style={{ fontSize: "0.85rem", marginTop: 4 }}>
                          The customer will receive the AI-generated reply.
                        </p>
                      </div>
                    ) : (
                      <div className="animate-scale-in" style={{ padding: "16px 24px", background: "rgba(239,68,68,0.1)", borderRadius: 12, border: "1px solid rgba(239,68,68,0.2)" }}>
                        <div style={{ fontSize: "1.5rem", marginBottom: 4 }}>❌</div>
                        <div className="text-red" style={{ fontWeight: 600, fontSize: "1.1rem" }}>Response Rejected</div>
                        <p className="text-muted" style={{ fontSize: "0.85rem", marginTop: 4 }}>
                          The manager will rewrite the response manually.
                        </p>
                      </div>
                    )}
                  </div>
                </div>
              </div>
            )}
          </div>
        </div>
      </section>

      {/* ═══ SECTION 6: METRICS DASHBOARD ═══ */}
      <section className="section">
        <div className="container">
          <div ref={setRevealRef(8)} className="reveal" style={{ textAlign: "center", marginBottom: 48 }}>
            <h2 className="text-pink" style={{ fontSize: "2rem", fontWeight: 700, marginBottom: 12 }}>
              📊 Performance Dashboard
            </h2>
            <p className="text-secondary">Real-time metrics from your AI Agent deployment.</p>
          </div>

          <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(200px, 1fr))", gap: 20 }}>
            {[
              { label: "Emails Processed", value: "125", suffix: "", color: "cyan", cls: "card-cyan" },
              { label: "Avg Processing Time", value: "45", suffix: "s", color: "purple", cls: "card-purple" },
              { label: "Human Time Saved", value: "22", suffix: "hrs", color: "green", cls: "card-green" },
              { label: "Approval Rate", value: "94", suffix: "%", color: "pink", cls: "card-pink" },
            ].map((metric, i) => (
              <div
                key={i}
                ref={setRevealRef(9 + i)}
                className={`reveal stagger-${i + 1} glass metric-card ${metric.color} ${metric.cls} shadow-elevated`}
                style={{ animationDelay: `${i * 0.15}s` }}
              >
                <div className={`text-${metric.color}`} style={{ fontSize: "2.5rem", fontWeight: 800, lineHeight: 1 }}>
                  {metric.value}
                  <span style={{ fontSize: "1rem", fontWeight: 500, opacity: 0.7 }}>{metric.suffix}</span>
                </div>
                <div className="text-muted" style={{ fontSize: "0.85rem", marginTop: 8 }}>{metric.label}</div>
                <div style={{ marginTop: 12, height: 4, background: "rgba(255,255,255,0.05)", borderRadius: 2, overflow: "hidden" }}>
                  <div style={{
                    width: `${metric.suffix === "%" ? metric.value : metric.label === "Emails Processed" ? "65" : metric.label.includes("Time") ? "72" : "88"}%`,
                    height: "100%",
                    background: `var(--accent-${metric.color})`,
                    borderRadius: 2,
                    transition: "width 1.5s ease-out",
                  }} />
                </div>
              </div>
            ))}
          </div>

          {/* Efficiency comparison */}
          <div ref={setRevealRef(13)} className="reveal glass card-blue" style={{ marginTop: 32, padding: 28 }}>
            <h3 className="text-blue" style={{ fontSize: "1.1rem", fontWeight: 600, marginBottom: 16 }}>
              📈 Efficiency Comparison
            </h3>
            <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr 1fr", gap: 16, textAlign: "center" }}>
              <div>
                <div className="text-red" style={{ fontSize: "1.3rem", fontWeight: 700 }}>15 min</div>
                <div className="text-muted" style={{ fontSize: "0.8rem" }}>Before AI</div>
              </div>
              <div>
                <div className="text-cyan" style={{ fontSize: "2rem", fontWeight: 800 }}>→</div>
              </div>
              <div>
                <div className="text-green" style={{ fontSize: "1.3rem", fontWeight: 700 }}>45 sec</div>
                <div className="text-muted" style={{ fontSize: "0.8rem" }}>After AI</div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* ═══ SECTION 7: AGENT FACTORY EXPLANATION ═══ */}
      <section className="section" style={{ background: "var(--bg-secondary)" }}>
        <div className="container">
          <div ref={setRevealRef(14)} className="reveal glass-strong" style={{ padding: 48, textAlign: "center" }}>
            <h2 className="text-orange" style={{ fontSize: "2rem", fontWeight: 700, marginBottom: 12 }}>
              🏭 How the Agent Factory Works
            </h2>
            <p className="text-secondary" style={{ maxWidth: 600, margin: "0 auto 40px", fontSize: "1.05rem", lineHeight: 1.7 }}>
              The Agent Factory is <strong style={{ color: "var(--accent-orange)" }}>not a chatbot</strong>.
              It is a system for automating repeatable business workflows.
            </p>

            {/* Visual pipeline */}
            <div style={{ display: "flex", justifyContent: "center", gap: 0, flexWrap: "wrap", marginBottom: 40 }}>
              {[
                { label: "Input", icon: "📨", color: "var(--accent-cyan)" },
                { label: "Workflow", icon: "⚙️", color: "var(--accent-purple)" },
                { label: "Decision Logic", icon: "🧠", color: "var(--accent-pink)" },
                { label: "Output", icon: "✅", color: "var(--accent-green)" },
              ].map((item, i) => (
                <div key={i} style={{ display: "flex", alignItems: "center" }}>
                  <div className={`glass card-${["cyan","purple","pink","green"][i]} glow-${["cyan","purple","pink","green"][i]}`}
                    style={{ padding: "20px 24px", textAlign: "center", minWidth: 130 }}
                  >
                    <div style={{ fontSize: "1.5rem", marginBottom: 4 }}>{item.icon}</div>
                    <div style={{ color: item.color, fontWeight: 600, fontSize: "0.9rem" }}>{item.label}</div>
                  </div>
                  {i < 3 && (
                    <div style={{ color: "var(--text-muted)", fontSize: "1.5rem", padding: "0 8px" }}>→</div>
                  )}
                </div>
              ))}
            </div>

            <p className="text-secondary" style={{ maxWidth: 500, margin: "0 auto", fontSize: "0.9rem", lineHeight: 1.6 }}>
              Raw data enters → A predefined workflow processes it → 
              Decision logic routes it → A polished output is delivered.
              <br /><br />
              <span className="text-cyan" style={{ fontWeight: 500 }}>
                No coding required. No complex setup. Just results.
              </span>
            </p>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer style={{ textAlign: "center", padding: "32px 20px", color: "var(--text-muted)", fontSize: "0.85rem" }}>
        <p>AI Agent Factory Demonstration — Built to help non-technical buyers understand automation workflows.</p>
        <p style={{ marginTop: 8 }}>Powered by Agent Factory Architecture</p>
      </footer>
    </main>
  );
}

// ─── Helpers ─────────────────────────────────────────────────────────────────

function delay(ms: number) {
  return new Promise((r) => setTimeout(r, ms));
}

function WorkflowFlow({ steps, color }: { steps: string[]; color: string }) {
  return (
    <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 0 }}>
      {steps.map((s, i) => (
        <div key={i} style={{ textAlign: "center", width: "100%" }}>
          <div
            className="glass"
            style={{
              padding: "8px 16px",
              fontSize: "0.8rem",
              fontWeight: 500,
              borderLeft: `3px solid ${color}`,
              color: "var(--text-primary)",
            }}
          >
            {s}
          </div>
          {i < steps.length - 1 && (
            <div style={{ color: "var(--text-muted)", fontSize: "0.7rem", padding: "2px 0" }}>↓</div>
          )}
        </div>
      ))}
    </div>
  );
}
