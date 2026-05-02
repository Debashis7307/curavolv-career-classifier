import json
from data.candidates import candidates
from src.classifier import classify


def main():
    results = []

    for c in candidates:
        res = classify(c)
        results.append(res)

    with open("outputs/results.json", "w") as f:
        json.dump(results, f, indent=4)

    print("Classification complete. Check outputs/results.json")


if __name__ == "__main__":
    main()