from .utils import normalize_text


class AIPredictor:
    """Simple AI prediction stub for demonstration purposes."""

    def predict(self, text: str) -> float:
        normalized = normalize_text(text)
        if not normalized:
            return 0.0
        return min(1.0, len(normalized) / 100.0)
