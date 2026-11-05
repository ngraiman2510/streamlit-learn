# Student Grade Tracker

A small Streamlit app for entering student names and marks. It assigns a
letter grade and displays the entered students along with the average, highest,
and lowest marks.

## Requirements

- Python 3
- Streamlit

## Set up

From this directory, create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows, activate it with:

```powershell
.venv\Scripts\Activate.ps1
```

Install Streamlit:

```bash
python -m pip install streamlit
```

## Run

```bash
streamlit run grade_app.py
```

Streamlit opens the app in your browser. Stop the local server with `Ctrl+C`.
With the project setting enabled, saving changes to `grade_app.py` reruns the
app in the browser. If a rerun prompt appears, select **Rerun**.

## Grade scale and validation

The app accepts marks from **1 to 100** and assigns grades as follows:

| Mark | Grade |
|---|---|
| 90–100 | A |
| 80–89 | B |
| 70–79 | C |
| 60–69 | D |
| 1–59 | E |

Although the number input allows 0, the submission validation rejects marks
less than or equal to 0.

Student entries are kept in Streamlit session state while the app session is
active; they are not saved to a file or database.
