import json

data_breakdown = {
    "MCQ": {
        "Primary 1": {
            "topics": [
                {
                    "topic": "Whole Numbers",
                    "question_count": 0,
                    "difficulty_1": 0,
                    "difficulty_2": 0,
                    "difficulty_3": 0,
                    "subtopics": [
                        {
                            "subtopic": "Numbers Up To 100",
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        },
                        {
                            "subtopic": "Addition And Subtraction",
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        },
                        {
                            "subtopic": "Multiplication And Division",
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        },
                        {
                            "subtopic": "Money",
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        }
                    ]
                },
                {
                    "topic": "Measurement",
                    "question_count": 0,
                    "difficulty_1": 0,
                    "difficulty_2": 0,
                    "difficulty_3": 0,
                    "subtopics": [
                        {
                            "subtopic": "Length",
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        },
                        {
                            "subtopic": "Time",
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        }
                    ]
                },
                {
                    "topic": "Geometry",
                    "question_count": 0,
                    "difficulty_1": 0,
                    "difficulty_2": 0,
                    "difficulty_3": 0,
                    "subtopics": [
                        {
                            "subtopic": "2D Shapes",
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        }
                    ]
                }
            ]
        }
    }
}



with open('math.txt', 'r', encoding='utf-8') as math_questions:
    questions = json.load(math_questions)["data"]["questions"]
    
    count = 0
    for question in questions:
        uuid = question["uuid"]
        question_type = question["type"]
        level = question["level"][0]
        topic = question["topics"][0]
        subtopic = question["subtopics"][0] if len(question["subtopics"]) > 0 else ""
        difficultyLevel = question["difficultyLevel"][0] if len(question["difficultyLevel"]) > 0 else ""

        # << To be deleted
        print("UUID = " + uuid + " ;\tlevel = " + level + " ;\ttopic=" + topic + " ;\tsubtopic = " + subtopic + " ;\tdifficultyLevel = " + difficultyLevel)
        print(count)
        count = count + 1
        # To be deleted >>

        for data_topic in data_breakdown[question_type][level]:
            if (data_topic["topic"] == topic):
                print("SAME TOPIC")
            

