import json
from re import sub
import numpy as np
import pandas as pd

data_breakdown = {
    "MCQ": {
        "Primary 1": {
            "topics": {
                "Whole Numbers": {
                    "question_count": 0,
                    "difficulty_1": 0,
                    "difficulty_2": 0,
                    "difficulty_3": 0,
                    "subtopics": {
                        "Numbers Up To 100": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        },
                        "Addition And Subtraction": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        },
                        "Multiplication And Division": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        },
                        "Money": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        }
                    }
                },
                "Measurement": {
                    "question_count": 0,
                    "difficulty_1": 0,
                    "difficulty_2": 0,
                    "difficulty_3": 0,
                    "subtopics": {
                        "Length": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        },
                        "Time": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        }
                    }
                },
                "Geometry": {
                    "question_count": 0,
                    "difficulty_1": 0,
                    "difficulty_2": 0,
                    "difficulty_3": 0,
                    "subtopics": {
                        "2D Shapes": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        }
                    }
                },
                "Data Representation And Interpretation": {
                    "question_count": 0,
                    "difficulty_1": 0,
                    "difficulty_2": 0,
                    "difficulty_3": 0,
                    "subtopics": {
                        "Picture Graphs": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        }
                    }
                }
            }
        },
        "Primary 2": {
            "topics": {
                "Whole Numbers": {
                    "question_count": 0,
                    "difficulty_1": 0,
                    "difficulty_2": 0,
                    "difficulty_3": 0,
                    "subtopics": {
                        "Numbers Up To 1000": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        },
                        "Addition And Subtraction": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        },
                        "Multiplication And Division": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        }
                    }
                },
                "Fractions": {
                    "question_count": 0,
                    "difficulty_1": 0,
                    "difficulty_2": 0,
                    "difficulty_3": 0,
                    "subtopics": {
                        "Fraction Of A Whole": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        },
                        "Addition And Subtraction": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        }
                    }
                },
                "Money": {
                    "question_count": 0,
                    "difficulty_1": 0,
                    "difficulty_2": 0,
                    "difficulty_3": 0,
                    "subtopics": {
                        "Money": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        }
                    }
                },
                "Measurement": {
                    "question_count": 0,
                    "difficulty_1": 0,
                    "difficulty_2": 0,
                    "difficulty_3": 0,
                    "subtopics": {
                        "Length, Mass And Volume": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        },
                        "Time": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        }
                    }
                },
                "Geometry": {
                    "question_count": 0,
                    "difficulty_1": 0,
                    "difficulty_2": 0,
                    "difficulty_3": 0,
                    "subtopics": {
                        "2D Shapes": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        },
                        "3D Shapes": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        }
                    }
                },
                "Data Representation And Interpretation": {
                    "question_count": 0,
                    "difficulty_1": 0,
                    "difficulty_2": 0,
                    "difficulty_3": 0,
                    "subtopics": {
                        "Picture Graphs With Scales": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        }
                    }
                }
            }
        },
        "Primary 3": {
            "topics": {
                "Whole Numbers": {
                    "question_count": 0,
                    "difficulty_1": 0,
                    "difficulty_2": 0,
                    "difficulty_3": 0,
                    "subtopics": {
                        "Numbers Up To 10 000": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        },
                        "Addition And Subtraction": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        },
                        "Multiplication And Division": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        }
                    }
                }, 
                "Fractions": {
                    "question_count": 0,
                    "difficulty_1": 0,
                    "difficulty_2": 0,
                    "difficulty_3": 0,
                    "subtopics": {
                        "Equivalent Fractions": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        },
                        "Addition And Subtraction": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        }
                    }
                },
                "Money": {
                    "question_count": 0,
                    "difficulty_1": 0,
                    "difficulty_2": 0,
                    "difficulty_3": 0,
                    "subtopics": {
                        "Money": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        }
                    }
                },
                "Measurement": {
                    "question_count": 0,
                    "difficulty_1": 0,
                    "difficulty_2": 0,
                    "difficulty_3": 0,
                    "subtopics": {
                        "Length, Mass And Volume": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        },
                        "Time": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        }
                    }
                },
                "Area And Volume": {
                    "question_count": 0,
                    "difficulty_1": 0,
                    "difficulty_2": 0,
                    "difficulty_3": 0,
                    "subtopics": {
                        "Area And Perimeter": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        }
                    }
                },
                "Geometry": {
                    "question_count": 0,
                    "difficulty_1": 0,
                    "difficulty_2": 0,
                    "difficulty_3": 0,
                    "subtopics": {
                        "Angles": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        },
                        "Perpendicular And Parallel Lines": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        }
                    }
                },
                "Data Representation And Interpretation": {
                    "question_count": 0,
                    "difficulty_1": 0,
                    "difficulty_2": 0,
                    "difficulty_3": 0,
                    "subtopics": {
                        "Bar Graphs": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        }
                    }
                }
            }
        },
        "Primary 4": {
            "topics": {
                "Whole Numbers": {
                    "question_count": 0,
                    "difficulty_1": 0,
                    "difficulty_2": 0,
                    "difficulty_3": 0,
                    "subtopics": {
                        "Numbers Up To 100 000": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        },
                        "Factors And Multiples": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        },
                        "Four Operations": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        }
                    }
                },
                "Fractions": {
                    "question_count": 0,
                    "difficulty_1": 0,
                    "difficulty_2": 0,
                    "difficulty_3": 0,
                    "subtopics": {
                        "Mixed Numbers And Improper Fractions": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        },
                        "Fraction Of A Set Of Objects": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        },
                        "Addition And Subtraction": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        }
                    }
                },
                "Decimals": {
                    "question_count": 0,
                    "difficulty_1": 0,
                    "difficulty_2": 0,
                    "difficulty_3": 0,
                    "subtopics": {
                        "Decimals Up To 3 Decimal Places": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        },
                        "Addition And Subtraction": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        },
                        "Multiplication And Division": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        }
                    }
                },
                "Measurement": {
                    "question_count": 0,
                    "difficulty_1": 0,
                    "difficulty_2": 0,
                    "difficulty_3": 0,
                    "subtopics": {
                        "Time": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        }
                    }
                },
                "Area And Volume": {
                    "question_count": 0,
                    "difficulty_1": 0,
                    "difficulty_2": 0,
                    "difficulty_3": 0,
                    "subtopics": {
                        "Area And Perimeter": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        }
                    }
                },
                "Geometry": {
                    "question_count": 0,
                    "difficulty_1": 0,
                    "difficulty_2": 0,
                    "difficulty_3": 0,
                    "subtopics": {
                        "Angles": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        },
                        "Rectangle And Square": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        },
                        "Line Symmetry": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        }
                    }
                },
                "Data Representation And Interpretation": {
                    "question_count": 0,
                    "difficulty_1": 0,
                    "difficulty_2": 0,
                    "difficulty_3": 0,
                    "subtopics": {
                        "Tables And Line Graphs": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        }
                    }
                }
            }
        },
        "Primary 5": {
            "topics": {
                "Whole Numbers": {
                    "question_count": 0,
                    "difficulty_1": 0,
                    "difficulty_2": 0,
                    "difficulty_3": 0,
                    "subtopics": {
                        "Numbers Up To 10 Million": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        },
                        "Four Operations": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        }
                    }
                },
                "Fractions": {
                    "question_count": 0,
                    "difficulty_1": 0,
                    "difficulty_2": 0,
                    "difficulty_3": 0,
                    "subtopics": {
                        "Fraction And Division": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        },
                        "Four Operations": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        }
                    }
                },
                "Decimals": {
                    "question_count": 0,
                    "difficulty_1": 0,
                    "difficulty_2": 0,
                    "difficulty_3": 0,
                    "subtopics": {
                        "Four Operations": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        }
                    }
                },
                "Percentage": {
                    "question_count": 0,
                    "difficulty_1": 0,
                    "difficulty_2": 0,
                    "difficulty_3": 0,
                    "subtopics": {
                        "Percentage": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        }
                    }
                },
                "Ratio": {
                    "question_count": 0,
                    "difficulty_1": 0,
                    "difficulty_2": 0,
                    "difficulty_3": 0,
                    "subtopics": {
                        "Ratio": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        }
                    }
                },
                "Rate And Speed": {
                    "question_count": 0,
                    "difficulty_1": 0,
                    "difficulty_2": 0,
                    "difficulty_3": 0,
                    "subtopics": {
                        "Rate": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        }
                    }
                },
                "Area And Volume": {
                    "question_count": 0,
                    "difficulty_1": 0,
                    "difficulty_2": 0,
                    "difficulty_3": 0,
                    "subtopics": {
                        "Area Of Triangle": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        },
                        "Volume Of Cube And Cuboid": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        }
                    }
                },
                "Geometry": {
                    "question_count": 0,
                    "difficulty_1": 0,
                    "difficulty_2": 0,
                    "difficulty_3": 0,
                    "subtopics": {
                        "Angles": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        },
                        "Triangle": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        },
                        "Parallelogram, Rhombus And Trapezium": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        }
                    }
                },
                "Data Analysis": {
                    "question_count": 0,
                    "difficulty_1": 0,
                    "difficulty_2": 0,
                    "difficulty_3": 0,
                    "subtopics": {
                        "Average Of A Set Of Data": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        }
                    }
                }
            }
        },
        "Primary 6": {
            "topics": {
                "Fractions": {
                    "question_count": 0,
                    "difficulty_1": 0,
                    "difficulty_2": 0,
                    "difficulty_3": 0,
                    "subtopics": {
                        "Four Operations": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        }
                    }
                },
                "Percentage": {
                    "question_count": 0,
                    "difficulty_1": 0,
                    "difficulty_2": 0,
                    "difficulty_3": 0,
                    "subtopics": {
                        "Percentage": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        }
                    }
                },
                "Ratio": {
                    "question_count": 0,
                    "difficulty_1": 0,
                    "difficulty_2": 0,
                    "difficulty_3": 0,
                    "subtopics": {
                        "Ratio": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        }
                    }
                },
                "Rate And Speed": {
                    "question_count": 0,
                    "difficulty_1": 0,
                    "difficulty_2": 0,
                    "difficulty_3": 0,
                    "subtopics": {
                        "Distance, Time And Speed": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        }
                    }
                },
                "Algebra": {
                    "question_count": 0,
                    "difficulty_1": 0,
                    "difficulty_2": 0,
                    "difficulty_3": 0,
                    "subtopics": {
                        "Algebra": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        }
                    }
                },
                "Area And Volume": {
                    "question_count": 0,
                    "difficulty_1": 0,
                    "difficulty_2": 0,
                    "difficulty_3": 0,
                    "subtopics": {
                        "Area And Circumference Of Circle": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        },
                        "Volume Of Cube And Cuboid": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        }
                    }
                },
                "Geometry": {
                    "question_count": 0,
                    "difficulty_1": 0,
                    "difficulty_2": 0,
                    "difficulty_3": 0,
                    "subtopics": {
                        "Special Quadrilaterals ": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        },
                        "Nets": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        }
                    }
                },
                "Data Representation And Interpretation": {
                    "question_count": 0,
                    "difficulty_1": 0,
                    "difficulty_2": 0,
                    "difficulty_3": 0,
                    "subtopics": {
                        "Pie Charts": {
                            "question_count": 0,
                            "difficulty_1": 0,
                            "difficulty_2": 0,
                            "difficulty_3": 0
                        }
                    }
                }
            }
        }
    }
}

