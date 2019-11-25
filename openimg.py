import cv2

img_name = input("Image name: ")

img = cv2.imread(img_name)

print(img.shape)

cv2.imshow(window, img)
cv2.waitkey(0)
