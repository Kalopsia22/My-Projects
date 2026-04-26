# Object Detection + Distance Estimation for Robotics Navigation  

---
# Contact Info 🔗

## Your Full Name:- Atharva Rewatkar | Phone Number:- 9004927409 | Email:- atharvarewatkar050@gmail.com

A modular pipeline for detecting navigation-relevant objects (cones, barriers, stop signs)
and estimating their distance from a robot's camera using monocular geometry.
Includes edge-device optimization via quantization, pruning, and lightweight backbones.

---

## Project Structure

```
robotics_perception/
├── configs/
│   └── config.yaml              # All hyperparameters and paths
├── data/
│   └── dataset.py               # BDD100K dataset loader & preprocessing
├── models/
│   ├── detector.py              # YOLOv8 transfer learning wrapper
│   └── distance_estimator.py    # Monocular distance estimation
├── utils/
│   ├── visualizer.py            # Bounding box + distance annotation
│   ├── metrics.py               # mAP, FPS, latency benchmarking
│   └── logger.py                # Structured logging
├── scripts/
│   ├── prepare_dataset.py       # Filter BDD100K → cones/barriers/stop signs
│   ├── train.py                 # Fine-tuning script
│   ├── infer.py                 # Run inference on images/video
│   ├── optimize.py              # Quantization + pruning pipeline
│   └── benchmark.py            # CPU vs GPU FPS comparison
├── results/                     # Saved outputs, charts, model weights
├── notebooks/
│   └── exploration.ipynb        # EDA + visualizations
└── requirements.txt
```

---

## Quickstart

```bash
pip install -r requirements.txt

# 1. Prepare dataset (filter BDD100K to target classes)
python scripts/prepare_dataset.py --data_root /path/to/bdd100k

# 2. Train (fine-tune YOLOv8 on your filtered dataset)
python scripts/train.py --config configs/config.yaml

# 3. Run inference with distance annotation
python scripts/infer.py --source /path/to/images --weights results/best.pt

# 4. Optimize for edge devices
python scripts/optimize.py --weights results/best.pt --method quantize

# 5. Benchmark CPU vs GPU FPS
python scripts/benchmark.py --weights results/best.pt
```

---

## Distance Estimation

Uses monocular geometry based on known object real-world heights:

```
distance (m) = (real_height × focal_length) / pixel_height
```

Known heights used:
- Traffic cone: 0.75 m
- Barrier: 1.0 m
- Stop sign: 0.9 m

---

## Optimization Techniques

| Method           | Tool                  | Expected Speedup |
|------------------|-----------------------|------------------|
| INT8 Quantization| PyTorch / ONNX Runtime| 2–4× on CPU      |
| Structured Pruning| torch.nn.utils.prune | 1.5–2× + smaller |
| MobileNetV3 backbone | Ultralytics swap  | 3–5× lighter     |

---

## Requirements

- Python 3.9+
- PyTorch 2.0+
- Ultralytics (YOLOv8)
- OpenCV
- ONNX Runtime

---

## Contact Info

- **Name:** Your Full Name
- **Contact Number:** Your Contact Number
- **Email Address:** your.email@example.com
