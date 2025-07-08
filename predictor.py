# predictor.py

def detect_patterns(multipliers):
    pattern = {
        "last_10": multipliers,
        "count_1x": 0,
        "count_3x": 0,
        "count_10x": 0,
        "count_100x": 0
    }

    for m in multipliers:
        if m <= 1.10:
            pattern["count_1x"] += 1
        if m >= 3:
            pattern["count_3x"] += 1
        if m >= 10:
            pattern["count_10x"] += 1
        if m >= 100:
            pattern["count_100x"] += 1

    return pattern


def generate_signal(pattern):
    if pattern["count_100x"] >= 1:
        return "💥💯 Jackpot Round aya — filhal Avoid karo 🔴"
    if pattern["count_10x"] >= 1:
        return "🔴 10x just aya hai — next 3 rounds risky hain!"
    if pattern["count_1x"] >= 3:
        return "🟡 3 baar crash hua ~ 1.00 — 3x aane ka chance!"
    if pattern["count_3x"] >= 2:
        return "🟢 Trend 3x ke favour me hai — Safe Bet 🔮"
    return "🟡 No strong pattern — Wait or Skip Round."

def predict_signal(multipliers):
    pattern = detect_patterns(multipliers)
    return generate_signal(pattern)
