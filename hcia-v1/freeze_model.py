import tensorflow as tf
from tensorflow.keras import backend as K


def freeze_session(session, keep_var_names=None, output_names=None, clear_devices=True):
    graph = session.graph
    with graph.as_default():
        freeze_var_names = list(set(v.op.name for v in tf.global_variables()).difference(keep_var_names or []))
        output_names = output_names or []
        output_names += [v.op.name for v in tf.global_variables()]
        input_graph_def = graph.as_graph_def()
        if clear_devices:
            for node in input_graph_def.node:
                node.device = ""
        frozen_graph = tf.graph_util.convert_variables_to_constants(
            session, input_graph_def, output_names, freeze_var_names)
        return frozen_graph

def freeze_model(model_h5_path='model.h5'):
  K.set_learning_phase(0)
  model = tf.keras.models.load_model(model_h5_path)
  frozen_graph = freeze_session(K.get_session(),
                                output_names=[out.op.name for out in model.outputs])

  tf.train.write_graph(frozen_graph, "model", "model.pb", as_text=False)


if __name__ == "__main__":
    freeze_model()
