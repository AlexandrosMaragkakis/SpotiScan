# SpotiScan

This project is a Python script that uses the Spotify API to retrieve a user's saved tracks and their respective genres. It then counts the number of occurrences of each genre and displays the top 10 genres.

## Prerequisites

Before you can use this script, you need to create a Spotify app to obtain a client ID, client secret, and redirect URI. Here's how:

1. Log in to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) using your Spotify account.

2. Click the "Create app" button and fill in the necessary information (e.g., app name, app description).

3. Once your app is created, click on its name to view its details.

4. Under "Redirect URIs", add the following URI: `http://localhost:8000/redirect` .

5. Note down the "Client ID" and "Client Secret" values displayed on the app details page. You'll need to use these values in the next section.

## Usage

### Linux

1. Clone the repository and navigate to the project directory:

   ```
   git clone https://github.com/AlexandrosMaragkakis/SpotiScan.git
   cd SpotiScan
   ```

2. Create a virtual environment and activate it:

   ```
   python3 -m venv env
   source env/bin/activate
   ```

3. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Create a copy of the `config.py.template` file and rename it to `config.py`, then replace the placeholder values with your actual Spotify client ID, client secret, and redirect URI.

5. Run the script:

   ```
   python app.py
   ```

### Windows

1. Clone the repository and navigate to the project directory:

   ```
   git clone https://github.com/AlexandrosMaragkakis/SpotiScan.git
   cd SpotiScan
   ```

2. Create a virtual environment and activate it:

   ```
   python -m venv env
   env\Scripts\activate
   ```

3. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Create a copy of the `config.py.template` file and rename it to `config.py`, then replace the placeholder values with your actual Spotify client ID, client secret, and redirect URI.

5. Run the script:

   ```
   python app.py
   ```

That's it! The script should now run and display the top 10 genres of your saved Spotify tracks.
