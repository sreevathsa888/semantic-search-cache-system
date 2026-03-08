import os

def load_dataset():
    """Load the 20_newsgroups dataset from the repository.

    This function prefers the dataset directory next to this file. It will
    also try a single-level `20_newsgroups` folder if the nested layout isn't
    present. If neither is found, it raises a clear FileNotFoundError.
    """

    base_path = os.path.abspath(os.path.dirname(__file__))

    # The repository contains a top-level folder `20_newsgroups` which itself
    # contains a `20_newsgroups/` subfolder with category subfolders. Try the
    # nested layout first, then fall back to the single folder layout.
    candidate1 = os.path.join(base_path, "20_newsgroups", "20_newsgroups")
    candidate2 = os.path.join(base_path, "20_newsgroups")

    if os.path.isdir(candidate1):
        dataset_path = candidate1
    elif os.path.isdir(candidate2):
        dataset_path = candidate2
    else:
        raise FileNotFoundError(
            f"Dataset directory not found. Checked: {candidate1!r} and {candidate2!r}"
        )

    documents = []

    for category in os.listdir(dataset_path):
        category_path = os.path.join(dataset_path, category)

        if os.path.isdir(category_path):
            for file in os.listdir(category_path):
                file_path = os.path.join(category_path, file)
                try:
                    with open(file_path, "r", encoding="latin1") as f:
                        documents.append(f.read())
                except Exception:
                    # Skip unreadable files but continue processing others
                    continue

    return documents