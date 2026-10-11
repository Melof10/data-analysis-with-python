import numpy as np


def calculate(numbers):
    """
    Calculate descriptive statistics for a 3x3 matrix.

    Args:
        numbers (list): A list containing exactly nine numbers.

    Returns:
        dict: Mean, variance, standard deviation, maximum,
              minimum, and sum across columns, rows, and
              the entire matrix.

    Raises:
        ValueError: If the list does not contain nine numbers.
    """

    # Validate input length
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")

    # Convert input list into a 3x3 NumPy matrix
    matrix = np.array(numbers).reshape(3, 3)

    # Calculate descriptive statistics
    calculations = {
        'mean': [
            np.mean(matrix, axis=0).tolist(),
            np.mean(matrix, axis=1).tolist(),
            np.mean(matrix).item()
        ],
        'variance': [
            np.var(matrix, axis=0).tolist(),
            np.var(matrix, axis=1).tolist(),
            np.var(matrix).item()
        ],
        'standard deviation': [
            np.std(matrix, axis=0).tolist(),
            np.std(matrix, axis=1).tolist(),
            np.std(matrix).item()
        ],
        'max': [
            np.max(matrix, axis=0).tolist(),
            np.max(matrix, axis=1).tolist(),
            np.max(matrix).item()
        ],
        'min': [
            np.min(matrix, axis=0).tolist(),
            np.min(matrix, axis=1).tolist(),
            np.min(matrix).item()
        ],
        'sum': [
            np.sum(matrix, axis=0).tolist(),
            np.sum(matrix, axis=1).tolist(),
            np.sum(matrix).item()
        ]
    }

    return calculations


if __name__ == "__main__":
    import pprint

    # Example input
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    # Execute calculations
    result = calculate(numbers)

    # Display formatted results
    print("\nMean-Variance-Standard Deviation Calculator")
    print("=" * 50)

    pprint.pprint(result, sort_dicts=False)