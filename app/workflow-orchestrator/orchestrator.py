import requests

agent_url = "http://agent-service.agentic-ai.svc.cluster.local:8080/run"

payload = {"input": "Start workflow"}

print("Triggering agent...")
response = requests.post(agent_url, json=payload)

print("Agent response:", response.json())
