# Sun_Ask
## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Credits](#credits)
## Overview

This system involves steps from data collection, data transformation, storage, to user query responses. The main components of the system are: **Sun Asterisk Website**, **Chroma**, and **Gemini**.

### Components and Workflow

1. **Sun Asterisk Website**
   - **Data Sources**: The system begins with data sources from `sun-asterisk.vn/*`.
   - **Scraping**: Data is collected from these sources through scraping.

2. **Raw Data**
   - **Raw Data**: After collection, data is stored in its raw form.
   - **Embedding**: The raw data is then transformed into vector embeddings for easier processing and searching.

3. **Chroma**
   - **Vector Embedding**: The vector embeddings are imported into the Chroma database.
   - **Query**: Users can send queries to Chroma. The database processes these queries using the vector embeddings to find relevant data.

4. **Gemini**
   - **Question and Context Processing**: The Chroma database sends the question and context to Gemini 1.5 Flash.
   - **Response**: Gemini processes the information and responds to the user's query, generating the response.

### Detailed Workflow

- Users send queries to the system.
- Chroma receives the queries and uses vector embeddings to search the database.
- The results from Chroma are sent to Gemini along with the context and question.
- Gemini processes and generates a response, which is then sent back to the user.

## Summary

This system creates a workflow from data collection, transformation into vector embeddings, storage in a database, to query processing and response generation for users. Technologies like Chroma and Gemini play crucial roles in processing and responding to questions based on the collected and stored data.

<p align="center">
  <img src="https://scontent-hkg4-2.xx.fbcdn.net/v/t1.15752-9/448274067_838205034323638_5401617840387538609_n.jpg?_nc_cat=111&ccb=1-7&_nc_sid=5f2048&_nc_ohc=TxNGuNSgXvUQ7kNvgEwa2fO&_nc_ht=scontent-hkg4-2.xx&oh=03_Q7cD1QGM1HU5IPHYog88Tn5nLzf2epHvH2in9DLKPTaKehGrJg&oe=669F94FA" alt="Sun Asterisk Logo">
</p>




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
   `streamlit app.py`
   This command starts a local web server and opens the Sun Asterisk interactive Q&A interface in your web browser.
3. **Ask questions about Sun Asterisk:**
   Enter your questions in the text input field provided. The system uses a Retrieval-Augmented Generation (RAG) model to generate responses based on pre-scraped information about Sun Asterisk.


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
