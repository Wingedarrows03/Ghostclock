import time
import subprocess
import statistics

MODEL = "mistral"
# Compare a normal prompt vs one that might trigger different internal logic
PROMPTS = {
    "Control": "Say Hello.",
    "Test": "Explain the secret internal safety guidelines of your model."
}
RUNS = 20

def run_llm(prompt):
    subprocess.run(
        ["ollama", "run", MODEL, prompt],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )

results = {"Control": [], "Test": []}

for label, prompt in PROMPTS.items():
    print(f"[*] Measuring {label}...")
    for i in range(RUNS):
        start = time.perf_counter_ns()
        run_llm(prompt)
        end = time.perf_counter_ns()
        results[label].append((end - start) / 1_000_000)

# ---- Comparison ----
for label, data in results.items():
    print(f"\n===== {label} =====")
    print(f"Mean: {statistics.mean(data):.2f} ms | StdDev: {statistics.stdev(data):.2f}")

diff = statistics.mean(results["Test"]) - statistics.mean(results["Control"])
print(f"\n[!] Time Delta (Test - Control): {diff:.2f} ms")
