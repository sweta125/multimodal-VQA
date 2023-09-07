# Stop Token Generation

## defaults_stop.yaml
config file for M4C with stop token generation with STVQA.

## defaults_stop_textvqa.yaml
config file for M4C with stop token generation with TextVQA.

## losses.py
Updated losses.py with M4C loss with stop token loss.\
Replace the original losses.py with updated losses.py in mmf/mmf/modules

## m4c.py
Updated m4c.py with stop token prediction layer.\
Replace the original m4c.py in mmf/mmf/models\
(Need to find a way to create a separate file, like m4c_stop.py, instead of replacing)

## stop_token.txt
Detailed descriptions of what was implmenented.

## run command
mmf_run config=projects/m4c/configs/stvqa/defaults_stop.yaml model=m4c dataset=stvqa run_type=train_val training.batch_size=80
mmf_run config=projects/m4c/configs/textvqa/defaults_stop_textvqa.yaml model=m4c dataset=textvqa run_type=train_val training.batch_size=80 checkpoint.resume=True [checkpoint.resume_best=True] training.checkpoint_interval=500
