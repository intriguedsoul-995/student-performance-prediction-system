def calculate_performance(attendance, study_hours, marks):
    score = (
        attendance * 0.3
        + marks * 0.5
        + study_hours * 2
    )

    if score > 100:
        score = 100

    return score