def parse_certifications(text: str):
    certifications=[]

    for line in text.splitlines():
        line=line.strip().lstrip("•").strip()
        if line:
            certifications.append(line)
    return certifications