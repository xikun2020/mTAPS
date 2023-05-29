# =======================================================================================================================
#	Author: Kun Xi, Lizhe Zhu									 
# =======================================================================================================================

# =======================================================================================================================
#	global import: future_print, numpy, mdtraj, os, re			 
# =======================================================================================================================

from __future__ import print_function, division
import mdtraj as md 	#python interface for md traj analysis#
import numpy as np 
import os 				
import re
import shutil
import time
import errno
import random as rdm 
from Confs import Confs	
from numpy import *

from Confs import Confs
from PcvInd import PcvInd
from Path import Path

# =======================================================================================================================
#	python interface for GROMACS								 
# =======================================================================================================================

import gromacs.setup
import gromacs.run
import gromacs.tools
import gromacs

# =======================================================================================================================
#	Check whether parameters for gromacs are right or not 		 
# =======================================================================================================================

import warnings

warnings.simplefilter('error', gromacs.AutoCorrectionWarning)
warnings.simplefilter('error', gromacs.BadParameterWarning)
warnings.simplefilter('error', gromacs.GromacsValueWarning)
warnings.simplefilter('error', gromacs.GromacsFailureWarning)

# =======================================================================================================================
#	mpi interface for parallel computing						  
# =======================================================================================================================

#mpi4py package#

# ======================================================================================================================
#                                       digits formater for iterations: "3 --> 03"
# ======================================================================================================================

def digits(s1):
	s2 = "%.3d" % s1
	return s2

# =======================================================================================================================
#                       parameters for three main parts: sampling / path trace / Imp. to Exp. sol. 
# =======================================================================================================================
engine = 'GROMACS'	

tolDist = 0.12 

Pswitch = value

# =======================================================================================================================
#											key input parameters 
# =======================================================================================================================

mConfs	>= 1	

rmsCut = 0.06	#Unit: nm#
rmsMax = 0.0	#Unit: nm#

n_iter = 20	
iter_start = 1	

dires = 'pars'

###
#under further refinement
###

# =======================================================================================================================
#											mdrun input files (default name for mdrun)
# =======================================================================================================================

runName = 'run'
trjName = 'run.xtc'
nodeName = 'node.pdb'
pluName = 'plumed.dat'

# =======================================================================================================================
#                                           key arrays used in HePaCS sampling
# =======================================================================================================================

#important parameters#

# =======================================================================================================================
#                                              path of key input files
# =======================================================================================================================

dirRoot = os.getcwd()	

###
#see more details in TAPS #
###

# ======================================================================================================================
#						         implicit solvent molecular dynamics simulation: IMD
# ======================================================================================================================

def runIMD(dire, engine, runName):
	if engine == 'GROMACS':
		md = gromacs.run.MDrunner(dire, nt=threads, deffnm=runName)
		md.run()
		os.chdir(dire)
		gromacs.energy(f='run.edr', o='run.xvg', input=('Potential'))
	else:
		raise ValueError("MD engines other than GROMACS are not support yet")

# ======================================================================================================================
#	                                       High-energy filtering
# ======================================================================================================================

def He_mdrun():

	pcut = int(mConfs*mConfs+125) 
	Enlst = []

	## filtering combined with k-center method for next iteration ## 
	###
	#under further refinement
	###

	#k-center filtering start#
	###
	#under further refinement
	###

# ======================================================================================================================
#											format used to write pdb file
# ======================================================================================================================

def _format_83(f):
	"""Format a single float into a string of width 8, with ideally 3 decimal
	places of precision. If the number is a little too large, we can
	gracefully degrade the precision by lopping off some of the decimal
	places. If it's much too large, we throw a ValueError"""
	if -999.999 < f < 9999.999:
		return '%8.3f' % f
	if -9999999 < f < 99999999:
		return ('%8.3f' % f)[:8]
	raise ValueError('coordinate "%s" could not be represented '
		'in a width-8 field' % f)

dataName = 'data' + digits(iter_start)	

# =======================================================================================================================
#                                 check whether path sampling already run or not
# =======================================================================================================================

if iter_start == 1 and not os.path.exists(dataName):
	os.makedirs(dataName)
else:
	raise #iter_start not correct or data file already exist#


print ("###DEBUG### Size:", size, "Rank:", rank, "begining.")

ftr = md.load(tarFile, top=initFile)	#	target conf

for i in range(iter_start, n_iter):

	if i == 1:

		itr = md.load(trj0File, top=initFile)
		itr.superpose(ftr, 0, align) 

		rmscal = md.rmsd(itr, ftr, 0, rms)
		rmsMax = (sorted(rmscal))[mConfs-1]
		print(rmsMax)

		itrconf = Confs.traj2conf(itr)
		itrconf.nodes = itrconf

		iterName = 'iter' + digits(iter_start)
		iterdir = dirRoot + '/' + dataName + '/' + iterName
		os.makedirs(iterdir)
		os.chdir(iterdir)

		#	implicit solvent MD sampling #
		for j_run in range(mConfs):
			confName = 'conf' + digits(j_run)
			dirRun = dirRoot + '/' + dataName + '/' + iterName + '/' + confName
			#gromacs.mdrun##
			###
			#under further refinement
			###
		os.chdir(dirRoot)

	if i > 1:

		iterName = 'iter' + digits(i-1)

		rmslist = []
		pathip = []

		#maximum rmsd between sampled data and target #
		###
		#under further refinement
		###


		print('###DEBUG### iteration', i, '#########')

		if Psample < Pswitch:	
			#high eenergy filtering#
			###
			#under further refinement
			###

		if Psample > Pswitch:	
			#Normal rms filtering#
			###
			#under further refinement
			###

# =======================================================================================================================
#                                       Part2 : build M-transtion pathways 
# =======================================================================================================================

###
#under further refinement
###
 

# =======================================================================================================================
#                                     Part3: Path Clustering/Filtering/TAPS Optimization
# =======================================================================================================================

###
#under further refinement
###
