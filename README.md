Perfect 🚀 This project captures webcam frames, saves them, and logs metadata into **SQLite**. Here's a **README.md** you can use on GitHub:

---

# 📸 Webcam Frame Capture with Metadata Logging

This project captures frames from a webcam using **OpenCV**, saves them locally as image files, and stores their metadata (timestamp & filename) in an **SQLite database**.

---

## 🚀 Features

* Captures **N frames** from the webcam (default: 5).
* Saves frames in the `captured_frames/` folder.
* Stores metadata (timestamp, filename) in an **SQLite database**.
* Displays live camera feed while capturing.
* Press **Q** to stop early.

---

## ⚙️ Requirements

Install dependencies using:

```bash
pip install opencv-python
```

(SQLite and `os`, `time` are built-in, no need to install them).

---

## ▶️ How to Run

1. Clone the repository / download the script.
2. Run the script:

```bash
python capture_frames.py
```

3. The program will:

   * Create a folder `captured_frames/` (if not already present).
   * Capture **5 frames** (1 per second).
   * Save each frame as `frame_<count>_<timestamp>.jpg`.
   * Insert metadata into `frame_metadata_db` under table `frame_info`.

---

## 📊 Database Structure

SQLite database: `frame_metadata_db`
Table: `frame_info`

| Column    | Type    | Description                  |
| --------- | ------- | ---------------------------- |
| id        | INTEGER | Auto-increment primary key   |
| timestamp | TEXT    | Time when frame was captured |
| filename  | TEXT    | Path of saved frame image    |

---

## 📂 Example Output

### Captured Images (in `captured_frames/`):

```
captured_frames/
├── frame_0_250820-103000.jpg
├── frame_1_250820-103001.jpg
├── frame_2_250820-103002.jpg
...
```

### Database Records (in `frame_metadata_db`):

```sql
SELECT * FROM frame_info;

id | timestamp   | filename
-----------------------------------------------
1  | 250820-103000 | captured_frames/frame_0_250820-103000.jpg
2  | 250820-103001 | captured_frames/frame_1_250820-103001.jpg
```

---

## 🛠 Customization

* Change **`total_frames=5`** in the script to capture more/less frames.
* Modify **delay** (`cv2.waitKey(1000)`) to adjust time gap between captures.
* Update **database name** (`frame_metadata_db`) if you want a different DB file.

---

## ✅ Use Cases

* Logging frames for **motion detection**.
* Building **datasets** for computer vision projects.
* Storing image references in a database for later retrieval.
 
