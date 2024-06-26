<div align="center">

# Myria3D: Aerial Lidar HD Semantic Segmentation with Deep Learning
# Fork adapted to train/infer on non-colorized data


Myria3D is a deep learning library designed with a focused scope: the multiclass semantic segmentation of large scale, high density aerial Lidar points cloud.

This fork includes option to train on Lidar HD data without RGB attributes. It also implements the PointNet baseline. Two pretrained models are available, RandLaNet and PointNet, in the form of .ckpt files with the best version of the model. The models were trained on the same twelve Lidar HD tiles, list of the tiles trained upon is in trained_model_assets/lidarhd_dataset_split.csv. Training metrics can be observed on Comet: https://shorturl.at/QHZVd

The training was performed on a laptop with 3070Ti GPU (8GB VRAM), 32 GB RAM and i7-12700H. Batch sizes were adapted to the specifications.
PointNet implementation subsamples the 50x50m tiles to 4096 points, then upsamples with 1-nn. RandLaNet remains unchanged.

___

Please cite Myria3D if it helped your own research. Here is an example BibTex entry:
```
@misc{gaydon2022myria3d,
  title={Myria3D: Deep Learning for the Semantic Segmentation of Aerial Lidar Point Clouds},
  url={https://github.com/IGNF/myria3d},
  author={Charles Gaydon},
  year={2022},
  note={IGN (French Mapping Agency)},
}
```
