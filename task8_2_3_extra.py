import time
import cv2


def tracking():
    video = cv2.VideoCapture(1)
    fly_image = cv2.imread("/Users/djinja/Downloads/fly64.png")  # путь к файлу необходимо переопределить
    down_points = (640, 480)
    i = 0
    while True:
        ret, frame = video.read()
        if not ret:
            break
        frame = cv2.resize(frame, down_points, interpolation=cv2.INTER_LINEAR)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        ret, thresh = cv2.threshold(gray, 110, 255, cv2.THRESH_BINARY_INV)

        contours, hierarchy = cv2.findContours(thresh,
                                               cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        if len(contours) > 0:
            c = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (230, 135), (430, 335), (0, 0, 225), 2)
            if (x + (w // 2)) >= 230 and (x + (w // 2)) <= 430 and (y + (w // 2)) >= 135 and (y + (w // 2)) <= 335:
                cv2.rectangle(frame, (230, 135), (430, 335), (0, 225, 0), 2)  # задание 3
            # cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)  # задание 2
            if i % 5 == 0:
                a = x + (w // 2)
                b = y + (h // 2)
                print(a, b)

                fly_resized = cv2.resize(fly_image, (a, b))
                for i in range(b):
                    for j in range(a):
                        if (fly_resized[i, j, 0] < 250) & (fly_resized[i, j, 1] < 250) & (fly_resized[i, j, 2] < 250):
                            frame[y + i, x + j] = fly_resized[i, j]

        cv2.imshow('Tracking', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        time.sleep(0.1)
        i += 1

    video.release()


if __name__ == '__main__':
    tracking()

cv2.destroyAllWindows()
