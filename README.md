# Separable Physics-Informed Neural Networks for Robust Inverse Quantification in Solid Mechanics

This repository contains the material corresponding to the publication: **"Separable Physics-Informed Neural Networks for Robust Inverse Quantification in Solid Mechanics"** presented at ISRERM 2024 conference.
https://www.researchgate.net/publication/385552345_Separable_Physics-Informed_Neural_Networks_for_Robust_Inverse_Quantification_in_Solid_Mechanics

## Contents

### 1. Analytical Example
We first consider a simple example introduced by Haghighat et al. (2020)[1]

- **PINN vs SPINN**:
  
https://github.com/user-attachments/assets/2d604fa6-2fb3-45ba-965d-a742a81e9b76

- **Inverse Quantification**:

https://github.com/user-attachments/assets/d1bc0645-b1de-433a-879a-4e6a74c878d0

- **Robustness to Noise**: Adding 10% of standard deviation Gaussian noise to FEM simulated displacement

![image](https://github.com/user-attachments/assets/8e89e414-70e7-442d-9162-3ddb2b4a8957)

### 2. Side Loaded Plate
- **Benchmark Example from Literature**: Comparison with other inverse quantification methods, using the benchmark example from Martins et al. (2018) [2]
- **Improved Results**: The results presented here are significantly better than those in the paper due to recent improvements:
    - **Convergence in a few minutes** instead of hours for both noise-free and noisy cases.
    - More accurate final results: **SPINN outperforms other methods for the noisy case**.
    - These improvements are mainly due to scaling the network outputs which was not done in the paper.

- **No Noise Results**: (with 16 simulated DIC points)

https://github.com/user-attachments/assets/94252fa3-7438-4a27-9d71-89fa7d5d71b0

- **Adding 10% of Std Deviation Noise**: (49 DIC points)

https://github.com/user-attachments/assets/56be40cd-8fe6-42df-b373-eb3be37991aa

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

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14039660.svg)](https://doi.org/10.5281/zenodo.14039660)

    @misc{bonnet2024spinniq,
      title={Separable Physics-Informed Neural Networks for Robust Inverse Quantification in Solid Mechanics},
      author={D. Bonnet-Eymard, A. Persoons, M. GR Faes, D. Moens},
      year={2024},
      organization={KU Leuven, TU Dortmund University},
      howpublished = {Presented at ISRERM conference, Hefei, China},
      doi={10.5281/zenodo.14039660}
    }
