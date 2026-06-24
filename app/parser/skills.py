SKILL_CATEGORIES = {
    "languages": [
        "languages",
        "programming languages",
        "language",
        "programming"
    ],

    "frameworks_tools": [
        "frameworks",
        "frameworks/tools",
        "frameworks & tools",
        "libraries",
        "libraries/frameworks",
        "web technologies",
        "web"
    ],

    "tools": [
        "tools",
        "developer tools",
        "software",
        "platforms"
    ],

    "databases": [
        "databases",
        "database",
        "database systems"
    ],
    "ai/ml":[
        "ai/ml",
        "artificial intelligence",
        "machine learning",
        "ai",
        "ml"
    ],
    "core_concepts": [
        "core concepts",
        "concepts",
        "computer science fundamentals",
        "fundamentals",
        "cs fundamentals"
    ]
}
from .section_detector import normalize_heading
def get_skill_category(category: str):
    category = normalize_heading(category)

    for key, keywords in SKILL_CATEGORIES.items():
        if category in keywords:
            return key

    return None

def parse_skills(text:str):
    skills ={
        category:[]
        for category in SKILL_CATEGORIES
    }

    for line in text.splitlines():
        line=line.strip()
        if not line:
            continue
        if ":" not in line:
            continue
        raw_category, raw_values = line.split(":", 1)

        category=get_skill_category(raw_category)
        values=[
            value.strip()
            for value in raw_values.split(",")
            if value.strip()
        ]
        if category:
            skills[category]=values
    return skills