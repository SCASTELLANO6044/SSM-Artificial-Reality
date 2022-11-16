# import the opencv library
import cv2

# define a video capture object
vid = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()

while vid.isOpened():
    # Capture the video frame by frame
    ret, frame = vid.read()

    data, bbox, straight_qrcode = detector.detectAndDecode(frame)

    scale_percent = 150  # percent of original size
    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    dim = (width, height)
    # marco =
    frame = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

    if data == 'image:1':
        print('Accepted QR')

    # Display the resulting frame
    cv2.imshow('frame', frame)
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()