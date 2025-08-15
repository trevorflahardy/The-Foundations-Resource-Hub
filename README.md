![The Foundations Resource Hub Header](./docs/_static/foundations_resource_hub.png)

# The Foundations Resource Hub

[![Documentation Status](https://readthedocs.org/projects/the-arduino-guide/badge/?version=latest)](https://the-arduino-guide.readthedocs.io/en/latest/)
[![wakatime](https://wakatime.com/badge/user/9e70bc6a-2430-4dc3-a452-4ec4d2a7a8b9/project/e65c8b32-b5ea-43ae-9362-9ea23fe3f91e.svg)](https://wakatime.com/badge/user/9e70bc6a-2430-4dc3-a452-4ec4d2a7a8b9/project/e65c8b32-b5ea-43ae-9362-9ea23fe3f91e)

Welcome to The Foundations Resource Hub, a repository dedicated to teaching students the programming, circuit design, and digital fabrication skills used in the Foundations of Engineering Lab (EGN 3000L) course at the University of South Florida. It covers Arduino-based microcontroller programming, practical electronics, and 3D printing workflows. Documentation is organized into dedicated sections for programming, 3D printing, and course assignments so you can easily navigate to the material you need. It is written in Markdown and intended to be read on GitHub.

## Key Features

- **Structured Learning Path**: Progressive tutorials from basic to advanced concepts
- **Interactive Code Examples**: Fully documented Arduino examples for common components
- **Integrated Quizzes**: Self-assessment tools that integrate with Canvas LMS
- **3D Printing Workflows**: Complete guides from design to finished print
- **Course Assignments**: Detailed instructions for practical engineering projects

## Technical Architecture

### Documentation System

The project is built using **Sphinx**, a powerful documentation generator originally created for Python documentation. Our implementation includes:

- **reStructuredText (RST)**: Primary markup language for content
- **Custom Sphinx Extensions**: Enhanced code blocks and interactive elements
- **Theme Customizations**: Improved navigation and reading experience
- **Automated Build Process**: Documentation automatically builds on updates

### Directory Structure

```
docs/               # Sphinx documentation source files
├── _build/         # Generated HTML output
├── _static/        # Static assets (images, CSS)
├── programming/    # Arduino programming tutorials
├── 3d_printing/    # 3D printing guides
├── assignments/    # Course project instructions
└── quizzes/        # Self-assessment materials
examples/           # Arduino code examples
quiz_to_qti/        # Quiz conversion tools
rst_to_html/        # Custom HTML generator
```

## Supporting Tools

### quiz_to_qti

A custom tool for converting Markdown-based quizzes to QTI format for Canvas LMS integration:

- **Purpose**: Automates the creation and importing of quizzes into Canvas
- **Features**:
  - Converts Markdown quizzes to QTI format
  - Generates intelligent quiz descriptions using LLM
  - Supports multiple question types (multiple choice, true/false, matching)
  - Batch processing for entire directories of quiz content
  - Automatic question shuffling and feedback options

### rst_to_html

A specialized tool for converting Sphinx RST content to standalone HTML:

- **Purpose**: Provides an alternative rendering path for content reuse
- **Features**:
  - Preserves Sphinx directives and extensions
  - Custom syntax highlighting with Pygments
  - Self-contained HTML output with embedded assets
  - Maintains navigation structure

### DevContainer Setup

The project includes a complete development environment using VS Code DevContainers:

- **Docker Compose Integration**: Multi-container setup with app and Ollama services
- **GPU Acceleration**: Optional NVIDIA/Apple Silicon GPU support for LLM processing
- **Automated Environment**: Pre-configured with all required dependencies
- **Cross-platform**: Works consistently on Windows, macOS, and Linux

## Canvas LMS Integration

### Automated Quiz Import

One of the project's key innovations is the seamless integration with Canvas LMS:

- **Quiz Workflow**:
  1. Authors write quizzes in Markdown format with question metadata
  2. `quiz_to_qti` processes quizzes and generates QTI packages
  3. AI-powered descriptions summarize quiz content and question count
  4. Generated packages import directly into Canvas course modules

### Benefits of Automation

- **Consistency**: Standardized format for all course quizzes
- **Efficiency**: Dramatic reduction in quiz creation time
- **Maintenance**: Version-controlled quizzes that can be updated and reimported
- **Analytics**: Better tracking of student performance across question types

## Development Workflow

### Contributing Content

1. Clone the repository and open in VS Code with DevContainers extension
2. Create or modify content in the appropriate directories
3. Preview changes using Sphinx's built-in server
4. Submit pull requests for review

### Building Documentation

```bash
# Generate HTML documentation
cd docs
make html

# Generate standalone HTML (alternative format)
python -m rst_to_html docs/_build_raw/html

# Build quizzes for Canvas
python -m quiz_to_qti batch --auto-desc
```

## Future Roadmap

- Interactive circuit simulation integration
- Video tutorial embedding
- Student contribution system for community examples
- Expansion to cover additional engineering topics

## License

This project is licensed under the terms specified in the LICENSE file.

## Acknowledgments

This project was developed to support engineering education at the University of South Florida. Special thanks to all contributors and faculty members who have provided valuable feedback and content suggestions.