uuids_with_issues = []

p1_whole_numbers_easy_uuids = ""
p1_whole_numbers_normal_uuids = ""

with open('math_new.txt', 'r', encoding='utf-8') as math_questions:
    questions = json.load(math_questions)["data"]["questions"]
    
    count = 0
    for question in questions:
        uuid = question["uuid"]
        question_type = question["type"]
        subject = question["subject"][0]
        level = question["level"][0]
        topic_name = question["topics"][0]
        subtopic_name = question["subtopics"][0] if len(question["subtopics"]) > 0 else ""
        difficultyLevel = question["difficultyLevel"][0] if len(question["difficultyLevel"]) > 0 else ""

        mcqs = data_breakdown[question_type]
        
        # Incrementing count
        if (level == "Primary 1" or level == "Primary 2" or level == "Primary 3" or level == "Primary 4" or level == "Primary 5" or level == "Primary 6"):
            mcq_topics = mcqs[level]["topics"]
            
            try:
                if len(topic_name) > 0 and topic_name in mcq_topics:
                    mcq_topics[topic_name]["question_count"] = mcq_topics[topic_name]["question_count"] + 1
                    mcq_topics[topic_name]["difficulty_1"] = mcq_topics[topic_name]["difficulty_1"] + 1 if difficultyLevel == "1" else mcq_topics[topic_name]["difficulty_1"]
                    mcq_topics[topic_name]["difficulty_2"] = mcq_topics[topic_name]["difficulty_2"] + 1 if difficultyLevel == "2" else mcq_topics[topic_name]["difficulty_2"]
                    mcq_topics[topic_name]["difficulty_3"] = mcq_topics[topic_name]["difficulty_3"] + 1 if difficultyLevel == "3" else mcq_topics[topic_name]["difficulty_3"]
                
                if len(subtopic_name) > 0 and topic_name in mcq_topics and subtopic_name in mcq_topics[topic_name]["subtopics"]:
                    print(topic_name)
                    print(subtopic_name)
                    mcq_topics[topic_name]["subtopics"][subtopic_name]["question_count"] = mcq_topics[topic_name]["subtopics"][subtopic_name]["question_count"] + 1
                    mcq_topics[topic_name]["subtopics"][subtopic_name]["difficulty_1"] = mcq_topics[topic_name]["subtopics"][subtopic_name]["difficulty_1"] + 1 if difficultyLevel == "1" else mcq_topics[topic_name]["subtopics"][subtopic_name]["difficulty_1"]
                    mcq_topics[topic_name]["subtopics"][subtopic_name]["difficulty_2"] = mcq_topics[topic_name]["subtopics"][subtopic_name]["difficulty_2"] + 1 if difficultyLevel == "2" else mcq_topics[topic_name]["subtopics"][subtopic_name]["difficulty_2"]
                    mcq_topics[topic_name]["subtopics"][subtopic_name]["difficulty_3"] = mcq_topics[topic_name]["subtopics"][subtopic_name]["difficulty_3"] + 1 if difficultyLevel == "3" else mcq_topics[topic_name]["subtopics"][subtopic_name]["difficulty_3"]
            except:
                uuids_with_issues.append("UUID = " + uuid + " ;\tlevel = " + level + " ;\ttopic=" + topic_name + " ;\tsubtopic = " + subtopic_name + " ;\tdifficultyLevel = " + difficultyLevel)
            

