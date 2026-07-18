class DesktopComputerUseClient:
    def plan_actions(self, screen_elements: list, goal_action: str) -> dict:
        goal_lower = goal_action.lower()
        sequence = []
        # Find relevant elements matching goal keywords
        matched = [el for el in screen_elements if any(kw in el.lower() for kw in goal_lower.split())]
        if matched:
            sequence.append(f"FOCUS: Locate element '{matched[0]}' on screen")
            sequence.append(f"CLICK: Click on '{matched[0]}'")
            if "type" in goal_lower or "input" in goal_lower or "enter" in goal_lower:
                sequence.append(f"TYPE: Input required text in active field")
            sequence.append("VERIFY: Confirm action result matches expected outcome")
            confidence = round(min(len(matched) / len(screen_elements) + 0.5, 1.0), 2)
        else:
            sequence = ["SCAN: No matching elements found -- expanding search context"]
            confidence = 0.2
        return {"action_sequence": sequence, "confidence": confidence}
