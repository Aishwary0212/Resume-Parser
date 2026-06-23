











def parse_summary(text: str):
    return text
from .section_detector import detect_sections
from .skills import parse_skills
from .projects import parse_projects
from .education import parse_education
from .experience import parse_experience
from .achievements import parse_achievements
from .certifications import parse_certifications
from .additional_info import parse_additional_information













def parse_resume(text: str):
    sections = detect_sections(text)

    return {
        "summary": parse_summary(sections["summary"]),
        "education": parse_education(sections["education"]),
        "skills": parse_skills(sections["skills"]),
        "projects": parse_projects(sections["projects"]),
        "experience": parse_experience(sections["experience"]),
        "achievements": parse_achievements(sections["achievements"]),
        "certifications": parse_certifications(sections["certifications"]),
        "additional_information": parse_additional_information(
            sections["additional_information"]
        ),
    }