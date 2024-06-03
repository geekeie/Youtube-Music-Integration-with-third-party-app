# YouTube Music Integration

This project demonstrates how to integrate YouTube Music search functionality using the YouTube Data API and Flask.

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/youtube-music-integration.git
    cd youtube-music-integration
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Set your YouTube API key in an `.env` file:
    ```sh
    echo "YOUTUBE_API_KEY=your-youtube-api-key" > .env
    ```

5. Run the application:
    ```sh
    flask run
    ```

6. Open your browser and go to `http://127.0.0.1:5000`.

## License

This project is licensed under the MIT License.
