
CosmoMC: คู่มือการติดตั้ง
===================
CosmoMC ("Cosmological Monte Carlo") เป็นซอฟแวร์ที่ใช้ในการศึกษา cosmological parameter space ซึ่งใช้ Markov Chain Monte Carlo (MCMC) เป็นอัลกอริทึม CosmoMC ถูกเขียนด้วยภาษา FORTRAN 2003/2008 และใช้ภาษา Python ในการวิเคราะห์ผล และพล็อตกราฟ โปรแกรมนี้มีส่วนประกอบภายในคือ \texttt{CAMB} สำหรับเพื่อคำนวณ by theoretical matter power spectrum และ temperature power spectrum และ polarization power spectrum ของ CMB 


Preparation
=============================

* Hardware : สำหรับการรัน CosmoMC ซึ่งต้องรันแบบ parallel compilation ดังนั้นควรใช้อุปกรณ์คอมพิวเตอร์ที่มี cpu ตั้งแต่ 2 core ขึ้นไป   
* Operating System : สามารถติดตั้งได้ในระปฏิบัติการ Linux เช่น Ubuntu และนอกจากนี้ยังสามารถติดตั้งได้ในระบบปฏิบัติการ MacOS หากต้องการติดตั้งในเครื่อง Windows ควรติดตั้งโปรแกรม Linux for Windows หรือ Virtual Machine เพื่อใช้ในการติดตั้ง สำหรับคู่มือติดตั้งนี้จะใช้ระบบปฏิบัติการ Linux บน Ubuntu
* Compilers : สำหรับ compiler ที่ต้องใช้ในการรัน CosmoMC มีหลายส่วนด้วยกัน จำเป็นต้องติดตั้งทั้งหมดเพื่อที่จะสามารถรันงานได้ ซึ่งจะประกอบไปด้วย C compiler, Fortran compiler และ Python compiler โดยหากติดตั้งแค่ GNU Compiler สามารถรันงานปกติ แต่หากต้องการให้การรันไวขึ้นสามารถติดตั้ง Intel Compiler เพิื่อเพิ่มประสิทธิภาพในการรันได้ไวขึ้น
* Open-MPI : ใช้ในการรัน CosmoMC บน parallel machine
* Cfitsio : ใช้สำหรับอ่านไฟล์ .fits โดยเฉพาะข้อมูล CMB ซึ่งเป็นไฟล์สกุลนี้

ระบบปฏิบัติการ Linux บน Ubuntu
==================

See the latest `paper <http://arxiv.org/abs/1304.4473>`_.

GetDist
===================

CosmoMC includes the GetDist python sample analysis and plotting package, which is
also `available separately <http://getdist.readthedocs.org/en/latest/>`_.


Branches
=============================

The master branch contains latest changes to the main release version, using latest CAMB 1.x.

.. image:: https://travis-ci.com/cmbant/CosmoMC.svg?branch=master
  :target: https://travis-ci.com/cmbant/CosmoMC/builds

The planck2018 branch contains the configuration used for the final Planck 2018 analysis, with
corresponding CAMB version.

The devel branch is a development branch.

=============

.. raw:: html

    <a href="https://www.sussex.ac.uk/astronomy/"><img src="https://cdn.cosmologist.info/antony/Sussex_white.svg" style="height:200px" height="200px"></a>
    <a href="https://erc.europa.eu/"><img src="https://cdn.cosmologist.info/antony/ERC_white.svg" style="height:200px" height="200px"></a>
    <a href="https://stfc.ukri.org/"><img src="https://cdn.cosmologist.info/antony/STFC_white.svg" style="height:200px" height="200px"></a>
