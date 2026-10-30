from ultralytics import YOLO
model= YOLO("yolo11n.pt")
results= model("foto2.jpg", save=True)
print("Concluído")