[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/code-written-by-chatgpt-ai-ftw.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)

# Basic Search App

This is a simple search application built with Python using the Tkinter library. It allows users to search for images and get summaries from Wikipedia. The application fetches images from Pexels and summaries from Wikipedia to display relevant information based on the user's input.

## Features

- Search for images using the Pexels API.
- Fetch and display summaries from Wikipedia.
- Display search results including images and text summaries.
- Clickable link to Wikipedia for more information.

## Requirements

- Python 3.x
- `tkinter` (usually included with Python)
- `PIL` (Pillow) - for image processing
- `requests` - for making HTTP requests

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/codewithj4ke/basic-search-app.git
    cd basic-search-app
    ```

2. **Install required packages**:
    ```sh
    pip install pillow requests
    ```

## API Keys

- Replace `PEXELS_API_KEY` with your own Pexels API key. You can obtain an API key by signing up at [Pexels](https://www.pexels.com/api/).

## Usage

1. **Run the application**:
    ```sh
    python main.py
    ```

2. **Search for images and summaries**:
    - Enter a search query in the text field.
    - Click the "Search" button or press the `Enter` key.
    - The application will display a random image related to the query and a summary from Wikipedia.

## Code Overview

- `fetch_image(query)`: Fetches a random image from Pexels based on the search query.
- `facts_link(query)`: Generates a Wikipedia link for the search query.
- `fetch_summary(query)`: Fetches a summary from Wikipedia.
- `on_button_click()`: Handles the button click event to fetch and display image and summary.
- `on_enter(event)`: Handles the Enter key press to trigger the search.

## Screenshots

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to Pexels for providing free image APIs.
- Wikipedia for accessible summaries and information.
- The Python and Tkinter community for extensive resources and support.

## Contact

For questions or feedback, please reach out to [Jake](mailto:thectzn@gmail.com).
