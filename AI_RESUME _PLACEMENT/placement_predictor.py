import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Load Dataset
df = pd.read_csv("dataset/placement_dataset.csv")

# Features
X = df[[
    "cgpa",
    "communication",
    "backlogs",
    "internships",
    "projects",
    "technical_skills",
    "certifications",
    "workshops",
    "coding_score"
]]

# Target
y = df["placement"]

# Train Model
model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

model.fit(X, y)


def predict_placement(
    cgpa,
    communication,
    backlogs,
    internships,
    projects,
    technical_skills,
    certifications,
    workshops,
    coding_score
):
    input_df = pd.DataFrame([{
        "cgpa": cgpa,
        "communication": communication,
        "backlogs": backlogs,
        "internships": internships,
        "projects": projects,
        "technical_skills": technical_skills,
        "certifications": certifications,
        "workshops": workshops,
        "coding_score": coding_score
    }])

    prediction = model.predict(input_df)[0]

    prediction = max(0, min(100, prediction))

    return round(prediction, 2)