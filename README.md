# 📇 Contact Management System (Web-based)

A simple Contact Management System built using **python** that runs directly in your browser.
It allows users to add, view, edit, and delete contacts with persistent storage using `localStorage`.

## 🚀 Features

- ✅ Add new contacts (name, phone, email)
- ✅ View all saved contacts
- ✅ Edit existing contact information
- ✅ Delete contacts
- ✅ Persistent storage using `localStorage`
- ✅ Clean and simple UI

---

## 🖥️ How to Run

### Option 1: Open in Browser
1. Download or copy the `contact_management.html` file.
2. Double-click the file to open it in your default browser.
3. Start managing your contacts.

### Option 2: Run in Visual Studio Code using Live Server
1. Open the folder in **VS Code**.
2. Install the **Live Server** extension (if not already installed).
3. Right-click on `contact_management.html` → Click **“Open with Live Server”**.
4. It will open in a new browser tab.

---

## 💾 Data Storage

This app uses the browser's `localStorage`, which means:
- Contacts are stored even after you close and reopen the browser.
- No external database or backend is needed.

To clear all contacts, simply open the **Developer Console** and run:
```js
localStorage.clear();
