import json
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
        level = question["level"][0]
        topic = question["topics"][0]
        subtopic = question["subtopics"][0] if len(question["subtopics"]) > 0 else ""
        difficultyLevel = question["difficultyLevel"][0] if len(question["difficultyLevel"]) > 0 else ""

        mcqs = data_breakdown[question_type]
        
        # Incrementing count
        if (level == "Primary 1" or level == "Primary 2" or level == "Primary 3" or level == "Primary 4" or level == "Primary 5" or level == "Primary 6"):
            mcq_topics = mcqs[level]["topics"]
            
            try:
                if len(topic) > 0 and topic in mcq_topics:
                    mcq_topics[topic]["question_count"] = mcq_topics[topic]["question_count"] + 1
                    mcq_topics[topic]["difficulty_1"] = mcq_topics[topic]["difficulty_1"] + 1 if difficultyLevel == "1" else mcq_topics[topic]["difficulty_1"]
                    mcq_topics[topic]["difficulty_2"] = mcq_topics[topic]["difficulty_2"] + 1 if difficultyLevel == "2" else mcq_topics[topic]["difficulty_2"]
                    mcq_topics[topic]["difficulty_3"] = mcq_topics[topic]["difficulty_3"] + 1 if difficultyLevel == "3" else mcq_topics[topic]["difficulty_3"]
                
                if len(subtopic) > 0 and topic in mcq_topics and subtopic in mcq_topics[topic]["subtopics"]:
                    print(topic)
                    print(subtopic)
                    mcq_topics[topic]["subtopics"][subtopic]["question_count"] = mcq_topics[topic]["subtopics"][subtopic]["question_count"] + 1
                    mcq_topics[topic]["subtopics"][subtopic]["difficulty_1"] = mcq_topics[topic]["subtopics"][subtopic]["difficulty_1"] + 1 if difficultyLevel == "1" else mcq_topics[topic]["subtopics"][subtopic]["difficulty_1"]
                    mcq_topics[topic]["subtopics"][subtopic]["difficulty_2"] = mcq_topics[topic]["subtopics"][subtopic]["difficulty_2"] + 1 if difficultyLevel == "2" else mcq_topics[topic]["subtopics"][subtopic]["difficulty_2"]
                    mcq_topics[topic]["subtopics"][subtopic]["difficulty_3"] = mcq_topics[topic]["subtopics"][subtopic]["difficulty_3"] + 1 if difficultyLevel == "3" else mcq_topics[topic]["subtopics"][subtopic]["difficulty_3"]
            except:
                uuids_with_issues.append("UUID = " + uuid + " ;\tlevel = " + level + " ;\ttopic=" + topic + " ;\tsubtopic = " + subtopic + " ;\tdifficultyLevel = " + difficultyLevel)
            

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
for topic in data_breakdown["MCQ"]["Primary 1"]["topics"].keys():
    series_primary_1_number_of_questions_per_topic.append(data_breakdown["MCQ"]["Primary 1"]["topics"][topic]["question_count"])
    series_primary_1_number_of_questions_per_topic_difficulty_1.append(data_breakdown["MCQ"]["Primary 1"]["topics"][topic]["difficulty_1"])
    series_primary_1_number_of_questions_per_topic_difficulty_2.append(data_breakdown["MCQ"]["Primary 1"]["topics"][topic]["difficulty_2"])
    series_primary_1_number_of_questions_per_topic_difficulty_3.append(data_breakdown["MCQ"]["Primary 1"]["topics"][topic]["difficulty_3"])


df_primary_1 = pd.DataFrame()
df_primary_1["Topic"] = series_primary_1_topics
df_primary_1["Count (App)"] = series_primary_1_number_of_questions_per_topic
df_primary_1["Difficulty_1"] = series_primary_1_number_of_questions_per_topic_difficulty_1
df_primary_1["Difficulty_2"] = series_primary_1_number_of_questions_per_topic_difficulty_2
df_primary_1["Difficulty_3"] = series_primary_1_number_of_questions_per_topic_difficulty_3

## Primary 1 : Sub-Topic Breakdown ##


print(df_primary_1)