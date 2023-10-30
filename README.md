
CosmoMC: คู่มือการติดตั้ง
===================
CosmoMC ("Cosmological Monte Carlo") เป็นซอฟแวร์ที่ใช้ในการศึกษา cosmological parameter space ซึ่งใช้ Markov Chain Monte Carlo (MCMC) เป็นอัลกอริทึม **CosmoMC** ถูกเขียนด้วยภาษา FORTRAN 2003/2008 และใช้ภาษา Python ในการวิเคราะห์ผล และพล็อตกราฟ โปรแกรมนี้มีส่วนประกอบภายในคือ **CAMB** สำหรับเพื่อคำนวณ by theoretical matter power spectrum และ temperature power spectrum และ polarization power spectrum ของ CMB 


>1. Preparation

* Hardware : สำหรับการรัน CosmoMC ซึ่งต้องรันแบบ parallel compilation ดังนั้นควรใช้อุปกรณ์คอมพิวเตอร์ที่มี cpu ตั้งแต่ 2 core ขึ้นไป   
* Operating System : สามารถติดตั้งได้ในระปฏิบัติการ Linux เช่น Ubuntu และนอกจากนี้ยังสามารถติดตั้งได้ในระบบปฏิบัติการ MacOS หากต้องการติดตั้งในเครื่อง Windows ควรติดตั้งโปรแกรม Linux for Windows หรือ Virtual Machine เพื่อใช้ในการติดตั้ง สำหรับคู่มือติดตั้งนี้จะใช้ระบบปฏิบัติการ Linux บน Ubuntu
* Compilers : สำหรับ compiler ที่ต้องใช้ในการรัน CosmoMC มีหลายส่วนด้วยกัน จำเป็นต้องติดตั้งทั้งหมดเพื่อที่จะสามารถรันงานได้ ซึ่งจะประกอบไปด้วย C compiler, Fortran compiler และ Python compiler โดยหากติดตั้งแค่ GNU Compiler สามารถรันงานปกติ แต่หากต้องการให้การรันไวขึ้นสามารถติดตั้ง Intel Compiler เพิื่อเพิ่มประสิทธิภาพในการรันได้ไวขึ้น
* Open-MPI : ใช้ในการรัน CosmoMC บน parallel machine
* Cfitsio : ใช้สำหรับอ่านไฟล์ .fits โดยเฉพาะข้อมูล CMB ซึ่งเป็นไฟล์สกุลนี้

>>1.1 ระบบปฏิบัติการ Linux บน Ubuntu

>>>1.1.1 การติดตั้ง GNU Compiler
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
หมายเหตุ: สำหรับการติดตั้งบนระบบปฏิบัติการ Linux ต้องติดตั้ง Open-MPI เองซึ่งมีวิธีการที่ค่อนข้างยุ่งยาก แต่สามารถใช้ Homebrew ซึ่งเป็นตัวช่วยในการติดตั้งโปรแกรมอย่างง่าย โดยพิมพ์คำสั่งดังต่อไปนี้เพื่อติดตั้ง Open-MPI บน Linux

```Linux
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install open-mpi
```
>>>1.1.2 การติดตั้ง Intel Compiler

ในส่วนของ Intel Compiler สามารถทำการติดตั้งเพิ่มเติมภายหลังจากติดตั้ง GNU Compiler ซึ่งประสิทธิภาพของ Intel Compiler จะไวกว่า GNU 10\%-20\% โดยปกติเพียงแค่ GNU Compiler สามารถรันงานได้เช่นเดียวกัน 

```Linux
wget https://registrationcenter-download.intel.com/akdlm/IRC_NAS/992857b9-624c-45de-9701-f6445d845359/l_BaseKit_p_2023.2.0.49397.sh
sudo sh ./l_BaseKit_p_2023.2.0.49397.sh
wget https://registrationcenter-download.intel.com/akdlm/IRC_NAS/0722521a-34b5-4c41-af3f-d5d14e88248d/l_HPCKit_p_2023.2.0.49440.sh
sudo sh ./l_HPCKit_p_2023.2.0.49440.sh
sudo apt update
sudo apt -y install cmake pkg-config build-essential
. /opt/intel/oneapi/setvars.sh 
```

>>1.2 ระบบปฏิบัติการ MacOS

