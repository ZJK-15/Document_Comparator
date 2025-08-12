# Document Comparator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Overview

**Document Comparator** is a tool designed to compare documents efficiently, providing clear insights into differences and similarities. Whether you need to analyze text files, code, or other document types, this project helps automate and streamline the comparison process with accuracy and flexibility.

## Features

- **Fast Document Comparison**: Quickly compare two or more documents side by side.
- **Difference Highlighting**: Visualize changes, additions, and deletions in an easy-to-read format.
- **Multiple File Formats**: Supports various document types (e.g., .txt, .md, .pdf, etc.).
- **User-Friendly Interface**: Simple commands and clear output.
- **Customizable Options**: Choose comparison sensitivity, ignore whitespace, or focus on specific sections.

## Getting Started

### Prerequisites

- [Python 3.x](https://www.python.org/downloads/) (if applicable)
- Required libraries (see [`requirements.txt`](requirements.txt))

### Installation

Clone the repository:

```bash
git clone https://github.com/ZJK-15/Document_Comparator.git
cd Document_Comparator
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### Usage

Basic command-line usage:

```bash
python compare.py file1.txt file2.txt
```

Or use the GUI (if available):

```bash
python gui.py
```

#### Example Output

```
Comparing file1.txt and file2.txt...

Line 3 differs:
- file1.txt: This is the original line.
+ file2.txt: This line has been changed.
```

## Project Structure

```
Document_Comparator/
│
├── compare.py           # Main script for comparison
├── gui.py               # Optional GUI interface
├── requirements.txt     # Dependencies
├── README.md            # Project documentation
└── ...
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a pull request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
