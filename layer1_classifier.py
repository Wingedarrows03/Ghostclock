import time
import subprocess
import statistics

MODEL = "mistral"
PROMPT = "Answer with only YES."
WARMUP_RUNS = 5
MEASURED_RUNS = 30

def run_llm():
    subprocess.run(
        ["ollama", "run", MODEL, PROMPT],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

# ---- Warm-up phase (very important) ----
print("[*] Warming up model...")
for _ in range(WARMUP_RUNS):
    run_llm()

print("[*] Starting timed runs...\n")

times_ms = []

for i in range(MEASURED_RUNS):
    start = time.perf_counter_ns()
    run_llm()
    end = time.perf_counter_ns()

    duration = (end - start) / 1_000_000
    times_ms.append(duration)

    print(f"Run {i+1:02d}: {duration:.2f} ms")

# ---- Analysis ----
print("\n===== Timing Summary =====")
print(f"Runs           : {MEASURED_RUNS}")
print(f"Mean (ms)      : {statistics.mean(times_ms):.2f}")
print(f"Median (ms)    : {statistics.median(times_ms):.2f}")
print(f"Std Deviation  : {statistics.stdev(times_ms):.2f}")
print(f"Min / Max (ms) : {min(times_ms):.2f} / {max(times_ms):.2f}")
