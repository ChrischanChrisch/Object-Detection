# model_main_tf2.py
# individuell angepasst werden müssen die Zeilen 23, 24

#from absl import flags
import os
import tensorflow.compat.v2 as tf
from object_detection import model_lib_v2
import time

Path_to_scripts = r'C:\Tensorflow2\workspace\Training_demo'
model_dir = os.path.join(Path_to_scripts, 'models\my_model')
pipeline_config_path = os.path.join(model_dir, 'pipeline.config')
num_train_steps = None
eval_on_train_data = False
sample_1_of_n_eval_examples = None
sample_1_of_n_eval_on_train_examples = 5
checkpoint_dir = model_dir
eval_timeout = 60
use_tpu = False
num_train_steps = None
num_workers = 1
checkpoint_every_n = 1000
record_summaries = True

def main(_):

  if checkpoint_dir:
    model_lib_v2.eval_continuously(
        pipeline_config_path=pipeline_config_path,
        model_dir=model_dir,
        train_steps=num_train_steps,
        sample_1_of_n_eval_examples=sample_1_of_n_eval_examples,
        sample_1_of_n_eval_on_train_examples=(
            sample_1_of_n_eval_on_train_examples),
        checkpoint_dir=checkpoint_dir,
        wait_interval=300, timeout=eval_timeout)
  else:
    if use_tpu:
      # TPU is automatically inferred if tpu_name is None and
      # we are running under cloud ai-platform.
      resolver = tf.distribute.cluster_resolver.TPUClusterResolver(
          tpu_name)
      tf.config.experimental_connect_to_cluster(resolver)
      tf.tpu.experimental.initialize_tpu_system(resolver)
      strategy = tf.distribute.experimental.TPUStrategy(resolver)
    elif num_workers > 1:
      strategy = tf.distribute.experimental.MultiWorkerMirroredStrategy()
    else:
      strategy = tf.compat.v2.distribute.MirroredStrategy()

    with strategy.scope():
      model_lib_v2.train_loop(
          pipeline_config_path=pipeline_config_path,
          model_dir=model_dir,
          train_steps=num_train_steps,
          use_tpu=use_tpu,
          checkpoint_every_n=checkpoint_every_n,
          record_summaries=record_summaries)

if __name__ == '__main__':
    start_time = time.perf_counter()
    #main()
    tf.compat.v1.app.run()
    end_time = time.perf_counter() - start_time
    print('Evaluierung abgeschlossen: Dauer = ', end_time)
  #tf.compat.v1.app.run()
