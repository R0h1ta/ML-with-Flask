import pandas as pd
screen_time = [2, 4, 6]
productive_hours = [5, 6, 7]
student_name = ["Madhan", "Ram", "Ro"]
dict1 = {
    "student_name": student_name,
    "productive_hours": productive_hours,
    "screen_time": screen_time
    }
    df = pd.DataFrame(dict1)
    print(df)
            