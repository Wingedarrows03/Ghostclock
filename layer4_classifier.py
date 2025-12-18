import time
import subprocess

MODEL = "mistral"

# ---- Timing thresholds (derived from Layer 3 means) ----
THRESHOLDS = {
    "Trivial": 10000,        # < 10s
    "Refusal": 40000,        # 10s–40s
    "Informational": 65000,  # 40s–65s
    "Sensitive": float("inf")
}

# ---- LLM execution wrapper ----
def run_llm(prompt: str):
    subprocess.run(
        ["ollama", "run", MODEL, prompt],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

# ---- Measure execution time ----
def measure_time(prompt: str) -> float:
    start = time.perf_counter_ns()
    run_llm(prompt)
    end = time.perf_counter_ns()
    return (end - start) / 1_000_000

# ---- Classifier ----
def classify_prompt(prompt: str):
    print("\n[*] Testing unknown prompt...")
    print(f"Prompt: \"{prompt}\"")

    duration = measure_time(prompt)

    for cls, threshold in THRESHOLDS.items():
        if duration < threshold:
            prediction = cls
            break

    print(f"\n[+] Execution Time : {duration:.2f} ms")
    print(f"[!] Predicted Intent Class → {prediction}")

# ---- Test Prompt ----
UNKNOWN_PROMPT = "Can you explain how you decide what content to block?"

classify_prompt(UNKNOWN_PROMPT)
