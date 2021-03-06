"""
Source: https://leimao.github.io/blog/Save-Load-Inference-From-TF2-Frozen-Graph/
"""
import sys
import tensorflow as tf
from tensorflow import keras
from tensorflow.python.framework.convert_to_constants import (
    convert_variables_to_constants_v2,
)

keras.backend.clear_session()
keras.backend.set_learning_phase(0)

model_path = sys.argv[1]
model = tf.keras.models.load_model(model_path)

full_model = tf.function(lambda x: model(x))
full_model = full_model.get_concrete_function(
    tf.TensorSpec(model.inputs[0].shape, model.inputs[0].dtype)
)

# Get frozen ConcreteFunction
frozen_func = convert_variables_to_constants_v2(full_model)

layers = [op.name for op in frozen_func.graph.get_operations()]
print("-" * 50)
for layer in layers:

    # Save frozen graph from frozen ConcreteFunction to hard drive
    tf.io.write_graph(
        graph_or_graph_def=frozen_func.graph,
        logdir="./model",
        name="model.pb",
        as_text=False,
    )

print("Done!")
