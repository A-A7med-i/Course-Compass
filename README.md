# CourseCompass

CourseCompass is a Python-based project designed to provide tools and utilities for various AI-driven tasks, including web scraping, search engine interaction, and report generation. The project is modular, with a focus on extensibility and ease of use.

## Features

- **Agent-based architecture**: Includes agents for scraping, searching, and reporting.
- **LLM Integration**: Supports large language model (LLM) interactions.
- **Utilities**: Helper functions and tools for common tasks.
- **Extensible Design**: Modular structure for easy customization and extension.

## Project Structure

```
CourseCompass
├── config
├── outs
├── src
│   ├── agents
│   ├── constants
│   ├── crew
│   ├── llm
│   ├── schemas
│   ├── tasks
│   ├── tools
│   └── utils
├── template
├── LICENSE
├── README.md
├── requirements.txt
├── setup.py
```

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd CourseCompass
   ```

2. Set up the virtual environment:

   ```bash
   python3 -m venv AI-AGENT
   source AI-AGENT/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

- Activate the virtual environment:

  ```bash
  source AI-AGENT/bin/activate
  ```

- Run the main script:

  ```bash
  python src/crew/main.py
  ```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the terms of the [LICENSE](LICENSE) file.
