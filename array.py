import os
import sys

def parse_scores_from_string(s):
    # accept comma/space separated numbers
    parts = [p.strip() for p in s.replace(',', ' ').split()]
    scores = []
    for p in parts:
        if p == '':
            continue
        try:
            scores.append(float(p))
        except ValueError:
            print(f"warning: skipping non-numeric token: {p}")
    return scores

def read_scores():
    # Priority: CLI args > SCORES env var > scores.txt > interactive prompt
    if len(sys.argv) > 1:
        # join all args into one string
        return parse_scores_from_string(" ".join(sys.argv[1:]))

    env = os.getenv("SCORES")
    if env:
        return parse_scores_from_string(env)

    if os.path.isfile("scores.txt"):
        with open("scores.txt", "r") as f:
            return parse_scores_from_string(f.read())

    # interactive prompt
    raw = input("Enter scores separated by spaces or commas: ")
    return parse_scores_from_string(raw)

def main():
    scores = read_scores()
    total = sum(scores) if scores else 0
    avg = total / len(scores) if scores else 0

    print("==main/master branch output==")
    print(f"count of scores: {len(scores)}")
    print(f"sum: {total}")
    print(f"Average: {avg}")

if __name__ == "__main__":
    main()