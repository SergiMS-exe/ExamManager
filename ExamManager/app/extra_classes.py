class Template_Group():
    name = ""
    examiner = ""
    id = 0
    totalParticipants = 0
    totalExams = 0

    def __init__(self, id, name, examiner, totalParticipants, totalExams):
        self.id=id
        self.name=name
        self.examiner=examiner
        self.totalExams=totalExams
        self.totalParticipants=totalParticipants
