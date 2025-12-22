import cv2
import os

VIDEO_PATH = 'data_video.mp4'
OUTPUT_FOLDER = 'raw_images'
TARGET_IMG_COUNT = 200


def extract_frames():
    if not os.path.exists(VIDEO_PATH):
        print(f"Error: Video file '{VIDEO_PATH}' not found.")
        return

    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
        print(f"Created directory: {OUTPUT_FOLDER}")

    cap = cv2.VideoCapture(VIDEO_PATH)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    if total_frames == 0:
        print("Error: Could not read video or video is empty.")
        return

    step = max(1, total_frames // TARGET_IMG_COUNT)

    print(f"Total Video Frames: {total_frames}")
    print(f"Target Image Count: {TARGET_IMG_COUNT}")
    print(f"Sampling Rate: Every {step} frame(s)")

    frame_count = 0
    saved_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % step == 0:
            img_name = f"{OUTPUT_FOLDER}/image_{saved_count:03d}.jpg"
            cv2.imwrite(img_name, frame)

            saved_count += 1
            print(f"Saved: {img_name}", end='\r')

            if saved_count >= TARGET_IMG_COUNT:
                break

        frame_count += 1

    cap.release()
    print(f"\n\nSUCCESS! Extracted {saved_count} images to '{OUTPUT_FOLDER}/'.")

if __name__ == "__main__":
    extract_frames()