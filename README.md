# Sun_Ask

This project utilizes web scraping, natural language processing, and generative AI to gather information about Sun Asterisk, process it, and provide interactive responses to user queries.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Credits](#credits)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/tuananh1006/Sun_Ask_RAG.git
   cd Sun_Ask_RAG

   ```

2. **Install dependencies:**

   `pip install -r requirements.txt`

3. **Setup environment variables**

   Create a `.env` file in the root directory with the following content:

   `GOOGLE_API_KEY=<your_google_api_key>`

   Replace <your_google_api_key> with your actual Google API key obtained from the Google Cloud Console.

## **Usage**

1. **Run the initial vectordatabase:**
   `python data.py`
   Get data,add data to vector database
2. **Run the Streamlit application:**
   `streamlit run app.py`
   This command starts a local web server and opens the Sun Asterisk interactive Q&A interface in your web browser.
3. **Ask questions about Sun Asterisk:**
   Enter your questions in the text input field provided. The system uses a Retrieval-Augmented Generation (RAG) model to generate responses based on pre-scraped information about Sun Asterisk.

<p align="center">
  <img src="https://scontent-hkg4-1.xx.fbcdn.net/v/t1.15752-9/448145943_1835300310230509_5864883126335463683_n.png?_nc_cat=106&ccb=1-7&_nc_sid=5f2048&_nc_ohc=xWHFvLn4iicQ7kNvgEfbsb0&_nc_ht=scontent-hkg4-1.xx&oh=03_Q7cD1QEe5c0P9j1c5_h_Cfcery0goS1v120CmHdQCG-PtA6Fxg&oe=669F07D5" alt="Sun Asterisk Logo">
</p>

<p align="center">
  <em>Results returned when asking for information about Sun* company </em>
</p>

## **Contributing**

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create your feature branch **(git checkout -b feature/YourFeature)**.
3. Commit your changes **(git commit -am 'Add some feature')**.
4. Push to the branch **(git push origin feature/YourFeature)**.
5. Open a pull request.

Please ensure your pull request adheres to the code of conduct.

## Credits

- **ChromaDB**: Used for document storage and retrieval with embeddings.
- **Google GenerativeAI**: Utilized for natural language generation capabilities.
- **Streamlit**: Used for building and deploying interactive web applications.
- **Beautiful Soup**: Used for parsing HTML and extracting data from web pages.
