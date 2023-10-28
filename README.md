
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




