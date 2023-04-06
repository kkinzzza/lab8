import cv2
image = cv2.imread("/Users/djinja/Downloads/variant-3.jpeg")  # путь к файлу необходимо переопределить
hsv_image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
cv2.imshow("result", hsv_image)
cv2.waitKey(5)