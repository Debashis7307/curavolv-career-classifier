cluster_map = {
    "anatomy": "C1", "physiology": "C1", "biochemistry": "C1",
    "finance": "C5", "accounting": "C5", "economics": "C5",
    "sociology": "C4", "anthropology": "C4",
    "python": "C7", "database": "C7", "machine learning": "C7",
    "public policy": "C8", "law": "C8"
}

cluster_to_degree = {
    "C1": ["MPH", "MSHI"],
    "C4": ["MPH", "MHA"],
    "C5": ["MBA-HC", "MHA"],
    "C7": ["MSHI", "MBA-HC"],
    "C8": ["MPH", "MHA"]
}

track_keywords = {
    "T01": ["leadership", "operations", "quality"],
    "T05": ["community", "health equity"],
    "T03": ["finance", "revenue", "payer"],
    "T09": ["ehr", "interoperability"],
    "T07": ["policy", "advocacy"]
}

weights = {
    "subject": 2,
    "experience": 3,
    "sop": 4,
    "strength": 1
}