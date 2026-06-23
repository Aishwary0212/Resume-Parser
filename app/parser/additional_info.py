ADDITIONAL_INFO_CATEGORIES = {
    "languages": [
        "languages",
        "language"
    ],
    "soft_skills": [
        "soft skills",
        "softskills",
        "skills"
    ]
}
from .section_detector import normalize_heading


from .section_detector import normalize_heading

ADDITIONAL_INFO_CATEGORIES = {
    "languages": [
        "languages",
        "language"
    ],
    "soft_skills": [
        "soft skills",
        "softskills",
        "skills"
    ]
}

def get_additional_info_category(category: str):
    category = normalize_heading(category)

    for key, keywords in ADDITIONAL_INFO_CATEGORIES.items():
        if category in keywords:
            return key

    return None
def parse_additional_information(text: str):
    info = {
        category: []
        for category in ADDITIONAL_INFO_CATEGORIES
    }

    for line in text.splitlines():

        line = line.strip()

        if not line:
            continue

        if ":" not in line:
            continue

        raw_category, raw_values = line.split(":", 1)

        category = get_additional_info_category(raw_category)

        values = [
            value.strip()
            for value in raw_values.split(",")
            if value.strip()
        ]

        if category:
            info[category] = values

    return info