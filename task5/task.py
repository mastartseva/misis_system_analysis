import pandas as pd
import numpy as np

def compute_entropy(probs):
    non_zero_probs = probs[probs > 0]
    return -np.sum(non_zero_probs * np.log2(non_zero_probs))

def calculate_information_measures(filename):
    dataset = pd.read_csv(filename, index_col=0).values

    total = np.sum(dataset)
    joint_probs = dataset / total

    marginal_a_probs = np.sum(joint_probs, axis=1)
    marginal_b_probs = np.sum(joint_probs, axis=0)

    joint_entropy = compute_entropy(joint_probs.ravel())
    entropy_a = compute_entropy(marginal_a_probs)
    entropy_b = compute_entropy(marginal_b_probs)

    conditional_entropy_b_given_a = joint_entropy - entropy_a
    mutual_information = entropy_b - conditional_entropy_b_given_a

    return [
        round(joint_entropy, 2),
        round(entropy_a, 2),
        round(entropy_b, 2),
        round(conditional_entropy_b_given_a, 2),
        round(mutual_information, 2),
    ]

if __name__ == "__main__":
    output = calculate_information_measures("условная-энтропия-данные.csv")
    print(output)