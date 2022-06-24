# multimodal-VQA
Understanding text in images for Visual Question Answering

Recent work in Visual Question Answering (VQA) has shown that state-of-the-art models fall short in detecting and semantically understand- ing “scene text,” or text present in images that is required to understand the image fully. 
Though there has been work in OCR, object detection, and VQA, most VQA work has not directly focused on the detection and understanding of scene text. 
In this repo, we use an M4C model to implement three main approaches to better solve this problem: stop token prediction, a global multimodal transformer to learn latent graphical representations between modalities, and additional pre-training and fine-tuning using a larger dataset, OCR-VQA.
