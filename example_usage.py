from client import DesktopComputerUseClient
client = DesktopComputerUseClient()
result = client.plan_actions(
    screen_elements=["File menu", "Save button", "Text editor area", "Search bar", "Close button"],
    goal_action="click save button"
)
print(f"Confidence: {result['confidence']}")
for step in result["action_sequence"]:
    print(f"  -> {step}")
