def route_message(text=None, has_image=False):
    tenancy_keywords = ["rent", "deposit", "eviction", "landlord", "notice", "lease", "agreement", "contract", "tenant", "owner"]

    if has_image:
        return "agent1"
    elif text:
        if any(keyword in text.lower() for keyword in tenancy_keywords):
            return "agent2"
        else:
            return "clarify"
    else:
        return "clarify"
