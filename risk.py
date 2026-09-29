def check_risk(attendance, marks):

    if attendance < 60 or marks < 30:
        return "YOU SHOULD CONSIDER DEATH RISK"

    elif attendance < 75 or marks < 60:
        return "MEDIUM RISK"

    else:
        return "LOW RISK"