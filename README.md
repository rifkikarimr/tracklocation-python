# Phone Number Geolocation Tracker

This script tracks the geolocation, service provider, and coordinates of a given phone number and visualizes the location on an interactive map.

---

## Features

1. **Location Tracking**: Displays the approximate geographic location of the phone number.
2. **Service Provider Identification**: Shows the telecom carrier of the phone number.
3. **Geolocation Coordinates**: Provides latitude and longitude coordinates of the location.
4. **Interactive Map**: Generates an HTML file with a map highlighting the location.

---

## Prerequisites

- **Python 3.x**: Ensure Python is installed on your system.
- **Libraries**:
  - `phonenumbers`: To parse and retrieve phone number details.
  - `opencage`: For geocoding the location.
  - `folium`: For creating an interactive map.
- **OpenCage API Key**: A valid OpenCage Geocoder API key is required.

---

## Installation

1. Clone this repository:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. Install Required Python libraries:
   `pip install phonenumbers opencage folium`

3. Replace the placeholder `number` variable with a valid phone number (including country code). Example:
   `number = "+1234567890"`

4. Replace the `key` variable with your OpenCage API Key:
   `key = $key`

## Usage 
1. Run the script:
   `python script_name.py`
2. The script will:
   - Print the location and service provider in the terminal
   - Save a file named `thelocation.html` with an interactive map.
3. Open `thelocation.html` in a web browser to view the location on the map.

## Example Output

Terminal Output:
```bash
Location: New York, United States
Service Provider: Verizon Wireless
Latitude: 40.7128, Longitude: -74.0060
```
Generated Map: Opens in the browser with a marker indicating the location.

## Notes
- **Ensure the phone number includes the correct country code.**
- **The location accuracy depends on the phone number's availability in the geocoder database.**
- **Replace the OpenCage API key with your personal key to avoid quota limits.**
