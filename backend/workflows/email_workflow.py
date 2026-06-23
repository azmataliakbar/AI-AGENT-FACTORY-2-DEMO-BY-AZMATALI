from agents.email_agent import process_email


def run_email_workflow(email_text: str):
    """Orchestrate the full email processing workflow."""
    steps, result = process_email(email_text)
    return {
        "steps": steps,
        "result": result,
        "summary": {
            "total_steps": len(steps),
            "automated_steps": len(steps),
            "human_steps": 1,  # Manager approval only
        },
    }
