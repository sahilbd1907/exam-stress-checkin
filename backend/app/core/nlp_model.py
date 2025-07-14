from typing import Tuple

# Dummy logic: You can later replace it with DistilBERT or fine-tuned model
def predict_emotion(text: str) -> Tuple[str, list, str]:
    # Simple keyword-based dummy model
    if any(word in text.lower() for word in ["stress", "pressure", "overwhelmed", "anxiety"]):
        emotion = "stressed"
        explanation = ["exam", "pressure", "overwhelmed"]
        advice = "Take a short break, try some deep breathing."
    elif any(word in text.lower() for word in ["happy", "excited", "joy"]):
        emotion = "happy"
        explanation = ["positive mood", "joy", "excitement"]
        advice = "Keep up the good energy! Maintain this positivity."
    elif any(word in text.lower() for word in ["sad", "depressed", "low"]):
        emotion = "sad"
        explanation = ["feeling down", "emotional burden"]
        advice = "Consider talking to a friend or counselor."
    else:
        emotion = "neutral"
        explanation = ["neutral tone", "no strong emotion detected"]
        advice = "Maintain balanced routines and self-care."

    return emotion, explanation, advice
