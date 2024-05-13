// sensor.js
// Function to fetch sensor data and update HTML elements
function fetchSensorData() {
    // Make an AJAX request to your Raspberry Pi Flask API endpoint
    fetch('http://<raspberry_pi_ip>:5000/api/sensor-data')
      .then(response => response.json())
      .then(data => {
        // Update HTML elements with sensor data
        document.getElementById('temperature').textContent = `Temperature: ${data.temperature} °C`;
        document.getElementById('humidity').textContent = `Humidity: ${data.humidity} %`;
        document.getElementById('co2').textContent = `CO₂: ${data.co2} ppm`;
      })
      .catch(error => console.error('Error fetching sensor data:', error));
  }
  
  // Call fetchSensorData function initially and every 5 seconds
  fetchSensorData();
  setInterval(fetchSensorData, 5000);
  