from keras.models import load_model

# load model
model = load_model('model.h5')

import numpy as np
from keras.preprocessing import image

test_image = image.load_img('image.png', target_size = (28,28))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = model.predict(test_image)

predicted_class_indices=np.argmax(result,axis=1)

labels = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 
          'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 
          'Z': 25}

labels = dict((v,k) for k,v in labels.items())
prediction = [labels[k] for k in predicted_class_indices]
print(prediction)
