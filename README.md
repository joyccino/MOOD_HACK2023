# Mood Light For Your Mood

Welcome to the Mood Light Hackathon project repository! In this hackathon project, we are creating a mood light that responds to your emotions. The light's color will change based on the detected emotion from your face using the 'deepface' Python library. Additionally, the emotion data will be stored in a MongoDB Cloud database for further analysis.

## Prerequisites

Before you get started, make sure you have the following:

- Python version: 3.8.8
- Git installed on your machine
- An active internet connection

## Installation

Follow these steps to set up the project:

1. Clone the repository to your local machine using the following command:

   ```bash
   git clone https://github.com/your-username/your-mood-light.git
   ```

2. Navigate to the project directory:

   ```bash
   cd mood_detector_deepface_to_db.py
   ```

3. Install the required dependencies using `pip3` by running:

   ```bash
   pip3 install -r requirements.txt
   ```

   This will install all the necessary libraries and packages needed for the project.

## Usage

1. Make sure you have a camera connected to your computer.

2. Run the main script to start the mood light:

   ```bash
   python3 mood_light.py
   ```

   This script captures video from your camera, detects faces, extracts emotions using the 'deepface' library, and controls the mood light accordingly.

## Configuration

Before running the project, you need to configure the MongoDB connection. Open the `config.py` file and provide your MongoDB Cloud credentials:

```python
# config.py

MONGO_URI = "your-mongodb-uri"
```

Replace `"your-mongodb-uri"` with your actual MongoDB Cloud URI.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and create a pull request with your changes. We welcome contributions!

## License

This project is licensed under the [MIT License](LICENSE).

---

We hope you enjoy working on the Mood Light Hackathon project! If you have any questions or run into issues, feel free to open an issue on this repository. Happy hacking!
