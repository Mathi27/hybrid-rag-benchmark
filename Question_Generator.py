import json
import random

# -----------------------------
# Configuration
# -----------------------------
OUTPUT_PATH = "questions_100.json"

QUESTION_TEMPLATES = {
    "factual": [
        "What is {}?",
        "What is the purpose of {}?",
        "What are the main components of {}?"
    ],
    "inferential": [
        "Why is {} important?",
        "How does {} improve system performance?",
        "Why is {} widely used?"
    ],
    "comparative": [
        "How does {} differ from related approaches?",
        "What is the difference between {} and similar methods?"
    ],
    "conceptual": [
        "Explain the concept of {}.",
        "What problem does {} aim to solve?"
    ]
}

# Topics mapped to Wikipedia URLs (must be part of fixed_urls.json)
TOPICS = [
    ("Machine learning", "https://en.wikipedia.org/wiki/Machine_learning"),
    ("Artificial intelligence", "https://en.wikipedia.org/wiki/Artificial_intelligence"),
    ("Neural network", "https://en.wikipedia.org/wiki/Neural_network"),
    ("Deep learning", "https://en.wikipedia.org/wiki/Deep_learning"),
    ("Gradient descent", "https://en.wikipedia.org/wiki/Gradient_descent"),
    ("Backpropagation", "https://en.wikipedia.org/wiki/Backpropagation"),
    ("Support vector machine", "https://en.wikipedia.org/wiki/Support_vector_machine"),
    ("Principal component analysis", "https://en.wikipedia.org/wiki/Principal_component_analysis"),
    ("Information retrieval", "https://en.wikipedia.org/wiki/Information_retrieval"),
    ("Natural language processing", "https://en.wikipedia.org/wiki/Natural_language_processing"),
    ("Computer vision", "https://en.wikipedia.org/wiki/Computer_vision"),
    ("Transformer model", "https://en.wikipedia.org/wiki/Transformer_(machine_learning)"),
    ("Retrieval-augmented generation", "https://en.wikipedia.org/wiki/Retrieval-augmented_generation"),
    ("FAISS", "https://en.wikipedia.org/wiki/FAISS"),
    ("BM25", "https://en.wikipedia.org/wiki/Okapi_BM25")
]

# -----------------------------
# Question Generation
# -----------------------------
questions = []
qid = 1

while len(questions) < 100:
    topic, url = random.choice(TOPICS)
    q_type = random.choice(list(QUESTION_TEMPLATES.keys()))
    template = random.choice(QUESTION_TEMPLATES[q_type])

    question_text = template.format(topic)

    questions.append({
        "id": qid,
        "question": question_text,
        "ground_truth_url": url,
        "type": q_type
    })

    qid += 1

# -----------------------------
# Save to JSON
# -----------------------------
with open(OUTPUT_PATH, "w") as f:
    json.dump({"questions": questions}, f, indent=2)

print(f"✅ Generated {len(questions)} questions")
print(f"📄 Saved to {OUTPUT_PATH}")
