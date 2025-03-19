# Permutation Letters

## Overview
This Python script generates all possible unique permutations of a given list of letters, ensuring that each character is used only once per permutation.

## Features
- Uses recursion to generate all possible permutations.
- Ensures each character appears only once in a given permutation.
- Outputs the permutations directly to the console.

## How It Works
1. **Function `check_letter(letter, prefix)`**
   - Checks if a letter is already present in the prefix to avoid duplication.
   
2. **Function `permutation_letters(letters, length=-1, prefix=None)`**
   - Recursively generates all unique permutations.
   - Prints the permutations to the console.
   
3. **Example Execution**
   ```python
   lst = ['a', 'e', 'i', 'o', 'u']
   permutation_letters(lst)
   ```
   - This will generate and print all possible unique permutations of the given vowels.

## How to Run
Run the script in a Python environment:
```sh
python Permutation_letters.py
```

## Future Improvements
- Optimize performance for large lists.
- Add support for storing results in a file.
- Implement an option to return results as a list instead of printing.

## License
This project is open-source and can be used freely.

---
**Author:** Oleksandr Onupko
