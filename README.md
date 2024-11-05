# Separable Physics-Informed Neural Networks for Robust Inverse Quantification in Solid Mechanics

This repository contains the material corresponding to the publication: **"Separable Physics-Informed Neural Networks for Robust Inverse Quantification in Solid Mechanics"** presented at ISRERM 2024 conference.

## Contents

### 1. Analytical Example
We first consider a simple example introduced by Haghighat et al. (2020)[1]

- **PINN vs SPINN**:
![image](https://github.com/bonneted/ISRERM2024/blob/main/analytical_example/results_forward/videos/Ux_time_pfnn_10min_vs_spinn_10min.mp4

- **Inverse Quantification**:
PINN:
![image](https://github.com/bonneted/ISRERM2024/blob/main/analytical_example/results_inverse/pfnn_lmbd-2.0_mu-0.3_nDIC-100_300000iter/Ux-Uy_time.mp4)
SPINN:
![image](https://github.com/bonneted/ISRERM2024/blob/main/analytical_example/results_inverse/spinn_lmbd-2.0_mu-0.3_nDIC-100_100000iter/Ux-Uy_time.mp4)

- **Robustness to Noise**: Adding 10% of standard deviation gaussian noise

### 2. Side Loaded Plate
- **Benchmark Example from Literature**: Comparison with other inverse quantification methods, using the benchmark example from Martins et al. (2018) [2]
- **Improved Results**: The results presented here are significantly better than those in the paper due to recent improvements:
    - **Convergence in few minutes** instead of hours for both noise free and noisy cases.
    - More accurate final results: **SPINN outperforms other methods for the noisy case**.
    - These improvements are mainly due to the scaling of the network outputs that was not done in the paper.

- **No Noise Results**:
![image](https://github.com/bonneted/ISRERM2024/blob/main/side_loaded_plate/results_inverse/spinn_E-100000.0_nu-0.2_nDIC-16_noise-0_5min/Ux-Uy-Sxx-Syy-Sxy_time.mp4)
- **Adding 10% of Std Deviation Noise**: [Video Placeholder for 10% Noise Results](path/to/video)
![image](https://github.com/bonneted/ISRERM2024/blob/main/side_loaded_plate/results_inverse/spinn_E-100000.0_nu-0.2_nDIC-49_noise-0.1_5min/Ux-Uy-Sxx-Syy-Sxy_time.mp4)

## How to Use
1. Install the custom deepxde library with SPINN implemented :
pip install git+https://github.com/bonneted/deepxde.git@ISRERM2024

2. Clone the repository.
3. The results .dat files are not stored in the repository due to size constraints. You can generate the results using the parameters in the config files.

## References
[1] R. Juanes, “A deep learning framework for solution and discovery in solid mechanics,” arXiv:2003.02751[cs, stat], May 2020.
[2] J. Martins, A. Andrade-Campos, and S. Thuillier, “Comparison of inverse identification strategies for constitutive mechanical models using full-field measurements,” International Journal of Mechanical Sciences, vol. 145, pp. 330–345, Sep. 2018.

## Citation
If you use this framework in your research, please consider citing our paper:

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.13907104.svg)](https://doi.org/10.5281/zenodo.13907104)

    @inproceedings{bonnet2024pinnpc,
      title={Physics-Informed Neural Networks to Propagate Random Field Properties of Composite Materials},
      author={D. Bonnet-Eymard, A. Persoons, P. Gavallas, M. GR Faes, G. Stefanou, D. Moens},
      booktitle={Proceedings of ISMA-USD 2024},
      year={2024},
      organization={KU Leuven, Aristotle University of Thessaloniki, TU Dortmund University},
      doi={10.5281/zenodo.13907104}
    }