print(data_breakdown)

print(len(uuids_with_issues))

for uuid in uuids_with_issues:
    print(uuid)



## Primary 1 : Topic Breakdown ##

series_primary_1_topics = data_breakdown["MCQ"]["Primary 1"]["topics"].keys()

series_primary_1_number_of_questions_per_topic = []
series_primary_1_number_of_questions_per_topic_difficulty_1 = []
series_primary_1_number_of_questions_per_topic_difficulty_2 = []
series_primary_1_number_of_questions_per_topic_difficulty_3 = []
for topic_name in data_breakdown["MCQ"]["Primary 1"]["topics"].keys():
    series_primary_1_number_of_questions_per_topic.append(data_breakdown["MCQ"]["Primary 1"]["topics"][topic_name]["question_count"])
    series_primary_1_number_of_questions_per_topic_difficulty_1.append(data_breakdown["MCQ"]["Primary 1"]["topics"][topic_name]["difficulty_1"])
    series_primary_1_number_of_questions_per_topic_difficulty_2.append(data_breakdown["MCQ"]["Primary 1"]["topics"][topic_name]["difficulty_2"])
    series_primary_1_number_of_questions_per_topic_difficulty_3.append(data_breakdown["MCQ"]["Primary 1"]["topics"][topic_name]["difficulty_3"])


