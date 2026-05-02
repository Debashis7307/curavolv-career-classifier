def generate_rationale(track, candidate):
    sop = candidate["sop"]

    return f"Aligned due to SOP focus: '{sop[:80]}...' and relevant background."