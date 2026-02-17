
#formerly list of key words is now a list of dictionary with term
# categorization based on what is captured from GDPR documentation
# This change is in preparation of an important update, where in the report file we also
# have category and severity of key words
keywords = [
    {"term": "passport",        "category": "ID",        "severity": "HIGH"},
    {"term": "national id",     "category": "ID",        "severity": "HIGH"},
    {"term": "driving license", "category": "ID",        "severity": "HIGH"},
    {"term": "pps",             "category": "ID",        "severity": "HIGH"},
    {"term": "ppsn",            "category": "ID",        "severity": "HIGH"},
    {"term": "social security number", "category": "ID", "severity": "HIGH"},
    {"term": "address",         "category": "Contact",   "severity": "MEDIUM"},
    {"term": "phone",           "category": "Contact",   "severity": "MEDIUM"},
    {"term": "ip address",      "category": "Contact",   "severity": "MEDIUM"},
    {"term": "email",           "category": "Contact",   "severity": "MEDIUM"},
    {"term": "health",          "category": "Medical",   "severity": "HIGH"},
    {"term": "disease",         "category": "Medical",   "severity": "HIGH"},
    {"term": "medical",         "category": "Medical",   "severity": "HIGH"},
    {"term": "clinical",        "category": "Medical",   "severity": "HIGH"},
    {"term": "treatment",       "category": "Medical",   "severity": "HIGH"},
    {"term": "religion",        "category": "Sensitive", "severity": "HIGH"},
    {"term": "religious",       "category": "Sensitive", "severity": "HIGH"},
    {"term": "political",       "category": "Sensitive", "severity": "HIGH"},
    {"term": "sexual",          "category": "Sensitive", "severity": "HIGH"},
    {"term": "orientation",     "category": "Sensitive", "severity": "HIGH"},
    {"term": "fingerprint",     "category": "Biometric", "severity": "HIGH"},
    {"term": "genetic",         "category": "Genetic",   "severity": "HIGH"},
    {"term": "name",            "category": "Identifier","severity": "LOW"},
    {"term": "surname",         "category": "Identifier","severity": "LOW"},
    {"term": "first name",      "category": "Identifier","severity": "LOW"},
    {"term": "second name",     "category": "Identifier","severity": "LOW"},
    {"term": "maiden name",     "category": "Identifier","severity": "LOW"},
    {"term": "location",        "category": "Location",  "severity": "MEDIUM"},
    {"term": "coordinates",     "category": "Location",  "severity": "MEDIUM"},
]