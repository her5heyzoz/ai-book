In the rapidly evolving field of artificial intelligence (AI), accessing structured and up-to-date information about academic resources—such as textbooks—is critical for researchers, educators, and students. However, valuable insights into AI literature are often scattered across platforms like Douban Books, where manual curation is time-consuming and inefficient. Additionally, while existing tools may scrape raw data, they lack the capability to perform domain-specific analysis or provide actionable insights into emerging trends in AI education. This project addresses these gaps by automating data extraction, applying advanced text analysis techniques, and delivering intuitive visualizations to empower users with a deeper understanding of AI textbook content and terminology. By streamlining the process of discovering key themes, popular topics, and influential terminology, this tool supports informed decision-making in academic research, curriculum design, and literature review efforts.



This project is a web crawler tool developed using the Selenium library, specifically designed to extract information about artificial intelligence (AI) textbooks from Douban Books (www.douban.com) and perform word frequency statistical analysis.

Key Features

Data Acquisition

Employs Selenium to simulate browser interactions and automate the scraping of textbook metadata (titles, descriptions, reviews) within the AI domain from Douban Books.

Implements intelligent pagination handling and anti-crawler countermeasures.

Text Processing

Executes comprehensive text preprocessing including noise removal, tokenization, and stopword filtering.

Performs TF-IDF weighted frequency analysis to identify domain-specific keywords and terminologies.

Analytics Visualization

Generates interactive visualizations (word clouds, frequency histograms) for intuitive pattern recognition.

Exports structured datasets (CSV/JSON) and statistical reports for further analysis.
