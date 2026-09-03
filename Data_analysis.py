import os

import csv
import io

from deepagents.backends import FilesystemBackend

if not (os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")):
    raise RuntimeError(
        "Set GOOGLE_API_KEY or GEMINI_API_KEY before running this script."
    )

# Create sample sales data
data = [
    ["Date", "Product", "Units Sold", "Revenue"],
    ["2025-08-01", "Widget A", 10, 250],
    ["2025-08-02", "Widget B", 5, 125],
    ["2025-08-03", "Widget A", 7, 175],
    ["2025-08-04", "Widget C", 3, 90],
    ["2025-08-05", "Widget B", 8, 200],
]

# Convert to CSV bytes
text_buf = io.StringIO()
writer = csv.writer(text_buf)
writer.writerows(data)
csv_bytes = text_buf.getvalue().encode("utf-8")
text_buf.close()

# Store the input locally so no LangSmith sandbox is required.
backend = FilesystemBackend(root_dir=".")
backend.upload_files([("data/sales_data.csv", csv_bytes)])

from langchain_core.utils.uuid import uuid7

from deepagents import create_deep_agent
from langchain.agents.middleware import TodoListMiddleware
from langgraph.checkpoint.memory import InMemorySaver

checkpointer = InMemorySaver()

agent = create_deep_agent(
    model="google_genai:gemini-3.5-flash",
    backend=backend,
    checkpointer=checkpointer,
    middleware=[TodoListMiddleware()],
)

thread_id = str(uuid7())
config = {"configurable": {"thread_id": thread_id}}

input_message = {
    "role": "user",
    "content": (
        "Analyze ./data/sales_data.csv in the current dir and generate a beautiful plot. "
        "When finished, display your analysis and the plot here."
    ),
}
stream = agent.stream(
    {"messages": [input_message]},
    config,
    stream_mode="values",
)
for snapshot in stream:
    snapshot["messages"][-1].pretty_print()
    
