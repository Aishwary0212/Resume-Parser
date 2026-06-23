import re

def parse_education(text: str):
    education = []
    lines = [line.strip() for line in text.splitlines() if line.strip()]

    current = None

    for line in lines:

        # Start a new education record
        if current is None:
            current = {
                "institution": line,
                "duration": "",
                "year": "",
                "degree": "",
                "grade": ""
            }
            continue

        # Year
        if re.fullmatch(r"\d{4}", line):
            current["year"] = line

        # Duration
        elif "-" in line or "-" in line:
            current["duration"] = line

        # Grade (percentage/CGPA)
        elif re.fullmatch(r"\d+(\.\d+)?%?", line):
            current["grade"] = line
            education.append(current)
            current = None

        # Degree/Class
        else:
            current["degree"] = line

    return education