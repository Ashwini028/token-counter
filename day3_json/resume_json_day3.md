Ashwini Dhomne. BE in Computer Science and Engineering ,2022
Skills: Python, Sql, AIML
Worked as Data Science and Analytics Intern for 6 month.
built a time series forcasting projects using ARIMA.

## Prompt 1 (JSON with schema)

Prompt: "You are a resume parser... Return ONLY valid JSON... Use exactly these keys: name, skills, experience_years, education."

Output:

```json
{
  "name": "Ashwini Dhomne",
  "skills": ["Python", "SQL", "AIML"],
  "experience_years": 0.5,
  "education": "B.E. in Computer Science, 2022"
}
```

Observations:
- Only valid JSON came back, with all four keys.
- experience_years was calculated correctly (6 months = 0.5).
- The model also added ARIMA and Time Series Forecasting to skills from the project line. My prompt did not say whether to use only the "Skills" line.

## Prompt 2 (stricter rule + example output)

Changes: added a rule "take skills ONLY from the Skills line" and one example output (few-shot).

Output:

```json
{
  "name": "Ashwini Dhomne",
  "skills": ["Python", "SQL", "AIML"],
  "experience_years": 0.5,
  "education": "B.E. in Computer Science, 2022"
}
```

Observations:
- Valid JSON, only JSON, all four keys present.
- Skills stayed limited to what was written in the "Skills" line, with no extra skills from projects (compared to Prompt 1).
- (CHOOSE ONE LINE)
  A: I used my own resume text, so the details match my resume.

## Summary

- A clear schema (exact keys), "return ONLY valid JSON" and "use null if missing" gave valid JSON with the right keys in both prompts.

- Prompt 1 added extra skills from the project line (ARIMA, Time Series Forecasting), because I did not say where to take skills from.

- Prompt 2 added a stricter rule and one example output, and the skills stayed limited to the "Skills" line.

- Lesson: for structured output, be specific about each field, give an example, and validate the JSON in code.
- 