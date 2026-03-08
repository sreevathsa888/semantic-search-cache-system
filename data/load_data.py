import os


def load_dataset():
    """Load the 20_newsgroups dataset relative to the repository root.

    Looks for either:
      - <repo>/20_newsgroups/20_newsgroups  (nested layout)
      - <repo>/20_newsgroups                (flat layout)

    Raises FileNotFoundError with the checked paths if not found.
    """

    # repo root is the parent of the `data/` directory
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

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
                    # Continue on unreadable files
                    continue

    return documents