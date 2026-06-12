import textstat
import re
from bs4 import BeautifulSoup
from app.models.readability_model import ReadabilityResult, ReadabilityIssue

# Common medical terms with simpler alternatives
MEDICAL_TERMS = {
    "hypertension": "high blood pressure",
    "dyspnea": "shortness of breath",
    "edema": "swelling",
    "myocardial infarction": "heart attack",
    "cerebrovascular accident": "stroke",
    "hyperlipidemia": "high cholesterol",
    "tachycardia": "fast heart rate",
    "bradycardia": "slow heart rate",
    "hyperglycemia": "high blood sugar",
    "hypoglycemia": "low blood sugar",
    "osteoporosis": "weak/brittle bones",
    "hypertrophy": "enlargement",
    "inflammation": "swelling and irritation",
    "arrhythmia": "irregular heartbeat",
    "dyslipidemia": "abnormal cholesterol levels",
}

class ReadabilityService:

    def analyze(self, text: str) -> ReadabilityResult:
        plain_text = self._extract_plain_text(text)
        issues = []

        raw_score = textstat.flesch_reading_ease(plain_text)
        score = max(0, min(100, raw_score))
        level = self._get_level(score)
        approved = score >= 50 and len(issues) < 10

        issues += self._detect_medical_terms(plain_text)
        issues += self._detect_long_sentences(plain_text)
        issues += self._detect_long_paragraphs(plain_text)
        issues += self._detect_missing_headings(text)

        return ReadabilityResult(
            score=round(score, 2),
            level=level,
            approved=approved,
            issues=issues
        )

    def _extract_plain_text(self, text: str) -> str:
        soup = BeautifulSoup(text, "html.parser")
        return soup.get_text(separator=" ", strip=True)

    def _get_level(self, score: float) -> str:
        if score >= 70:
            return "Beginner Friendly"
        elif score >= 50:
            return "Intermediate"
        else:
            return "Advanced"

    def _detect_medical_terms(self, text: str):
        issues = []
        detected_terms = set()
        lower_text = text.lower()
        for term, suggestion in MEDICAL_TERMS.items():
            if term in lower_text and term not in detected_terms:
                detected_terms.add(term)
                issues.append(ReadabilityIssue(
                    type="complex_word",
                    text=term,
                    suggestion=f"Consider using '{suggestion}' instead of '{term}'",
                    severity="medium"
                ))
        return issues

    def _detect_long_sentences(self, text: str):
        issues = []
        sentences = re.split(r'(?<=[.!?])\s+', text)
        for sentence in sentences:
            if len(sentence.split()) > 18:
                issues.append(ReadabilityIssue(
                    type="long_sentence",
                    text=sentence[:100] + "..." if len(sentence) > 100 else sentence,
                    suggestion="Consider breaking this sentence into smaller ones",
                    severity="high"
                ))
        return issues

    def _detect_long_paragraphs(self, text: str):
        issues = []
        paragraphs = text.split("\n\n")
        for para in paragraphs:
            if len(para.split()) > 100:
                issues.append(ReadabilityIssue(
                    type="long_paragraph",
                    text=para[:100] + "...",
                    suggestion="Consider breaking this paragraph into smaller ones",
                    severity="medium"
                ))
        return issues

    def _detect_missing_headings(self, text: str):
        issues = []
        has_heading = bool(re.search(r'<h[1-6]', text, re.IGNORECASE)) or \
                      bool(re.search(r'^#{1,6}\s', text, re.MULTILINE))
        if not has_heading:
            issues.append(ReadabilityIssue(
                type="missing_heading",
                text="No headings detected",
                suggestion="Add headings to improve article structure and readability",
                severity="low"
            ))
        return issues