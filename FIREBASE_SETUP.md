# Firebase Firestore setup

The app uses Firestore when `FIREBASE_SERVICE_ACCOUNT` is configured. Without that variable it uses `data.json`, so the pages can still be demonstrated offline.

## 1. Create a Firebase project

1. Open the Firebase Console and create a project.
2. Enable **Cloud Firestore**.
3. Open Project settings, Service accounts, and create a private key.
4. Store the downloaded JSON outside the repository, for example:
   `C:\\Users\\your-name\\.firebase\\unicanteen-service-account.json`

## 2. Configure the environment

PowerShell for the current terminal:

```powershell
$env:FIREBASE_SERVICE_ACCOUNT = "C:\\Users\\your-name\\.firebase\\unicanteen-service-account.json"
```

The adapter also accepts the complete service-account JSON string in the same variable, but a file path is easier for students.

Do not commit the key. The repository ignores `.env` and service-account JSON files.

## 3. Install and run

```powershell
python -m pip install -r requirements.txt
python app.py
```

Open `/page1`, `/page2`, and `/page3`. The page badge shows whether the current backend is Firestore or local JSON.

## Firestore structure

The adapter creates a `restaurants` collection. Each restaurant is a document, and its menus are stored in a `menus` subcollection. Reviews remain inside the restaurant document for this beginner project so rating aggregation stays easy to explain.

A service account is server-only. Never put its key in a template, JavaScript file, `data.json`, or browser request.
