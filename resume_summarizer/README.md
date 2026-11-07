# Resume Summarizer

A small Python script that reads a resume from a text file and uses the Gemini API to write a 3-point summary for a recruiter.

## What it does
- Reads `resume.txt`
- Sends the text to the Gemini API with a clear prompt (role, task, format, and "use only the given text")
- Prints a 3-bullet summary
- Retries with waiting if the API gives an error

## Tech used
- Python
- Google Gemini API (`google-genai`)
- `python-dotenv` for the API key

## How to run
1. Install the libraries:

   ```
   pip install google-genai python-dotenv
   ```

2. Create a file named `.env` in this folder and add your key:

   ```
   GEMINI_API_KEY=your_key_here
   ```

   Never share this file or push it to GitHub.

3. Put your resume text in `resume.txt` (do not add phone number or email if the repo is public).

4. Run:

   ```
   python summarizer.py
   ```

## Example output
* Holds a B.E. in Computer Science (2022) with technical skills in Python, SQL, Pandas, NumPy, Machine Learning, and NLP.
* Completed a 3-month Data Science and Analytics Internship, building time series forecasting and a chatbot.
* Completed a 3-month AIML with Data Science Internship focused on data preprocessing and predictive models.


## What I learned
- How to call an LLM API from Python and keep the key safe in a `.env` file
- How a clear prompt with a role and rules gives a better summary
- How to handle API errors with retry and exponential backoff
- That free API plans have daily limits (rate limit error 429)

## Next steps
- Return the result as JSON (name, skills, experience)
- Read PDF resumes
- Compare a resume with a job description