```Linux
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
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
ภายหลังจากการติดตั้งส่วนของ compiler และ library ต่าง ๆ เสร็จเรียบร้อยแล้วถัดไปจะเป็นการติดตั้ง Planck 2018 data เพื่อใช้ในการรันโปรแกรม **CosmoMC**

> 2. Planck Likelihood

เนื่องจากไฟล์ข้อมูลมีขนาดรวมประมาณ 20 Gb จึงแนะนำให้ดาวน์โหลดเฉพาะบรรทัดที่ 1 - 2 เพื่อทำการคอมไพล์ และในส่วนบรรทัด 3 - 7 สามารถดาวน์โหลดและย้ายไฟล์เข้าไปในไฟล์ที่คอมไพล์สำเร็จแล้ว หรือสามารถเข้าไปดาน์โหลดไฟล์โดยตรงที่ [Planck Likelihood](https://pla.esac.esa.int) เข้าไปที่หน้า **Cosmology** และกดที่ **Likelihood** จะแสดงไฟล์ให้ดาวน์โหลดทั้งหมด 7 ไฟล์
```Linux
wget -O COM_Likelihood_Code-v3.0_R3.10.tar.gz "http://pla.esac.esa.int/pla/aio/product-action?COSMOLOGY.FILE_ID=COM_Likelihood_Code-v3.0_R3.10.tar.gz"
wget -O COM_Likelihood_Data-baseline_R3.00.tar.gz "http://pla.esac.esa.int/pla/aio/product-action?COSMOLOGY.FILE_ID=COM_Likelihood_Data-baseline_R3.00.tar.gz"
tar -xzvf COM_Likelihood_Code-v3.0_R3.10.tar.gz
tar -xzvf COM_Likelihood_Data-baseline_R3.00.tar.gz
cd code/plc_3.0/plc-3.1/
python3 ./waf configure --install_all_deps
python3 ./waf install
source ./bin/clik_profile.sh
```
หมายเหตุ: หากต้องการใช้ Intel Compiler ให้เพิ่มคำสั่ง **--lapack\_mkl=\$MKLROOT** ต่อท้ายของบรรทัดที่ 4 ภายหลังจากติดตั้งไฟล์ **code** เสร็จแล้ว จากนั้นทำการแตกไฟล์ที่เหลือและทำการย้ายไฟล์ **hi\_l**, **low\_l**, **lensing** จากไฟล์ที่ทำการแตกไฟล์ออก ย้ายไปที่ไฟล์ **code/plc\_3.0/plc-3.1/** 
```Linux
wget -O COM_Likelihood_Data-extra-plik-lite-ext_R3.00.tar.gz "http://pla.esac.esa.int/pla/aio/product-action?COSMOLOGY.FILE_ID=COM_Likelihood_Data-extra-plik-lite-ext_R3.00.tar.gz"
wget -O COM_Likelihood_Data-extra-camspec-ext_R3.00.tar.gz "http://pla.esac.esa.int/pla/aio/product-action?COSMOLOGY.FILE_ID=COM_Likelihood_Data-extra-camspec-ext_R3.00.tar.gz"
wget -O COM_Likelihood_Data-extra-plik-ext_R3.00.tar.gz "http://pla.esac.esa.int/pla/aio/product-action?COSMOLOGY.FILE_ID=COM_Likelihood_Data-extra-plik-ext_R3.00.tar.gz"
wget -O COM_Likelihood_Data-extra-bflike-ext_R3.00.tar.gz "http://pla.esac.esa.int/pla/aio/product-action?COSMOLOGY.FILE_ID=COM_Likelihood_Data-extra-bflike-ext_R3.00.tar.gz"
wget -O COM_Likelihood_Data-extra-lensing-ext_R3.00.tar.gz "http://pla.esac.esa.int/pla/aio/product-action?COSMOLOGY.FILE_ID=COM_Likelihood_Data-extra-lensing-ext_R3.00.tar.gz"
```

> 3. CosmoMC

>> 3.1 Installation

```Linux
git clone --recursive https://github.com/cmbant/CosmoMC.git
cd CosmoMC
ln -s </plc-3.1 PATH> ./data/clik_14.0
```
หมายเหตุ: PATH ของไฟล์ **/plc-3.1** สามารถทำการเช็คด้วยการพิมพ์คำสั่ง `echo $CLIK_PATH` จะขึ้น PATH ของไฟล์

>> 3.2 Compilation

ในส่วนโปรแกรม \texttt{CosmoMC} ต้องทำการสร้างไฟล์ .exe ชื่อ \texttt{cosmomc} ซึ่งจะใช้ในการรันงานโดยพิมคำสั่งดังนี้บนหน้าต่าง CosmoMC/  
```Linux
make
```
โดยภายหลังจากคอมไพล์สำเร็จจะมีไฟล์ \texttt{cosmomc} ปรากฏขึ้นในไฟล์ และหากต้องการที่จะสร้างไฟล์ \texttt{cosmomc} ใหม่เมื่อมีการแก้ไขไฟล์ พิมพ์คำสั่ง
```Linux
make clean && make
```
หากไม่สามารถสั่ง \texttt{make} ได้ ให้ทำการลบไฟล์ \texttt{cosmomc} ก่อน โดยพิมพ์คำสั่ง \texttt{rm cosmomc} ในส่วนของการคอมไพล์โปรแกรม \texttt{CAMB} ซึ่งเป็นโปรแกรมที่สำหรับคำนวณส่วนทฤษฎีของ \texttt{CosmoMC} จะอยู่ภายในไฟล์ย่อย

```Linux
cd camb/fortran/
make
```
หากคอมไพล์สำเร็จจะปรากฎไฟล์ \texttt{camb} ขึ้นมาบนไฟล์

>> 3.3 Running

การรัน \texttt{CosmoMC} จะต้องใช้คำสั่ง \texttt{mpirun} เพื่อทำการรันงานแบบ parallel running โดยต้องระบุจำนวนคอร์ในการรัน หากไม่ระบุจะถูกตั้งค่าให้เป็น 1 คอร์ และไฟล์ .ini คือไฟล์สำหรับการสั่งรันงานซึ่งจะระบุชุดข้อมูลที่ใช้ การกำหนดพารามิเตอร์ และการเซ็คค่าต่าง ๆ ซึ่งสำคัญในการรันงาน

```Linux
mpirun -np <number of processers (cores)> ./cosmomc <.ini file>
```

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
ส่วนนี้เป็นส่วนสำคัญในไฟล์ .ini ซึ่งส่วนแรกคือ propose matrix ซึ่งควรจะเซ็ตให้เหมาะสมการการเลือกใช้ชุดข้อมูลและพารามิเตอร์ โดยสามารถเช็คได้ที่ไฟล์ plank\_covmat ซึ่งจะมีไฟล์จำนวนมากสำหรับเซ็ต propose matrix แต่หากไม่ได้เลือก propose matrix ที่เหมาะสมไว้โปรแกรมจะทำการประมาณค่าเองซึ่งอาจจะทำให้การรันงานนานขึ้น 

ส่วนสำคัญถัดมาคือ root\_dir ซึ่งเป็นตำแหน่งไฟล์มี่จะเก็บผลจากการรันงานเพื่อนำไปสร้างกราฟ โดยหากทำการรันหลายงานควรจะระมัดระวังในการสร้างไฟล์ทับกัน ควรจะเปลี่ยนชื่อไฟล์ หรือ สร้างไฟล์ใหม่ขึ้นมาเพื่อเก็บผลการรัน สำหรับข้อมูลเพิ่มเติมสามารถศึกษาได้ \texttt{https://cosmologist.info/cosmomc/readme.html}

>> 3.4 Cluster Running

การรัน \texttt{CosmoMC} สามารถสั่งการบนเครื่อง HPC (High Performance Computing) เพื่อให้สามารถรันเสร็จได้ไวกว่าการใช้คอมพิวเตอร์ทั่วไป ซึ่งปัจจุบันในไทยสามารถขอใช้งานเครื่อง Chalawan HPC ของสถาบันวิจัยดาราศาสตร์แห่งชาติ (NARIT) เพื่อทำการรันงาน โดยจะมี 2 node หลักที่สามารถใช้งานการรันได้ pollux node (gpu) และ castor node (cpu) ประสิทธิภาพจะของ pollux จะรันไว้ไวกว่าแต่เนื่องจากมีเพียง 2 node จึงแนะนำให้ใช้ castor ซึ่งมีจำนวน node ให้ใช้งานมากกว่า

 สำหรับการรันงานบนคลัสเตอร์จะต้องใช้ไฟล์ .sh เพื่อบรรจุคำสั่งให้ hpc ทำการรันงาน โดยในเครื่อง Chalawan จะมีโมดูลสำเร็จรูปซึ่งสามารถใช้สำหรับสั่งรันแบบจำลองที่ไม่ได้มีการแก้ไขได้เลย เช่น แบบจำลอง LCDM

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
สำหรับการรันบน pollux node หากมีการแก้ไขแบบจำลอง (Modified model) ต้องทำการสร้าง symbolic link สำหรับ CLIK\_PATH ในขั้นตอน 3.1 บรรทัดที่ 3 จากนั้นต้องทำการสั่งคอมไพล์ ซึ่งต้องทำการโหลดโมดูลที่สำคัญดังนี้ หลังจากนั้นทำตามขั้นตอนที่ 3.2

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
สำหรับการรันบน castor node ต้องทำการติดตั้ง Planck likelihood และทำการคอมไพล์ใหม่ทั้งหมดด้วย GNU Compiler ซึ่งจะต้องโหลดโมดูลสำคัญดังนี้ จากนั้นทำตามขั้นตอนที่ 2 จนถึงขั้นตอนที่ 3 ตามคู่มือ
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

>> 3.5 Output

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
```python
g2 = plots.get_subplot_plotter(width_inch=5)
g2.settings.axes_fontsize = 16
g2.settings.axes_labelsize = 20
g2.plot_2d([samples1],'omegabh2','omegach2',filled=True,contour_lws=1.5)
```









