# 🔐 Zoom Server-to-Server OAuth Integration in Python

This project provides a simple **Python wrapper** around Zoom's REST API using **Server-to-Server OAuth authentication**. It allows you to:

- 🔄 Authenticate securely with Zoom
- 📅 Create Zoom meetings
- 📖 Retrieve meeting information
- ❌ Delete meetings

Built using Python's `requests` library.

---

## 📦 Features

- ✅ Server-to-Server OAuth flow (no user interaction)
- ✅ Create scheduled meetings
- ✅ Fetch meeting details
- ✅ Delete meetings
- 🔒 Token-based authentication using your Zoom app credentials

---

## ⚙️ Prerequisites

- Python 3.6+
- A Zoom App with **Server-to-Server OAuth** enabled from the [Zoom App Marketplace](https://marketplace.zoom.us/)

---

## 🗂️ Project Structure
```mathematica
├── zoom.py # Main script
├── README.md # This documentation
```
---


---

## 🔐 Get Your Zoom Credentials

1. Log into [Zoom App Marketplace](https://marketplace.zoom.us/)
2. Create a new **Server-to-Server OAuth** app
3. Note down the following from the App Credentials tab:
   - Client ID
   - Client Secret
   - Account ID

---

## 📥 Installation

Clone this repository:


    git clone https://github.com/yourusername/zoom-server-oauth.git
    cd zoom-server-oauth

## Install dependencies:
    pip install requests

---

🚀 Usage
1. Initialize Zoom Meeting API
```
    from zoom_server_oauth import Zoommeeting
    
    client_id = "YOUR_CLIENT_ID"
    account_id = "YOUR_ACCOUNT_ID"
    client_secret = "YOUR_CLIENT_SECRET"
    
    zoommeeting = Zoommeeting(client_id, account_id, client_secret)
```
2. Create a Meeting

```
    zoommeeting.CreateMeeting(
        topic="Team Sync",
        duration=60,
        start_date="2025-05-20",
        start_time="14:30",  # HH:MM
        password="secure123"
    )
```

3. Get Meeting Info
```
    zoommeeting.GetMeetingInfo("MEETING_ID")
```
4. Delete a Meeting
```
    zoommeeting.DeleteMeeting("MEETING_ID")
```



