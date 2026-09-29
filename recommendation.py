def give_recommendation(attendance, study_hours, marks):

    recommendations = []

    if attendance < 75:
        recommendations.append("Improve your attendance to at least 75%.")

    if study_hours < 4:
        recommendations.append("Study for at least 4 hours daily.")
    

    if marks < 60:
        recommendations.append("Practice more questions and revise weak topics.")

    if marks >= 60 and marks < 80:
        recommendations.append("Focus on improving your marks to above 80%.")    

    if marks >= 80:
        recommendations.append("Maintain your performance and aim for excllence.")    

    if marks < 40:
        recommendations.append("Seek help from teachers or tutors to improve your marks.")

    if marks >= 40 and marks < 60: 
        recommendations.append("Focus on improving your marks to above 60%.")

    if marks < 20 :
        recommendations.append("you are fail you should consider suicide.")       


    if len(recommendations) == 0:
        recommendations.append("Keep following your current study routine.")

    return recommendations