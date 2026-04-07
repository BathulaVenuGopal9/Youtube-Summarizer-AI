# YouTube to Website AI Generator
## Overview

The YouTube to Website AI Generator is an end-to-end Generative AI application that automatically transforms YouTube video content into structured, high-quality written articles and fully functional, responsive websites.

This project demonstrates the practical application of Large Language Models (LLMs) in content transformation, automation, and frontend generation. It integrates transcript extraction, intelligent summarization, and dynamic webpage creation into a seamless pipeline.

## Objective

The primary objective of this project is to:

Automate the conversion of video-based content into readable blog formats
Generate production-ready web pages from unstructured data
Demonstrate real-world usage of GenAI pipelines using modern tools like LangChain and Gemini
### Key Features
#### YouTube Transcript Extraction
Automatically fetches video transcripts using a document loader
#### AI-Powered Content Transformation
Converts raw transcripts into structured, engaging, and professional articles
#### Automated Website Generation
Dynamically generates:
HTML (content structure)
CSS (styling & layout)
JavaScript (basic interactivity)
#### Exportable Output
Outputs a complete website bundle:
index.html
style.css
script.js
website.zip
#### End-to-End Automation
Entire pipeline runs with a single command
#### Tech Stack
## Backend & AI
Python
LangChain
Google Gemini API (Gemini 2.5 Flash)
### Frontend
HTML5
CSS3
JavaScript
##@ Utilities
dotenv (environment management)
zipfile (output packaging)
### Architecture Overview

The project follows a modular pipeline architecture:

Input Layer
Accepts YouTube video URL
Data Extraction
Uses YouTube Loader to extract transcript
Processing Layer
LangChain prompt templates structure the content
Gemini LLM transforms transcript into an article
Transformation Layer
Converts article into web-ready components (HTML, CSS, JS)
Output Layer
Saves files and generates downloadable ZIP

### Installation & Setup
#### Clone Repository
git clone https://github.com/your-username/youtube-summarizer-ai.git
cd youtube-summarizer-ai
#### Install Dependencies
pip install -r requirements.txt
#### Configure Environment Variables

Create a .env file in the root directory:

GEMINI_API_KEY=your_api_key_here( not included due to security reasons)
### Usage

Run the application:

python summarizer.py
### Output

After execution, the following files are generated:

index.html → Main webpage
style.css → Styling and layout
script.js → Interactive behavior
website.zip → Packaged website
### Important Note on API Usage

This project leverages Google Gemini 2.5 Flash (Free Tier) for generating content.

While the free tier is highly effective for development, experimentation, and small-scale use cases, it comes with strict quota limitations, including:

Limited number of requests per day
Token usage constraints
Temporary rate limiting under high usage

Due to these restrictions, users may occasionally encounter quota-related errors during execution.

For consistent performance, higher throughput, and production-grade reliability, it is strongly recommended to upgrade to a paid plan or enhanced quota tier provided by Google.

This ensures:

Stable API availability
Faster response times
Scalability for larger workloads
#### Future Enhancements
#### Web-based UI using Streamlit or React
#### User input field for dynamic video URLs
#### Deployment on cloud platforms (AWS / GCP / Vercel)
#### Support for batch video processing
#### Advanced summarization with multi-step reasoning
#### Improved UI/UX for generated websites
#### Learning Outcomes

This project demonstrates:

Practical implementation of Generative AI pipelines
Prompt engineering for structured outputs
Integration of LLMs with real-world data sources
Automated frontend generation using AI
Handling API limitations and optimization strategies

## Author
Bathula Venu Gopal| Gen-AI Intern at Innomatics Research Labs.



### Support

If you found this project valuable, consider giving it a ⭐ on GitHub.
It helps increase visibility and encourages further development.

### Contact
Feel free to connect for collaboration, feedback, or discussions on AI and development.
