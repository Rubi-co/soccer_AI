import cv2
import os

input_video = "football.mp4"
output_directory = "frames"

# Создание папок если отсутствуют
os.makedirs(output_directory, exist_ok=True)

# открытие видео, как объекта
cap = cv2.VideoCapture(input_video)

if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

frame_count = 0

while True:
	# чтение кадра
    ret, frame = cap.read()

	# завершение чтение видео если кадры закончились
    if not ret:
        break

	# построение путя сохранения файла
	# в фигурных скобрах происходит встраивание переменной `frame_count` в название файла, где `:04d` указывает, что минимальная длинна числа 4 символа "4" -> "0004"
    frame_filename = os.path.join(output_directory, f"frame_{frame_count:04d}.jpg")
    # сохранение кадра по пути
    cv2.imwrite(frame_filename, frame)

    frame_count += 1

# закрытие потока видео
cap.release()

print(f"Extracted {frame_count} frames.")

cv2.destroyAllWindows()
