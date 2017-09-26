import tensorflow as tf
import sys
import os

#tokenise and strip class id
def extractName(tokenstring):
    tokens = tokenstring.split(' ')
    solstr = ""

    for it in range(1,len(tokens)-1):
        solstr += tokens[it] + " "
    solstr += tokens[len(tokens)-1]
    return tokens[0], solstr

def main(image_path):
    #disabling warnings, logging
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
    #path of the image
    image_data = tf.gfile.FastGFile(image_path, 'rb').read()

    #loads label file, strips off carriage return
    label_lines = [line.strip() for line in tf.gfile.GFile("output_labels.txt")]

    # Unpersists graph from file
    with tf.gfile.FastGFile("output_graph.pb", 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')

    with tf.Session() as sess:
        # Feed the image data as input to the graph an get first prediction
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
        predictions = sess.run(softmax_tensor, \
                 {'DecodeJpeg/contents:0':image_data})
        # Sort to show labels of first prediction in order of confidence
        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]

        # Print by selecting top 5 scored labels
        species_list = []
        class_list = []
        for index in range(0,5):
            label_name = label_lines[top_k[index]]
            class_id, extractedName = extractName(label_name)
            class_list.append(class_id)
            species_list.append(extractedName)

    return class_list, species_list