df_primary_1 = pd.DataFrame()
df_primary_1["Topic"] = series_primary_1_topics
df_primary_1["Count (App)"] = series_primary_1_number_of_questions_per_topic
df_primary_1["Difficulty_1"] = series_primary_1_number_of_questions_per_topic_difficulty_1
df_primary_1["Difficulty_2"] = series_primary_1_number_of_questions_per_topic_difficulty_2
df_primary_1["Difficulty_3"] = series_primary_1_number_of_questions_per_topic_difficulty_3

## Primary 1 : Sub-Topic Breakdown ##

## TODO: IN-PROGRESS -> Topic Breakdown for all levels
df_master = pd.DataFrame()

academic_level_list = []
topic_list = []
topic_question_count_list = []
topic_difficulty_1_question_count_list = []
topic_difficulty_2_question_count_list = []
topic_difficulty_3_question_count_list = []

subtopic_list = []
subtopic_question_count_list = []
subtopic_difficulty_1_question_count_list = []
subtopic_difficulty_2_question_count_list = []
subtopic_difficulty_3_question_count_list = []

for academic_level in data_breakdown["MCQ"].keys():
    for topic_name in data_breakdown["MCQ"][academic_level]["topics"].keys():
        
        topic_question_count = data_breakdown["MCQ"][academic_level]["topics"][topic_name]["question_count"]
        topic_difficulty_1_question_count = data_breakdown["MCQ"][academic_level]["topics"][topic_name]["difficulty_1"]
        topic_difficulty_2_question_count = data_breakdown["MCQ"][academic_level]["topics"][topic_name]["difficulty_2"]
        topic_difficulty_3_question_count = data_breakdown["MCQ"][academic_level]["topics"][topic_name]["difficulty_3"]
        
        for subtopic_name in data_breakdown["MCQ"][academic_level]["topics"][topic_name]["subtopics"]:
            subtopic_question_count = data_breakdown["MCQ"][academic_level]["topics"][topic_name]["subtopics"][subtopic_name]["question_count"]
            subtopic_difficulty_1_question_count = data_breakdown["MCQ"][academic_level]["topics"][topic_name]["subtopics"][subtopic_name]["difficulty_1"]
            subtopic_difficulty_2_question_count = data_breakdown["MCQ"][academic_level]["topics"][topic_name]["subtopics"][subtopic_name]["difficulty_2"]
            subtopic_difficulty_3_question_count = data_breakdown["MCQ"][academic_level]["topics"][topic_name]["subtopics"][subtopic_name]["difficulty_3"]

            # TODO: Create a data-frame here that comprise of all topic and subtopics
            academic_level_list.append(academic_level)

            topic_list.append(topic_name)
            topic_question_count_list.append(topic_question_count)
            topic_difficulty_1_question_count_list.append(topic_difficulty_1_question_count)
            topic_difficulty_2_question_count_list.append(topic_difficulty_2_question_count)
            topic_difficulty_3_question_count_list.append(topic_difficulty_3_question_count)

            subtopic_list.append(subtopic_name)
            subtopic_question_count_list.append(subtopic_question_count)
            subtopic_difficulty_1_question_count_list.append(subtopic_difficulty_1_question_count)
            subtopic_difficulty_2_question_count_list.append(subtopic_difficulty_2_question_count)
            subtopic_difficulty_3_question_count_list.append(subtopic_difficulty_3_question_count)

df_master["Academic Level"] = academic_level_list
df_master["Topic"] = topic_list
df_master["Topic Question Count"] = topic_question_count_list
df_master["Topic Difficulty 1 Question Count"] = topic_difficulty_1_question_count_list
df_master["Topic Difficulty 2 Question Count"] = topic_difficulty_2_question_count_list
df_master["Topic Difficulty 3 Question Count"] = topic_difficulty_3_question_count_list

df_master["Subtopic"] = subtopic_list
df_master["Subtopic Question Count"] = subtopic_question_count_list
df_master["Subtopic Difficulty 1 Question Count"] = subtopic_difficulty_1_question_count_list
df_master["Subtopic Difficulty 2 Question Count"] = subtopic_difficulty_2_question_count_list
df_master["Subtopic Difficulty 3 Question Count"] = subtopic_difficulty_3_question_count_list

print(df_master)
df_master.to_excel('math_content_breakdown.xlsx', sheet_name='Master')