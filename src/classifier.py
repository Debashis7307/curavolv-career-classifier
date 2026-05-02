from src.scorer import score_candidate
from src.rationale import generate_rationale


def classify(candidate):
    track_scores, degree_scores = score_candidate(candidate)

    top_tracks = sorted(track_scores.items(), key=lambda x: x[1], reverse=True)[:3]

    result_tracks = []
    for t, _ in top_tracks:
        result_tracks.append({
            "track": t,
            "reason": generate_rationale(t, candidate)
        })

    best_degree = max(degree_scores, key=degree_scores.get) if degree_scores else "MPH"

    return {
        "candidate_id": candidate["id"],
        "top_tracks": result_tracks,
        "recommended_degree": best_degree
    }