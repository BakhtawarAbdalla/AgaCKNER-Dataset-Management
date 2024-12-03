- Dataset Splition

1. Read the Input Dataset
    - Load the entire dataset from the input file.
    - Each line in the dataset contains a word followed by its NER tag (e.g., "word B-LOC").
    - Sentences are separated by blank lines, where each sentence ends when the line ". O" appears.

2. Extract Sentences
    - Group the lines into sentences.
    - A sentence ends when the line equals ". O".
    - Accumulate lines for each sentence and store the complete sentences in a list.

3. Shuffle the Sentences
    - Randomize the order of the sentences to avoid any order bias.
    - Use a fixed random seed for reproducibility to ensure consistent results across multiple runs.

4. Split the Dataset
    - Split the shuffled list of sentences into training, validation, and test sets.
    - The dataset is split based on the following ratios (by default):
        - 70% for the training set.
        - 20% for the validation set.
        - 10% for the test set.
    - Calculate the number of sentences in each subset based on the specified ratios.

5. Write the Subsets to Output Files
    - Write each of the subsets (train, validation, and test) to their respective output files.
    - Ensure that each sentence is written without extra blank lines between sentences.

6. Print Split Statistics
    - Print the total number of sentences in the dataset.
    - Print the number of sentences in the training, validation, and test sets, along with the corresponding percentages.
