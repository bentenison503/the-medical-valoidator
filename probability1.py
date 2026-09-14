import numpy as np

 # the law of large numbers int the probability.

categories = ["Fact", "Opinion", "Creative"]
theoretical_probs = [0.70, 0.20, 0.10] # 70%, 20%, 10%

print("--- THE THEORY ---")
for cat, prob in zip(categories, theoretical_probs):
    print(f"{cat}: {prob * 100}% expected")

