# Voice-Based Food Ordering System

A simple and efficient web application that allows users to place food orders using either voice or text input. The system processes the input and displays the structured order in a user-friendly table format. It is developed using HTML, JavaScript, and Python (Flask).

## Project Screenshot

<img width="915" height="432" alt="Screenshot 2025-06-08 181003" src="https://github.com/user-attachments/assets/59da549c-9d42-47f8-b381-e1eb00e30db9" />

## Features

- **Voice Recognition Support** - Utilizes the Web Speech API for hands-free ordering
- **Text-Based Input Support** - Traditional text input for users who prefer typing
- **Flask Backend** - Robust Python backend with JSON-based data storage
- **Intelligent Parsing** - Natural language processing for orders (e.g., "2 parathas and 1 lassi")
- **Real-time Order Summary** - Automatically updating order summary table
- **Asynchronous Communication** - Fully asynchronous communication using `fetch()` and APIs
- **CORS-Enabled** - Supports frontend-backend communication during local development

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python Flask
- **Voice Recognition**: Web Speech API
- **Data Storage**: JSON format (`food.json`)
- **Communication**: RESTful APIs with CORS support

## Folder Structure

```
voice-food-ordering-system/
├── app.py                    # Flask backend script
├── food.json                 # JSON file to store orders
├── requirements.txt          # Python dependencies
├── static/
│   ├── css/
│   │   └── style.css        # Custom styles
│   └── js/
│       └── script.js        # JavaScript handling voice/text input and fetch requests
├── templates/
│   └── index.html           # Frontend HTML file (served via Flask)
└── README.md                # Project documentation
└── screenshots/             # This folder contains screenshots
```

## Setup Instructions

### Prerequisites
- Python 3.7 or higher
- Modern web browser with Web Speech API support (Chrome, Firefox, Safari)

### 1. Clone or Download the Repository
Clone the repository using Git or download the ZIP file and extract it locally.

```bash
git clone https://github.com/your-username/voice-food-ordering-system.git
cd voice-food-ordering-system
```

### 2. Set Up the Python Backend
Install the required Python dependencies and run the Flask server:

```bash
# Install dependencies
pip install -r requirements.txt

# Run the Flask application
python app.py
```

The backend server will start running on `http://localhost:5000`

### 3. Access the Application
Open your web browser and navigate to:
```
http://localhost:5000
```

The application will be served directly through Flask.

## Usage

### Voice Input
1. Click the **"Start Voice Recognition"** button
2. Speak your order clearly (e.g., "I want 2 parathas and 1 lassi")
3. The system will process your speech and add items to your order

### Text Input
1. Type your order in the text input field
2. Use natural language (e.g., "3 samosas and 2 teas")
3. Click **"Add to Order"** or press Enter

### Order Management
- View your complete order in the summary table
- Items are automatically parsed and quantities are calculated
- Orders are stored in `food.json` for persistence

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Serves the main application page |
| `POST` | `/add_order` | Adds new items to the order |
| `GET` | `/get_orders` | Retrieves current order data |

## Customization

### Styling
Modify `static/css/style.css` to customize the appearance of the application.

### Menu Items
Update the parsing logic in `app.py` to recognize additional food items and their variations.

### Voice Commands
Enhance the speech recognition patterns in `static/js/script.js` for better accuracy.

## Browser Compatibility

| Browser | Voice Recognition | Text Input | Overall Support |
|---------|------------------|------------|-----------------|
| Chrome | ✅ | ✅ | Full Support |
| Firefox | ✅ | ✅ | Full Support |
| Safari | ⚠️ | ✅ | Limited Voice Support |
| Edge | ✅ | ✅ | Full Support |

*Note: Voice recognition requires HTTPS in production environments*

## Troubleshooting

### Common Issues

**Voice Recognition Not Working:**
- Ensure microphone permissions are granted
- Use HTTPS in production (required by Web Speech API)
- Check browser compatibility

**Backend Connection Issues:**
- Verify Flask server is running on port 5000
- Check CORS configuration in `app.py`
- Ensure `food.json` file exists and has proper permissions

**Order Not Saving:**
- Check write permissions for `food.json`
- Verify JSON file format is valid
- Check Flask console for error messages

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Acknowledgments

- Web Speech API for voice recognition capabilities
- Flask community for the excellent web framework
- Contributors and testers who helped improve this project

---

**Star this repository if you found it helpful!**
