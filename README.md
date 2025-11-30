# WHO Food Safety Navigator

This project hosts a set of AI agents designed to navigate and provide verdicts on food safety inquiries using the **Google Agent Development Kit (ADK)** and **Gemini API**.

## Prerequisites

- **Python 3.10+** installed on your system.
- A **Google Gemini API Key**.

## Setup

### 1. Clone the Repository

**Windows / MacOS / Linux:**
```bash
git clone [https://github.com/YOUR_USERNAME/Food-Safety-Navigator-Capstone.git](https://github.com/YOUR_USERNAME/Food-Safety-Navigator-Capstone.git)
cd who-food-safety-navigator
```

### 2. Set Up a Virtual Environment (Recommended)

It is best practice to use a virtual environment to manage dependencies.

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**MacOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

Install the required Python packages listed in requirements.txt:

```bash
pip install -r requirements.txt
```

### 4. Configuration

This project requires environment variables to function (specifically for the AI models).

Create a file named .env in the root directory of the project.
Add your Google API key to it:

```bash
GOOGLE_API_KEY=<your-gemini-api-key>
```

### Usage

To start the agent system, run the main script:

```bash
python main.py
```

Follow the on-screen prompts to interact with the Food Safety Navigator.

