# Company Brochure Generator

The **Company Brochure Generator** is a Python-based application that uses web scraping and AI to generate a professional brochure for a company. Built with Streamlit for an interactive user interface, this tool is perfect for showcasing company culture, customer focus, and career opportunities.

## Features

- **Dynamic Web Scraping**: Extracts information from the company's website using `requests` and `BeautifulSoup`.
- **AI-Powered Content Generation**: Leverages OpenAI's API to analyze and generate meaningful content for the brochure.
- **Real-Time Streaming**: Displays the generated brochure content dynamically in the browser.
- **Customizable Prompts**: Tailored prompts to extract relevant company details.

## Installation

Follow these steps to set up and run the application:

### Prerequisites

- Python 3.11 or newer
- Conda (recommended for managing environments)
- Dependencies listed in `environment.yml` file
- Access to OpenAI API (or local Ollama server for `llama3.2`)

### Setup

1. **Starting the Ollama Server**:
Install [Ollama](https://ollama.com/) on your system.
2. **Start Ollama server**:
```bash
ollama serve
```
3. **Clone the repository**:
```bash
git clone https://github.com/KamRoki/brochure-generator.git
cd brochure-generator
```
4. **Install dependencies**:
```bash
conda env create -f environment.yml
conda activate brochure_generator
```
5. **Start the Streamlit app**:
```bash
streamlit run app.py
```

### Usage
1. Enter the company name and its website URL
2. Click the Generate Brochure button.
3. The app will scrape the website, analyze the content, and generate a brochure in real-time.
4. The generated brochure will appear in markdown format on the main page.

### API Integration
This project uses the **Ollama API** for local inference with the `llama3.2` model. To ensure the application runs correctly, please download Ollama.

---

## Author
Created by Kamil Stachurski.
