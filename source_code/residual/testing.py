#import ultralytics
#ultralytics.checks()
from ultralytics import YOLO
print("imported yolo")

#model=YOLO('yolov8n-cls.pt')

#destination_directory = r'D:\VIT_Morning_Slot-main\farm_insects_ds\farm_insects_splitted'
#model.train(data=destination_directory,epochs=4)

path=r"C:\users\aakash\documents\codes\runs\classify\train5\weights\last.pt"

model = YOLO(path)
print("Model loaded successfully!")

# img_path = r"D:\VIT_Morning_Slot-main\smartbridge_project\uploads\Image_23.jpg"
# results=model(img_path)

# print(results)
# model=YOLO("yolov8n.pt","v8")
# res=model.predict(source=r"D:\VIT_Morning_Slot-main\smartbridge_project\uploads\Image_15.jpg",conf=0.25,save=True)

# print(res)

# prob_list = results[0].probs.data.tolist()
# names_dict=results[0].names
# print(names_dict[prob_list.index(max(prob_list))])




# YOLOv8n-cls summary (fused): 73 layers, 1454095 parameters, 0 gradients, 3.3 GFLOPs
# WARNING  Dataset 'split=val' not found, using 'split=test' instead.
# train: D:\VIT_Morning_Slot-main\farm_insects_ds\farm_insects_splitted\train... found 1507 images in 15 classes  
# val: None...
# test: D:\VIT_Morning_Slot-main\farm_insects_ds\farm_insects_splitted\test... found 72 images in 15 classes  
#                classes   top1_acc   top5_acc: 100%|██████████| 3/3 [00:02<00:00,  1.48it/s]
#                    all      0.806      0.958
# Speed: 0.0ms preprocess, 9.6ms inference, 0.0ms loss, 0.0ms postprocess per image
# Results saved to c:\users\aakash\documents\codes\runs\classify\train2
# Results saved to c:\users\aakash\documents\codes\runs\classify\train2
# ultralytics.utils.metrics.ClassifyMetrics object with attributes:

# confusion_matrix: <ultralytics.utils.metrics.ConfusionMatrix object at 0x000001D71030D110>
# curves: []
# curves_results: []
# fitness: 0.8819444477558136
# keys: ['metrics/accuracy_top1', 'metrics/accuracy_top5']
# results_dict: {'metrics/accuracy_top1': 0.8055555820465088, 'metrics/accuracy_top5': 0.9583333134651184, 'fitness': 0.8819444477558136}
# save_dir: WindowsPath('c:/users/aakash/documents/codes/runs/classify/train2')
# speed: {'preprocess': 0.0, 'inference': 9.603086445066664, 'loss': 0.0, 'postprocess': 0.0}
# task: 'classify'
# top1: 0.8055555820465088
# top5: 0.9583333134651184

# yolo val model="C:\\Users\\Aakash\\Documents\\codes\\runs\classify\\train5\\weights\\last.pt" data="C:\\Users\\Aakash\\Documents\\codes\\runs\classify\\train5\\args.yaml"



print(model.val())
