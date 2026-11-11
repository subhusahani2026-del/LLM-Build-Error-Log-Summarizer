
import os
from log_analyzer import summarize_log

def main():

    print("\n====================================")
    print(" LLM BUILD ERROR LOG SUMMARIZER")
    print("====================================")

    file_path = input("\nEnter log file path: ")

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            log_text = file.read()

        if not log_text.strip():
            print("The log file is empty.")
            return

        print("\nAnalyzing log using LLM...\n")

        summary = summarize_log(log_text)

        print("\n========== BUILD SUMMARY ==========\n")
        print(summary)

        os.makedirs("output", exist_ok=True)

        with open("output/summary.txt", "w", encoding="utf-8") as file:
            file.write(summary)

        print("\nSummary saved successfully!")

    except FileNotFoundError:
        print("\nError: Log file not found.")

if __name__ == "__main__":
    main()
