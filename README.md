# LangChain Explore

This repository documents my step-by-step journey through the LangChain documentation. Each example is a small experiment that helps me understand how LangChain, Deep Agents, model providers, tools, memory, and file-based workflows fit together.

## Learning Path

I am working through the documentation in the following order:

1. Set up Python and install the required LangChain packages.
2. Configure environment variables for the selected model provider.
3. Learn how chat models receive messages and return responses.
4. Build a basic agent with `create_deep_agent`.
5. Give the agent access to a local filesystem backend.
6. Upload and read structured data such as CSV files.
7. Ask the agent to analyze data and generate a plot.
8. Display the agent's analysis and results locally.
9. Add memory and checkpointing with LangGraph.
10. Continue experimenting with tools, middleware, tracing, and more advanced workflows.

## Current Example

[`Data_analysis.py`](Data_analysis.py) creates sample sales data, stores it in a local filesystem backend, and asks a Gemini-powered Deep Agent to analyze the CSV file and display the results.

The script uses a local backend instead of a LangSmith sandbox, so it does not need to publish the analysis to Slack or create a remote sandbox.

## Requirements

- Python 3.13 or later
- A Gemini API key
- The project's Python dependencies installed in your environment

Set the Gemini key in PowerShell before running the example:

```powershell
$env:GOOGLE_API_KEY = "your-gemini-api-key"
python Data_analysis.py
```

`GEMINI_API_KEY` can also be used instead of `GOOGLE_API_KEY`.

## Running the Example

From the project directory:

```powershell
python Data_analysis.py
```

The script creates the sample file at `data/sales_data.csv`, runs the agent, and prints the agent messages in the terminal.

## Security Notes

- Never commit API keys to the repository.
- Store keys in environment variables or a local `.env` file excluded by `.gitignore`.
- If a key is accidentally exposed, revoke it and create a new one immediately.

## Project Files

- `Data_analysis.py` - Current CSV analysis and Deep Agent experiment.
- `main.py` - Reserved for future examples.
- `data/` - Local data files used by the examples.

## Goal

The goal of this project is to learn LangChain by following its documentation carefully, testing each concept in a small working example, and recording what I learn as the project grows.
