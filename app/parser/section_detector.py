SECTION_KEYWORDS = {
    "summary": [
        "summary",
        "professional summary",
        "profile",
        "objective",
        "career objective",
        "about me"
    ],

    "education": [
        "education",
        "academics",
        "academic background",
        "qualification",
        "educational qualifications"
    ],

    "skills": [
        "skills",
        "technical skills",
        "core competencies",
        "technologies",
        "tech stack",
        "expertise"
    ],

    "projects": [
        "projects",
        "academic projects",
        "personal projects",
        "key projects"
    ],

    "experience": [
        "experience",
        "work experience",
        "professional experience",
        "employment",
        "internship",
        "internships"
    ],

    "achievements": [
        "achievements",
        "awards",
        "honors",
        "accomplishments"
    ],

    "certifications": [
        "certifications",
        "certificates",
        "licenses"
    ],

    "additional_information": [
        "additional information",
        "additional details",
        "personal information"
    ]
}
def normalize_heading(line:str)->str:
    
    return line.strip().lower().rstrip(":").rstrip("-")
def get_section_name(line:str):
    heading=normalize_heading(line)
    for section, keywords in SECTION_KEYWORDS.items():
        if heading in keywords:
            return section
    return None

def detect_sections(text:str):
    sections={section:[] for section in SECTION_KEYWORDS}
    current_section =None
    lines=text.splitlines()
    for line in lines:
        line=line.strip()
        if not line:
            continue
        section=get_section_name(line)
        if section:
            current_section=section
            continue
        if current_section:
            sections[current_section].append(line)
    for section in sections:
        sections[section]= "\n".join(sections[section])
    return sections