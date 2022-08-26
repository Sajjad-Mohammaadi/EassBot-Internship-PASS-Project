<div align="center">
<img src="docs/source/_static/images/source_separation_io.png" width="50%">

**EassBot the English audio source separator bot in Telegram**



</div>

--------------------------------------------------------------------------------


EassBot is a Telegram bot that can receive a sound that is a combination of two sources in mp3 format and output the estimated sources. This bot uses the pretrained models of the asteroid project to calculate the output.



## Contents
- [Installation prerequisites](#installation-prerequisites)
- [Tutorials](#tutorials)
- [Available recipes](#available-recipes)
- [Supported datasets](#supported-datasets)
- [Use other Pretrained models](#use-other-pretrained-models)

## Installation prerequisites
([↑up to contents](#contents))
For running code first we need to install Asteroid, clone the repo and install it using
conda, pip or python :
```bash
# First clone and enter the repo
git clone https://github.com/asteroid-team/asteroid
cd asteroid
```

- With `pip`
```bash
# Install with pip in editable mode
pip install -e .
# Or, install with python in dev mode
# python setup.py develop
```
- With conda (if you don't already have conda, see [here][miniconda].)
```bash
conda env create -f environment.yml
conda activate asteroid
```

- Asteroid is also on PyPI, you can install the latest release with
```bash
pip install asteroid
```

## Tutorials
([↑up to contents](#contents))
Here is a list of notebooks showing example usage of Asteroid's features.if you want to use  this code you must change every directory path that exist in code to what you want.


## Available recipes
([↑up to contents](#contents))
* [x] [ConvTasnet](./egs/wham/ConvTasNet) ([Luo et al.](https://arxiv.org/abs/1809.07454))
* [x] [Tasnet](./egs/whamr/TasNet) ([Luo et al.](https://arxiv.org/abs/1711.00541))
* [x] [Deep clustering](./egs/wsj0-mix/DeepClustering) ([Hershey et al.](https://arxiv.org/abs/1508.04306) and [Isik et al.](https://arxiv.org/abs/1607.02173))
* [x] [Chimera ++](./egs/wsj0-mix/DeepClustering) ([Luo et al.](https://arxiv.org/abs/1611.06265) and [Wang et al.](https://ieeexplore.ieee.org/document/8462507))
* [x] [DualPathRNN](./egs/wham/DPRNN) ([Luo et al.](https://arxiv.org/abs/1910.06379))
* [x] [Two step learning](./egs/wham/TwoStep)([Tzinis et al.](https://arxiv.org/abs/1910.09804))
* [x] [SudoRMRFNet](./asteroid/models/sudormrf.py) ([Tzinis et al.](https://arxiv.org/abs/2007.06833))
* [x] [DPTNet](./asteroid/models/dptnet.py) ([Chen et al.](https://arxiv.org/abs/2007.13975))
* [x] [DCCRNet](./asteroid/models/dccrnet.py) ([Hu et al.](https://arxiv.org/abs/2008.00264))
* [x] [DCUNet](./asteroid/models/dcunet.py) ([Choi et al.](https://arxiv.org/abs/1903.03107))
* [x] [CrossNet-Open-Unmix](./asteroid/models/x_umx.py) ([Sawata et al.](https://arxiv.org/abs/2010.04228))
* [ ] Open-Unmix (coming) ([Stöter et al.](https://sigsep.github.io/open-unmix/))
* [ ] Wavesplit (coming) ([Zeghidour et al.](https://arxiv.org/abs/2002.08933))

## Supported datasets
([↑up to contents](#contents))
* [x] [WSJ0-2mix](./asteroid/egs/wsj0-mix) / WSJ03mix ([Hershey et al.](https://arxiv.org/abs/1508.04306))
* [x] [WHAM](./asteroid/egs/wham) ([Wichern et al.](https://arxiv.org/abs/1907.01160))
* [x] [WHAMR](./asteroid/egs/whamr) ([Maciejewski et al.](https://arxiv.org/abs/1910.10279))
* [x] [LibriMix](./asteroid/egs/librimix) ([Cosentino et al.](https://arxiv.org/abs/2005.11262))
* [x] [Microsoft DNS Challenge](./asteroid/egs/dns_challenge) ([Chandan et al.](https://arxiv.org/abs/2001.08662))
* [x] [SMS_WSJ](./asteroid/egs/sms_wsj) ([Drude et al.](https://arxiv.org/abs/1910.13934))
* [x] [MUSDB18](./asteroid/asteroid/data/musdb18_dataset.py) ([Raffi et al.](https://hal.inria.fr/hal-02190845))
* [x] [FUSS](./asteroid/asteroid/data/fuss_dataset.py) ([Wisdom et al.](https://zenodo.org/record/3694384#.XmUAM-lw3g4))
* [x] [AVSpeech](./asteroid/asteroid/data/avspeech_dataset.py) ([Ephrat et al.](https://arxiv.org/abs/1804.03619))
* [x] [Kinect-WSJ](./asteroid/asteroid/data/kinect_wsj.py) ([Sivasankaran et al.](https://github.com/sunits/Reverberated_WSJ_2MIX))

## Use other Pretrained models
([↑up to contents](#contents))
See [here](./asteroid/docs/source/readmes/pretrained_models.md)



