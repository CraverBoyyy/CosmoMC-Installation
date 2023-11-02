
CosmoMC: Installation and Using Guide
===================
This project will guide you through the detailed installation process of CosmoMC. It includes instructions for compiling and running on both a computer and a cluster. Additionally, it demonstrates how to analyze the chains from CosmoMC and generate 2D plots or triangle plots using GetDist. This guidance has been adapted from [arXiv:1409.1354](https://arxiv.org/abs/1409.1354) and [arXiv:1808.05080](https://arxiv.org/abs/1808.05080).

Preparation 
===================
* Hardware : To employ the provided parallel capabilities of CosmoMC, you need more than just one core. Markov chain algorithms are time-consuming and performing them on parallel machines will boost the code’s performance.
* Operating System : CosmoMC is available for Linux and MacOS. Here, we installed and tested CosmoMC on Ubuntu and also MacOS.
* Compilers : CosmoMC is compatible with GFORTRAN compiler (GNU) and IFORT compiler (Oneapi).
* Open-MPI : OpenMPI library is required for running on parallel machines.
* Cfitsio : CosmoMC uses the CFITSIO library to read file FITS data format including CMB data files.
* Planck Likelihood : Planck Likelihood Code V3.0 is required to run CosmoMC with Planck 2018 data.
 
1. Ubuntu
- Install GNU Compiler
```Linux
sudo apt update && sudo apt upgrade
sudo apt install gcc
sudo apt install gfortran
sudo apt install g++
sudo apt install make
sudo apt install gedit
sudo apt install nano
sudo apt install wget
sudo apt install git -y
sudo apt install python3
sudo apt install python3-pip
pip3 install numpy
pip3 install scipy
pip3 install matplotlib
pip3 install getdist
sudo apt install liblapack-dev
sudo apt install libcfitsio-dev
```
- Install HomeBrew
```Linux
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install open-mpi
```
หมายเหตุ: สําหรับการติดตั้งบนระบบปฏิบัติการ Linux ต้องติดตั้ง Open-MPI เองซึ่งมีวิธีการที่ค่อนข้างยุ่งยาก แต่สามารถใช้ Homebrew ซึ่งเป็นตัว
ช่วยในการติดตั้งโปรแกรมอย่างง่าย โดยพิมพ์คําสั่งดังต่อไปนี้เพื่อติดตั้ง Open-MPI บน Linux

- Install Intel Compiler (Optional)
ในส่วนของ Intel Compiler สามารถทําการติดตั้งเพิ่มเติมภายหลังจากติดตั้ง GNU Compiler ซึ่งประสิทธิภาพของ Intel Compiler จะไวกว่า GNU
10%-20% โดยปกติเพียงแค่ GNU Compiler สามารถรันงานได้เช่นเดียวกัน
```Linux
wget https://registrationcenter-download.intel.com/akdlm/IRC_NAS/992857b9-624c-45de-9701-f6445d845359/l_BaseKit_p_2023.2.0.49397.sh
sudo sh ./l_BaseKit_p_2023.2.0.49397.sh
wget https://registrationcenter-download.intel.com/akdlm/IRC_NAS/0722521a-34b5-4c41-af3f-d5d14e88248d/l_HPCKit_p_2023.2.0.49440.sh
sudo sh ./l_HPCKit_p_2023.2.0.49440.sh
sudo apt update
sudo apt -y install cmake pkg-config build-essential
. /opt/intel/oneapi/setvars.sh 
```

2. MacOS
- Install HomeBrew
```Linux
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
- Install GNU Compiler
```Linux
brew install gcc
brew install gfortran
brew install g++
brew install make
brew install gedit
brew install wget
brew install git
brew install nano
brew install python3
python3 -m pip install --upgrade pip
pip3 install numpy
pip3 install scipy
pip3 install matplotlib
pip3 install getdist
brew install lapack
brew install cfitsio
brew install open-mpi
```

Planck Likelihood
===================
Due to the large size of the data file, approximately 20 GB, it is recommended to download only **Code** and **Baseline** for compilation. For other files, you can download and move the files into the successfully compiled directory. Alternatively, you can directly download the files from  [Planck Likelihood](https://pla.esac.esa.int) on the Cosmology page by clicking on Likelihood, which will display all 7 files available for download.
```Linux
wget -O COM_Likelihood_Code-v3.0_R3.10.tar.gz "http://pla.esac.esa.int/pla/aio/product-action?COSMOLOGY.FILE_ID=COM_Likelihood_Code-v3.0_R3.10.tar.gz"
wget -O COM_Likelihood_Data-baseline_R3.00.tar.gz "http://pla.esac.esa.int/pla/aio/product-action?COSMOLOGY.FILE_ID=COM_Likelihood_Data-baseline_R3.00.tar.gz"
tar -xzvf COM_Likelihood_Code-v3.0_R3.10.tar.gz
tar -xzvf COM_Likelihood_Data-baseline_R3.00.tar.gz
mv -rf baseline/plc_3.0/* code/plc_3.0/plc-3.1/
cd code/plc_3.0/plc-3.1/
python3 ./waf configure --install_all_deps
python3 ./waf install
source ./bin/clik_profile.sh
```
If you want to use the Intel Compiler, add the command **--lapack\_mkl=\$MKLROOT** at the end of `python3 ./waf configure --install_all_deps` line. After installing the **code** file, proceed to extract the remaining files. Then, move the **hi\_l**, **low\_l**, **lensing** files from the extracted directory to the **code/plc\_3.0/plc-3.1/** directory.
```Linux
wget -O COM_Likelihood_Data-extra-plik-lite-ext_R3.00.tar.gz "http://pla.esac.esa.int/pla/aio/product-action?COSMOLOGY.FILE_ID=COM_Likelihood_Data-extra-plik-lite-ext_R3.00.tar.gz"
wget -O COM_Likelihood_Data-extra-camspec-ext_R3.00.tar.gz "http://pla.esac.esa.int/pla/aio/product-action?COSMOLOGY.FILE_ID=COM_Likelihood_Data-extra-camspec-ext_R3.00.tar.gz"
wget -O COM_Likelihood_Data-extra-plik-ext_R3.00.tar.gz "http://pla.esac.esa.int/pla/aio/product-action?COSMOLOGY.FILE_ID=COM_Likelihood_Data-extra-plik-ext_R3.00.tar.gz"
wget -O COM_Likelihood_Data-extra-bflike-ext_R3.00.tar.gz "http://pla.esac.esa.int/pla/aio/product-action?COSMOLOGY.FILE_ID=COM_Likelihood_Data-extra-bflike-ext_R3.00.tar.gz"
wget -O COM_Likelihood_Data-extra-lensing-ext_R3.00.tar.gz "http://pla.esac.esa.int/pla/aio/product-action?COSMOLOGY.FILE_ID=COM_Likelihood_Data-extra-lensing-ext_R3.00.tar.gz"
```

```Linux
tar -xzvf <.tar.gz file>

```

CosmoMC
===================

1. Installation
```Linux
git clone --recursive https://github.com/cmbant/CosmoMC.git
cd CosmoMC
ln -s </plc-3.1 PATH> ./data/clik_14.0
```
The PATH of the `/plc-3.1` file can be checked by typing the command `echo $CLIK_PATH`. It will display the PATH of the file.

2. Compilation
```Linux
make
```
After successful compiling, a file named `cosmomc` will be created in CosmoMC directory.

```Linux
make clean && make
```
If unable to execute the `make` command, delete the file `cosmomc` first by typing the command `rm cosmomc`. The compilation of the CAMB program, which is used for calculating the theoretical part of CosmoMC and is located within a subdirectory `camb/fortran/`. If the compilation is successful, the file `camb` will appear in the directory.

```Linux
cd camb/fortran/
make
```

3. Running
To run CosmoMC you need to run it with MPI using mpirun command. Set your corrent directory to CosmoMC directory and run this command.

```Linux
mpirun -np <number of processers (cores)> ./cosmomc <.ini file>
```
Inside the `.ini file` there are some lines which start with DEFAULT keyword. If these lines are not commented, it means we can use likelihoods related to these data.
```
#high-L plik likelihood
DEFAULT(batch3/plik_rd12_HM_v22_TTTEEE.ini)

#low-L temperature
DEFAULT(batch3/lowl.ini)

#low-L EE polarization
DEFAULT(batch3/simall_EE.ini)

#Bicep-Keck-Planck 2015, varying cosmological parameters (use only if varying r)
DEFAULT(batch3/BK15.ini)

#DES 1-yr joint
DEFAULT(batch3/DES.ini)

#Planck 2018 lensing (native code, does not require Planck likelihood code)
DEFAULT(batch3/lensing.ini)

#BAO compilation
DEFAULT(batch3/BAO.ini)

#Pantheon SN
DEFAULT(batch3/Pantheon.ini)

#general settings
DEFAULT(batch3/common.ini)

propose_matrix= planck_covmats/<.covmat file for each work>

#Folder where files (chains, checkpoints, etc.) are stored
root_dir = chains/<model directory for each work>/

#Root name for files produced
file_root=<name>
#action= 0 runs chains, 1 importance samples, 2 minimizes
#use action=4 just to quickly test likelihoods
action = 0

#turn on checkpoint for real runs where you want to be able to continue them
checkpoint = T
```
To do a MCMC run you need to find the line which starts with action and set its value to 0.

4. Running on Cluster

Running CosmoMC can be initiated on an HPC (High Performance Computing) machine for faster completion compared to using a regular computer. Currently in Thailand, access to the Chalawan HPC facility at the National Astronomical Research Institute of Thailand (NARIT) can be requested for running jobs. There are two main nodes available for execution: the pollux node (GPU) and the castor node (CPU). The pollux node tends to run faster, but since there are only 2 nodes, it is recommended to use the castor node, which offers more nodes for processing.

For running jobs on the cluster, `.sh` files must be used to keep commands for the HPC to execute the jobs. In the Chalawan HPC, built-in modules are available for running unmodified models. For instance, the LCDM model can be run using these built-in modules.

 ```Linux
#!/bin/bash

#SBATCH -J CosmoMC      # Job name
#SBATCH -n 10           # Number of tasks

module purge
module load hwloc
module load intel/19.0.5.281
module load openmpi3/4.0.2
module load CosmoMC
mpirun <path to .ini file>
```
For running on the pollux node, if model has been modified, a symbolic link for CLIK_PATH must be created in step 1. Following this, compilation is required, and it is essential to load the necessary modules as follows.
```Linux
module purge
module load hwloc
module load intel/19.0.5.281
module load openmpi3/4.0.2
export PLANCKLIKE=cliklike
export CLIK_DATA=/data3/opt/ohpc/pub/apps/CosmoMC-Oct19/plc_3.1/share/clik
export CLIK_PATH=/data3/opt/ohpc/pub/apps/CosmoMC-Oct19/plc_3.1
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CLIK_PATH/lib
```
```Linux
#!/bin/bash

#SBATCH -J CosmoMC      # Job name
#SBATCH -n 10           # Number of tasks
#SBATCH -p chalawan_gpu # Partition
#SBATCH -w pollux3

module purge
module load hwloc
module load intel/19.0.5.281
module load openmpi3/4.0.2
export PLANCKLIKE=cliklike
export CLIK_DATA=/data3/opt/ohpc/pub/apps/CosmoMC-Oct19/plc_3.1/share/clik
export CLIK_PATH=/data3/opt/ohpc/pub/apps/CosmoMC-Oct19/plc_3.1
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CLIK_PATH/lib
mpirun ./cosmomc <path to .ini file>
```
For running on the castor node, it is necessary to install the Planck likelihood and recompile using the GNU Compiler. The important modules should be loaded as follows.
```Linux
module purge
module load gnu8
module load hwloc
module load openmpi3
```
```Linux
#!/bin/bash

#SBATCH -J CosmoMC      # Job name
#SBATCH -p chalawan_cpu # Partition
#SBATCH -n 10           # Number of task

module purge
module load gnu8
module load hwloc
module load openmpi3
source data/clik_14.0/bin/clik_profile.sh

mpirun ./cosmomc <path to .ini file>
```

5. Output

หลังจากทำการสั่งรัน \texttt{CosmoMc} ภายใน chains dierctory จะปรากฏไฟล์ซึ่งเป็น output ไฟล์หลายชนิด

* `.txt file` เป็นไฟล์ซึ่งบรรจุค่าของพารามิเตอร์จากการรันเพื่อนำไปใช้ในการพล็อตกราฟ
* `.log file` เป็นไฟล์เก็บข้อมูลสำคัญสำหรับการรัน
* `.data file` เป็นไฟล์เก็บข้อมูลของแบบจำลองในแต่ละจุดสุ่มที่ต่างกัน
* `.chk file` เป็นไฟล์สำหรับเก็บข้อมูลซึ่งรันไว้ก่อนที่งานจะสำเร็จหรือถูกยกเลิก สามารถใช้ไฟล์นี้เพื่อทำการรันต่อจากจุดที่หยุดโดยไม่ต้องเริ่มใหม่
* `.inputparams file` ไฟล์แสดงพารามิเตอร์เริ่มต้นของแบบจำลอง
* `.likelihood file` ไฟล์แสดง likelihoods ที่ใช้ในการรัน
* `.paramnames file` ไฟล์แสดงพารามิเตอร์ทั้งหมด
* `.ranges file` ไฟล์แสดงช่วงของค่าของพารามิเตอร์
* `.converge_stat file` ไฟล์แสดงค่า R-1 ซึ่งจะบอกถึงค่าที่ยอมรับเพื่อนหยุดการรัน

>> Plotting with GetDist

การสร้างกราฟการกระจาย (distribution plot) และ กราฟสามเหลี่ยม (triangle plot) ต้องใช้แพคเกจสำหรับสร้างกราฟจากไฟล์ซึ่งเป็นเอาพุตท์ไฟล์จากการรัน \texttt{CosmoMC} รวมไปถึงการวิเคราะห์ค่าต่าง ๆ จากการรัน โดยแพคเกจต้องใช้ภาษา python ในการเขียนคำสั่ง โปรแกรมสำหรับเพื่อแสดงกราฟฟิกของ python แนะนำให้ใช้ jupyter notebook หรือ jupyter lab โดยสามารถติดตั้งได้ด้วยตัวเองจากอินเทอร์เน็ตในทุกระบบปฏิบัติการ
และสามารถศึกษาเพิ่มเติมจาก https://getdist.readthedocs.io/en/latest/ และ https://getdist.readthedocs.io/en/latest/plot\_gallery.html

```python
%matplotlib inline
import getdist
from getdist import plots, MCSamples, loadMCSamples

file_root1 = 'planck/plikHM_TTTEEE_lowl_lowE_BK15_lensing/base_r_plikHM_TTTEEE_lowl_lowE_BK15_lensing_post_BAO'
file_root2 = 'planck/plikHM_TTTEEE_lowl_lowE_BK15_lensing/base_r_plikHM_TTTEEE_lowl_lowE_BK15_lensing'

samples1 = loadMCSamples(file_root=file_root1,settings={'ignore_rows':0.5})
samples2 = loadMCSamples(file_root=file_root2,settings={'ignore_rows':0.5})
```
ขั้นแรกทําการนําเข้า getdist library และเลือก chain ที่ต้องการนํามาพล็อตกราฟโดยใส่ directory path ไปสุ๋ไฟล์ที่เลือกที่บรรทัด file_root
```python
g2 = plots.get_subplot_plotter(width_inch=5)
g2.settings.axes_fontsize = 16
g2.settings.axes_labelsize = 20
g2.plot_2d([samples1],'omegabh2','omegach2',filled=True,contour_lws=1.5)
```
การพล็อตรูปเดี่ยวเฉพาะ 2 พารามิเตอร์ที่สนใจโดยใช้คําสั่งดังแสดงด้านบน
<p align="center">
<img src="https://github.com/CraverBoyyy/CosmoMC-Installation/assets/109847168/989574bd-510b-4488-a995-6935a7ace3cf"  width="500px" height="500px">
</p>
การพล็อตกราฟสามเหลี่ยม โดยสามารถเลือกพารามิเตอร์ที่สนใจจํานวนเท่าใดก็ได้ แต่หากใส่ในจํานวนที่มากเกินไปอาจจะทําให้ภาพมีขนาดใหญ่และราย
ละเอียดมากเกินไป ควรจะเลือกใส่พารามิเตอร์ที่เหมาะสมไม่มากเกินไป

```python
g = plots.get_subplot_plotter(width_inch=10)
g.settings.axes_fontsize = 16
g.settings.axes_labelsize = 20
g.triangle_plot(samples1,['omegabh2','omegach2','theta','tau','logA','ns'],filled=True,contour_lws=1.5)
```
<p align="center">  
<img src="https://github.com/CraverBoyyy/CosmoMC-Installation/assets/109847168/0edd073e-28fc-4938-8080-1a53e685f0ad" width="700px" height="700px"  align="center" >
</p>
สามารถให้กราฟแสดงผลค่า mean และ uncertainty ได้ โดยจะปรากฎด้านบนของกราฟการกระจายของแต่ละพารามิเตอร์ ซึ่งสามารถเลือกได้ทั้ง
uncertainty ที่ 68%CL และ 95%CL

```python
g.triangle_plot(samples1,['omegabh2','omegach2','theta','tau','logA','ns'],filled=True,contour_lws=1.5,title_limit=2)
```
<p align="center">  
<img src="https://github.com/CraverBoyyy/CosmoMC-Installation/assets/109847168/823b3b03-2636-4bf0-b49c-7c11eecd0538" width="700px" height="700px"  align="center" >
</p>

หากต้องการเปรียบเทียบผลของ 2 แบบจําลองหรือมากกว่า สามารถเพิ่ม chain เข้าไปในคําสั่งได้โดยเพิ่ม file_root เช่นเดียวกับข้อมูลชุดแรก และ
สามารถปรับจํานวนพารามิตอร์ได้เช่นเดียวกัน
```python
 g.triangle_plot((samples1,samples2),['omegabh2','omegach2','theta','tau','logA','ns'],filled=True,contour_lws=1.5)
```
<p align="center">        
<img src="https://github.com/CraverBoyyy/CosmoMC-Installation/assets/109847168/25c0c31d-37b1-4ffc-853a-4ae32b7444f8" width="700px" height="700px"  align="center" >
</p>


