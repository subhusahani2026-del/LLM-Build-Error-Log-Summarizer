\# LLM-Based Build/Error-Log Summarizer



\## 1. Project Overview

This project uses a Large Language Model (LLM) to analyze software build logs and generate simple explanations of errors with possible solutions.



\## 2. Technologies Used

\- Python

\- Ollama

\- Llama 3.2

\- Requests Library



\## 3. Features

\- Reads build and error log files.

\- Identifies build failures.

\- Detects important errors.

\- Explains errors in simple language.

\- Suggests possible solutions.

\- Saves generated summaries into a text file.



\## 4. Project Structure

```text

LLM-Build-Error-Log-Summarizer/

├── app.py

├── log\_analyzer.py

├── requirements.txt

├── README.md

├── .gitignore

├── logs/

│   └── sample.log

└── output/

&#x20;   └── summary.txt

```



\## 5. Installation



Install Python dependencies:



```bash

pip install -r requirements.txt

```



Install Ollama and download the model:



```bash

ollama pull llama3.2

```



\## 6. Execution



Run the application:



```bash

python app.py

```



Enter the log file path:



```text

logs/sample.log

```



\## 7. Output

The application generates:

\- Build status

\- Main errors

\- Explanation of errors

\- Possible solutions



The generated summary is saved in `output/summary.txt`.



\## 8. Conclusion

This project demonstrates how Large Language Models can simplify software debugging by analyzing build logs, identifying errors, explaining their causes, and recommending solutions.



