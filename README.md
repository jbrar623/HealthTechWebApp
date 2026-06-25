# GuardDog: Worker Heat Stress Prevention Device

**Project Status**: Inactive

## Project Intro / Objective

As the environment changes rapidly, outdoor and industrial workers face increasing risks from unpredictable air quality and extreme temperatures. Our team was tasked with identifying an environmental threat and developing a viable technological intervention. After consulting with industry professionals, we identified a critical gap: real-time, localized data for workers in high-risk zones.

### The GuardDog

We engineered a functional proof-of-concept — a portable, real-time detection device designed to monitor critical environmental factors simultaneously:

- **CO2 and CO:** Monitoring for poor ventilation and respiratory safety.
- **Methane:** Providing early warning for explosive or asphyxiant gas leaks.
- **Ambient Temperature:** Protecting workers from heat stress and thermal exhaustion.

The device provides immediate, localized feedback, allowing workers to make split-second safety decisions that broad-area sensors might miss. By integrating these four sensors into a single portable unit, we bridged the gap between complex industrial hardware and accessible safety tech.

GuardDog is a project developed as part of the 2024 cohort of the HealthTech Challenge with the Institute for Innovation and Entrepreneurship @ MRU.

## Team

| Name | LinkedIn |
|---|---|
| Joban Brar | [joban](https://www.linkedin.com/in/joban-brar) |
| Shweta Limbu | [shweta](https://www.linkedin.com/in/shweta-limbu/) |
| Nate Ostojic | [nate](https://www.linkedin.com/in/-fields/) |
| Edward Montilla | [edward](https://www.linkedin.com/in/gabrieledwardmontilla/) |
| Christopher Lassota | [chris](https://www.linkedin.com/in/christopherlassota/) |

## Components, Tools & Technologies

**Hardware**
- Raspberry Pi 4
- Touch Screen Display
- Speakers
- Fans
- 3D Printed Casing

**Sensors**
- Air Particulates
- Humidity
- Hydrogen Sulfide (H2S)
- Methane (CH4)
- Carbon Monoxide (CO)
- Carbon Dioxide (CO2)

**Software**
- Python
- JavaScript
- JSON
- HTML
- CSS
- Flask

## Running GuardDog on Raspberry Pi

### 1. Transfer Project Files

Copy the project folder from your laptop to the Raspberry Pi using SCP, SFTP, Git, or a USB drive.

```bash
scp -r GuardDog/ pi@<raspberry_pi_ip>:/home/pi/
```

### 2. Connect to the Raspberry Pi

```bash
ssh pi@<raspberry_pi_ip>
```

### 3. Install Required Dependencies

```bash
pip install flask adafruit-blinka adafruit-circuitpython-scd4x
```

### 4. Run the Flask Application

Navigate to the project directory and start the Flask server:

```bash
cd GuardDog
python app.py
```

The web application will be available at:

```
http://<raspberry_pi_ip>:5000
```

### 5. View the Dashboard

Open a web browser on the Raspberry Pi or another device on the same network and navigate to:

```
http://<raspberry_pi_ip>:5000
```

The dashboard will automatically retrieve and display live temperature, humidity, and CO₂ sensor data from the SCD-41 sensor using Flask and JavaScript.

### Optional: Run on Startup

To automatically launch the GuardDog dashboard when the Raspberry Pi boots, configure the Flask application as a systemd service or add it to the Raspberry Pi startup sequence.
