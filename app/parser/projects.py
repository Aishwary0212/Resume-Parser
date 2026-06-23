def parse_projects(text: str):
    projects = []

    lines = [line.strip() for line in text.splitlines() if line.strip()]

    current_project = None
    i = 0

    while i < len(lines):

        line=lines[i]
        if (
            i + 1 < len(lines)
            and "," in lines[i + 1]
            and not line.startswith("•")
            and not lines[i + 1].startswith("•")
        ):
            if current_project:
                projects.append(current_project)

            title = line
            subtitle = ""
            if "(" in line and ")" in line:
                title, subtitle = line.split("(", 1)
                subtitle = subtitle.rstrip(")").strip()
            current_project = {
                "title": title.strip(),
                "subtitle": subtitle,
                "technologies": [
                    tech.strip()
                    for tech in lines[i + 1].split(",")
                    if tech.strip()
                ],
                "description": []
            }

            i += 2
            continue
        if current_project and line.startswith("•"):

            current_project["description"].append(
                line.lstrip("•").strip()
            )
        elif current_project and current_project["description"]:

            current_project["description"][-1] += " " + line

        i += 1

    if current_project:
        projects.append(current_project)

    return projects