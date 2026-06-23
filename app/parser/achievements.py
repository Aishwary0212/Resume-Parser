def parse_achievements(text: str):
    achievements = []

    for line in text.splitlines():
        line = line.strip().lstrip("•").strip(
            
        )

        if line:
            achievements.append(line)


    return achievements