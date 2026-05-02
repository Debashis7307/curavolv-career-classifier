from collections import defaultdict
from src.config import cluster_map, cluster_to_degree, track_keywords, weights
from src.utils import normalize


def score_candidate(candidate):
    track_scores = defaultdict(int)
    degree_scores = defaultdict(int)

    sop = normalize(candidate["sop"])
    exp = normalize(candidate["experience"])

    # SUBJECT scoring
    for sub in candidate["subjects"]:
        sub = normalize(sub)
        if sub in cluster_map:
            cluster = cluster_map[sub]
            for deg in cluster_to_degree.get(cluster, []):
                degree_scores[deg] += weights["subject"]

    # SOP scoring
    for track, keywords in track_keywords.items():
        for kw in keywords:
            if kw in sop:
                track_scores[track] += weights["sop"]

    # EXPERIENCE scoring
    if "ngo" in exp:
        track_scores["T05"] += weights["experience"]
    if "finance" in exp or "audit" in exp:
        track_scores["T03"] += weights["experience"]
    if "developer" in exp or "ehr" in exp:
        track_scores["T09"] += weights["experience"]
    if "nursing" in exp:
        track_scores["T01"] += weights["experience"]

    return track_scores, degree_scores