# -*- coding: utf-8 -*-
# Spearmint
#
# Academic and Non-Commercial Research Use Software License and Terms
# of Use
#
# Spearmint is a software package to perform Bayesian optimization
# according to specific algorithms (the “Software”).  The Software is
# designed to automatically run experiments (thus the code name
# 'spearmint') in a manner that iteratively adjusts a number of
# parameters so as to minimize some objective in as few runs as
# possible.
#
# The Software was developed by Ryan P. Adams, Michael Gelbart, and
# Jasper Snoek at Harvard University, Kevin Swersky at the
# University of Toronto (“Toronto”), and Hugo Larochelle at the
# Université de Sherbrooke (“Sherbrooke”), which assigned its rights
# in the Software to Socpra Sciences et Génie
# S.E.C. (“Socpra”). Pursuant to an inter-institutional agreement
# between the parties, it is distributed for free academic and
# non-commercial research use by the President and Fellows of Harvard
# College (“Harvard”).
#
# Using the Software indicates your agreement to be bound by the terms
# of this Software Use Agreement (“Agreement”). Absent your agreement
# to the terms below, you (the “End User”) have no rights to hold or
# use the Software whatsoever.
#
# Harvard agrees to grant hereunder the limited non-exclusive license
# to End User for the use of the Software in the performance of End
# User’s internal, non-commercial research and academic use at End
# User’s academic or not-for-profit research institution
# (“Institution”) on the following terms and conditions:
#
# 1.  NO REDISTRIBUTION. The Software remains the property Harvard,
# Toronto and Socpra, and except as set forth in Section 4, End User
# shall not publish, distribute, or otherwise transfer or make
# available the Software to any other party.
#
# 2.  NO COMMERCIAL USE. End User shall not use the Software for
# commercial purposes and any such use of the Software is expressly
# prohibited. This includes, but is not limited to, use of the
# Software in fee-for-service arrangements, core facilities or
# laboratories or to provide research services to (or in collaboration
# with) third parties for a fee, and in industry-sponsored
# collaborative research projects where any commercial rights are
# granted to the sponsor. If End User wishes to use the Software for
# commercial purposes or for any other restricted purpose, End User
# must execute a separate license agreement with Harvard.
#
# Requests for use of the Software for commercial purposes, please
# contact:
#
# Office of Technology Development
# Harvard University
# Smith Campus Center, Suite 727E
# 1350 Massachusetts Avenue
# Cambridge, MA 02138 USA
# Telephone: (617) 495-3067
# Facsimile: (617) 495-9568
# E-mail: otd@harvard.edu
#
# 3.  OWNERSHIP AND COPYRIGHT NOTICE. Harvard, Toronto and Socpra own
# all intellectual property in the Software. End User shall gain no
# ownership to the Software. End User shall not remove or delete and
# shall retain in the Software, in any modifications to Software and
# in any Derivative Works, the copyright, trademark, or other notices
# pertaining to Software as provided with the Software.
#
# 4.  DERIVATIVE WORKS. End User may create and use Derivative Works,
# as such term is defined under U.S. copyright laws, provided that any
# such Derivative Works shall be restricted to non-commercial,
# internal research and academic use at End User’s Institution. End
# User may distribute Derivative Works to other Institutions solely
# for the performance of non-commercial, internal research and
# academic use on terms substantially similar to this License and
# Terms of Use.
#
# 5.  FEEDBACK. In order to improve the Software, comments from End
# Users may be useful. End User agrees to provide Harvard with
# feedback on the End User’s use of the Software (e.g., any bugs in
# the Software, the user experience, etc.).  Harvard is permitted to
# use such information provided by End User in making changes and
# improvements to the Software without compensation or an accounting
# to End User.
#
# 6.  NON ASSERT. End User acknowledges that Harvard, Toronto and/or
# Sherbrooke or Socpra may develop modifications to the Software that
# may be based on the feedback provided by End User under Section 5
# above. Harvard, Toronto and Sherbrooke/Socpra shall not be
# restricted in any way by End User regarding their use of such
# information.  End User acknowledges the right of Harvard, Toronto
# and Sherbrooke/Socpra to prepare, publish, display, reproduce,
# transmit and or use modifications to the Software that may be
# substantially similar or functionally equivalent to End User’s
# modifications and/or improvements if any.  In the event that End
# User obtains patent protection for any modification or improvement
# to Software, End User agrees not to allege or enjoin infringement of
# End User’s patent against Harvard, Toronto or Sherbrooke or Socpra,
# or any of the researchers, medical or research staff, officers,
# directors and employees of those institutions.
#
# 7.  PUBLICATION & ATTRIBUTION. End User has the right to publish,
# present, or share results from the use of the Software.  In
# accordance with customary academic practice, End User will
# acknowledge Harvard, Toronto and Sherbrooke/Socpra as the providers
# of the Software and may cite the relevant reference(s) from the
# following list of publications:
#
# Practical Bayesian Optimization of Machine Learning Algorithms
# Jasper Snoek, Hugo Larochelle and Ryan Prescott Adams
# Neural Information Processing Systems, 2012
#
# Multi-Task Bayesian Optimization
# Kevin Swersky, Jasper Snoek and Ryan Prescott Adams
# Advances in Neural Information Processing Systems, 2013
#
# Input Warping for Bayesian Optimization of Non-stationary Functions
# Jasper Snoek, Kevin Swersky, Richard Zemel and Ryan Prescott Adams
# Preprint, arXiv:1402.0929, http://arxiv.org/abs/1402.0929, 2013
#
# Bayesian Optimization and Semiparametric Models with Applications to
# Assistive Technology Jasper Snoek, PhD Thesis, University of
# Toronto, 2013
#
# 8.  NO WARRANTIES. THE SOFTWARE IS PROVIDED "AS IS." TO THE FULLEST
# EXTENT PERMITTED BY LAW, HARVARD, TORONTO AND SHERBROOKE AND SOCPRA
# HEREBY DISCLAIM ALL WARRANTIES OF ANY KIND (EXPRESS, IMPLIED OR
# OTHERWISE) REGARDING THE SOFTWARE, INCLUDING BUT NOT LIMITED TO ANY
# IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
# PURPOSE, OWNERSHIP, AND NON-INFRINGEMENT.  HARVARD, TORONTO AND
# SHERBROOKE AND SOCPRA MAKE NO WARRANTY ABOUT THE ACCURACY,
# RELIABILITY, COMPLETENESS, TIMELINESS, SUFFICIENCY OR QUALITY OF THE
# SOFTWARE.  HARVARD, TORONTO AND SHERBROOKE AND SOCPRA DO NOT WARRANT
# THAT THE SOFTWARE WILL OPERATE WITHOUT ERROR OR INTERRUPTION.
#
# 9.  LIMITATIONS OF LIABILITY AND REMEDIES. USE OF THE SOFTWARE IS AT
# END USER’S OWN RISK. IF END USER IS DISSATISFIED WITH THE SOFTWARE,
# ITS EXCLUSIVE REMEDY IS TO STOP USING IT.  IN NO EVENT SHALL
# HARVARD, TORONTO OR SHERBROOKE OR SOCPRA BE LIABLE TO END USER OR
# ITS INSTITUTION, IN CONTRACT, TORT OR OTHERWISE, FOR ANY DIRECT,
# INDIRECT, SPECIAL, INCIDENTAL, CONSEQUENTIAL, PUNITIVE OR OTHER
# DAMAGES OF ANY KIND WHATSOEVER ARISING OUT OF OR IN CONNECTION WITH
# THE SOFTWARE, EVEN IF HARVARD, TORONTO OR SHERBROOKE OR SOCPRA IS
# NEGLIGENT OR OTHERWISE AT FAULT, AND REGARDLESS OF WHETHER HARVARD,
# TORONTO OR SHERBROOKE OR SOCPRA IS ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGES.
#
# 10. INDEMNIFICATION. To the extent permitted by law, End User shall
# indemnify, defend and hold harmless Harvard, Toronto and Sherbrooke
# and Socpra, their corporate affiliates, current or future directors,
# trustees, officers, faculty, medical and professional staff,
# employees, students and agents and their respective successors,
# heirs and assigns (the "Indemnitees"), against any liability,
# damage, loss or expense (including reasonable attorney's fees and
# expenses of litigation) incurred by or imposed upon the Indemnitees
# or any one of them in connection with any claims, suits, actions,
# demands or judgments arising from End User’s breach of this
# Agreement or its Institution’s use of the Software except to the
# extent caused by the gross negligence or willful misconduct of
# Harvard, Toronto or Sherbrooke or Socpra. This indemnification
# provision shall survive expiration or termination of this Agreement.
#
# 11. GOVERNING LAW. This Agreement shall be construed and governed by
# the laws of the Commonwealth of Massachusetts regardless of
# otherwise applicable choice of law standards.
#
# 12. NON-USE OF NAME.  Nothing in this License and Terms of Use shall
# be construed as granting End Users or their Institutions any rights
# or licenses to use any trademarks, service marks or logos associated
# with the Software.  You may not use the terms “Harvard” or
# “University of Toronto” or “Université de Sherbrooke” or “Socpra
# Sciences et Génie S.E.C.” (or a substantially similar term) in any
# way that is inconsistent with the permitted uses described
# herein. You agree not to use any name or emblem of Harvard, Toronto
# or Sherbrooke, or any of their subdivisions for any purpose, or to
# falsely suggest any relationship between End User (or its
# Institution) and Harvard, Toronto and/or Sherbrooke, or in any
# manner that would infringe or violate any of their rights.
#
# 13. End User represents and warrants that it has the legal authority
# to enter into this License and Terms of Use on behalf of itself and
# its Institution.

import numpy          as np
import numpy.random   as npr
import scipy.stats    as sps
import scipy.linalg   as spla
import numpy.linalg   as npla
import scipy.optimize as spo
import copy
import traceback
import warnings
import sys

from collections import defaultdict
from spearmint.grids import sobol_grid
from spearmint.acquisition_functions.abstract_acquisition_function import AbstractAcquisitionFunction
from spearmint.utils.numerics import logcdf_robust
from spearmint.models.gp import GP
from spearmint.utils.moop            import MOOP_basis_functions
from spearmint.utils.moop            import _cull_algorithm
from spearmint.utils.moop            import _compute_pareto_front_and_set_summary_x_space
from scipy.spatial.distance import cdist

from spearmint.models.abstract_model import function_over_hypers
import logging

try:
    import nlopt
except:
    nlopt_imported = False
else:
    nlopt_imported = True
# see http://ab-initio.mit.edu/wiki/index.php/NLopt_Python_Reference

EPS = 1e-6
NUM_RANDOM_FEATURES = 1000
PARETO_SET_SIZE = 10
NSGA2_POP = 100
NSGA2_EPOCHS = 100
GRID_SIZE = 1000
USE_GRID_ONLY = False

PESM_OPTION_DEFAULTS  = {
    'mesmoc_num_random_features'      : 1000,
    'mesmoc_pareto_set_size'      : 10,
    'mesmoc_grid_size'      : 1000,
    'mesmoc_not_constrain_predictions' : False,
    'mesmoc_samples_per_hyper' : 1,
    'mesmoc_use_grid_only_to_solve_problem' : False,
    'mesmoc_nsga2_pop' : 100,
    'mesmoc_nsga2_epochs' : 100,
    'mesmoc_noisy' : True
    }

"""
FOR GP MODELS ONLY
"""

# get the values of samples of the solution to the problem

def sample_solution(num_dims, obj_model_dict, con_models_dict, grid_default_chooser):

    # We find the inputs to be added to the grid (we avoid adding repeated inputs)
    objectives_gp = obj_model_dict.values()
    constraint_gps = con_models_dict.values()

    X = objectives_gp[ 0 ].inputs

    for i in range(len(objectives_gp) - 1):
        X_to_add = objectives_gp[ i + 1 ].inputs

        for j in range(X_to_add.shape[ 0 ]):
            if np.min(cdist(X, X_to_add[ j : (j + 1), : ])) > 1e-8:
                X = np.vstack((X , X_to_add[ j : (j + 1), : ]))

    for i in range(len(constraint_gps)):
        X_to_add = constraint_gps[ i ].inputs

        for j in range(X_to_add.shape[ 0 ]):
            if np.min(cdist(X, X_to_add[ j : (j + 1), : ])) > 1e-8:
                X = np.vstack((X , X_to_add[ j : (j + 1), : ]))

    inputs = X

    while True:
        MAX_ATTEMPTS = 10
        num_attempts = 0

        while num_attempts < MAX_ATTEMPTS:

            # 1. The procedure is: sample all f on the grid "cand" (or use a smaller grid???)
            # 2. Look for the pareto set

            gp_samples = dict()

            gp_samples['objectives'] = [ sample_gp_with_random_features(objective_gp, NUM_RANDOM_FEATURES) for \
                objective_gp in objectives_gp ]
            gp_samples['constraints'] = [sample_gp_with_random_features(constraint_gp, NUM_RANDOM_FEATURES) for \
                constraint_gp in constraint_gps]
            # import pdb; pdb.set_trace()
            pareto_set = global_optimization_of_GP_approximation(gp_samples, num_dims, inputs, grid_default_chooser)

            if pareto_set is not None: # success
                logging.debug('successfully sampled X* in %d attempt(s)' % (num_attempts+1))

                pareto_front = {'objectives': dict(), 'constraints': dict()}
                for k, gp_sampler in zip(obj_model_dict.keys(), gp_samples['objectives']):
                    pareto_front['objectives'][ k ] = gp_sampler(pareto_set, False)

                for k, gp_sampler in zip(con_models_dict.keys(), gp_samples['constraints']):
                    pareto_front['constraints'][ k ] = gp_sampler(pareto_set, False)

                return pareto_front #, pareto_set

            num_attempts += 1

        print "10 attempts aren't enough, so we're running another 10\n"

    # We mustn't return None, because it cause to end the execution
    return None

# raise npla.linalg.LinAlgError("Unable to sample valid pareto set that satisfies the constrains !")

# Compute log of the normal CDF of x in a robust way
# Based on the fact that log(cdf(x)) = log(1-cdf(-x))
# and log(1-z) ~ -z when z is small, so  this is approximately
# -cdf(-x), which is just the same as -sf(x) in scipy
def logcdf_robust(x):

    if isinstance(x, np.ndarray):
        ret = sps.norm.logcdf(x)
        ret[x > 5] = -sps.norm.sf(x[x > 5])
    elif x > 5:
        ret = -sps.norm.sf(x)
    else:
        ret = sps.norm.logcdf(x)

    return ret

# Compute log(exp(a)+exp(b)) in a robust way.
def logSumExp_scalar(a, b):

    if a > b:
        # compute log(exp(a)+exp(b))
        # this is just the log-sum-exp trick but with only 2 terms in the sum
        # we chooser to factor out the largest one
        # log(exp(a)+exp(b)) = log( exp(a) [1 + exp(b-a) ] )
        # = a + log(1 + exp(b-a))
        return a + log_1_plus_exp_x(b-a)
    else:
        return b + log_1_plus_exp_x(a-b)

def logSumExp(a,b):
    if (not isinstance(a, np.ndarray) or a.size==1) and (not isinstance(b, np.ndarray) or b.size==1):
        return logSumExp_scalar(a,b)

    result = np.zeros(a.shape)
    result[a>b] =  a[a>b]  + log_1_plus_exp_x(b[a>b] -a[a>b])
    result[a<=b] = b[a<=b] + log_1_plus_exp_x(a[a<=b]-b[a<=b])
    return result

def log_1_plus_exp_x_scalar(x):
# Compute log(1+exp(x)) in a robust way
    if x < np.log(1e-6):
        # if exp(x) is very small, i.e. less than 1e-6, then we can apply the taylor expansion:
        # log(1+x) approx equals x when x is small
        return np.exp(x)
    elif x > np.log(100):
        # if exp(x) is very large, i.e. greater than 100, then we say the 1 is negligible comared to it
        # so we just return log(exp(x))=x
        return x
    else:
        return np.log(1.0+np.exp(x))

def log_1_plus_exp_x(x):
    if not isinstance(x, np.ndarray) or x.size==1:
        return log_1_plus_exp_x_scalar(x)

    result = np.log(1.0+np.exp(x)) # case 3
    result[x < np.log(1e-6)] = np.exp(x[x < np.log(1e-6)])
    result[x > np.log(100) ] = x [x > np.log(100) ]
    return result

# Compute log(1-exp(x)) in a robust way, when exp(x) is between 0 and 1
# well, exp(x) is always bigger than 0
# but it cannot be above 1 because then we have log of a negative number
def log_1_minus_exp_x_scalar(x):
    if x < np.log(1e-6):
        # if exp(x) is very small, i.e. less than 1e-6, then we can apply the taylor expansion:
        # log(1-x) approx equals -x when x is small
        return -np.exp(x)
    elif x > -1e-6:
        # if x > -1e-6, i.e. exp(x) > exp(-1e-6), then we do the Taylor expansion of exp(x)=1+x+...
        # then the argument of the log, 1- exp(x), becomes, approximately, 1-(1+x) = -x
        # so we are left with log(-x)
        return np.log(-x)
    else:
        return np.log(1.0-np.exp(x))

def log_1_minus_exp_x(x):
    if not isinstance(x, np.ndarray) or x.size==1:
        return log_1_minus_exp_x_scalar(x)

    assert np.all(x <= 0)

    case1 = x < np.log(1e-6) # -13.8
    case2 = x > -1e-6
    case3 = np.logical_and(x >= np.log(1e-6), x <= -1e-6)
    assert np.all(case1+case2+case3 == 1)

    result = np.zeros(x.shape)
    result[case1] = -np.exp(x[case1])
    with np.errstate(divide='ignore'): # if x is exactly 0, give -inf without complaining
        result[case2] = np.log(-x[case2])
    result[case3] = np.log(1.0-np.exp(x[case3]))

    return result

def chol2inv(chol):
    return spla.cho_solve((chol, False), np.eye(chol.shape[0]))

def matrixInverse(M):
    return chol2inv(spla.cholesky(M, lower=False))

def ep(obj_models, pareto_set, minimize=True, con_models=[], input_space=None):

    all_tasks = obj_models.copy()
    all_constraints= con_models.copy()

    # X contains first the pareto set and then, the observed data instances

    X = pareto_set

    for t in all_tasks:
	Xtask = obj_models[ t ].observed_inputs
	for i in range(Xtask.shape[ 0 ]):
		if np.min(cdist(Xtask[ i : (i + 1), : ], X)) > 1e-8:
		    	X = np.vstack((X, Xtask[ i, ]))

    for t in all_constraints:
	Xtask = con_models[ t ].observed_inputs
	for i in range(Xtask.shape[ 0 ]):
		if np.min(cdist(Xtask[ i : (i + 1), : ], X)) > 1e-8:
		    	X = np.vstack((X, Xtask[ i, ]))

    n_obs = X.shape[ 0 ] - pareto_set.shape[ 0 ]

    # We only consider at most 100 observations

    if n_obs >= 100:
        X_sel = X[ pareto_set.shape[ 0 ] + np.random.choice(n_obs, 100, False), : ]
        X = np.vstack((pareto_set, X_sel))
        n_obs = 100

    n_total = X.shape[ 0 ]
    n_pset = pareto_set.shape[ 0 ]

    q = len(all_tasks)
    c = len(all_constraints)

    # We construct the Vpred matrices and the mPred vectors

    mPred         = dict()
    Vpred         = dict()
    cholVpred     = dict()
    VpredInv      = dict()
    cholKstarstar = dict()

    mPred_cons         = dict()
    Vpred_cons         = dict()
    cholVpred_cons     = dict()
    VpredInv_cons      = dict()
    cholKstarstar_cons = dict()

    for t in all_tasks:
        mPred[t], Vpred[t] = all_tasks[t].predict(X, full_cov=True)
        cholVpred[t]       = spla.cholesky(Vpred[t])
        VpredInv[t]        = chol2inv(cholVpred[t])
        # Perform a redundant computation of this thing because predict() doesn't return it...
        cholKstarstar[t]   = spla.cholesky(all_tasks[t].noiseless_kernel.cov(X))

    for cons in all_constraints:
        mPred_cons[cons], Vpred_cons[cons] = all_constraints[cons].predict(X, full_cov=True)
        cholVpred_cons[cons]        = spla.cholesky(Vpred_cons[cons])
        VpredInv_cons[cons]         = chol2inv(cholVpred_cons[cons])
        # Perform a redundant computation of this thing because predict() doesn't return it...
        cholKstarstar_cons[cons]   = spla.cholesky(all_constraints[cons].noiseless_kernel.cov(X))

    jitter = dict()
    for task in all_tasks:
        jitter[ task ] = obj_models[ task ].jitter_value()
    for cons in all_constraints:
        jitter[ cons ] = con_models[ cons ].jitter_value()

    # We create the posterior approximation

    a = {
        'objs'     : obj_models,
        'cons'     : con_models,
        'ahfhat'   : np.zeros((n_obs, n_pset, q, 2, 2)), # intiialize approximate factors to 0
        'bhfhat'   : np.zeros((n_obs, n_pset, q, 2)),
        'chfhat'   : np.zeros((n_pset, n_pset, q, 2, 2)), # intiialize approximate factors to 0
        'dhfhat'   : np.zeros((n_pset, n_pset, q, 2)),
        'ehfhat'   : np.zeros((n_pset, c)), # intiialize approximate factors to 0
        'fhfhat'   : np.zeros((n_pset, c)),
        'a_c_hfhat'   : np.zeros((n_obs, n_pset, c)), # intiialize approximate factors to 0
        'b_c_hfhat'   : np.zeros((n_obs, n_pset, c)),
        'c_c_hfhat'   : np.zeros((n_pset, n_pset, c)), # intiialize approximate factors to 0
        'd_c_hfhat'   : np.zeros((n_pset, n_pset, c)),
        'm'        : defaultdict(lambda: np.zeros(n_total)),  # marginals
        'm_nat'    : defaultdict(lambda: np.zeros(n_total)),  # marginals (natural parameters)
        'V'        : defaultdict(lambda: np.zeros((n_total, n_total))),
        'Vinv'     : defaultdict(lambda: np.zeros((n_total, n_total))),
        'm_cons'        : defaultdict(lambda: np.zeros(n_total)),  # marginals
        'm_nat_cons'    : defaultdict(lambda: np.zeros(n_total)),  # marginals (natural parameters)
        'V_cons'        : defaultdict(lambda: np.zeros((n_total, n_total))),
        'Vinv_cons'     : defaultdict(lambda: np.zeros((n_total, n_total))),
	'n_obs'    : n_obs,
	'n_total'  : n_total,
	'n_pset'   : n_pset,
	'q'        : q,
	'c'        : c,
        'cholV'    : dict(),
        'cholV_cons'    : dict(),
        'mPred'    : mPred,
        'Vpred'    : Vpred,
        'VpredInv' : VpredInv,
        'cholKstarstar' : cholKstarstar,
        'mPred_cons'    : mPred_cons,
        'Vpred_cons'    : Vpred_cons,
        'VpredInv_cons' : VpredInv_cons,
        'cholKstarstar_cons' : cholKstarstar_cons,
        'jitter'   : jitter,
	'X'        : X
    }

    # We start the main loop of EP

    convergence = False
    damping     = 0.5
    iteration   = 1

    a = updateMarginals(copy.deepcopy(a))
    aOld = copy.deepcopy(a)
    aOriginal = copy.deepcopy(a)

    while not convergence:

	update_correct = False
	damping_inner = damping
	fail = False
	second_update = False

        # We update the factors

        while update_correct == False:

            error = False

            try:

                # We update the factors Ahfhat, bhfhat, ahchat, bhchat, agchat, bgchat

#		aNew = updateFactors_fast_daniel_robust(copy.deepcopy(a), damping_inner, minimize = minimize, \
#                    no_negative_variances_nor_nands = True)

#		aNew = updateFactors_fast_daniel(copy.deepcopy(a), damping_inner, minimize = minimize)

		aNew = updateFactors_fast_daniel_no_constraints_pareto_set_robust(copy.deepcopy(a), damping_inner, minimize = minimize,
                    no_negative_variances_nor_nands = False)
                aNew = updateMarginals(copy.deepcopy(aNew))

            except npla.linalg.LinAlgError as e:
		error = True

	    if error == False:

		if fail == True and second_update == False:
			a = aNew.copy()
			second_update = True
		else:
			update_correct = True

	    else:

		a = copy.deepcopy(aOld)
		damping_inner = damping_inner * 0.5
		fail = True
		second_update = False

		print 'Reducing damping factor to guarantee EP update! Damping: %f' % (damping_inner)

	aOld = copy.deepcopy(a)
	a = copy.deepcopy(aNew)

        change = 0.0

        for t in all_tasks:
            change = max(change, np.max(np.abs(a['m'][t] - aOld['m'][t])))
            change = max(change, np.max(np.abs(a['V'][t] - aOld['V'][t])))

	#if damping < 0.01:
	 #	import pdb; pdb.set_trace();

	print '%d:\t change=%f \t damping: %f' % (iteration, change, damping)

        if change < 1e-3 and iteration > 2:
            convergence = True

        damping   *= 0.99
        iteration += 1

    # DHL: I have changed this since it seems it is only required outside EP

    for obj in all_tasks:
        a['cholV'][ obj ] = spla.cholesky(a['V'][obj], lower=False)
    for cons in all_constraints:
        a['cholV_cons'][ cons ] = spla.cholesky(a['V_cons'][cons], lower=False)

    #import pdb; pdb.set_trace()

    return a

# Updated a['V'], a['Vinv'] and a['m']
def updateMarginals(a):

	n_obs = a['n_obs']
	n_total = a['n_total']
	n_pset = a['n_pset']
	objectives = a['objs']
	constraints = a['cons']
	all_tasks = objectives
	all_constraints = constraints

	ntask = 0

	# Updating constraint distribution marginals.

	for cons in all_constraints:

		# Summing all the factors into the diagonal. Reescribir.

		vTilde_cons = np.zeros((n_total,n_total))
		vTilde_cons[ np.eye(n_total).astype('bool') ] = np.append(np.sum(a['c_c_hfhat'][ :, : , ntask ], axis = 1) + \
			a['ehfhat'][ :, ntask ], np.sum(a['a_c_hfhat'][ :, : , ntask ], axis = 1))

		mTilde_cons = np.append(np.sum(a['d_c_hfhat'][ :, : , ntask ], axis = 1) + a['fhfhat'][ :, ntask ] , \
			np.sum(a['b_c_hfhat'][ :, : , ntask ], axis = 1))

		# Natural parameter conversion and update of the marginal variance matrices.

		a['Vinv_cons'][cons] = a['VpredInv_cons'][cons] + vTilde_cons
		a['V_cons'][cons] = matrixInverse(a['VpredInv_cons'][cons] + vTilde_cons)

		# Natural parameter conversion and update of the marginal mean vector.

		a['m_nat_cons'][cons] = np.dot(a['VpredInv_cons'][cons], a['mPred_cons'][cons]) + mTilde_cons
		a['m_cons'][cons] = np.dot(a['V_cons'][cons], a['m_nat_cons'][ cons ])
		ntask = ntask + 1

	# We compute the updated distribution for the objectives (means and covariance matrices)

	ntask = 0
	for obj in all_tasks:

		vTilde = np.zeros((n_total,n_total))

		vTilde[ np.eye(n_total).astype('bool') ] = np.append(np.sum(a['ahfhat'][ :, : , ntask, 1, 1 ], axis = 0) + \
			np.sum(a['chfhat'][ :, : , ntask, 0, 0 ], axis = 1) + np.sum(a['chfhat'][ :, : , ntask, 1, 1 ], axis = 0),  \
			np.sum(a['ahfhat'][ :, : , ntask, 0, 0 ], axis = 1))

		vTilde[ 0 : n_pset, 0 : n_pset ] = vTilde[ 0 : n_pset, 0 : n_pset ] + \
			a['chfhat'][ :, : , ntask, 0, 1 ] + a['chfhat'][ :, : , ntask, 1, 0 ].T

		vTilde[ n_pset : n_total, 0 : n_pset ] = a['ahfhat'][ :, :, ntask, 0, 1]
		vTilde[ 0 : n_pset, n_pset : n_total ] =  a['ahfhat'][ :, :, ntask, 0, 1].transpose()

		a['Vinv'][obj] = a['VpredInv'][obj] + vTilde
		a['V'][obj] = matrixInverse(a['VpredInv'][obj] + vTilde)

		mTilde = np.append(np.sum(a['bhfhat'][ :, : , ntask, 1 ], axis = 0) + \
			np.sum(a['dhfhat'][ :, : , ntask, 0 ], axis = 1) + np.sum(a['dhfhat'][ :, : , ntask, 1 ], axis = 0), \
			np.sum(a['bhfhat'][ :, : , ntask, 0 ], axis = 1))
		a['m_nat'][obj] = np.dot(a['VpredInv'][obj], a['mPred'][obj]) + mTilde
		a['m'][obj] = np.dot(a['V'][obj], a['m_nat'][ obj ])
		ntask = ntask + 1

	return a

def two_by_two_symmetric_matrix_inverse(a, b, c):

	det = a * b - c * c
	a_new = 1.0 / det * b
	b_new = 1.0 / det * a
	c_new = 1.0 / det * - c

	return a_new, b_new, c_new

def two_by_two_matrix_inverse(a, b, c, d):

	det = a * d - c * b
	a_new = 1.0 / det * d
	b_new = 1.0 / det * -b
	c_new = 1.0 / det * - c
	d_new = 1.0 / det * a

	return a_new, b_new, c_new, d_new

def two_by_two_symmetric_matrix_product_vector(a, b, c, v_a, v_b):

	return a * v_a + c * v_b, c * v_a + b * v_b

# Based on the original code, with a few modifications

def updateFactors_daniel_robust(a, damping, minimize=True):

	# used to switch between minimizing and maximizing

	sgn = -1.0 if minimize else 1.0

	# We update the h factors

	all_tasks = a['objs']
	constraints = a['cons']

	n_obs = a['n_obs']
	n_pset = a['n_pset']
	n_total = a['n_total']

	# First we update the external (easy) factors that only affect the constraints

	n_cons = 0
	for cons in constraints:

		# We obtain the cavities

		Vfinv = 1.0 / np.diag(a['V_cons'][ cons ])[ 0 : n_pset ]
		VfOldinv = Vfinv - a['ehfhat'][ :, n_cons ]
		VfOld = 1.0 / VfOldinv
		m_nat = a['m_cons'][ cons ][ 0 : n_pset ] / np.diag(a['V_cons'][ cons ])[ 0 : n_pset ]
		mfOld = VfOld * (m_nat - a['fhfhat'][ :, n_cons ])

		if np.any(VfOld < 0):
			raise npla.linalg.LinAlgError("Negative value in the sqrt!")

		# We compute the quantities required for the update

		alpha = mfOld / np.sqrt(VfOld)
		logZ = logcdf_robust(alpha)

		ratio = np.exp(sps.norm.logpdf(alpha) - logZ)
		dlogZdmfOld = ratio / np.sqrt(VfOld)
                dlogZdmfOld2 = - ratio * (alpha + ratio) / VfOld

		# We find the parameters of the updated factors

		ehfHatNew = - dlogZdmfOld2 / (1.0 + dlogZdmfOld2 * VfOld)
		fhfHatNew = (dlogZdmfOld - mfOld * dlogZdmfOld2) / (1.0 + dlogZdmfOld2 * VfOld)

		# We do the actual update with damping

		a['ehfhat'][ :, n_cons ] = damping * ehfHatNew + (1 - damping) * a['ehfhat'][ :, n_cons ]
		a['fhfhat'][ :, n_cons ] = damping * fhfHatNew + (1 - damping) * a['fhfhat'][ :, n_cons ]

		n_cons +=1

	alpha = np.zeros(a['q'])
	alpha_cons = np.zeros(a['c'])
	ratio = np.zeros(a['q'])
	ratio_cons = np.zeros(a['c'])
	s = np.zeros(a['q'])
	s_cons  = np.zeros(a['c'])
	mfOld = dict()
	VfOld = dict()
	mfOld_cons = dict()
	VfOld_cons = dict()

	# Next we update the complicated factors

	# First we update the factors corresponding to the observed data

	for i in xrange(n_obs):
		for j in xrange(n_pset):

			n_task = 0
			for obj in all_tasks:

				# We obtain the cavities

				Vfinv = matrixInverse(a['V'][ obj ][ np.ix_([ i + n_pset, j ], [ i + n_pset, j ]) ])
				VfOldinv = Vfinv - a['ahfhat'][ i, j, n_task, :, : ]
				VfOld[ obj ] = matrixInverse(VfOldinv)
        			mfOld[ obj ] = np.dot(VfOld[ obj ], np.dot(Vfinv, a['m'][ obj ][[ i + n_pset, j ]]) \
					- a['bhfhat'][ i, j, n_task,: ])

				# We compute the quantities required for the updates

				s[ n_task ]  = VfOld[ obj ][0, 0] + VfOld[ obj ][1, 1] - 2.0 * VfOld[ obj ][1, 0]

				if s[ n_task ] < 0:
					raise npla.linalg.LinAlgError("Negative value in the sqrt!")

				# The first component of mfOld[ obj ] contains the point and the second the point from the pareto set

        			alpha[ n_task ] = (mfOld[ obj ][ 0 ] - mfOld[ obj ][ 1 ]) / np.sqrt(s[ n_task ]) * sgn
				n_task = n_task + 1

			# Now for the constrains

			n_cons = 0
			for cons in constraints:

				# We obtain the cavities

				Vfinv = 1.0 / np.diag(a['V_cons'][ cons ])[ i + n_pset ]
				VfOldinv = Vfinv - a['a_c_hfhat'][ i, j, n_cons ]
				VfOld_cons[ cons ] = 1.0 / VfOldinv
				m_nat = a['m_cons'][ cons ][ i + n_pset ] / np.diag(a['V_cons'][ cons ])[ i + n_pset ]
				mfOld_cons[ cons ] = VfOld_cons[ cons ] * (m_nat - a['b_c_hfhat'][ i, j, n_cons ])
				s_cons[ n_cons ] = VfOld_cons[ cons ]

				if s_cons[ n_cons ] < 0:
					raise npla.linalg.LinAlgError("Negative value in the sqrt!")

				alpha_cons[ n_cons ] = mfOld_cons[ cons ] / np.sqrt(VfOld_cons[ cons ])

				n_cons += 1

                        # Robust implementation

       			log_phi = logcdf_robust(alpha)
       			log_phi_cons = logcdf_robust(alpha_cons)
        		logZ_orig = log_1_minus_exp_x(np.sum(log_phi))

                        if logZ_orig  == -np.inf:
                            logZ_orig = logcdf_robust(-np.min(alpha))

			logZ_term1 = np.sum(log_phi_cons) + logZ_orig
			logZ_term2 = log_1_minus_exp_x(np.sum(log_phi_cons))

                        if logZ_term2 == -np.inf:
                            logZ_term2 = logcdf_robust(-np.min(alpha_cons))

                        max_value = np.maximum(logZ_term1, logZ_term2)

			logZ = np.log(np.exp(logZ_term1 - max_value) + np.exp(logZ_term2 - max_value)) + max_value

			n_task = 0
			for obj in all_tasks:

				ratio[ n_task ] = - np.exp(sps.norm.logpdf(alpha[ n_task ]) - logZ + np.sum(logcdf_robust(alpha)) \
					- logcdf_robust(alpha[ n_task ]) + np.sum(logcdf_robust(alpha_cons)))

				dlogZdmfOld = ratio[ n_task ] / np.sqrt(s[ n_task ]) * np.array([ 1.0, -1.0 ]) * sgn
                                dlogZdmfOld2 = - ratio[ n_task ] / s[ n_task ] * (alpha[ n_task ] + ratio[ n_task ]) \
                                            * np.array([[1.0,-1.0], [-1.0, 1.0]])

                                ahfHatNew = - np.dot(dlogZdmfOld2, spla.inv(np.dot(VfOld[ obj ], dlogZdmfOld2) + np.eye(2)))
                                bhfHatNew = np.dot(dlogZdmfOld - np.dot(mfOld[ obj ], dlogZdmfOld2), \
                                     spla.inv(np.dot(VfOld[ obj ], dlogZdmfOld2) + np.eye(2)))

				# We do the actual update with damping

				a['ahfhat'][ i, j , n_task, :, : ] = damping * ahfHatNew + (1 - damping) * a['ahfhat'][ i, j , n_task, :, : ]
				a['bhfhat'][ i, j , n_task, : ] = damping * bhfHatNew + (1 - damping) * a['bhfhat'][ i, j , n_task, : ]

				n_task = n_task + 1

			# Now for the constraints

			n_cons = 0
			for cons in constraints:

				ratio_cons[ n_cons ] = np.exp(sps.norm.logpdf(alpha_cons[ n_cons ]) - logZ + \
					logZ_orig + np.sum(logcdf_robust(alpha_cons)) - logcdf_robust(alpha_cons[ n_cons ])) - \
					np.exp(sps.norm.logpdf(alpha_cons[ n_cons ]) - logZ + np.sum(logcdf_robust(alpha_cons)) \
					- logcdf_robust(alpha_cons[ n_cons ]))

				dlogZdmfOld = ratio_cons[ n_cons ] / np.sqrt(s_cons[ n_cons ])
                                dlogZdmfOld2 = - ratio_cons[ n_cons ] / s_cons[ n_cons ] * (alpha_cons[ n_cons ] + ratio_cons[ n_cons ])

            		        achfhatNew = - dlogZdmfOld2 / (1.0 + dlogZdmfOld2 * VfOld_cons[ cons ])
                                bchfhatNew = (dlogZdmfOld - mfOld_cons[ cons ] * dlogZdmfOld2) / (1.0 + dlogZdmfOld2 * VfOld_cons[ cons ])

				a['a_c_hfhat'][ i, j , n_cons ] = damping * achfhatNew + (1 - damping) * a['a_c_hfhat'][ i, j , n_cons ]
				a['b_c_hfhat'][ i, j , n_cons ] = damping * bchfhatNew + (1 - damping) * a['b_c_hfhat'][ i, j , n_cons ]

				n_cons += 1

	# Second we update the factors corresponding to the pareto set

	for j1 in xrange(n_pset):
		for j2 in xrange(n_pset):

			if not j1 == j2:

				n_task = 0
				for obj in all_tasks:

					# We obtain the cavities

					Vfinv = matrixInverse(a['V'][ obj ][ np.ix_([ j1, j2 ], [ j1, j2 ]) ])
					VfOldinv = Vfinv - a['chfhat'][ j1, j2, n_task, :, : ]
					VfOld[ obj ] = matrixInverse(VfOldinv)
	       	 			mfOld[ obj ] = np.dot(VfOld[ obj ], np.dot(Vfinv, a['m'][ obj ][[ j1, j2 ]]) \
						- a['dhfhat'][ j1, j2, n_task, : ])

					# We compute the quantities required for the updates

					s[ n_task ]  = VfOld[ obj ][0, 0] +  VfOld[ obj ][1, 1] - 2.0 * VfOld[ obj ][1, 0]

					if s[ n_task ] < 0:
						raise npla.linalg.LinAlgError("Negative value in the sqrt!")

					# The first component of mfOld[ obj ] contains the point and the second the point from the pareto set

       		 			alpha[ n_task ] = (mfOld[ obj ][ 0 ] - mfOld[ obj ][ 1 ]) / np.sqrt(s[ n_task ]) * sgn
					n_task = n_task + 1

        			# Now for the constrains

				n_cons = 0
				for cons in constraints:

					# We obtain the cavities

					Vfinv = 1.0 / np.diag(a['V_cons'][ cons ])[ j1 ]
					VfOldinv = Vfinv - a['c_c_hfhat'][ j1, j2, n_cons ]
					VfOld_cons[ cons ] = 1.0 / VfOldinv
					m_nat = a['m_cons'][ cons ][ j1 ] / np.diag(a['V_cons'][ cons ])[ j1 ]
					mfOld_cons[ cons ] = VfOld_cons[ cons ] * (m_nat - a['d_c_hfhat'][ j1, j2, n_cons ])
					s_cons[ n_cons ] = VfOld_cons[ cons ]

					if s_cons[ n_cons ] < 0:
						raise npla.linalg.LinAlgError("Negative value in the sqrt!")

					alpha_cons[ n_cons ] = mfOld_cons[ cons ] / np.sqrt(VfOld_cons[ cons ])

					n_cons += 1

                                # Robust implementation

       	        		log_phi = logcdf_robust(alpha)
       		        	log_phi_cons = logcdf_robust(alpha_cons)
        	        	logZ_orig = log_1_minus_exp_x(np.sum(log_phi))

                                if logZ_orig  == -np.inf:
                                    logZ_orig = logcdf_robust(-np.min(alpha))

                                logZ_term1 = np.sum(log_phi_cons) + logZ_orig
                                logZ_term2 = log_1_minus_exp_x(np.sum(log_phi_cons))

                                if logZ_term2 == -np.inf:
                                    logZ_term2 = logcdf_robust(-np.min(alpha_cons))

                                max_value = np.maximum(logZ_term1, logZ_term2)

                                logZ = np.log(np.exp(logZ_term1 - max_value) + np.exp(logZ_term2 - max_value)) + max_value

				n_task = 0
				for obj in all_tasks:

        				ratio[ n_task ] = - np.exp(sps.norm.logpdf(alpha[ n_task ]) - logZ + np.sum(logcdf_robust(alpha)) \
        					- logcdf_robust(alpha[ n_task ]) + np.sum(logcdf_robust(alpha_cons)))

					dlogZdmfOld = ratio[ n_task ] / np.sqrt(s[ n_task ]) * np.array([ 1.0, -1.0 ]) * sgn
                                        dlogZdmfOld2 = - ratio[ n_task ] / s[ n_task ] * (alpha[ n_task ] + ratio[ n_task ]) \
                                            * np.array([[1.0,-1.0], [-1.0, 1.0]])

                                        chfHatNew = - np.dot(dlogZdmfOld2, spla.inv(np.dot(VfOld[ obj ], dlogZdmfOld2) + np.eye(2)))
                                        dhfHatNew = np.dot(dlogZdmfOld - np.dot(mfOld[ obj ], dlogZdmfOld2), \
                                            spla.inv(np.dot(VfOld[ obj ], dlogZdmfOld2) + np.eye(2)))

					# We do the actual update with damping

					a['chfhat'][ j1, j2, n_task, :, : ] = damping * chfHatNew + \
						(1 - damping) * a['chfhat'][ j1, j2, n_task, :, : ]
					a['dhfhat'][ j1, j2, n_task, : ] = damping * dhfHatNew + \
						(1 - damping) * a['dhfhat'][ j1, j2 , n_task, : ]

					n_task = n_task + 1

                                # Now for the constraints

                                n_cons = 0
                                for cons in constraints:

                                    ratio_cons[ n_cons ] = np.exp(sps.norm.logpdf(alpha_cons[ n_cons ]) - logZ + \
                                        logZ_orig + np.sum(logcdf_robust(alpha_cons)) - logcdf_robust(alpha_cons[ n_cons ])) - \
					np.exp(sps.norm.logpdf(alpha_cons[ n_cons ]) - logZ + np.sum(logcdf_robust(alpha_cons)) \
					- logcdf_robust(alpha_cons[ n_cons ]))

                                    dlogZdmfOld = ratio_cons[ n_cons ] / np.sqrt(s_cons[ n_cons ])
                                    dlogZdmfOld2 = - ratio_cons[ n_cons ] / s_cons[ n_cons ] * (alpha_cons[ n_cons ] + ratio_cons[ n_cons ])

                                    cchfhatNew = - dlogZdmfOld2 / (1.0 + dlogZdmfOld2 * VfOld_cons[ cons ])
                                    dchfhatNew = (dlogZdmfOld - mfOld_cons[ cons ] * dlogZdmfOld2) / (1.0 + dlogZdmfOld2 * VfOld_cons[ cons ])

                                    a['c_c_hfhat'][ j1, j2, n_cons ] = damping * cchfhatNew + (1 - damping) * a['c_c_hfhat'][ j1, j2, n_cons ]
                                    a['d_c_hfhat'][ j1, j2, n_cons ] = damping * dchfhatNew + (1 - damping) * a['d_c_hfhat'][ j1, j2, n_cons ]

                                    n_cons += 1

	return a


# Based on the original code, with a few modifications

def updateFactors_daniel_no_constraints_pareto_set_robust(a, damping, minimize=True):

	# used to switch between minimizing and maximizing

	sgn = -1.0 if minimize else 1.0

	# We update the h factors

	all_tasks = a['objs']
	constraints = a['cons']

	n_obs = a['n_obs']
	n_pset = a['n_pset']
	n_total = a['n_total']

	# First we update the external (easy) factors that only affect the constraints

	n_cons = 0
	for cons in constraints:

		# We obtain the cavities

		Vfinv = 1.0 / np.diag(a['V_cons'][ cons ])[ 0 : n_pset ]
		VfOldinv = Vfinv - a['ehfhat'][ :, n_cons ]
		VfOld = 1.0 / VfOldinv
		m_nat = a['m_cons'][ cons ][ 0 : n_pset ] / np.diag(a['V_cons'][ cons ])[ 0 : n_pset ]
		mfOld = VfOld * (m_nat - a['fhfhat'][ :, n_cons ])

		if np.any(VfOld < 0):
			raise npla.linalg.LinAlgError("Negative value in the sqrt!")

		# We compute the quantities required for the update

		alpha = mfOld / np.sqrt(VfOld)
		logZ = logcdf_robust(alpha)

		ratio = np.exp(sps.norm.logpdf(alpha) - logZ)
		dlogZdmfOld = ratio / np.sqrt(VfOld)
                dlogZdmfOld2 = - ratio * (alpha + ratio) / VfOld

		# We find the parameters of the updated factors

		ehfHatNew = - dlogZdmfOld2 / (1.0 + dlogZdmfOld2 * VfOld)
		fhfHatNew = (dlogZdmfOld - mfOld * dlogZdmfOld2) / (1.0 + dlogZdmfOld2 * VfOld)

		# We do the actual update with damping

		a['ehfhat'][ :, n_cons ] = damping * ehfHatNew + (1 - damping) * a['ehfhat'][ :, n_cons ]
		a['fhfhat'][ :, n_cons ] = damping * fhfHatNew + (1 - damping) * a['fhfhat'][ :, n_cons ]

		n_cons +=1

	alpha = np.zeros(a['q'])
	alpha_cons = np.zeros(a['c'])
	ratio = np.zeros(a['q'])
	ratio_cons = np.zeros(a['c'])
	s = np.zeros(a['q'])
	s_cons  = np.zeros(a['c'])
	mfOld = dict()
	VfOld = dict()
	mfOld_cons = dict()
	VfOld_cons = dict()

	# Next we update the complicated factors

	# First we update the factors corresponding to the observed data

	for i in xrange(n_obs):
		for j in xrange(n_pset):

			n_task = 0
			for obj in all_tasks:

				# We obtain the cavities

				Vfinv = matrixInverse(a['V'][ obj ][ np.ix_([ i + n_pset, j ], [ i + n_pset, j ]) ])
				VfOldinv = Vfinv - a['ahfhat'][ i, j, n_task, :, : ]
				VfOld[ obj ] = matrixInverse(VfOldinv)
        			mfOld[ obj ] = np.dot(VfOld[ obj ], np.dot(Vfinv, a['m'][ obj ][[ i + n_pset, j ]]) \
					- a['bhfhat'][ i, j, n_task,: ])

				# We compute the quantities required for the updates

				s[ n_task ]  = VfOld[ obj ][0, 0] + VfOld[ obj ][1, 1] - 2.0 * VfOld[ obj ][1, 0]

				if s[ n_task ] < 0:
					raise npla.linalg.LinAlgError("Negative value in the sqrt!")

				# The first component of mfOld[ obj ] contains the point and the second the point from the pareto set

        			alpha[ n_task ] = (mfOld[ obj ][ 0 ] - mfOld[ obj ][ 1 ]) / np.sqrt(s[ n_task ]) * sgn
				n_task = n_task + 1

			# Now for the constrains

			n_cons = 0
			for cons in constraints:

				# We obtain the cavities

				Vfinv = 1.0 / np.diag(a['V_cons'][ cons ])[ i + n_pset ]
				VfOldinv = Vfinv - a['a_c_hfhat'][ i, j, n_cons ]
				VfOld_cons[ cons ] = 1.0 / VfOldinv
				m_nat = a['m_cons'][ cons ][ i + n_pset ] / np.diag(a['V_cons'][ cons ])[ i + n_pset ]
				mfOld_cons[ cons ] = VfOld_cons[ cons ] * (m_nat - a['b_c_hfhat'][ i, j, n_cons ])
				s_cons[ n_cons ] = VfOld_cons[ cons ]

				if s_cons[ n_cons ] < 0:
					raise npla.linalg.LinAlgError("Negative value in the sqrt!")

				alpha_cons[ n_cons ] = mfOld_cons[ cons ] / np.sqrt(VfOld_cons[ cons ])

				n_cons += 1

                        # Robust implementation

       			log_phi = logcdf_robust(alpha)
       			log_phi_cons = logcdf_robust(alpha_cons)
        		logZ_orig = log_1_minus_exp_x(np.sum(log_phi))

                        if logZ_orig  == -np.inf:
                            logZ_orig = logcdf_robust(-np.min(alpha))

			logZ_term1 = np.sum(log_phi_cons) + logZ_orig
			logZ_term2 = log_1_minus_exp_x(np.sum(log_phi_cons))

                        if logZ_term2 == -np.inf:
                            logZ_term2 = logcdf_robust(-np.min(alpha_cons))

                        max_value = np.maximum(logZ_term1, logZ_term2)

			logZ = np.log(np.exp(logZ_term1 - max_value) + np.exp(logZ_term2 - max_value)) + max_value

			n_task = 0
			for obj in all_tasks:

				ratio[ n_task ] = - np.exp(sps.norm.logpdf(alpha[ n_task ]) - logZ + np.sum(logcdf_robust(alpha)) \
					- logcdf_robust(alpha[ n_task ]) + np.sum(logcdf_robust(alpha_cons)))

				dlogZdmfOld = ratio[ n_task ] / np.sqrt(s[ n_task ]) * np.array([ 1.0, -1.0 ]) * sgn
                                dlogZdmfOld2 = - ratio[ n_task ] / s[ n_task ] * (alpha[ n_task ] + ratio[ n_task ]) \
                                            * np.array([[1.0,-1.0], [-1.0, 1.0]])

                                ahfHatNew = - np.dot(dlogZdmfOld2, spla.inv(np.dot(VfOld[ obj ], dlogZdmfOld2) + np.eye(2)))
                                bhfHatNew = np.dot(dlogZdmfOld - np.dot(mfOld[ obj ], dlogZdmfOld2), \
                                     spla.inv(np.dot(VfOld[ obj ], dlogZdmfOld2) + np.eye(2)))

				# We do the actual update with damping

				a['ahfhat'][ i, j , n_task, :, : ] = damping * ahfHatNew + (1 - damping) * a['ahfhat'][ i, j , n_task, :, : ]
				a['bhfhat'][ i, j , n_task, : ] = damping * bhfHatNew + (1 - damping) * a['bhfhat'][ i, j , n_task, : ]

				n_task = n_task + 1

			# Now for the constraints

			n_cons = 0
			for cons in constraints:

				ratio_cons[ n_cons ] = np.exp(sps.norm.logpdf(alpha_cons[ n_cons ]) - logZ + \
					logZ_orig + np.sum(logcdf_robust(alpha_cons)) - logcdf_robust(alpha_cons[ n_cons ])) - \
					np.exp(sps.norm.logpdf(alpha_cons[ n_cons ]) - logZ + np.sum(logcdf_robust(alpha_cons)) \
					- logcdf_robust(alpha_cons[ n_cons ]))

				dlogZdmfOld = ratio_cons[ n_cons ] / np.sqrt(s_cons[ n_cons ])
                                dlogZdmfOld2 = - ratio_cons[ n_cons ] / s_cons[ n_cons ] * (alpha_cons[ n_cons ] + ratio_cons[ n_cons ])

            		        achfhatNew = - dlogZdmfOld2 / (1.0 + dlogZdmfOld2 * VfOld_cons[ cons ])
                                bchfhatNew = (dlogZdmfOld - mfOld_cons[ cons ] * dlogZdmfOld2) / (1.0 + dlogZdmfOld2 * VfOld_cons[ cons ])

				a['a_c_hfhat'][ i, j , n_cons ] = damping * achfhatNew + (1 - damping) * a['a_c_hfhat'][ i, j , n_cons ]
				a['b_c_hfhat'][ i, j , n_cons ] = damping * bchfhatNew + (1 - damping) * a['b_c_hfhat'][ i, j , n_cons ]

				n_cons += 1

	# Second we update the factors corresponding to the pareto set

	for j1 in xrange(n_pset):
		for j2 in xrange(n_pset):

			if not j1 == j2:

				n_task = 0
				for obj in all_tasks:

					# We obtain the cavities

					Vfinv = matrixInverse(a['V'][ obj ][ np.ix_([ j1, j2 ], [ j1, j2 ]) ])
					VfOldinv = Vfinv - a['chfhat'][ j1, j2, n_task, :, : ]
					VfOld[ obj ] = matrixInverse(VfOldinv)
	       	 			mfOld[ obj ] = np.dot(VfOld[ obj ], np.dot(Vfinv, a['m'][ obj ][[ j1, j2 ]]) \
						- a['dhfhat'][ j1, j2, n_task, : ])

					# We compute the quantities required for the updates

					s[ n_task ]  = VfOld[ obj ][0, 0] +  VfOld[ obj ][1, 1] - 2.0 * VfOld[ obj ][1, 0]

					if s[ n_task ] < 0:
						raise npla.linalg.LinAlgError("Negative value in the sqrt!")

					# The first component of mfOld[ obj ] contains the point and the second the point from the pareto set

       		 			alpha[ n_task ] = (mfOld[ obj ][ 0 ] - mfOld[ obj ][ 1 ]) / np.sqrt(s[ n_task ]) * sgn
					n_task = n_task + 1

	       			log_phi = logcdf_robust(alpha)
       		 		logZ = log_1_minus_exp_x(np.sum(log_phi))

                                if logZ == -np.inf:
                                    logZ = logcdf_robust(-np.min(alpha))

				n_task = 0
				for obj in all_tasks:

					ratio[ n_task ] = - np.exp(sps.norm.logpdf(alpha[ n_task ]) - logZ + np.sum(logcdf_robust(alpha)) \
						- logcdf_robust(alpha[ n_task ]))

					dlogZdmfOld = ratio[ n_task ] / np.sqrt(s[ n_task ]) * np.array([ 1.0, -1.0 ]) * sgn
                                        dlogZdmfOld2 = - ratio[ n_task ] / s[ n_task ] * (alpha[ n_task ] + ratio[ n_task ]) \
                                            * np.array([[1.0,-1.0], [-1.0, 1.0]])

                                        chfHatNew = - np.dot(dlogZdmfOld2, spla.inv(np.dot(VfOld[ obj ], dlogZdmfOld2) + np.eye(2)))
                                        dhfHatNew = np.dot(dlogZdmfOld - np.dot(mfOld[ obj ], dlogZdmfOld2), \
                                            spla.inv(np.dot(VfOld[ obj ], dlogZdmfOld2) + np.eye(2)))

					# We do the actual update with damping

					a['chfhat'][ j1, j2, n_task, :, : ] = damping * chfHatNew + \
						(1 - damping) * a['chfhat'][ j1, j2, n_task, :, : ]
					a['dhfhat'][ j1, j2, n_task, : ] = damping * dhfHatNew + \
						(1 - damping) * a['dhfhat'][ j1, j2 , n_task, : ]


					n_task = n_task + 1

	return a


# Based on the original code, with a few modifications

def updateFactors_daniel_no_constraints_pareto_set(a, damping, minimize=True):

	# used to switch between minimizing and maximizing

	sgn = -1.0 if minimize else 1.0

	# We update the h factors

	all_tasks = a['objs']
	constraints = a['cons']

	n_obs = a['n_obs']
	n_pset = a['n_pset']
	n_total = a['n_total']

	# First we update the external (easy) factors that only affect the constraints

	n_cons = 0
	for cons in constraints:

		# We obtain the cavities

		Vfinv = 1.0 / np.diag(a['V_cons'][ cons ])[ 0 : n_pset ]
		VfOldinv = Vfinv - a['ehfhat'][ :, n_cons ]
		VfOld = 1.0 / VfOldinv
		m_nat = a['m_cons'][ cons ][ 0 : n_pset ] / np.diag(a['V_cons'][ cons ])[ 0 : n_pset ]
		mfOld = VfOld * (m_nat - a['fhfhat'][ :, n_cons ])

		if np.any(VfOld < 0):
			raise npla.linalg.LinAlgError("Negative value in the sqrt!")

		# We compute the quantities required for the update

		alpha = mfOld / np.sqrt(VfOld)
		logZ = logcdf_robust(alpha)

		ratio = np.exp(sps.norm.logpdf(alpha) - logZ)
		dlogZdmfOld = ratio / np.sqrt(VfOld)
		dlogZdVfOld = -0.5 * ratio * alpha * 1.0 / VfOld

		mNew = mfOld + VfOld * dlogZdmfOld
		VfNew = VfOld - VfOld * (dlogZdmfOld**2 - 2.0 * dlogZdVfOld) * VfOld

		# We find the parameters of the updated factors

		ehfHatNew = 1.0 / VfNew - 1.0 / VfOld
		fhfHatNew = mNew / VfNew - mfOld / VfOld

		# We do the actual update with damping

		a['ehfhat'][ :, n_cons ] = damping * ehfHatNew + (1 - damping) * a['ehfhat'][ :, n_cons ]
		a['fhfhat'][ :, n_cons ] = damping * fhfHatNew + (1 - damping) * a['fhfhat'][ :, n_cons ]

		n_cons +=1

	alpha = np.zeros(a['q'])
	alpha_cons = np.zeros(a['c'])
	ratio = np.zeros(a['q'])
	ratio_cons = np.zeros(a['c'])
	s = np.zeros(a['q'])
	s_cons  = np.zeros(a['c'])
	mfOld = dict()
	VfOld = dict()
	mfOld_cons = dict()
	VfOld_cons = dict()

	# Next we update the complicated factors

	# First we update the factors corresponding to the observed data

	for i in xrange(n_obs):
		for j in xrange(n_pset):

			n_task = 0
			for obj in all_tasks:

				# We obtain the cavities

				Vfinv = matrixInverse(a['V'][ obj ][ np.ix_([ i + n_pset, j ], [ i + n_pset, j ]) ])
				VfOldinv = Vfinv - a['ahfhat'][ i, j, n_task, :, : ]
				VfOld[ obj ] = matrixInverse(VfOldinv)
        			mfOld[ obj ] = np.dot(VfOld[ obj ], np.dot(Vfinv, a['m'][ obj ][[ i + n_pset, j ]]) \
					- a['bhfhat'][ i, j, n_task,: ])

				# We compute the quantities required for the updates

				s[ n_task ]  = VfOld[ obj ][0, 0] + VfOld[ obj ][1, 1] - 2.0 * VfOld[ obj ][1, 0]

				if s[ n_task ] < 0:
					raise npla.linalg.LinAlgError("Negative value in the sqrt!")

				# The first component of mfOld[ obj ] contains the point and the second the point from the pareto set

        			alpha[ n_task ] = (mfOld[ obj ][ 0 ] - mfOld[ obj ][ 1 ]) / np.sqrt(s[ n_task ]) * sgn
				n_task = n_task + 1

			# Now for the constrains

			n_cons = 0
			for cons in constraints:

				# We obtain the cavities

				Vfinv = 1.0 / np.diag(a['V_cons'][ cons ])[ i + n_pset ]
				VfOldinv = Vfinv - a['a_c_hfhat'][ i, j, n_cons ]
				VfOld_cons[ cons ] = 1.0 / VfOldinv
				m_nat = a['m_cons'][ cons ][ i + n_pset ] / np.diag(a['V_cons'][ cons ])[ i + n_pset ]
				mfOld_cons[ cons ] = VfOld_cons[ cons ] * (m_nat - a['b_c_hfhat'][ i, j, n_cons ])
				s_cons[ n_cons ] = VfOld_cons[ cons ]

				if s_cons[ n_cons ] < 0:
					raise npla.linalg.LinAlgError("Negative value in the sqrt!")

				alpha_cons[ n_cons ] = mfOld_cons[ cons ] / np.sqrt(VfOld_cons[ cons ])

				n_cons += 1

                        # Robust implementation

       			log_phi = logcdf_robust(alpha)
       			log_phi_cons = logcdf_robust(alpha_cons)
        		logZ_orig = log_1_minus_exp_x(np.sum(log_phi))

                        if logZ_orig  == -np.inf:
                            logZ_orig = logcdf_robust(-np.min(alpha))

			logZ_term1 = np.sum(log_phi_cons) + logZ_orig
			logZ_term2 = log_1_minus_exp_x(np.sum(log_phi_cons))

                        if logZ_term2 == -np.inf:
                            logZ_term2 = logcdf_robust(-np.min(alpha_cons))

                        max_value = np.maximum(logZ_term1, logZ_term2)

			logZ = np.log(np.exp(logZ_term1 - max_value) + np.exp(logZ_term2 - max_value)) + max_value

			n_task = 0
			for obj in all_tasks:

				ratio[ n_task ] = - np.exp(sps.norm.logpdf(alpha[ n_task ]) - logZ + np.sum(logcdf_robust(alpha)) \
					- logcdf_robust(alpha[ n_task ]) + np.sum(logcdf_robust(alpha_cons)))

				dlogZdmfOld = ratio[ n_task ] / np.sqrt(s[ n_task ]) * np.array([ 1.0, -1.0 ]) * sgn
				dlogZdVfOld = -0.5 * ratio[ n_task ] * alpha[ n_task ] / s[ n_task ] * np.array([[1.0,-1.0], [-1.0,1.0]])

        			mfNew = mfOld[ obj ] + np.dot(VfOld[ obj ], dlogZdmfOld)
				VfNew = VfOld[ obj ] - np.dot(np.dot(VfOld[ obj ], np.outer(dlogZdmfOld, dlogZdmfOld) - \
					2.0 * dlogZdVfOld), VfOld[ obj ])

				# We compute the approximate factors

        			ahfHatNew = matrixInverse(VfNew) - matrixInverse(VfOld[ obj ])
        			bhfHatNew = np.dot(matrixInverse(VfNew), mfNew) - np.dot(matrixInverse(VfOld[ obj ]), mfOld[ obj ])

				# We do the actual update with damping

				a['ahfhat'][ i, j , n_task, :, : ] = damping * ahfHatNew + (1 - damping) * a['ahfhat'][ i, j , n_task, :, : ]
				a['bhfhat'][ i, j , n_task, : ] = damping * bhfHatNew + (1 - damping) * a['bhfhat'][ i, j , n_task, : ]

				n_task = n_task + 1

			# Now for the constraints

			n_cons = 0
			for cons in constraints:

				ratio_cons[ n_cons ] = np.exp(sps.norm.logpdf(alpha_cons[ n_cons ]) - logZ + \
					logZ_orig + np.sum(logcdf_robust(alpha_cons)) - logcdf_robust(alpha_cons[ n_cons ])) - \
					np.exp(sps.norm.logpdf(alpha_cons[ n_cons ]) - logZ + np.sum(logcdf_robust(alpha_cons)) \
					- logcdf_robust(alpha_cons[ n_cons ]))

				dlogZdmfOld = ratio_cons[ n_cons ] / np.sqrt(s_cons[ n_cons ])
				dlogZdVfOld = -0.5 * ratio_cons[ n_cons ] * alpha_cons[ n_cons ] / s_cons[ n_cons ]

				mfNew = mfOld_cons[ cons ] + VfOld_cons[ cons ] * dlogZdmfOld
				VfNew = VfOld_cons[ cons ] - VfOld_cons[ cons ] * (dlogZdmfOld**2 - 2.0 * dlogZdVfOld) * VfOld_cons[ cons ]

				achfhatNew = 1.0 / VfNew - 1.0 / VfOld_cons[ cons ]
				bchfhatNew = mfNew / VfNew - mfOld_cons[ cons ] / VfOld_cons[ cons ]

				a['a_c_hfhat'][ i, j , n_cons ] = damping * achfhatNew + (1 - damping) * a['a_c_hfhat'][ i, j , n_cons ]
				a['b_c_hfhat'][ i, j , n_cons ] = damping * bchfhatNew + (1 - damping) * a['b_c_hfhat'][ i, j , n_cons ]

				n_cons += 1

	# Second we update the factors corresponding to the pareto set

	for j1 in xrange(n_pset):
		for j2 in xrange(n_pset):

			if not j1 == j2:

				n_task = 0
				for obj in all_tasks:

					# We obtain the cavities

					Vfinv = matrixInverse(a['V'][ obj ][ np.ix_([ j1, j2 ], [ j1, j2 ]) ])
					VfOldinv = Vfinv - a['chfhat'][ j1, j2, n_task, :, : ]
					VfOld[ obj ] = matrixInverse(VfOldinv)
	       	 			mfOld[ obj ] = np.dot(VfOld[ obj ], np.dot(Vfinv, a['m'][ obj ][[ j1, j2 ]]) \
						- a['dhfhat'][ j1, j2, n_task, : ])

					# We compute the quantities required for the updates

					s[ n_task ]  = VfOld[ obj ][0, 0] +  VfOld[ obj ][1, 1] - 2.0 * VfOld[ obj ][1, 0]

					if s[ n_task ] < 0:
						raise npla.linalg.LinAlgError("Negative value in the sqrt!")

					# The first component of mfOld[ obj ] contains the point and the second the point from the pareto set

       		 			alpha[ n_task ] = (mfOld[ obj ][ 0 ] - mfOld[ obj ][ 1 ]) / np.sqrt(s[ n_task ]) * sgn
					n_task = n_task + 1

	       			log_phi = logcdf_robust(alpha)
       		 		logZ = log_1_minus_exp_x(np.sum(log_phi))

                                if logZ == -np.inf:
                                    logZ = logcdf_robust(-np.min(alpha))

				n_task = 0
				for obj in all_tasks:

					ratio[ n_task ] = - np.exp(sps.norm.logpdf(alpha[ n_task ]) - logZ + np.sum(logcdf_robust(alpha)) \
						- logcdf_robust(alpha[ n_task ]))
					dlogZdmfOld = ratio[ n_task ] / np.sqrt(s[ n_task ]) * np.array([ 1.0, -1.0 ]) * sgn
					dlogZdVfOld = -0.5 * ratio[ n_task ] * alpha[ n_task ] / s[ n_task ] * np.array([[1.0,-1.0], [-1.0,1.0]])

        	       	 		mfNew = mfOld[ obj ] + np.dot(VfOld[ obj ], dlogZdmfOld)
					VfNew = VfOld[ obj ] - np.dot(np.dot(VfOld[ obj ], np.outer(dlogZdmfOld, dlogZdmfOld) - \
						2.0 * dlogZdVfOld), VfOld[ obj ])

					# We compute the approximate factors

	        			chfHatNew = matrixInverse(VfNew) - matrixInverse(VfOld[ obj ])
           		 		dhfHatNew = np.dot(matrixInverse(VfNew), mfNew) - np.dot(matrixInverse(VfOld[ obj ]), mfOld[ obj ])

					# We do the actual update with damping

					a['chfhat'][ j1, j2, n_task, :, : ] = damping * chfHatNew + \
						(1 - damping) * a['chfhat'][ j1, j2, n_task, :, : ]
					a['dhfhat'][ j1, j2, n_task, : ] = damping * dhfHatNew + \
						(1 - damping) * a['dhfhat'][ j1, j2 , n_task, : ]

					n_task = n_task + 1

	#if np.any(np.isnan())
#        print "Update factors Daniel"
#        print "====================="
#        print "Factors Report"
#        print "=============="
#        print 'ahfhat'
#        print a['ahfhat'][ :, :, :, 0, 0 ]
#        print a['ahfhat'][ :, :, :, 0, 1 ]
#        print a['ahfhat'][ :, :, :, 1, 1 ]
#        print 'bhfhat'
#        print a['bhfhat'][ :, :, :, 0 ]
#        print a['bhfhat'][ :, :, :, 1 ]
#        print 'chfhat'
#        print a['chfhat'][ :, :, :, 0, 0 ]
#        print a['chfhat'][ :, :, :, 1, 1 ]
#        print a['chfhat'][ :, :, :, 0, 1 ]
#        print 'dhfhat'
#        print a['dhfhat'][ :, :, :, 0 ]
#        print a['dhfhat'][ :, :, :, 1 ]
#        print 'a_c_hfhat'
#        print a['a_c_hfhat'][ :, :, : ]
#        print 'b_c_hfhat'
#        print a['b_c_hfhat'][ :, :, : ]
#        print 'c_c_hfhat'
#        print a['c_c_hfhat'][ :, :, : ]
#        print 'd_c_hfhat'
#        print a['d_c_hfhat'][ :, :, : ]
#        print 'ehfhat'
#        print a['ehfhat'][ :, : ]
#        print 'fhfhat'
#        print a['fhfhat'][ :, : ]

	return a

# Based on the original code, with a few modifications

def updateFactors_daniel(a, damping, minimize=True):

	# used to switch between minimizing and maximizing

	sgn = -1.0 if minimize else 1.0

	# We update the h factors

	all_tasks = a['objs']
	constraints = a['cons']

	n_obs = a['n_obs']
	n_pset = a['n_pset']
	n_total = a['n_total']

	# First we update the external (easy) factors that only affect the constraints

	n_cons = 0
	for cons in constraints:

		# We obtain the cavities

		Vfinv = 1.0 / np.diag(a['V_cons'][ cons ])[ 0 : n_pset ]
		VfOldinv = Vfinv - a['ehfhat'][ :, n_cons ]
		VfOld = 1.0 / VfOldinv
		m_nat = a['m_cons'][ cons ][ 0 : n_pset ] / np.diag(a['V_cons'][ cons ])[ 0 : n_pset ]
		mfOld = VfOld * (m_nat - a['fhfhat'][ :, n_cons ])

		if np.any(VfOld < 0):
			raise npla.linalg.LinAlgError("Negative value in the sqrt!")

		# We compute the quantities required for the update
		alpha = mfOld / np.sqrt(VfOld)
		logZ = logcdf_robust(alpha)

		ratio = np.exp(sps.norm.logpdf(alpha) - logZ)
		dlogZdmfOld = ratio / np.sqrt(VfOld)
		dlogZdVfOld = -0.5 * ratio * alpha * 1.0 / VfOld

		mNew = mfOld + VfOld * dlogZdmfOld
		VfNew = VfOld - VfOld * (dlogZdmfOld**2 - 2.0 * dlogZdVfOld) * VfOld

		# We find the parameters of the updated factors

		ehfHatNew = 1.0 / VfNew - 1.0 / VfOld
		fhfHatNew = mNew / VfNew - mfOld / VfOld

		# We do the actual update with damping

		a['ehfhat'][ :, n_cons ] = damping * ehfHatNew + (1 - damping) * a['ehfhat'][ :, n_cons ]
		a['fhfhat'][ :, n_cons ] = damping * fhfHatNew + (1 - damping) * a['fhfhat'][ :, n_cons ]

		n_cons +=1

	alpha = np.zeros(a['q'])
	alpha_cons = np.zeros(a['c'])
	ratio = np.zeros(a['q'])
	ratio_cons = np.zeros(a['c'])
	s = np.zeros(a['q'])
	s_cons  = np.zeros(a['c'])
	mfOld = dict()
	VfOld = dict()
	mfOld_cons = dict()
	VfOld_cons = dict()

	# Next we update the complicated factors

	# First we update the factors corresponding to the observed data

	for i in xrange(n_obs):
		for j in xrange(n_pset):

			n_task = 0
			for obj in all_tasks:

				# We obtain the cavities

				Vfinv = matrixInverse(a['V'][ obj ][ np.ix_([ i + n_pset, j ], [ i + n_pset, j ]) ])
				VfOldinv = Vfinv - a['ahfhat'][ i, j, n_task, :, : ]
				VfOld[ obj ] = matrixInverse(VfOldinv)
        			mfOld[ obj ] = np.dot(VfOld[ obj ], np.dot(Vfinv, a['m'][ obj ][[ i + n_pset, j ]]) \
					- a['bhfhat'][ i, j, n_task,: ])

				# We compute the quantities required for the updates

				s[ n_task ]  = VfOld[ obj ][0, 0] + VfOld[ obj ][1, 1] - 2.0 * VfOld[ obj ][1, 0]

				if s[ n_task ] < 0:
					raise npla.linalg.LinAlgError("Negative value in the sqrt!")

				# The first component of mfOld[ obj ] contains the point and the second the point from the pareto set

        			alpha[ n_task ] = (mfOld[ obj ][ 0 ] - mfOld[ obj ][ 1 ]) / np.sqrt(s[ n_task ]) * sgn
				n_task = n_task + 1

			# Now for the constrains

			n_cons = 0
			for cons in constraints:

				# We obtain the cavities

				Vfinv = 1.0 / np.diag(a['V_cons'][ cons ])[ i + n_pset ]
				VfOldinv = Vfinv - a['a_c_hfhat'][ i, j, n_cons ]
				VfOld_cons[ cons ] = 1.0 / VfOldinv
				m_nat = a['m_cons'][ cons ][ i + n_pset ] / np.diag(a['V_cons'][ cons ])[ i + n_pset ]
				mfOld_cons[ cons ] = VfOld_cons[ cons ] * (m_nat - a['b_c_hfhat'][ i, j, n_cons ])
				s_cons[ n_cons ] = VfOld_cons[ cons ]

				if s_cons[ n_cons ] < 0:
					raise npla.linalg.LinAlgError("Negative value in the sqrt!")

				alpha_cons[ n_cons ] = mfOld_cons[ cons ] / np.sqrt(VfOld_cons[ cons ])

				n_cons += 1

       			log_phi = logcdf_robust(alpha)
       			log_phi_cons = logcdf_robust(alpha_cons)
        		logZ_orig = log_1_minus_exp_x(np.sum(log_phi))
			logZ_term1 = np.sum(log_phi_cons) + logZ_orig
			logZ_term2 = log_1_minus_exp_x(np.sum(log_phi_cons))
			logZ = np.log(np.exp(logZ_term1) + np.exp(logZ_term2))		# TODO: This should be done robustly

			n_task = 0
			for obj in all_tasks:

				ratio[ n_task ] = - np.exp(sps.norm.logpdf(alpha[ n_task ]) - logZ + np.sum(logcdf_robust(alpha)) \
					- logcdf_robust(alpha[ n_task ]) + np.sum(logcdf_robust(alpha_cons)))

				dlogZdmfOld = ratio[ n_task ] / np.sqrt(s[ n_task ]) * np.array([ 1.0, -1.0 ]) * sgn
				dlogZdVfOld = -0.5 * ratio[ n_task ] * alpha[ n_task ] / s[ n_task ] * np.array([[1.0,-1.0], [-1.0,1.0]])

        			mfNew = mfOld[ obj ] + np.dot(VfOld[ obj ], dlogZdmfOld)
				VfNew = VfOld[ obj ] - np.dot(np.dot(VfOld[ obj ], np.outer(dlogZdmfOld, dlogZdmfOld) - \
					2.0 * dlogZdVfOld), VfOld[ obj ])

				# We compute the approximate factors

        			ahfHatNew = matrixInverse(VfNew) - matrixInverse(VfOld[ obj ])
        			bhfHatNew = np.dot(matrixInverse(VfNew), mfNew) - np.dot(matrixInverse(VfOld[ obj ]), mfOld[ obj ])

				# We do the actual update with damping

				a['ahfhat'][ i, j , n_task, :, : ] = damping * ahfHatNew + (1 - damping) * a['ahfhat'][ i, j , n_task, :, : ]
				a['bhfhat'][ i, j , n_task, : ] = damping * bhfHatNew + (1 - damping) * a['bhfhat'][ i, j , n_task, : ]

				n_task = n_task + 1

			# Now for the constraints

			n_cons = 0
			for cons in constraints:

				ratio_cons[ n_cons ] = np.exp(sps.norm.logpdf(alpha_cons[ n_cons ]) - logZ + \
					logZ_orig + np.sum(logcdf_robust(alpha_cons)) - logcdf_robust(alpha_cons[ n_cons ])) - \
					np.exp(sps.norm.logpdf(alpha_cons[ n_cons ]) - logZ + np.sum(logcdf_robust(alpha_cons)) \
					- logcdf_robust(alpha_cons[ n_cons ]))

				dlogZdmfOld = ratio_cons[ n_cons ] / np.sqrt(s_cons[ n_cons ])
				dlogZdVfOld = -0.5 * ratio_cons[ n_cons ] * alpha_cons[ n_cons ] / s_cons[ n_cons ]

				mfNew = mfOld_cons[ cons ] + VfOld_cons[ cons ] * dlogZdmfOld
				VfNew = VfOld_cons[ cons ] - VfOld_cons[ cons ] * (dlogZdmfOld**2 - 2.0 * dlogZdVfOld) * VfOld_cons[ cons ]

				achfhatNew = 1.0 / VfNew - 1.0 / VfOld_cons[ cons ]
				bchfhatNew = mfNew / VfNew - mfOld_cons[ cons ] / VfOld_cons[ cons ]

				a['a_c_hfhat'][ i, j , n_cons ] = damping * achfhatNew + (1 - damping) * a['a_c_hfhat'][ i, j , n_cons ]
				a['b_c_hfhat'][ i, j , n_cons ] = damping * bchfhatNew + (1 - damping) * a['b_c_hfhat'][ i, j , n_cons ]

				n_cons += 1

	# Second we update the factors corresponding to the pareto set

	for j1 in xrange(n_pset):
		for j2 in xrange(n_pset):

			if not j1 == j2:

				n_task = 0
				for obj in all_tasks:

					# We obtain the cavities

					Vfinv = matrixInverse(a['V'][ obj ][ np.ix_([ j1, j2 ], [ j1, j2 ]) ])
					VfOldinv = Vfinv - a['chfhat'][ j1, j2, n_task, :, : ]
					VfOld[ obj ] = matrixInverse(VfOldinv)
	       	 			mfOld[ obj ] = np.dot(VfOld[ obj ], np.dot(Vfinv, a['m'][ obj ][[ j1, j2 ]]) \
						- a['dhfhat'][ j1, j2, n_task, : ])

					# We compute the quantities required for the updates

					s[ n_task ]  = VfOld[ obj ][0, 0] +  VfOld[ obj ][1, 1] - 2.0 * VfOld[ obj ][1, 0]

					if s[ n_task ] < 0:
						raise npla.linalg.LinAlgError("Negative value in the sqrt!")

					# The first component of mfOld[ obj ] contains the point and the second the point from the pareto set

       		 			alpha[ n_task ] = (mfOld[ obj ][ 0 ] - mfOld[ obj ][ 1 ]) / np.sqrt(s[ n_task ]) * sgn
					n_task = n_task + 1

				# Now for the constrains

				n_cons = 0
				for cons in constraints:

					# We obtain the cavities

					Vfinv = 1.0 / np.diag(a['V_cons'][ cons ])[ j1 ]
					VfOldinv = Vfinv - a['c_c_hfhat'][ j1, j2, n_cons ]
					VfOld_cons[ cons ] = 1.0 / VfOldinv
					m_nat = a['m_cons'][ cons ][ j1 ] / np.diag(a['V_cons'][ cons ])[ j1 ]
					mfOld_cons[ cons ] = VfOld_cons[ cons ] * (m_nat - a['d_c_hfhat'][ j1, j2, n_cons ])
					s_cons[ n_cons ] = VfOld_cons[ cons ]

#					if a['chfhat'][ 0, 1, 0, 0, 0 ] != 0.0 and j1 == 0 and j2 == 1 and n_cons == 0:
#						VfOld_cons[ cons ] += 1e-4

					if s_cons[ n_cons ] < 0:
						raise npla.linalg.LinAlgError("Negative value in the sqrt!")

					alpha_cons[ n_cons ] = mfOld_cons[ cons ] / np.sqrt(VfOld_cons[ cons ])

					n_cons += 1

	       			log_phi = logcdf_robust(alpha)
	       			log_phi_cons = logcdf_robust(alpha_cons)
       		 		logZ_orig = log_1_minus_exp_x(np.sum(log_phi))
				logZ_term1 = np.sum(log_phi_cons) + logZ_orig
				logZ_term2 = log_1_minus_exp_x(np.sum(log_phi_cons))
				logZ = np.log(np.exp(logZ_term1) + np.exp(logZ_term2))		# TODO: This should be done robustly

				n_task = 0
				for obj in all_tasks:

					ratio[ n_task ] = - np.exp(sps.norm.logpdf(alpha[ n_task ]) - logZ + np.sum(logcdf_robust(alpha)) \
						- logcdf_robust(alpha[ n_task ]) + np.sum(logcdf_robust(alpha_cons)))
					dlogZdmfOld = ratio[ n_task ] / np.sqrt(s[ n_task ]) * np.array([ 1.0, -1.0 ]) * sgn
					dlogZdVfOld = -0.5 * ratio[ n_task ] * alpha[ n_task ] / s[ n_task ] * np.array([[1.0,-1.0], [-1.0,1.0]])

        	       	 		mfNew = mfOld[ obj ] + np.dot(VfOld[ obj ], dlogZdmfOld)
					VfNew = VfOld[ obj ] - np.dot(np.dot(VfOld[ obj ], np.outer(dlogZdmfOld, dlogZdmfOld) - \
						2.0 * dlogZdVfOld), VfOld[ obj ])

					# We compute the approximate factors

	        			chfHatNew = matrixInverse(VfNew) - matrixInverse(VfOld[ obj ])
           		 		dhfHatNew = np.dot(matrixInverse(VfNew), mfNew) - np.dot(matrixInverse(VfOld[ obj ]), mfOld[ obj ])

					# We do the actual update with damping

					a['chfhat'][ j1, j2, n_task, :, : ] = damping * chfHatNew + \
						(1 - damping) * a['chfhat'][ j1, j2, n_task, :, : ]
					a['dhfhat'][ j1, j2, n_task, : ] = damping * dhfHatNew + \
						(1 - damping) * a['dhfhat'][ j1, j2 , n_task, : ]

					n_task = n_task + 1

				# Now for the constrains

				n_cons = 0
				for cons in constraints:

					ratio_cons[ n_cons ] = np.exp(sps.norm.logpdf(alpha_cons[ n_cons ]) - logZ + \
						logZ_orig + np.sum(logcdf_robust(alpha_cons)) - logcdf_robust(alpha_cons[ n_cons ])) - \
						np.exp(sps.norm.logpdf(alpha_cons[ n_cons ]) - logZ + np.sum(logcdf_robust(alpha_cons)) \
						- logcdf_robust(alpha_cons[ n_cons ]))

					dlogZdmfOld = ratio_cons[ n_cons ] / np.sqrt(s_cons[ n_cons ])
					dlogZdVfOld = -0.5 * ratio_cons[ n_cons ] * alpha_cons[ n_cons ] / s_cons[ n_cons ]

					mfNew = mfOld_cons[ cons ] + VfOld_cons[ cons ] * dlogZdmfOld
					VfNew = VfOld_cons[ cons ] - VfOld_cons[ cons ] * (dlogZdmfOld**2 - 2.0 * dlogZdVfOld) * VfOld_cons[ cons ]

					cchfhatNew = 1.0 / VfNew - 1.0 / VfOld_cons[ cons ]
					dchfhatNew = mfNew / VfNew - mfOld_cons[ cons ] / VfOld_cons[ cons ]

					a['c_c_hfhat'][ j1, j2, n_cons ] = damping * cchfhatNew + (1 - damping) * a['c_c_hfhat'][ j1, j2, n_cons ]
					a['d_c_hfhat'][ j1, j2, n_cons ] = damping * dchfhatNew + (1 - damping) * a['d_c_hfhat'][ j1, j2, n_cons ]

					n_cons += 1

	#if np.any(np.isnan())
#        print "Update factors Daniel"
#        print "====================="
#        print "Factors Report"
#        print "=============="
#        print 'ahfhat'
#        print a['ahfhat'][ :, :, :, 0, 0 ]
#        print a['ahfhat'][ :, :, :, 0, 1 ]
#        print a['ahfhat'][ :, :, :, 1, 1 ]
#        print 'bhfhat'
#        print a['bhfhat'][ :, :, :, 0 ]
#        print a['bhfhat'][ :, :, :, 1 ]
#        print 'chfhat'
#        print a['chfhat'][ :, :, :, 0, 0 ]
#        print a['chfhat'][ :, :, :, 1, 1 ]
#        print a['chfhat'][ :, :, :, 0, 1 ]
#        print 'dhfhat'
#        print a['dhfhat'][ :, :, :, 0 ]
#        print a['dhfhat'][ :, :, :, 1 ]
#        print 'a_c_hfhat'
#        print a['a_c_hfhat'][ :, :, : ]
#        print 'b_c_hfhat'
#        print a['b_c_hfhat'][ :, :, : ]
#        print 'c_c_hfhat'
#        print a['c_c_hfhat'][ :, :, : ]
#        print 'd_c_hfhat'
#        print a['d_c_hfhat'][ :, :, : ]
#        print 'ehfhat'
#        print a['ehfhat'][ :, : ]
#        print 'fhfhat'
#        print a['fhfhat'][ :, : ]

	return a

def updateFactors_fast_daniel_robust(a, damping, minimize=True, no_negative_variances_nor_nands = False):
    # used to switch between minimizing and maximizing
    sgn = -1.0 if minimize else 1.0

    # We update the h factors
    all_tasks = a['objs']
    all_constraints = a['cons']
    n_obs = a['n_obs']
    n_pset = a['n_pset']
    n_total = a['n_total']
    q = a['q']
    c = a['c']

    alpha = np.zeros(a['q'])
    s = np.zeros(a['q'])
    ratio_cons = np.zeros(c)

    # First we update the factors corresponding to the observed data

    # We compute an "old" distribution

    # Data structures for objective npset nobs cavities (a, b).

    m_pset = np.zeros((q, n_pset, n_obs))
    m_obs = np.zeros((q, n_pset, n_obs))
    v_pset = np.zeros((q, n_pset, n_obs))
    v_obs = np.zeros((q, n_pset, n_obs))
    v_cov = np.zeros((q, n_pset, n_obs))

    # Data structures for constraint npset nobs cavities (c_a, c_b).

    c_m = np.zeros((c, n_pset, n_obs))
    c_v = np.zeros((c, n_pset, n_obs))

    # We do the update of the external factors.

    c_m_external = np.zeros((c, n_pset))
    c_v_external = np.zeros((c, n_pset))
    alpha_external = np.zeros(c)

    # First we update the external (easy) factors that only affect the constraints

    n_task = 0
    for cons in all_constraints:
        c_m_external[ n_task, : ] = a['m_cons'][ cons ][ 0 : n_pset ]
        c_v_external[ n_task, : ] = np.diag(a['V_cons'][ cons ])[ 0 : n_pset ]
        n_task += 1

    c_vTilde_external = a['ehfhat'][ :, : ].T
    c_mTilde_external = a['fhfhat'][ :, : ].T

    c_vOld_external = 1.0 / (1.0 / c_v_external - c_vTilde_external)
    c_mOld_external = c_vOld_external * (c_m_external / c_v_external - c_mTilde_external)

    if np.any(c_vOld_external < 0):
        raise npla.linalg.LinAlgError("Negative value in the sqrt!")

    alpha_external = c_mOld_external / np.sqrt(c_vOld_external)
    logZ = logcdf_robust(alpha_external)

    ratio = np.exp(sps.norm.logpdf(alpha_external) - logZ)
    dlogZdmfOld_external = ratio / np.sqrt(c_vOld_external)
    dlogZdmfOld2_external = - ratio * (alpha_external + ratio) / c_vOld_external

     # We find the parameters of the updated factors

    ehfhat_act = (- dlogZdmfOld2_external / (1.0 + dlogZdmfOld2_external * c_vOld_external)).T
    fhfhat_act = ((dlogZdmfOld_external - c_mOld_external * dlogZdmfOld2_external) / (1.0 + dlogZdmfOld2_external * c_vOld_external)).T

    if no_negative_variances_nor_nands == True:
        neg = np.where(ehfhat_act < 0)

        ehfhat_act[ neg ] = 0.0
        fhfhat_act[ neg ] = 0.0

    a['ehfhat'][ :, : ] = ehfhat_act * damping + (1 - damping) * a['ehfhat'][ :, : ]
    a['fhfhat'][ :, : ] = fhfhat_act * damping + (1 - damping) * a['fhfhat'][ :, : ]

    # Done!

    n_task = 0
    for obj in all_tasks:
        m_obs[ n_task, :, : ] = np.tile(a['m'][ obj ][ n_pset : n_total ], n_pset).reshape((n_pset, n_obs))
        m_pset[ n_task, :, : ] = np.tile(a['m'][ obj ][ 0 : n_pset ], n_obs).reshape((n_obs, n_pset)).T
        v_cov[ n_task, :, : ] = a['V'][ obj ][ 0 : n_pset, n_pset : n_total ]
        v_obs[ n_task, :, : ] = np.tile(np.diag(a['V'][ obj ])[ n_pset : n_total ], n_pset).reshape((n_pset, n_obs))
        v_pset[ n_task, :, : ] = np.tile(np.diag(a['V'][ obj ])[ 0 : n_pset ], n_obs).reshape((n_obs, n_pset)).T
        n_task += 1

    n_task = 0

    for cons in all_constraints:
        c_m[ n_task, :, : ] = a['m_cons'][ cons ][ n_pset : n_total ]
        c_v[ n_task, :, : ] = np.diag(a['V_cons'][ cons ])[ n_pset : n_total ]
        n_task += 1

    vTilde_obs = a['ahfhat'][ :, :, :, 0, 0 ].T
    vTilde_pset = a['ahfhat'][ :, :, :, 1, 1 ].T
    covTilde = a['ahfhat'][ :, :, :, 0, 1 ].T
    mTilde_obs = a['bhfhat'][ :, :, :, 0, ].T
    mTilde_pset = a['bhfhat'][ :, :, :, 1, ].T

    c_vTilde = a['a_c_hfhat'][ :, :, : ].T
    c_mTilde = a['b_c_hfhat'][ :, :, : ].T

    # Obtaining cavities.

    inv_v_obs, inv_v_pset, inv_v_cov = two_by_two_symmetric_matrix_inverse(v_obs, v_pset, v_cov)
    inv_c_v = 1.0 / c_v

    inv_vOld_obs = inv_v_obs - vTilde_obs
    inv_vOld_pset = inv_v_pset - vTilde_pset
    inv_vOld_cov =  inv_v_cov - covTilde
    inv_c_vOld = inv_c_v - c_vTilde

    vOld_obs, vOld_pset, vOld_cov = two_by_two_symmetric_matrix_inverse(inv_vOld_obs, inv_vOld_pset, inv_vOld_cov)
    c_vOld = 1.0 / inv_c_vOld

    mOld_obs, mOld_pset  = two_by_two_symmetric_matrix_product_vector(inv_v_obs, inv_v_pset, inv_v_cov, m_obs, m_pset)
    mOld_obs = mOld_obs - mTilde_obs
    mOld_pset = mOld_pset - mTilde_pset
    mOld_obs, mOld_pset  = two_by_two_symmetric_matrix_product_vector(vOld_obs, vOld_pset, vOld_cov, mOld_obs, mOld_pset)

    c_mOld = c_vOld * (c_m / c_v - c_mTilde)

    #Computing factors.

    s = vOld_pset + vOld_obs - 2 * vOld_cov
    s_cons = c_vOld

    if np.any(vOld_pset < 0):
        raise npla.linalg.LinAlgError("Negative variance in the sqrt!")

    if np.any(vOld_obs < 0):
        raise npla.linalg.LinAlgError("Negative variance in the sqrt!")

    if np.any(c_vOld < 0):
        raise npla.linalg.LinAlgError("Negative value in the sqrt!")

    alpha_cons = c_mOld / np.sqrt(c_vOld)

    scale = 1.0 - 1e-4
    while np.any(s / (vOld_pset + vOld_obs) < 1e-6):
        scale = scale**2
        s = vOld_pset + vOld_obs - 2 * vOld_cov * scale

    alpha = (mOld_obs - mOld_pset) / np.sqrt(s) * sgn

    log_phi = logcdf_robust(alpha)
    log_phi_cons = logcdf_robust(alpha_cons)

    logZ_orig = log_1_minus_exp_x(np.sum(log_phi, axis = 0))

    if np.any(np.logical_not(logZ_orig == -np.inf)):
        sel = (logZ_orig == -np.inf)
        logZ_orig[ sel ] = logcdf_robust(-np.min(alpha[ :, sel ], axis = 0))

    logZ_term1 = np.sum(log_phi_cons, axis = 0) + logZ_orig
    logZ_term2 = log_1_minus_exp_x(np.sum(log_phi_cons, axis = 0))

    if np.any(np.logical_not(logZ_term2 == -np.inf)):
        sel = (logZ_term2 == -np.inf)
        logZ_term2[ sel ] = logcdf_robust(-np.min(alpha_cons[ :, sel ], axis = 0))

    # TODO: This should be done robustly

    max_value = np.maximum(logZ_term1, logZ_term2)

    logZ = np.tile(np.log(np.exp(logZ_term1 - max_value) + np.exp(logZ_term2 - max_value)) + \
        max_value, q).reshape((n_pset, q, n_obs)).swapaxes(0, 1)
    logZ_cons = np.tile(np.log(np.exp(logZ_term1 - max_value) + np.exp(logZ_term2 - max_value)) + \
        max_value, c).reshape((n_pset, c, n_obs)).swapaxes(0, 1)

    log_phi_sum = np.tile(np.sum(log_phi, axis = 0), q).reshape((n_pset, q, n_obs)).swapaxes(0, 1)
    log_phi_sum_cons = np.tile(np.sum(log_phi_cons, axis = 0), q).reshape((n_pset, q, n_obs)).swapaxes(0, 1)

    ratio = - np.exp(sps.norm.logpdf(alpha) - logZ + log_phi_sum - logcdf_robust(alpha) + log_phi_sum_cons)

    logZ_orig_cons = np.tile(logZ_orig, c).reshape((n_pset, c, n_obs)).swapaxes(0, 1)
    log_phi_sum_cons = np.tile(np.sum(log_phi_cons, axis = 0), c).reshape((n_pset, c, n_obs)).swapaxes(0, 1)

    ratio_cons = np.exp(sps.norm.logpdf(alpha_cons) - logZ_cons + logZ_orig_cons + log_phi_sum_cons - logcdf_robust(alpha_cons)) - \
        np.exp(sps.norm.logpdf(alpha_cons) - logZ_cons + log_phi_sum_cons - logcdf_robust(alpha_cons))

    # Derivatives, non vector form.

    dlogZdmfOld_obs = ratio / np.sqrt(s) * sgn
    dlogZdmfOld_pset = ratio / np.sqrt(s) * -1.0 * sgn

    dlogZdmfOld_obs2 = - ratio / s * (alpha + ratio)
    dlogZdmfOld_pset2 = - ratio / s * (alpha + ratio)
    dlogZdmfOld_cov2 = - ratio / s * (alpha + ratio) * -1.0

    dlogZdmcOld = ratio_cons / np.sqrt(s_cons)
    dlogZdmcOld2 = - ratio_cons / s_cons * (alpha_cons + ratio_cons)

    a_VfOld_times_dlogZdmfOld2 = vOld_obs * dlogZdmfOld_obs2 + vOld_cov * dlogZdmfOld_cov2 + 1.0
    b_VfOld_times_dlogZdmfOld2 = vOld_obs * dlogZdmfOld_cov2 + vOld_cov * dlogZdmfOld_pset2
    c_VfOld_times_dlogZdmfOld2 = vOld_cov * dlogZdmfOld_obs2 + vOld_pset * dlogZdmfOld_cov2
    d_VfOld_times_dlogZdmfOld2 = vOld_cov * dlogZdmfOld_cov2 + vOld_pset * dlogZdmfOld_pset2 + 1.0

    a_inv, b_inv, c_inv, d_inv = two_by_two_matrix_inverse(a_VfOld_times_dlogZdmfOld2, b_VfOld_times_dlogZdmfOld2, \
        c_VfOld_times_dlogZdmfOld2, d_VfOld_times_dlogZdmfOld2)

    vTilde_obs_new = - (dlogZdmfOld_obs2 * a_inv + dlogZdmfOld_cov2 * c_inv)
    vTilde_pset_new = - (dlogZdmfOld_cov2 * b_inv + dlogZdmfOld_pset2 * d_inv)
    vTilde_cov_new = - (dlogZdmfOld_obs2 * b_inv + dlogZdmfOld_cov2 * d_inv)

    v_1, v_2 = two_by_two_symmetric_matrix_product_vector(dlogZdmfOld_obs2, \
        dlogZdmfOld_pset2, dlogZdmfOld_cov2, mOld_obs, mOld_pset)

    v_1 = dlogZdmfOld_obs - v_1
    v_2 = dlogZdmfOld_pset - v_2
    mTilde_obs_new = v_1 * a_inv + v_2 * c_inv
    mTilde_pset_new = v_1 * b_inv + v_2 * d_inv

    vTilde_cons =  - dlogZdmcOld2 / (1.0 + dlogZdmcOld2 * c_vOld)
    mTilde_cons = (dlogZdmcOld - c_mOld * dlogZdmcOld2) / (1.0 + dlogZdmcOld2 * c_vOld)

    if no_negative_variances_nor_nands == True:

        finite = np.logical_and(np.logical_and(np.logical_and(np.logical_and(np.isfinite(vTilde_obs_new), np.isfinite(vTilde_pset_new)), \
            np.isfinite(vTilde_cov_new)), np.isfinite(mTilde_obs_new)), np.isfinite(mTilde_pset_new))

        c_finite = np.logical_and(np.isfinite(vTilde_cons), np.isfinite(mTilde_cons))

        neg1 = np.where(np.logical_or(np.logical_not(finite), vTilde_obs_new < 0))
        neg2 = np.where(np.logical_or(np.logical_not(finite), vTilde_pset_new < 0))
        c_neg = np.where(np.logical_or(np.logical_not(c_finite), vTilde_cons < 0))

        vTilde_obs_new[ neg1 ] = 0.0
        vTilde_obs_new[ neg2 ] = 0.0
        vTilde_pset_new[ neg1 ] = 0.0
        vTilde_pset_new[ neg2 ] = 0.0
        vTilde_cov_new[ neg1 ] = 0.0
        vTilde_cov_new[ neg2 ] = 0.0
        mTilde_obs_new[ neg1 ] = 0.0
        mTilde_obs_new[ neg2 ] = 0.0
        mTilde_pset_new[ neg1 ] = 0.0
        mTilde_pset_new[ neg2 ] = 0.0
        vTilde_cons[ c_neg ] = 0.0
        mTilde_cons[ c_neg ] = 0.0

    # We do the actual update

    a_c_hfHatNew = vTilde_cons
    b_c_hfHatNew = mTilde_cons

    a['ahfhat'][ :, :, :, 0, 0 ] = vTilde_obs_new.T * damping + (1 - damping) * a['ahfhat'][ :, :, :, 0, 0 ]
    a['ahfhat'][ :, :, :, 1, 1 ] = vTilde_pset_new.T * damping + (1 - damping) * a['ahfhat'][ :, :, :, 1, 1 ]
    a['ahfhat'][ :, :, :, 0, 1 ] = vTilde_cov_new.T * damping + (1 - damping) * a['ahfhat'][ :, :, :, 0, 1 ]
    a['ahfhat'][ :, :, :, 1, 0 ] = vTilde_cov_new.T * damping + (1 - damping) * a['ahfhat'][ :, :, :, 1, 0 ]
    a['bhfhat'][ :, :, :, 0 ] = mTilde_obs_new.T * damping + (1 - damping) * a['bhfhat'][ :, :, :, 0 ]
    a['bhfhat'][ :, :, :, 1 ] = mTilde_pset_new.T * damping + (1 - damping) * a['bhfhat'][ :, :, :, 1 ]
    a['a_c_hfhat'][ :, :, : ] = a_c_hfHatNew.T * damping + (1 - damping) * a['a_c_hfhat'][ :, :, : ]
    a['b_c_hfhat'][ :, :, : ] = b_c_hfHatNew.T * damping + (1 - damping) * a['b_c_hfhat'][ :, :, : ]

    # Second we update the factors corresponding to the pareto set

    # We compute an "old" distribution

    m_pset1 = np.zeros((q, n_pset, n_pset))
    m_pset2 = np.zeros((q, n_pset, n_pset))
    v_pset1 = np.zeros((q, n_pset, n_pset))
    v_pset2 = np.zeros((q, n_pset, n_pset))
    v_cov = np.zeros((q, n_pset, n_pset))

    c_m_pset = np.zeros((c, n_pset, n_pset))
    c_v_pset = np.zeros((c, n_pset, n_pset))

    n_task = 0
    for obj in all_tasks:
        m_pset1[ n_task, :, : ] = np.tile(a['m'][ obj ][ 0 : n_pset ], n_pset).reshape((n_pset, n_pset))
        m_pset2[ n_task, :, : ] = np.tile(a['m'][ obj ][ 0 : n_pset ], n_pset).reshape((n_pset, n_pset)).T
        v_cov[ n_task, :, : ] = a['V'][ obj ][ 0 : n_pset, 0 : n_pset ]
        v_cov[ n_task, :, : ] = v_cov[ n_task, :, : ] - np.diag(np.diag(v_cov[ n_task, :, : ]))
        v_pset1[ n_task, :, : ] = np.tile(np.diag(a['V'][ obj ])[ 0 : n_pset ], n_pset).reshape((n_pset, n_pset))
        v_pset2[ n_task, :, : ] = np.tile(np.diag(a['V'][ obj ])[ 0 : n_pset ], n_pset).reshape((n_pset, n_pset)).T
        n_task += 1

    n_task = 0
    for cons in all_constraints:
        c_m_pset[ n_task, :, : ] = a['m_cons'][ cons ][ 0 : n_pset ]
        c_v_pset[ n_task, :, : ] = np.diag(a['V_cons'][ cons ])[0 : n_pset]
        n_task += 1

    vTilde_pset1 = a['chfhat'][ :, :, :, 0, 0 ].T
    vTilde_pset2 = a['chfhat'][ :, :, :, 1, 1 ].T
    covTilde = a['chfhat'][ :, :, :, 0, 1 ].T
    mTilde_pset1 = a['dhfhat'][ :, :, :, 0 ].T
    mTilde_pset2 = a['dhfhat'][ :, :, :, 1 ].T

    c_vTilde_pset = a['c_c_hfhat'][ :, :, : ].T
    c_mTilde_pset = a['d_c_hfhat'][ :, :, : ].T

    inv_v_pset1, inv_v_pset2, inv_v_cov = two_by_two_symmetric_matrix_inverse(v_pset1, v_pset2, v_cov)

    inv_vOld_pset1 = inv_v_pset1 - vTilde_pset1
    inv_vOld_pset2 = inv_v_pset2 - vTilde_pset2
    inv_vOld_cov =  inv_v_cov - covTilde

    vOld_pset1, vOld_pset2, vOld_cov = two_by_two_symmetric_matrix_inverse(inv_vOld_pset1, inv_vOld_pset2, inv_vOld_cov)
    c_vOld_pset = 1.0 / (1.0 / c_v_pset - c_vTilde_pset)

    mOld_pset1, mOld_pset2  = two_by_two_symmetric_matrix_product_vector(inv_v_pset1, inv_v_pset2, inv_v_cov, m_pset1, m_pset2)
    mOld_pset1 = mOld_pset1 - mTilde_pset1
    mOld_pset2 = mOld_pset2 - mTilde_pset2
    mOld_pset1, mOld_pset2  = two_by_two_symmetric_matrix_product_vector(vOld_pset1, vOld_pset2, vOld_cov, mOld_pset1, mOld_pset2)

    c_mOld_pset = c_vOld_pset * (c_m_pset / c_v_pset - c_mTilde_pset)

    s = vOld_pset1 + vOld_pset2 - 2 * vOld_cov
    s_cons = c_vOld_pset

    if np.any(vOld_pset1  < 0):
        raise npla.linalg.LinAlgError("Negative value in the sqrt!")

    if np.any(vOld_pset2  < 0):
        raise npla.linalg.LinAlgError("Negative value in the sqrt!")

    if np.any(c_vOld_pset < 0):
        raise npla.linalg.LinAlgError("Negative value in the sqrt!")

    alpha_cons = c_mOld_pset / np.sqrt(c_vOld_pset)

    scale = 1.0 - 1e-4
    while np.any(s / (vOld_pset1 + vOld_pset2) < 1e-6):
        print "Reducing scale to guarantee positivity!"
        scale = scale**2
        s = vOld_pset1 + vOld_pset2 - 2 * vOld_cov * scale

    alpha = (mOld_pset1 - mOld_pset2) / np.sqrt(s) * sgn

    log_phi = logcdf_robust(alpha)
    log_phi_cons = logcdf_robust(alpha_cons)

    logZ_orig = log_1_minus_exp_x(np.sum(log_phi, axis = 0))

    if np.any(np.logical_not(logZ_orig == -np.inf)):
        sel = (logZ_orig == -np.inf)
        logZ_orig[ sel ] = logcdf_robust(-np.min(alpha[ :, sel ], axis = 0))

    logZ_term1 = np.sum(log_phi_cons, axis = 0) + logZ_orig
    logZ_term2 = log_1_minus_exp_x(np.sum(log_phi_cons, axis = 0))

    if np.any(np.logical_not(logZ_term2 == -np.inf)):
        sel = (logZ_term2 == -np.inf)
        logZ_term2[ sel ] = logcdf_robust(-np.min(alpha_cons[ :, sel ], axis = 0))

    # TODO: This should be done robustly

    max_value = np.maximum(logZ_term1, logZ_term2)

    logZ = np.tile(np.log(np.exp(logZ_term1 - max_value) + np.exp(logZ_term2 - max_value)) + \
        max_value, q).reshape((n_pset, q, n_pset)).swapaxes(0, 1)
    logZ_cons = np.tile(np.log(np.exp(logZ_term1 - max_value) + np.exp(logZ_term2 - max_value)) + \
        max_value, c).reshape((n_pset, c, n_pset)).swapaxes(0, 1)

    log_phi_sum = np.tile(np.sum(log_phi, axis = 0), q).reshape((n_pset, q, n_pset)).swapaxes(0, 1)
    log_phi_sum_cons = np.tile(np.sum(log_phi_cons, axis = 0), q).reshape((n_pset, q, n_pset)).swapaxes(0, 1)

    ratio = - np.exp(sps.norm.logpdf(alpha) - logZ + log_phi_sum - logcdf_robust(alpha) + log_phi_sum_cons)

    logZ_orig_cons = np.tile(logZ_orig, c).reshape((n_pset, c, n_pset)).swapaxes(0, 1)
    log_phi_sum_cons = np.tile(np.sum(log_phi_cons, axis = 0), c).reshape((n_pset, c, n_pset)).swapaxes(0, 1)

    ratio_cons = np.exp(sps.norm.logpdf(alpha_cons) - logZ_cons + logZ_orig_cons + log_phi_sum_cons - logcdf_robust(alpha_cons)) - \
        np.exp(sps.norm.logpdf(alpha_cons) - logZ_cons + log_phi_sum_cons - logcdf_robust(alpha_cons))

    # Derivatives, non vector form.

    dlogZdmfOld_pset1 = ratio / np.sqrt(s) * sgn
    dlogZdmfOld_pset2 = ratio / np.sqrt(s) * -1.0 * sgn

    dlogZdmfOld_pset12 = - ratio / s * (alpha + ratio)
    dlogZdmfOld_pset22 = - ratio / s * (alpha + ratio)
    dlogZdmfOld_cov2 = - ratio / s * (alpha + ratio) * -1.0

    dlogZdmcOld_pset = ratio_cons / np.sqrt(s_cons)
    dlogZdmcOld_pset2 = - ratio_cons / s_cons * (alpha_cons + ratio_cons)

    vTilde_cons_pset = - dlogZdmcOld_pset2 / (1.0 + dlogZdmcOld_pset2 * c_vOld_pset)
    mTilde_cons_pset = (dlogZdmcOld_pset - c_mOld_pset * dlogZdmcOld_pset2) / (1.0 + dlogZdmcOld_pset2 * c_vOld_pset)

    a_VfOld_times_dlogZdmfOld2 = vOld_pset1 * dlogZdmfOld_pset12 + vOld_cov * dlogZdmfOld_cov2 + 1.0
    b_VfOld_times_dlogZdmfOld2 = vOld_pset1 * dlogZdmfOld_cov2 + vOld_cov * dlogZdmfOld_pset22
    c_VfOld_times_dlogZdmfOld2 = vOld_cov * dlogZdmfOld_pset12 + vOld_pset2 * dlogZdmfOld_cov2
    d_VfOld_times_dlogZdmfOld2 = vOld_cov * dlogZdmfOld_cov2 + vOld_pset2 * dlogZdmfOld_pset22 + 1.0

    a_inv, b_inv, c_inv, d_inv = two_by_two_matrix_inverse(a_VfOld_times_dlogZdmfOld2, b_VfOld_times_dlogZdmfOld2, \
        c_VfOld_times_dlogZdmfOld2, d_VfOld_times_dlogZdmfOld2)

    vTilde_pset1_new = - (dlogZdmfOld_pset12 * a_inv + dlogZdmfOld_cov2 * c_inv)
    vTilde_pset2_new = - (dlogZdmfOld_cov2 * b_inv + dlogZdmfOld_pset22 * d_inv)
    vTilde_cov_new = - (dlogZdmfOld_pset12 * b_inv + dlogZdmfOld_cov2 * d_inv)

    v_1, v_2 = two_by_two_symmetric_matrix_product_vector(dlogZdmfOld_pset12, \
        dlogZdmfOld_pset22, dlogZdmfOld_cov2, mOld_pset1, mOld_pset2)

    v_1 = dlogZdmfOld_pset1 - v_1
    v_2 = dlogZdmfOld_pset2 - v_2
    mTilde_pset1_new = v_1 * a_inv + v_2 * c_inv
    mTilde_pset2_new = v_1 * b_inv + v_2 * d_inv

    n_task = 0
    for obj in all_tasks:
        vTilde_pset1_new[ n_task, :, : ] -= np.diag(np.diag(vTilde_pset1_new[ n_task, :, :, ]))
        vTilde_pset2_new[ n_task, :, : ] -= np.diag(np.diag(vTilde_pset2_new[ n_task, :, :, ]))
        vTilde_cov_new[ n_task, :, : ] -= np.diag(np.diag(vTilde_cov_new[ n_task, :, : ]))
        mTilde_pset1_new[ n_task, :, : ] -= np.diag(np.diag(mTilde_pset1_new[ n_task, :, : ]))
        mTilde_pset2_new[ n_task, :, : ] -= np.diag(np.diag(mTilde_pset2_new[ n_task, :, : ]))
        n_task += 1

    if no_negative_variances_nor_nands == True:
        finite = np.logical_and(np.logical_and(np.logical_and(np.logical_and(np.isfinite(vTilde_pset1_new), np.isfinite(vTilde_pset2_new)), \
            np.isfinite(vTilde_cov_new)), np.isfinite(mTilde_pset1_new)), np.isfinite(mTilde_pset2_new))
        c_finite = np.logical_and(np.isfinite(vTilde_cons_pset),np.isfinite(mTilde_cons_pset))

        neg1 = np.where(np.logical_or(np.logical_not(finite), vTilde_pset1_new < 0))
        neg2 = np.where(np.logical_or(np.logical_not(finite), vTilde_pset2_new < 0))
        c_neg = np.where(np.logical_or(np.logical_not(c_finite), vTilde_cons_pset < 0))

        vTilde_pset1_new[ neg1 ] = 0.0
        vTilde_pset1_new[ neg2 ] = 0.0
        vTilde_pset2_new[ neg1 ] = 0.0
        vTilde_pset2_new[ neg2 ] = 0.0
        vTilde_cov_new[ neg1 ] = 0.0
        vTilde_cov_new[ neg2 ] = 0.0
        mTilde_pset1_new[ neg1 ] = 0.0
        mTilde_pset1_new[ neg2 ] = 0.0
        mTilde_pset2_new[ neg1 ] = 0.0
        mTilde_pset2_new[ neg2 ] = 0.0
        vTilde_cons_pset[ c_neg ] = 0.0
        mTilde_cons_pset[ c_neg ] = 0.0

    # We do the actual update

    c_c_hfHatNew = vTilde_cons_pset
    d_c_hfHatNew = mTilde_cons_pset

    #i not equal to j condition.

    for i in range(0,n_pset,1):
        c_c_hfHatNew[:,i,i] = 0.0
        d_c_hfHatNew[:,i,i] = 0.0

    #i not equal to j condition.

    a['chfhat'][ :, :, :, 0, 0 ] = vTilde_pset1_new.T * damping + (1 - damping) * a['chfhat'][ :, :, :, 0, 0 ]
    a['chfhat'][ :, :, :, 1, 1 ] = vTilde_pset2_new.T * damping + (1 - damping) * a['chfhat'][ :, :, :, 1, 1 ]
    a['chfhat'][ :, :, :, 0, 1 ] = vTilde_cov_new.T * damping + (1 - damping) * a['chfhat'][ :, :, :, 0, 1 ]
    a['chfhat'][ :, :, :, 1, 0 ] = vTilde_cov_new.T * damping + (1 - damping) * a['chfhat'][ :, :, :, 1, 0 ]
    a['dhfhat'][ :, :, :, 0 ] = mTilde_pset1_new.T * damping + (1 - damping) * a['dhfhat'][ :, :, :, 0 ]
    a['dhfhat'][ :, :, :, 1 ] = mTilde_pset2_new.T * damping + (1 - damping) * a['dhfhat'][ :, :, :, 1 ]
    a['c_c_hfhat'][ :, :, : ] = c_c_hfHatNew.T * damping + (1 - damping) * a['c_c_hfhat'][ :, :, : ]
    a['d_c_hfhat'][ :, :, : ] = d_c_hfHatNew.T * damping + (1 - damping) * a['d_c_hfhat'][ :, :, : ]


    return a


def updateFactors_fast_daniel_no_constraints_pareto_set_robust(a, damping, minimize=True, no_negative_variances_nor_nands = False):
    # used to switch between minimizing and maximizing
    sgn = -1.0 if minimize else 1.0

    # We update the h factors
    all_tasks = a['objs']
    all_constraints = a['cons']
    n_obs = a['n_obs']
    n_pset = a['n_pset']
    n_total = a['n_total']
    q = a['q']
    c = a['c']

    alpha = np.zeros(a['q'])
    s = np.zeros(a['q'])
    ratio_cons = np.zeros(c)

    # First we update the factors corresponding to the observed data

    # We compute an "old" distribution

    # Data structures for objective npset nobs cavities (a, b).

    m_pset = np.zeros((q, n_pset, n_obs))
    m_obs = np.zeros((q, n_pset, n_obs))
    v_pset = np.zeros((q, n_pset, n_obs))
    v_obs = np.zeros((q, n_pset, n_obs))
    v_cov = np.zeros((q, n_pset, n_obs))

    # Data structures for constraint npset nobs cavities (c_a, c_b).

    c_m = np.zeros((c, n_pset, n_obs))
    c_v = np.zeros((c, n_pset, n_obs))

    # We do the update of the external factors.

    c_m_external = np.zeros((c, n_pset))
    c_v_external = np.zeros((c, n_pset))
    alpha_external = np.zeros(c)

    # First we update the external (easy) factors that only affect the constraints

    n_task = 0
    for cons in all_constraints:
        c_m_external[ n_task, : ] = a['m_cons'][ cons ][ 0 : n_pset ]
        c_v_external[ n_task, : ] = np.diag(a['V_cons'][ cons ])[ 0 : n_pset ]
        n_task += 1

    c_vTilde_external = a['ehfhat'][ :, : ].T
    c_mTilde_external = a['fhfhat'][ :, : ].T

    c_vOld_external = 1.0 / (1.0 / c_v_external - c_vTilde_external)
    c_mOld_external = c_vOld_external * (c_m_external / c_v_external - c_mTilde_external)

    if np.any(c_vOld_external < 0):
        raise npla.linalg.LinAlgError("Negative value in the sqrt!")

    alpha_external = c_mOld_external / np.sqrt(c_vOld_external)
    logZ = logcdf_robust(alpha_external)

    ratio = np.exp(sps.norm.logpdf(alpha_external) - logZ)
    dlogZdmfOld_external = ratio / np.sqrt(c_vOld_external)
    dlogZdmfOld2_external = - ratio * (alpha_external + ratio) / c_vOld_external

     # We find the parameters of the updated factors

    ehfhat_act = (- dlogZdmfOld2_external / (1.0 + dlogZdmfOld2_external * c_vOld_external)).T
    fhfhat_act = ((dlogZdmfOld_external - c_mOld_external * dlogZdmfOld2_external) / (1.0 + dlogZdmfOld2_external * c_vOld_external)).T

    if no_negative_variances_nor_nands == True:
        neg = np.where(ehfhat_act < 0)

        ehfhat_act[ neg ] = 0.0
        fhfhat_act[ neg ] = 0.0

    a['ehfhat'][ :, : ] = ehfhat_act * damping + (1 - damping) * a['ehfhat'][ :, : ]
    a['fhfhat'][ :, : ] = fhfhat_act * damping + (1 - damping) * a['fhfhat'][ :, : ]

    # Done!

    n_task = 0
    for obj in all_tasks:
        m_obs[ n_task, :, : ] = np.tile(a['m'][ obj ][ n_pset : n_total ], n_pset).reshape((n_pset, n_obs))
        m_pset[ n_task, :, : ] = np.tile(a['m'][ obj ][ 0 : n_pset ], n_obs).reshape((n_obs, n_pset)).T
        v_cov[ n_task, :, : ] = a['V'][ obj ][ 0 : n_pset, n_pset : n_total ]
        v_obs[ n_task, :, : ] = np.tile(np.diag(a['V'][ obj ])[ n_pset : n_total ], n_pset).reshape((n_pset, n_obs))
        v_pset[ n_task, :, : ] = np.tile(np.diag(a['V'][ obj ])[ 0 : n_pset ], n_obs).reshape((n_obs, n_pset)).T
        n_task += 1

    n_task = 0

    for cons in all_constraints:
        c_m[ n_task, :, : ] = a['m_cons'][ cons ][ n_pset : n_total ]
        c_v[ n_task, :, : ] = np.diag(a['V_cons'][ cons ])[ n_pset : n_total ]
        n_task += 1

    vTilde_obs = a['ahfhat'][ :, :, :, 0, 0 ].T
    vTilde_pset = a['ahfhat'][ :, :, :, 1, 1 ].T
    covTilde = a['ahfhat'][ :, :, :, 0, 1 ].T
    mTilde_obs = a['bhfhat'][ :, :, :, 0, ].T
    mTilde_pset = a['bhfhat'][ :, :, :, 1, ].T

    c_vTilde = a['a_c_hfhat'][ :, :, : ].T
    c_mTilde = a['b_c_hfhat'][ :, :, : ].T

    # Obtaining cavities.

    inv_v_obs, inv_v_pset, inv_v_cov = two_by_two_symmetric_matrix_inverse(v_obs, v_pset, v_cov)
    inv_c_v = 1.0 / c_v

    inv_vOld_obs = inv_v_obs - vTilde_obs
    inv_vOld_pset = inv_v_pset - vTilde_pset
    inv_vOld_cov =  inv_v_cov - covTilde
    inv_c_vOld = inv_c_v - c_vTilde

    vOld_obs, vOld_pset, vOld_cov = two_by_two_symmetric_matrix_inverse(inv_vOld_obs, inv_vOld_pset, inv_vOld_cov)
    c_vOld = 1.0 / inv_c_vOld

    mOld_obs, mOld_pset  = two_by_two_symmetric_matrix_product_vector(inv_v_obs, inv_v_pset, inv_v_cov, m_obs, m_pset)
    mOld_obs = mOld_obs - mTilde_obs
    mOld_pset = mOld_pset - mTilde_pset
    mOld_obs, mOld_pset  = two_by_two_symmetric_matrix_product_vector(vOld_obs, vOld_pset, vOld_cov, mOld_obs, mOld_pset)

    c_mOld = c_vOld * (c_m / c_v - c_mTilde)

    #Computing factors.

    s = vOld_pset + vOld_obs - 2 * vOld_cov
    s_cons = c_vOld

    if np.any(vOld_pset < 0):
        raise npla.linalg.LinAlgError("Negative variance in the sqrt!")

    if np.any(vOld_obs < 0):
        raise npla.linalg.LinAlgError("Negative variance in the sqrt!")

    if np.any(c_vOld < 0):
        raise npla.linalg.LinAlgError("Negative value in the sqrt!")

    alpha_cons = c_mOld / np.sqrt(c_vOld)

    scale = 1.0 - 1e-4
    while np.any(s / (vOld_pset + vOld_obs) < 1e-6):
        scale = scale**2
        s = vOld_pset + vOld_obs - 2 * vOld_cov * scale

    alpha = (mOld_obs - mOld_pset) / np.sqrt(s) * sgn

    log_phi = logcdf_robust(alpha)
    log_phi_cons = logcdf_robust(alpha_cons)

    logZ_orig = log_1_minus_exp_x(np.sum(log_phi, axis = 0))

    if np.any(np.logical_not(logZ_orig == -np.inf)):
        sel = (logZ_orig == -np.inf)
        logZ_orig[ sel ] = logcdf_robust(-np.min(alpha[ :, sel ], axis = 0))

    logZ_term1 = np.sum(log_phi_cons, axis = 0) + logZ_orig
    logZ_term2 = log_1_minus_exp_x(np.sum(log_phi_cons, axis = 0))

    if np.any(np.logical_not(logZ_term2 == -np.inf)):
        sel = (logZ_term2 == -np.inf)
        logZ_term2[ sel ] = logcdf_robust(-np.min(alpha_cons[ :, sel ], axis = 0))

    # TODO: This should be done robustly

    max_value = np.maximum(logZ_term1, logZ_term2)

    logZ = np.tile(np.log(np.exp(logZ_term1 - max_value) + np.exp(logZ_term2 - max_value)) + \
        max_value, q).reshape((n_pset, q, n_obs)).swapaxes(0, 1)
    logZ_cons = np.tile(np.log(np.exp(logZ_term1 - max_value) + np.exp(logZ_term2 - max_value)) + \
        max_value, c).reshape((n_pset, c, n_obs)).swapaxes(0, 1)

    log_phi_sum = np.tile(np.sum(log_phi, axis = 0), q).reshape((n_pset, q, n_obs)).swapaxes(0, 1)
    log_phi_sum_cons = np.tile(np.sum(log_phi_cons, axis = 0), q).reshape((n_pset, q, n_obs)).swapaxes(0, 1)

    ratio = - np.exp(sps.norm.logpdf(alpha) - logZ + log_phi_sum - logcdf_robust(alpha) + log_phi_sum_cons)

    logZ_orig_cons = np.tile(logZ_orig, c).reshape((n_pset, c, n_obs)).swapaxes(0, 1)
    log_phi_sum_cons = np.tile(np.sum(log_phi_cons, axis = 0), c).reshape((n_pset, c, n_obs)).swapaxes(0, 1)

    ratio_cons = np.exp(sps.norm.logpdf(alpha_cons) - logZ_cons + logZ_orig_cons + log_phi_sum_cons - logcdf_robust(alpha_cons)) - \
        np.exp(sps.norm.logpdf(alpha_cons) - logZ_cons + log_phi_sum_cons - logcdf_robust(alpha_cons))

    # Derivatives, non vector form.

    dlogZdmfOld_obs = ratio / np.sqrt(s) * sgn
    dlogZdmfOld_pset = ratio / np.sqrt(s) * -1.0 * sgn

    dlogZdmfOld_obs2 = - ratio / s * (alpha + ratio)
    dlogZdmfOld_pset2 = - ratio / s * (alpha + ratio)
    dlogZdmfOld_cov2 = - ratio / s * (alpha + ratio) * -1.0

    dlogZdmcOld = ratio_cons / np.sqrt(s_cons)
    dlogZdmcOld2 = - ratio_cons / s_cons * (alpha_cons + ratio_cons)

    a_VfOld_times_dlogZdmfOld2 = vOld_obs * dlogZdmfOld_obs2 + vOld_cov * dlogZdmfOld_cov2 + 1.0
    b_VfOld_times_dlogZdmfOld2 = vOld_obs * dlogZdmfOld_cov2 + vOld_cov * dlogZdmfOld_pset2
    c_VfOld_times_dlogZdmfOld2 = vOld_cov * dlogZdmfOld_obs2 + vOld_pset * dlogZdmfOld_cov2
    d_VfOld_times_dlogZdmfOld2 = vOld_cov * dlogZdmfOld_cov2 + vOld_pset * dlogZdmfOld_pset2 + 1.0

    a_inv, b_inv, c_inv, d_inv = two_by_two_matrix_inverse(a_VfOld_times_dlogZdmfOld2, b_VfOld_times_dlogZdmfOld2, \
        c_VfOld_times_dlogZdmfOld2, d_VfOld_times_dlogZdmfOld2)

    vTilde_obs_new = - (dlogZdmfOld_obs2 * a_inv + dlogZdmfOld_cov2 * c_inv)
    vTilde_pset_new = - (dlogZdmfOld_cov2 * b_inv + dlogZdmfOld_pset2 * d_inv)
    vTilde_cov_new = - (dlogZdmfOld_obs2 * b_inv + dlogZdmfOld_cov2 * d_inv)

    v_1, v_2 = two_by_two_symmetric_matrix_product_vector(dlogZdmfOld_obs2, \
        dlogZdmfOld_pset2, dlogZdmfOld_cov2, mOld_obs, mOld_pset)

    v_1 = dlogZdmfOld_obs - v_1
    v_2 = dlogZdmfOld_pset - v_2
    mTilde_obs_new = v_1 * a_inv + v_2 * c_inv
    mTilde_pset_new = v_1 * b_inv + v_2 * d_inv

    vTilde_cons =  - dlogZdmcOld2 / (1.0 + dlogZdmcOld2 * c_vOld)
    mTilde_cons = (dlogZdmcOld - c_mOld * dlogZdmcOld2) / (1.0 + dlogZdmcOld2 * c_vOld)

    if no_negative_variances_nor_nands == True:

        finite = np.logical_and(np.logical_and(np.logical_and(np.logical_and(np.isfinite(vTilde_obs_new), np.isfinite(vTilde_pset_new)), \
            np.isfinite(vTilde_cov_new)), np.isfinite(mTilde_obs_new)), np.isfinite(mTilde_pset_new))

        c_finite = np.logical_and(np.isfinite(vTilde_cons), np.isfinite(mTilde_cons))

        neg1 = np.where(np.logical_or(np.logical_not(finite), vTilde_obs_new < 0))
        neg2 = np.where(np.logical_or(np.logical_not(finite), vTilde_pset_new < 0))
        c_neg = np.where(np.logical_or(np.logical_not(c_finite), vTilde_cons < 0))

        vTilde_obs_new[ neg1 ] = 0.0
        vTilde_obs_new[ neg2 ] = 0.0
        vTilde_pset_new[ neg1 ] = 0.0
        vTilde_pset_new[ neg2 ] = 0.0
        vTilde_cov_new[ neg1 ] = 0.0
        vTilde_cov_new[ neg2 ] = 0.0
        mTilde_obs_new[ neg1 ] = 0.0
        mTilde_obs_new[ neg2 ] = 0.0
        mTilde_pset_new[ neg1 ] = 0.0
        mTilde_pset_new[ neg2 ] = 0.0
        vTilde_cons[ c_neg ] = 0.0
        mTilde_cons[ c_neg ] = 0.0

    # We do the actual update

    a_c_hfHatNew = vTilde_cons
    b_c_hfHatNew = mTilde_cons

    a['ahfhat'][ :, :, :, 0, 0 ] = vTilde_obs_new.T * damping + (1 - damping) * a['ahfhat'][ :, :, :, 0, 0 ]
    a['ahfhat'][ :, :, :, 1, 1 ] = vTilde_pset_new.T * damping + (1 - damping) * a['ahfhat'][ :, :, :, 1, 1 ]
    a['ahfhat'][ :, :, :, 0, 1 ] = vTilde_cov_new.T * damping + (1 - damping) * a['ahfhat'][ :, :, :, 0, 1 ]
    a['ahfhat'][ :, :, :, 1, 0 ] = vTilde_cov_new.T * damping + (1 - damping) * a['ahfhat'][ :, :, :, 1, 0 ]
    a['bhfhat'][ :, :, :, 0 ] = mTilde_obs_new.T * damping + (1 - damping) * a['bhfhat'][ :, :, :, 0 ]
    a['bhfhat'][ :, :, :, 1 ] = mTilde_pset_new.T * damping + (1 - damping) * a['bhfhat'][ :, :, :, 1 ]
    a['a_c_hfhat'][ :, :, : ] = a_c_hfHatNew.T * damping + (1 - damping) * a['a_c_hfhat'][ :, :, : ]
    a['b_c_hfhat'][ :, :, : ] = b_c_hfHatNew.T * damping + (1 - damping) * a['b_c_hfhat'][ :, :, : ]

    # Second we update the factors corresponding to the pareto set

    # We compute an "old" distribution

    m_pset1 = np.zeros((q, n_pset, n_pset))
    m_pset2 = np.zeros((q, n_pset, n_pset))
    v_pset1 = np.zeros((q, n_pset, n_pset))
    v_pset2 = np.zeros((q, n_pset, n_pset))
    v_cov = np.zeros((q, n_pset, n_pset))

    c_m_pset = np.zeros((c, n_pset, n_pset))
    c_v_pset = np.zeros((c, n_pset, n_pset))

    n_task = 0
    for obj in all_tasks:
        m_pset1[ n_task, :, : ] = np.tile(a['m'][ obj ][ 0 : n_pset ], n_pset).reshape((n_pset, n_pset))
        m_pset2[ n_task, :, : ] = np.tile(a['m'][ obj ][ 0 : n_pset ], n_pset).reshape((n_pset, n_pset)).T
        v_cov[ n_task, :, : ] = a['V'][ obj ][ 0 : n_pset, 0 : n_pset ]
        v_cov[ n_task, :, : ] = v_cov[ n_task, :, : ] - np.diag(np.diag(v_cov[ n_task, :, : ]))
        v_pset1[ n_task, :, : ] = np.tile(np.diag(a['V'][ obj ])[ 0 : n_pset ], n_pset).reshape((n_pset, n_pset))
        v_pset2[ n_task, :, : ] = np.tile(np.diag(a['V'][ obj ])[ 0 : n_pset ], n_pset).reshape((n_pset, n_pset)).T
        n_task += 1

    n_task = 0
    for cons in all_constraints:
        c_m_pset[ n_task, :, : ] = a['m_cons'][ cons ][ 0 : n_pset ]
        c_v_pset[ n_task, :, : ] = np.diag(a['V_cons'][ cons ])[0 : n_pset]
        n_task += 1

    vTilde_pset1 = a['chfhat'][ :, :, :, 0, 0 ].T
    vTilde_pset2 = a['chfhat'][ :, :, :, 1, 1 ].T
    covTilde = a['chfhat'][ :, :, :, 0, 1 ].T
    mTilde_pset1 = a['dhfhat'][ :, :, :, 0 ].T
    mTilde_pset2 = a['dhfhat'][ :, :, :, 1 ].T

    c_vTilde_pset = a['c_c_hfhat'][ :, :, : ].T
    c_mTilde_pset = a['d_c_hfhat'][ :, :, : ].T

    inv_v_pset1, inv_v_pset2, inv_v_cov = two_by_two_symmetric_matrix_inverse(v_pset1, v_pset2, v_cov)

    inv_vOld_pset1 = inv_v_pset1 - vTilde_pset1
    inv_vOld_pset2 = inv_v_pset2 - vTilde_pset2
    inv_vOld_cov =  inv_v_cov - covTilde

    vOld_pset1, vOld_pset2, vOld_cov = two_by_two_symmetric_matrix_inverse(inv_vOld_pset1, inv_vOld_pset2, inv_vOld_cov)

    mOld_pset1, mOld_pset2  = two_by_two_symmetric_matrix_product_vector(inv_v_pset1, inv_v_pset2, inv_v_cov, m_pset1, m_pset2)
    mOld_pset1 = mOld_pset1 - mTilde_pset1
    mOld_pset2 = mOld_pset2 - mTilde_pset2
    mOld_pset1, mOld_pset2  = two_by_two_symmetric_matrix_product_vector(vOld_pset1, vOld_pset2, vOld_cov, mOld_pset1, mOld_pset2)

    s = vOld_pset1 + vOld_pset2 - 2 * vOld_cov

    if np.any(vOld_pset1  < 0):
        raise npla.linalg.LinAlgError("Negative value in the sqrt!")

    if np.any(vOld_pset2  < 0):
        raise npla.linalg.LinAlgError("Negative value in the sqrt!")

    scale = 1.0 - 1e-4
    while np.any(s / (vOld_pset1 + vOld_pset2) < 1e-6):
        print "Reducing scale to guarantee positivity!"
        scale = scale**2
        s = vOld_pset1 + vOld_pset2 - 2 * vOld_cov * scale

    alpha = (mOld_pset1 - mOld_pset2) / np.sqrt(s) * sgn

    log_phi = logcdf_robust(alpha)
    logZ = log_1_minus_exp_x(np.sum(log_phi, axis = 0))

    if np.any(np.logical_not(logZ == -np.inf)):
        sel = (logZ == -np.inf)
        logZ[ sel ] = logcdf_robust(-np.min(alpha[ :, sel ], axis = 0))

    log_phi_sum = np.tile(np.sum(log_phi, axis = 0), q).reshape((n_pset, q, n_pset)).swapaxes(0, 1)

    ratio = - np.exp(sps.norm.logpdf(alpha) - logZ + log_phi_sum - logcdf_robust(alpha))

    # Derivatives, non vector form.

    dlogZdmfOld_pset1 = ratio / np.sqrt(s) * sgn
    dlogZdmfOld_pset2 = ratio / np.sqrt(s) * -1.0 * sgn

    dlogZdmfOld_pset12 = - ratio / s * (alpha + ratio)
    dlogZdmfOld_pset22 = - ratio / s * (alpha + ratio)
    dlogZdmfOld_cov2 = - ratio / s * (alpha + ratio) * -1.0

    a_VfOld_times_dlogZdmfOld2 = vOld_pset1 * dlogZdmfOld_pset12 + vOld_cov * dlogZdmfOld_cov2 + 1.0
    b_VfOld_times_dlogZdmfOld2 = vOld_pset1 * dlogZdmfOld_cov2 + vOld_cov * dlogZdmfOld_pset22
    c_VfOld_times_dlogZdmfOld2 = vOld_cov * dlogZdmfOld_pset12 + vOld_pset2 * dlogZdmfOld_cov2
    d_VfOld_times_dlogZdmfOld2 = vOld_cov * dlogZdmfOld_cov2 + vOld_pset2 * dlogZdmfOld_pset22 + 1.0

    a_inv, b_inv, c_inv, d_inv = two_by_two_matrix_inverse(a_VfOld_times_dlogZdmfOld2, b_VfOld_times_dlogZdmfOld2, \
        c_VfOld_times_dlogZdmfOld2, d_VfOld_times_dlogZdmfOld2)

    vTilde_pset1_new = - (dlogZdmfOld_pset12 * a_inv + dlogZdmfOld_cov2 * c_inv)
    vTilde_pset2_new = - (dlogZdmfOld_cov2 * b_inv + dlogZdmfOld_pset22 * d_inv)
    vTilde_cov_new = - (dlogZdmfOld_pset12 * b_inv + dlogZdmfOld_cov2 * d_inv)

    v_1, v_2 = two_by_two_symmetric_matrix_product_vector(dlogZdmfOld_pset12, \
        dlogZdmfOld_pset22, dlogZdmfOld_cov2, mOld_pset1, mOld_pset2)

    v_1 = dlogZdmfOld_pset1 - v_1
    v_2 = dlogZdmfOld_pset2 - v_2
    mTilde_pset1_new = v_1 * a_inv + v_2 * c_inv
    mTilde_pset2_new = v_1 * b_inv + v_2 * d_inv

    n_task = 0
    for obj in all_tasks:
        vTilde_pset1_new[ n_task, :, : ] -= np.diag(np.diag(vTilde_pset1_new[ n_task, :, :, ]))
        vTilde_pset2_new[ n_task, :, : ] -= np.diag(np.diag(vTilde_pset2_new[ n_task, :, :, ]))
        vTilde_cov_new[ n_task, :, : ] -= np.diag(np.diag(vTilde_cov_new[ n_task, :, : ]))
        mTilde_pset1_new[ n_task, :, : ] -= np.diag(np.diag(mTilde_pset1_new[ n_task, :, : ]))
        mTilde_pset2_new[ n_task, :, : ] -= np.diag(np.diag(mTilde_pset2_new[ n_task, :, : ]))
        n_task += 1

    if no_negative_variances_nor_nands == True:
        finite = np.logical_and(np.logical_and(np.logical_and(np.logical_and(np.isfinite(vTilde_pset1_new), np.isfinite(vTilde_pset2_new)), \
            np.isfinite(vTilde_cov_new)), np.isfinite(mTilde_pset1_new)), np.isfinite(mTilde_pset2_new))

        neg1 = np.where(np.logical_or(np.logical_not(finite), vTilde_pset1_new < 0))
        neg2 = np.where(np.logical_or(np.logical_not(finite), vTilde_pset2_new < 0))

        vTilde_pset1_new[ neg1 ] = 0.0
        vTilde_pset1_new[ neg2 ] = 0.0
        vTilde_pset2_new[ neg1 ] = 0.0
        vTilde_pset2_new[ neg2 ] = 0.0
        vTilde_cov_new[ neg1 ] = 0.0
        vTilde_cov_new[ neg2 ] = 0.0
        mTilde_pset1_new[ neg1 ] = 0.0
        mTilde_pset1_new[ neg2 ] = 0.0
        mTilde_pset2_new[ neg1 ] = 0.0
        mTilde_pset2_new[ neg2 ] = 0.0

    # We do the actual update

    #i not equal to j condition.

    a['chfhat'][ :, :, :, 0, 0 ] = vTilde_pset1_new.T * damping + (1 - damping) * a['chfhat'][ :, :, :, 0, 0 ]
    a['chfhat'][ :, :, :, 1, 1 ] = vTilde_pset2_new.T * damping + (1 - damping) * a['chfhat'][ :, :, :, 1, 1 ]
    a['chfhat'][ :, :, :, 0, 1 ] = vTilde_cov_new.T * damping + (1 - damping) * a['chfhat'][ :, :, :, 0, 1 ]
    a['chfhat'][ :, :, :, 1, 0 ] = vTilde_cov_new.T * damping + (1 - damping) * a['chfhat'][ :, :, :, 1, 0 ]
    a['dhfhat'][ :, :, :, 0 ] = mTilde_pset1_new.T * damping + (1 - damping) * a['dhfhat'][ :, :, :, 0 ]
    a['dhfhat'][ :, :, :, 1 ] = mTilde_pset2_new.T * damping + (1 - damping) * a['dhfhat'][ :, :, :, 1 ]

    return a


def updateFactors_fast_daniel_no_constraints_pareto_set(a, damping, minimize=True):
    # used to switch between minimizing and maximizing
    sgn = -1.0 if minimize else 1.0

    # We update the h factors
    all_tasks = a['objs']
    all_constraints = a['cons']
    n_obs = a['n_obs']
    n_pset = a['n_pset']
    n_total = a['n_total']
    q = a['q']
    c = a['c']

    alpha = np.zeros(a['q'])
    s = np.zeros(a['q'])
    ratio_cons = np.zeros(c)

    # First we update the factors corresponding to the observed data

    # We compute an "old" distribution

    # Data structures for objective npset nobs cavities (a, b).

    m_pset = np.zeros((q, n_pset, n_obs))
    m_obs = np.zeros((q, n_pset, n_obs))
    v_pset = np.zeros((q, n_pset, n_obs))
    v_obs = np.zeros((q, n_pset, n_obs))
    v_cov = np.zeros((q, n_pset, n_obs))

    # Data structures for constraint npset nobs cavities (c_a, c_b).

    c_m = np.zeros((c, n_pset, n_obs))
    c_v = np.zeros((c, n_pset, n_obs))

    # We do the update of the external factors.

    c_m_external = np.zeros((c, n_pset))
    c_v_external = np.zeros((c, n_pset))
    alpha_external = np.zeros(c)

    # First we update the external (easy) factors that only affect the constraints

    n_task = 0
    for cons in all_constraints:
        c_m_external[ n_task, : ] = a['m_cons'][ cons ][ 0 : n_pset ]
        c_v_external[ n_task, : ] = np.diag(a['V_cons'][ cons ])[ 0 : n_pset ]
        n_task += 1

    c_vTilde_external = a['ehfhat'][ :, : ].T
    c_mTilde_external = a['fhfhat'][ :, : ].T

    c_vOld_external = 1.0 / (1.0 / c_v_external - c_vTilde_external)
    c_mOld_external = c_vOld_external * (c_m_external / c_v_external - c_mTilde_external)

    if np.any(c_vOld_external < 0):
        raise npla.linalg.LinAlgError("Negative value in the sqrt!")

    alpha_external = c_mOld_external / np.sqrt(c_vOld_external)
    logZ = logcdf_robust(alpha_external)

    ratio = np.exp(sps.norm.logpdf(alpha_external) - logZ)
    dlogZdmfOld_external = ratio / np.sqrt(c_vOld_external)
    dlogZdVfOld_external = -0.5 * ratio * alpha_external * 1.0 / c_vOld_external

    mcNew_external = c_mOld_external + c_vOld_external * dlogZdmfOld_external
    vcNew_external = c_vOld_external - c_vOld_external * (dlogZdmfOld_external**2 - 2.0 * dlogZdVfOld_external) * c_vOld_external

    ehfhat_act = (1.0 / vcNew_external - 1.0 / c_vOld_external).T
    fhfhat_act = (mcNew_external / vcNew_external - c_mOld_external / c_vOld_external).T

    neg = np.where(ehfhat_act < 0)

    ehfhat_act[ neg ] = 0.0
    fhfhat_act[ neg ] = 0.0

    a['ehfhat'][ :, : ] = ehfhat_act * damping + (1 - damping) * a['ehfhat'][ :, : ]
    a['fhfhat'][ :, : ] = fhfhat_act * damping + (1 - damping) * a['fhfhat'][ :, : ]

    # Done!

    n_task = 0
    for obj in all_tasks:
        m_obs[ n_task, :, : ] = np.tile(a['m'][ obj ][ n_pset : n_total ], n_pset).reshape((n_pset, n_obs))
        m_pset[ n_task, :, : ] = np.tile(a['m'][ obj ][ 0 : n_pset ], n_obs).reshape((n_obs, n_pset)).T
        v_cov[ n_task, :, : ] = a['V'][ obj ][ 0 : n_pset, n_pset : n_total ]
        v_obs[ n_task, :, : ] = np.tile(np.diag(a['V'][ obj ])[ n_pset : n_total ], n_pset).reshape((n_pset, n_obs))
        v_pset[ n_task, :, : ] = np.tile(np.diag(a['V'][ obj ])[ 0 : n_pset ], n_obs).reshape((n_obs, n_pset)).T
        n_task += 1

    n_task = 0

    for cons in all_constraints:
        c_m[ n_task, :, : ] = a['m_cons'][ cons ][ n_pset : n_total ]
        c_v[ n_task, :, : ] = np.diag(a['V_cons'][ cons ])[ n_pset : n_total ]
        n_task += 1

    vTilde_obs = a['ahfhat'][ :, :, :, 0, 0 ].T
    vTilde_pset = a['ahfhat'][ :, :, :, 1, 1 ].T
    covTilde = a['ahfhat'][ :, :, :, 0, 1 ].T
    mTilde_obs = a['bhfhat'][ :, :, :, 0, ].T
    mTilde_pset = a['bhfhat'][ :, :, :, 1, ].T

    c_vTilde = a['a_c_hfhat'][ :, :, : ].T
    c_mTilde = a['b_c_hfhat'][ :, :, : ].T

    # Obtaining cavities.

    inv_v_obs, inv_v_pset, inv_v_cov = two_by_two_symmetric_matrix_inverse(v_obs, v_pset, v_cov)
    inv_c_v = 1.0 / c_v

    inv_vOld_obs = inv_v_obs - vTilde_obs
    inv_vOld_pset = inv_v_pset - vTilde_pset
    inv_vOld_cov =  inv_v_cov - covTilde
    inv_c_vOld = inv_c_v - c_vTilde

    vOld_obs, vOld_pset, vOld_cov = two_by_two_symmetric_matrix_inverse(inv_vOld_obs, inv_vOld_pset, inv_vOld_cov)
    c_vOld = 1.0 / inv_c_vOld

    mOld_obs, mOld_pset  = two_by_two_symmetric_matrix_product_vector(inv_v_obs, inv_v_pset, inv_v_cov, m_obs, m_pset)
    mOld_obs = mOld_obs - mTilde_obs
    mOld_pset = mOld_pset - mTilde_pset
    mOld_obs, mOld_pset  = two_by_two_symmetric_matrix_product_vector(vOld_obs, vOld_pset, vOld_cov, mOld_obs, mOld_pset)

    c_mOld = c_vOld * (c_m / c_v - c_mTilde)

    #Computing factors.

    s = vOld_pset + vOld_obs - 2 * vOld_cov
    s_cons = c_vOld

    if np.any(vOld_pset < 0):
        raise npla.linalg.LinAlgError("Negative variance in the sqrt!")

    if np.any(vOld_obs < 0):
        raise npla.linalg.LinAlgError("Negative variance in the sqrt!")

    if np.any(c_vOld < 0):
        raise npla.linalg.LinAlgError("Negative value in the sqrt!")

    alpha_cons = c_mOld / np.sqrt(c_vOld)

    scale = 1.0 - 1e-4
    while np.any(s / (vOld_pset + vOld_obs) < 1e-6):
        scale = scale**2
        s = vOld_pset + vOld_obs - 2 * vOld_cov * scale

    alpha = (mOld_obs - mOld_pset) / np.sqrt(s) * sgn

    log_phi = logcdf_robust(alpha)
    log_phi_cons = logcdf_robust(alpha_cons)

    logZ_orig = log_1_minus_exp_x(np.sum(log_phi, axis = 0))

    if np.any(np.logical_not(logZ_orig == -np.inf)):
        sel = (logZ_orig == -np.inf)
        logZ_orig[ sel ] = logcdf_robust(-np.min(alpha[ :, sel ], axis = 0))

    logZ_term1 = np.sum(log_phi_cons, axis = 0) + logZ_orig
    logZ_term2 = log_1_minus_exp_x(np.sum(log_phi_cons, axis = 0))

    if np.any(np.logical_not(logZ_term2 == -np.inf)):
        sel = (logZ_term2 == -np.inf)
        logZ_term2[ sel ] = logcdf_robust(-np.min(alpha_cons[ :, sel ], axis = 0))

    # TODO: This should be done robustly

    max_value = np.maximum(logZ_term1, logZ_term2)

    logZ = np.tile(np.log(np.exp(logZ_term1 - max_value) + np.exp(logZ_term2 - max_value)) + \
        max_value, q).reshape((n_pset, q, n_obs)).swapaxes(0, 1)
    logZ_cons = np.tile(np.log(np.exp(logZ_term1 - max_value) + np.exp(logZ_term2 - max_value)) + \
        max_value, c).reshape((n_pset, c, n_obs)).swapaxes(0, 1)

    log_phi_sum = np.tile(np.sum(log_phi, axis = 0), q).reshape((n_pset, q, n_obs)).swapaxes(0, 1)
    log_phi_sum_cons = np.tile(np.sum(log_phi_cons, axis = 0), q).reshape((n_pset, q, n_obs)).swapaxes(0, 1)

    ratio = - np.exp(sps.norm.logpdf(alpha) - logZ + log_phi_sum - logcdf_robust(alpha) + log_phi_sum_cons)

    logZ_orig_cons = np.tile(logZ_orig, c).reshape((n_pset, c, n_obs)).swapaxes(0, 1)
    log_phi_sum_cons = np.tile(np.sum(log_phi_cons, axis = 0), c).reshape((n_pset, c, n_obs)).swapaxes(0, 1)

    ratio_cons = np.exp(sps.norm.logpdf(alpha_cons) - logZ_cons + logZ_orig_cons + log_phi_sum_cons - logcdf_robust(alpha_cons)) - \
        np.exp(sps.norm.logpdf(alpha_cons) - logZ_cons + log_phi_sum_cons - logcdf_robust(alpha_cons))

    # Derivatives, non vector form.

    dlogZdmfOld_obs = ratio / np.sqrt(s) * sgn
    dlogZdmfOld_pset = ratio / np.sqrt(s) * -1.0 * sgn

    dlogZdVfOld_obs = -0.5 * ratio * alpha / s
    dlogZdVfOld_pset = -0.5 * ratio * alpha / s
    dlogZdVfOld_cov = -0.5 * ratio * alpha / s * -1.0

    dlogZdmcOld = ratio_cons / np.sqrt(s_cons)
    dlogZdVcOld = -0.5 * ratio_cons * alpha_cons / s_cons

    # The following lines compute the updates in parallel C = dmdm - 2 dv
    # First the first natural parameter

    c_11 = dlogZdmfOld_obs * dlogZdmfOld_obs - 2 * dlogZdVfOld_obs
    c_22 = dlogZdmfOld_pset * dlogZdmfOld_pset - 2 * dlogZdVfOld_pset
    c_12 = dlogZdmfOld_pset * dlogZdmfOld_obs - 2 * dlogZdVfOld_cov

    cp_11 = c_11 * vOld_obs + c_12 * vOld_cov
    cp_12 = c_11 * vOld_cov + c_12 * vOld_pset
    cp_21 = c_12 * vOld_obs + c_22 * vOld_cov
    cp_22 = c_12 * vOld_cov + c_22 * vOld_pset

    vNew_obs = vOld_obs - (vOld_obs * cp_11 + vOld_cov * cp_21)
    vNew_cov = vOld_cov - (vOld_obs * cp_12 + vOld_cov * cp_22)
    vNew_pset = vOld_pset - (vOld_cov * cp_12 + vOld_pset * cp_22)

    vNew_inv_obs, vNew_inv_pset, vNew_inv_cov = two_by_two_symmetric_matrix_inverse(vNew_obs, vNew_pset, vNew_cov)

    # This is the approx factor

    vTilde_obs_new = (vNew_inv_obs - inv_vOld_obs)
    vTilde_pset_new = (vNew_inv_pset - inv_vOld_pset)
    vTilde_cov_new = (vNew_inv_cov - inv_vOld_cov)

    v_1 = mOld_obs + vOld_obs * dlogZdmfOld_obs + vOld_cov * dlogZdmfOld_pset
    v_2 = mOld_pset + vOld_cov * dlogZdmfOld_obs + vOld_pset * dlogZdmfOld_pset

    # Now the second natural parameter = A~ (mOld + Vold dlogz_dm) + dlogz_dm

    mTilde_obs_new, mTilde_pset_new = two_by_two_symmetric_matrix_product_vector(vTilde_obs_new, vTilde_pset_new, vTilde_cov_new, v_1, v_2)
    mTilde_obs_new = mTilde_obs_new + dlogZdmfOld_obs
    mTilde_pset_new = mTilde_pset_new + dlogZdmfOld_pset

    mcNew = c_mOld + c_vOld * dlogZdmcOld
    vcNew = c_vOld - c_vOld * (dlogZdmcOld**2 - 2.0 * dlogZdVcOld) * c_vOld

    vTilde_cons = 1.0 / vcNew - 1.0 / c_vOld
    mTilde_cons = mcNew / vcNew - c_mOld / c_vOld

    finite = np.logical_and(np.logical_and(np.logical_and(np.logical_and(np.isfinite(vTilde_obs_new), np.isfinite(vTilde_pset_new)), \
        np.isfinite(vTilde_cov_new)), np.isfinite(mTilde_obs_new)), np.isfinite(mTilde_pset_new))

    c_finite = np.logical_and(np.isfinite(vTilde_cons), np.isfinite(mTilde_cons))

    neg1 = np.where(vTilde_obs_new < 0)
    neg2 = np.where(vTilde_pset_new < 0)
    c_neg = np.where(vTilde_cons < 0)

    vTilde_obs_new[ neg1 ] = 0.0
    vTilde_obs_new[ neg2 ] = 0.0
    vTilde_pset_new[ neg1 ] = 0.0
    vTilde_pset_new[ neg2 ] = 0.0
    vTilde_cov_new[ neg1 ] = 0.0
    vTilde_cov_new[ neg2 ] = 0.0
    mTilde_obs_new[ neg1 ] = 0.0
    mTilde_obs_new[ neg2 ] = 0.0
    mTilde_pset_new[ neg1 ] = 0.0
    mTilde_pset_new[ neg2 ] = 0.0
    vTilde_cons[ c_neg ] = 0.0
    mTilde_cons[ c_neg ] = 0.0

    # We do the actual update

    a_c_hfHatNew = vTilde_cons
    b_c_hfHatNew = mTilde_cons

    a['ahfhat'][ :, :, :, 0, 0 ] = vTilde_obs_new.T * damping + (1 - damping) * a['ahfhat'][ :, :, :, 0, 0 ]
    a['ahfhat'][ :, :, :, 1, 1 ] = vTilde_pset_new.T * damping + (1 - damping) * a['ahfhat'][ :, :, :, 1, 1 ]
    a['ahfhat'][ :, :, :, 0, 1 ] = vTilde_cov_new.T * damping + (1 - damping) * a['ahfhat'][ :, :, :, 0, 1 ]
    a['ahfhat'][ :, :, :, 1, 0 ] = vTilde_cov_new.T * damping + (1 - damping) * a['ahfhat'][ :, :, :, 1, 0 ]
    a['bhfhat'][ :, :, :, 0 ] = mTilde_obs_new.T * damping + (1 - damping) * a['bhfhat'][ :, :, :, 0 ]
    a['bhfhat'][ :, :, :, 1 ] = mTilde_pset_new.T * damping + (1 - damping) * a['bhfhat'][ :, :, :, 1 ]
    a['a_c_hfhat'][ :, :, : ] = a_c_hfHatNew.T * damping + (1 - damping) * a['a_c_hfhat'][ :, :, : ]
    a['b_c_hfhat'][ :, :, : ] = b_c_hfHatNew.T * damping + (1 - damping) * a['b_c_hfhat'][ :, :, : ]

    # Second we update the factors corresponding to the pareto set

    # We compute an "old" distribution

    m_pset1 = np.zeros((q, n_pset, n_pset))
    m_pset2 = np.zeros((q, n_pset, n_pset))
    v_pset1 = np.zeros((q, n_pset, n_pset))
    v_pset2 = np.zeros((q, n_pset, n_pset))
    v_cov = np.zeros((q, n_pset, n_pset))

    c_m_pset = np.zeros((c, n_pset, n_pset))
    c_v_pset = np.zeros((c, n_pset, n_pset))

    n_task = 0
    for obj in all_tasks:
        m_pset1[ n_task, :, : ] = np.tile(a['m'][ obj ][ 0 : n_pset ], n_pset).reshape((n_pset, n_pset))
        m_pset2[ n_task, :, : ] = np.tile(a['m'][ obj ][ 0 : n_pset ], n_pset).reshape((n_pset, n_pset)).T
        v_cov[ n_task, :, : ] = a['V'][ obj ][ 0 : n_pset, 0 : n_pset ]
        v_cov[ n_task, :, : ] = v_cov[ n_task, :, : ] - np.diag(np.diag(v_cov[ n_task, :, : ]))
        v_pset1[ n_task, :, : ] = np.tile(np.diag(a['V'][ obj ])[ 0 : n_pset ], n_pset).reshape((n_pset, n_pset))
        v_pset2[ n_task, :, : ] = np.tile(np.diag(a['V'][ obj ])[ 0 : n_pset ], n_pset).reshape((n_pset, n_pset)).T
        n_task += 1

    n_task = 0
    for cons in all_constraints:
        c_m_pset[ n_task, :, : ] = a['m_cons'][ cons ][ 0 : n_pset ]
        c_v_pset[ n_task, :, : ] = np.diag(a['V_cons'][ cons ])[0 : n_pset]
        n_task += 1

    vTilde_pset1 = a['chfhat'][ :, :, :, 0, 0 ].T
    vTilde_pset2 = a['chfhat'][ :, :, :, 1, 1 ].T
    covTilde = a['chfhat'][ :, :, :, 0, 1 ].T
    mTilde_pset1 = a['dhfhat'][ :, :, :, 0 ].T
    mTilde_pset2 = a['dhfhat'][ :, :, :, 1 ].T

    c_vTilde_pset = a['c_c_hfhat'][ :, :, : ].T
    c_mTilde_pset = a['d_c_hfhat'][ :, :, : ].T

    inv_v_pset1, inv_v_pset2, inv_v_cov = two_by_two_symmetric_matrix_inverse(v_pset1, v_pset2, v_cov)

    inv_vOld_pset1 = inv_v_pset1 - vTilde_pset1
    inv_vOld_pset2 = inv_v_pset2 - vTilde_pset2
    inv_vOld_cov =  inv_v_cov - covTilde

    vOld_pset1, vOld_pset2, vOld_cov = two_by_two_symmetric_matrix_inverse(inv_vOld_pset1, inv_vOld_pset2, inv_vOld_cov)

    mOld_pset1, mOld_pset2  = two_by_two_symmetric_matrix_product_vector(inv_v_pset1, inv_v_pset2, inv_v_cov, m_pset1, m_pset2)
    mOld_pset1 = mOld_pset1 - mTilde_pset1
    mOld_pset2 = mOld_pset2 - mTilde_pset2
    mOld_pset1, mOld_pset2  = two_by_two_symmetric_matrix_product_vector(vOld_pset1, vOld_pset2, vOld_cov, mOld_pset1, mOld_pset2)

    s = vOld_pset1 + vOld_pset2 - 2 * vOld_cov

    if np.any(vOld_pset1  < 0):
        raise npla.linalg.LinAlgError("Negative value in the sqrt!")

    if np.any(vOld_pset2  < 0):
        raise npla.linalg.LinAlgError("Negative value in the sqrt!")

    scale = 1.0 - 1e-4
    while np.any(s / (vOld_pset1 + vOld_pset2) < 1e-6):
        print "Reducing scale to guarantee positivity!"
        scale = scale**2
        s = vOld_pset1 + vOld_pset2 - 2 * vOld_cov * scale

    alpha = (mOld_pset1 - mOld_pset2) / np.sqrt(s) * sgn

    log_phi = logcdf_robust(alpha)
    logZ = log_1_minus_exp_x(np.sum(log_phi, axis = 0))

    if np.any(np.logical_not(logZ == -np.inf)):
        sel = (logZ == -np.inf)
        logZ[ sel ] = logcdf_robust(-np.min(alpha[ :, sel ], axis = 0))

    log_phi_sum = np.tile(np.sum(log_phi, axis = 0), q).reshape((n_pset, q, n_pset)).swapaxes(0, 1)

    ratio = - np.exp(sps.norm.logpdf(alpha) - logZ + log_phi_sum - logcdf_robust(alpha))

    # Derivatives, non vector form.

    dlogZdmfOld_pset1 = ratio / np.sqrt(s) * sgn
    dlogZdmfOld_pset2 = ratio / np.sqrt(s) * -1.0 * sgn

    dlogZdVfOld_pset1 = -0.5 * ratio * alpha / s
    dlogZdVfOld_pset2 = -0.5 * ratio * alpha / s
    dlogZdVfOld_cov = -0.5 * ratio * alpha / s * -1.0

    # The following lines compute the updates in parallel C = dmdm - 2 dv
    # First the first natural parameter

    c_11 = dlogZdmfOld_pset1 * dlogZdmfOld_pset1 - 2 * dlogZdVfOld_pset1
    c_22 = dlogZdmfOld_pset2 * dlogZdmfOld_pset2 - 2 * dlogZdVfOld_pset2
    c_12 = dlogZdmfOld_pset2 * dlogZdmfOld_pset1 - 2 * dlogZdVfOld_cov

    cp_11 = c_11 * vOld_pset1 + c_12 * vOld_cov
    cp_12 = c_11 * vOld_cov + c_12 * vOld_pset2
    cp_21 = c_12 * vOld_pset1 + c_22 * vOld_cov
    cp_22 = c_12 * vOld_cov + c_22 * vOld_pset2

    vNew_pset1 = vOld_pset1 - (vOld_pset1 * cp_11 + vOld_cov * cp_21)
    vNew_pset2 = vOld_pset2 - (vOld_cov * cp_12 + vOld_pset2 * cp_22)
    vNew_cov = vOld_cov - (vOld_pset1 * cp_12 + vOld_cov * cp_22)

    vNew_inv_pset1, vNew_inv_pset2, vNew_inv_cov = two_by_two_symmetric_matrix_inverse(vNew_pset1, vNew_pset2, vNew_cov)

    # This is the approx factor

    vTilde_pset1_new = (vNew_inv_pset1 - inv_vOld_pset1)
    vTilde_pset2_new = (vNew_inv_pset2 - inv_vOld_pset2)
    vTilde_cov_new = (vNew_inv_cov - inv_vOld_cov)

    v_1 = mOld_pset1 + vOld_pset1 * dlogZdmfOld_pset1 + vOld_cov * dlogZdmfOld_pset2
    v_2 = mOld_pset2 + vOld_cov * dlogZdmfOld_pset1 + vOld_pset2 * dlogZdmfOld_pset2

    # Now the second natural parameter = A~ (mOld + Vold dlogz_dm) + dlogz_dm

    mTilde_pset1_new, mTilde_pset2_new = two_by_two_symmetric_matrix_product_vector(vTilde_pset1_new, vTilde_pset2_new, vTilde_cov_new, v_1, v_2)
    mTilde_pset1_new = mTilde_pset1_new + dlogZdmfOld_pset1
    mTilde_pset2_new = mTilde_pset2_new + dlogZdmfOld_pset2

    n_task = 0
    for obj in all_tasks:
        vTilde_pset1_new[ n_task, :, : ] -= np.diag(np.diag(vTilde_pset1_new[ n_task, :, :, ]))
        vTilde_pset2_new[ n_task, :, : ] -= np.diag(np.diag(vTilde_pset2_new[ n_task, :, :, ]))
        vTilde_cov_new[ n_task, :, : ] -= np.diag(np.diag(vTilde_cov_new[ n_task, :, : ]))
        mTilde_pset1_new[ n_task, :, : ] -= np.diag(np.diag(mTilde_pset1_new[ n_task, :, : ]))
        mTilde_pset2_new[ n_task, :, : ] -= np.diag(np.diag(mTilde_pset2_new[ n_task, :, : ]))
        n_task += 1

    finite = np.logical_and(np.logical_and(np.logical_and(np.logical_and(np.isfinite(vTilde_pset1_new), np.isfinite(vTilde_pset2_new)), \
        np.isfinite(vTilde_cov_new)), np.isfinite(mTilde_pset1_new)), np.isfinite(mTilde_pset2_new))

    neg1 = np.where(vTilde_pset1_new < 0)
    neg2 = np.where(vTilde_pset2_new < 0)

    vTilde_pset1_new[ neg1 ] = 0.0
    vTilde_pset1_new[ neg2 ] = 0.0
    vTilde_pset2_new[ neg1 ] = 0.0
    vTilde_pset2_new[ neg2 ] = 0.0
    vTilde_cov_new[ neg1 ] = 0.0
    vTilde_cov_new[ neg2 ] = 0.0
    mTilde_pset1_new[ neg1 ] = 0.0
    mTilde_pset1_new[ neg2 ] = 0.0
    mTilde_pset2_new[ neg1 ] = 0.0
    mTilde_pset2_new[ neg2 ] = 0.0

    # We do the actual update

    #i not equal to j condition.

    a['chfhat'][ :, :, :, 0, 0 ] = vTilde_pset1_new.T * damping + (1 - damping) * a['chfhat'][ :, :, :, 0, 0 ]
    a['chfhat'][ :, :, :, 1, 1 ] = vTilde_pset2_new.T * damping + (1 - damping) * a['chfhat'][ :, :, :, 1, 1 ]
    a['chfhat'][ :, :, :, 0, 1 ] = vTilde_cov_new.T * damping + (1 - damping) * a['chfhat'][ :, :, :, 0, 1 ]
    a['chfhat'][ :, :, :, 1, 0 ] = vTilde_cov_new.T * damping + (1 - damping) * a['chfhat'][ :, :, :, 1, 0 ]
    a['dhfhat'][ :, :, :, 0 ] = mTilde_pset1_new.T * damping + (1 - damping) * a['dhfhat'][ :, :, :, 0 ]
    a['dhfhat'][ :, :, :, 1 ] = mTilde_pset2_new.T * damping + (1 - damping) * a['dhfhat'][ :, :, :, 1 ]

    return a


def updateFactors_fast_daniel(a, damping, minimize=True):
    # used to switch between minimizing and maximizing
    sgn = -1.0 if minimize else 1.0

    # We update the h factors
    all_tasks = a['objs']
    all_constraints = a['cons']
    n_obs = a['n_obs']
    n_pset = a['n_pset']
    n_total = a['n_total']
    q = a['q']
    c = a['c']

    alpha = np.zeros(a['q'])
    s = np.zeros(a['q'])
    ratio_cons = np.zeros(c)

    # First we update the factors corresponding to the observed data

    # We compute an "old" distribution

    # Data structures for objective npset nobs cavities (a, b).

    m_pset = np.zeros((q, n_pset, n_obs))
    m_obs = np.zeros((q, n_pset, n_obs))
    v_pset = np.zeros((q, n_pset, n_obs))
    v_obs = np.zeros((q, n_pset, n_obs))
    v_cov = np.zeros((q, n_pset, n_obs))

    # Data structures for constraint npset nobs cavities (c_a, c_b).

    c_m = np.zeros((c, n_pset, n_obs))
    c_v = np.zeros((c, n_pset, n_obs))

    # We do the update of the external factors.

    c_m_external = np.zeros((c, n_pset))
    c_v_external = np.zeros((c, n_pset))
    alpha_external = np.zeros(c)

    # First we update the external (easy) factors that only affect the constraints

    n_task = 0
    for cons in all_constraints:
        c_m_external[ n_task, : ] = a['m_cons'][ cons ][ 0 : n_pset ]
        c_v_external[ n_task, : ] = np.diag(a['V_cons'][ cons ])[ 0 : n_pset ]
        n_task += 1

    c_vTilde_external = a['ehfhat'][ :, : ].T
    c_mTilde_external = a['fhfhat'][ :, : ].T

    c_vOld_external = 1.0 / (1.0 / c_v_external - c_vTilde_external)
    c_mOld_external = c_vOld_external * (c_m_external / c_v_external - c_mTilde_external)

    if np.any(c_vOld_external < 0):
        raise npla.linalg.LinAlgError("Negative value in the sqrt!")

    alpha_external = c_mOld_external / np.sqrt(c_vOld_external)
    logZ = logcdf_robust(alpha_external)

    ratio = np.exp(sps.norm.logpdf(alpha_external) - logZ)
    dlogZdmfOld_external = ratio / np.sqrt(c_vOld_external)
    dlogZdVfOld_external = -0.5 * ratio * alpha_external * 1.0 / c_vOld_external

    mcNew_external = c_mOld_external + c_vOld_external * dlogZdmfOld_external
    vcNew_external = c_vOld_external - c_vOld_external * (dlogZdmfOld_external**2 - 2.0 * dlogZdVfOld_external) * c_vOld_external

    ehfhat_act = (1.0 / vcNew_external - 1.0 / c_vOld_external).T
    fhfhat_act = (mcNew_external / vcNew_external - c_mOld_external / c_vOld_external).T

    a['ehfhat'][ :, : ] = ehfhat_act * damping + (1 - damping) * a['ehfhat'][ :, : ]
    a['fhfhat'][ :, : ] = fhfhat_act * damping + (1 - damping) * a['fhfhat'][ :, : ]

    # Done!

    n_task = 0
    for obj in all_tasks:
        m_obs[ n_task, :, : ] = np.tile(a['m'][ obj ][ n_pset : n_total ], n_pset).reshape((n_pset, n_obs))
        m_pset[ n_task, :, : ] = np.tile(a['m'][ obj ][ 0 : n_pset ], n_obs).reshape((n_obs, n_pset)).T
        v_cov[ n_task, :, : ] = a['V'][ obj ][ 0 : n_pset, n_pset : n_total ]
        v_obs[ n_task, :, : ] = np.tile(np.diag(a['V'][ obj ])[ n_pset : n_total ], n_pset).reshape((n_pset, n_obs))
        v_pset[ n_task, :, : ] = np.tile(np.diag(a['V'][ obj ])[ 0 : n_pset ], n_obs).reshape((n_obs, n_pset)).T
        n_task += 1

    n_task = 0

    for cons in all_constraints:
        c_m[ n_task, :, : ] = a['m_cons'][ cons ][ n_pset : n_total ]
        c_v[ n_task, :, : ] = np.diag(a['V_cons'][ cons ])[ n_pset : n_total ]
        n_task += 1

    vTilde_obs = a['ahfhat'][ :, :, :, 0, 0 ].T
    vTilde_pset = a['ahfhat'][ :, :, :, 1, 1 ].T
    covTilde = a['ahfhat'][ :, :, :, 0, 1 ].T
    mTilde_obs = a['bhfhat'][ :, :, :, 0, ].T
    mTilde_pset = a['bhfhat'][ :, :, :, 1, ].T

    c_vTilde = a['a_c_hfhat'][ :, :, : ].T
    c_mTilde = a['b_c_hfhat'][ :, :, : ].T

    # Obtaining cavities.

    inv_v_obs, inv_v_pset, inv_v_cov = two_by_two_symmetric_matrix_inverse(v_obs, v_pset, v_cov)
    inv_c_v = 1.0 / c_v

    inv_vOld_obs = inv_v_obs - vTilde_obs
    inv_vOld_pset = inv_v_pset - vTilde_pset
    inv_vOld_cov =  inv_v_cov - covTilde
    inv_c_vOld = inv_c_v - c_vTilde

    vOld_obs, vOld_pset, vOld_cov = two_by_two_symmetric_matrix_inverse(inv_vOld_obs, inv_vOld_pset, inv_vOld_cov)
    c_vOld = 1.0 / inv_c_vOld

    mOld_obs, mOld_pset  = two_by_two_symmetric_matrix_product_vector(inv_v_obs, inv_v_pset, inv_v_cov, m_obs, m_pset)
    mOld_obs = mOld_obs - mTilde_obs
    mOld_pset = mOld_pset - mTilde_pset
    mOld_obs, mOld_pset  = two_by_two_symmetric_matrix_product_vector(vOld_obs, vOld_pset, vOld_cov, mOld_obs, mOld_pset)

    c_mOld = c_vOld * (c_m / c_v - c_mTilde)

    #Computing factors.

    s = vOld_pset + vOld_obs - 2 * vOld_cov
    s_cons = c_vOld

    if np.any(vOld_pset < 0):
        raise npla.linalg.LinAlgError("Negative variance in the sqrt!")

    if np.any(vOld_obs < 0):
        raise npla.linalg.LinAlgError("Negative variance in the sqrt!")

    if np.any(c_vOld < 0):
        raise npla.linalg.LinAlgError("Negative value in the sqrt!")

    alpha_cons = c_mOld / np.sqrt(c_vOld)

    scale = 1.0 - 1e-4
    while np.any(s / (vOld_pset + vOld_obs) < 1e-6):
        print "Reducing scale to guarantee positivity!"
        scale = scale**2
        s = vOld_pset + vOld_obs - 2 * vOld_cov * scale

    alpha = (mOld_obs - mOld_pset) / np.sqrt(s) * sgn

    log_phi = logcdf_robust(alpha)
    log_phi_cons = logcdf_robust(alpha_cons)

    logZ_orig = log_1_minus_exp_x(np.sum(log_phi, axis = 0))

    logZ_term1 = np.sum(log_phi_cons, axis = 0) + logZ_orig
    logZ_term2 = log_1_minus_exp_x(np.sum(log_phi_cons, axis = 0))

    # TODO: This should be done robustly

    logZ = np.tile(np.log(np.exp(logZ_term1) + np.exp(logZ_term2)), q).reshape((n_pset, q, n_obs)).swapaxes(0, 1)
    logZ_cons = np.tile(np.log(np.exp(logZ_term1) + np.exp(logZ_term2)), c).reshape((n_pset, c, n_obs)).swapaxes(0, 1)

    log_phi_sum = np.tile(np.sum(log_phi, axis = 0), q).reshape((n_pset, q, n_obs)).swapaxes(0, 1)
    log_phi_sum_cons = np.tile(np.sum(log_phi_cons, axis = 0), q).reshape((n_pset, q, n_obs)).swapaxes(0, 1)

    ratio = - np.exp(sps.norm.logpdf(alpha) - logZ + log_phi_sum - logcdf_robust(alpha) + log_phi_sum_cons)

    logZ_orig_cons = np.tile(logZ_orig, c).reshape((n_pset, c, n_obs)).swapaxes(0, 1)
    log_phi_sum_cons = np.tile(np.sum(log_phi_cons, axis = 0), c).reshape((n_pset, c, n_obs)).swapaxes(0, 1)

    ratio_cons = np.exp(sps.norm.logpdf(alpha_cons) - logZ_cons + logZ_orig_cons + log_phi_sum_cons - logcdf_robust(alpha_cons)) - \
        np.exp(sps.norm.logpdf(alpha_cons) - logZ_cons + log_phi_sum_cons - logcdf_robust(alpha_cons))

    # Derivatives, non vector form.

    dlogZdmfOld_obs = ratio / np.sqrt(s) * sgn
    dlogZdmfOld_pset = ratio / np.sqrt(s) * -1.0 * sgn

    dlogZdVfOld_obs = -0.5 * ratio * alpha / s
    dlogZdVfOld_pset = -0.5 * ratio * alpha / s
    dlogZdVfOld_cov = -0.5 * ratio * alpha / s * -1.0

    dlogZdmcOld = ratio_cons / np.sqrt(s_cons)
    dlogZdVcOld = -0.5 * ratio_cons * alpha_cons / s_cons

    # The following lines compute the updates in parallel C = dmdm - 2 dv
    # First the first natural parameter

    c_11 = dlogZdmfOld_obs * dlogZdmfOld_obs - 2 * dlogZdVfOld_obs
    c_22 = dlogZdmfOld_pset * dlogZdmfOld_pset - 2 * dlogZdVfOld_pset
    c_12 = dlogZdmfOld_pset * dlogZdmfOld_obs - 2 * dlogZdVfOld_cov

    cp_11 = c_11 * vOld_obs + c_12 * vOld_cov
    cp_12 = c_11 * vOld_cov + c_12 * vOld_pset
    cp_21 = c_12 * vOld_obs + c_22 * vOld_cov
    cp_22 = c_12 * vOld_cov + c_22 * vOld_pset

    vNew_obs = vOld_obs - (vOld_obs * cp_11 + vOld_cov * cp_21)
    vNew_cov = vOld_cov - (vOld_obs * cp_12 + vOld_cov * cp_22)
    vNew_pset = vOld_pset - (vOld_cov * cp_12 + vOld_pset * cp_22)

    vNew_inv_obs, vNew_inv_pset, vNew_inv_cov = two_by_two_symmetric_matrix_inverse(vNew_obs, vNew_pset, vNew_cov)

    # This is the approx factor

    vTilde_obs_new = (vNew_inv_obs - inv_vOld_obs)
    vTilde_pset_new = (vNew_inv_pset - inv_vOld_pset)
    vTilde_cov_new = (vNew_inv_cov - inv_vOld_cov)

    v_1 = mOld_obs + vOld_obs * dlogZdmfOld_obs + vOld_cov * dlogZdmfOld_pset
    v_2 = mOld_pset + vOld_cov * dlogZdmfOld_obs + vOld_pset * dlogZdmfOld_pset

    # Now the second natural parameter = A~ (mOld + Vold dlogz_dm) + dlogz_dm

    mTilde_obs_new, mTilde_pset_new = two_by_two_symmetric_matrix_product_vector(vTilde_obs_new, vTilde_pset_new, vTilde_cov_new, v_1, v_2)
    mTilde_obs_new = mTilde_obs_new + dlogZdmfOld_obs
    mTilde_pset_new = mTilde_pset_new + dlogZdmfOld_pset

    mcNew = c_mOld + c_vOld * dlogZdmcOld
    vcNew = c_vOld - c_vOld * (dlogZdmcOld**2 - 2.0 * dlogZdVcOld) * c_vOld

    vTilde_cons = 1.0 / vcNew - 1.0 / c_vOld
    mTilde_cons = mcNew / vcNew - c_mOld / c_vOld

    finite = np.logical_and(np.logical_and(np.logical_and(np.logical_and(np.isfinite(vTilde_obs_new), np.isfinite(vTilde_pset_new)), \
        np.isfinite(vTilde_cov_new)), np.isfinite(mTilde_obs_new)), np.isfinite(mTilde_pset_new))

    c_finite = np.logical_and(np.isfinite(vTilde_cons), np.isfinite(mTilde_cons))

    neg1 = np.where(np.logical_or(vTilde_obs_new < 0, np.logical_not(finite)))
    neg2 = np.where(np.logical_or(vTilde_pset_new < 0, np.logical_not(finite)))
    c_neg = np.where(np.logical_or(vTilde_cons < 0, np.logical_not(c_finite)))

    vTilde_obs_new[ neg1 ] = 0.0
    vTilde_obs_new[ neg2 ] = 0.0
    vTilde_pset_new[ neg1 ] = 0.0
    vTilde_pset_new[ neg2 ] = 0.0
    vTilde_cov_new[ neg1 ] = 0.0
    vTilde_cov_new[ neg2 ] = 0.0
    mTilde_obs_new[ neg1 ] = 0.0
    mTilde_obs_new[ neg2 ] = 0.0
    mTilde_pset_new[ neg1 ] = 0.0
    mTilde_pset_new[ neg2 ] = 0.0
    vTilde_cons[ c_neg ] = 0.0
    mTilde_cons[ c_neg ] = 0.0

    # We do the actual update

    a_c_hfHatNew = vTilde_cons
    b_c_hfHatNew = mTilde_cons

    a['ahfhat'][ :, :, :, 0, 0 ] = vTilde_obs_new.T * damping + (1 - damping) * a['ahfhat'][ :, :, :, 0, 0 ]
    a['ahfhat'][ :, :, :, 1, 1 ] = vTilde_pset_new.T * damping + (1 - damping) * a['ahfhat'][ :, :, :, 1, 1 ]
    a['ahfhat'][ :, :, :, 0, 1 ] = vTilde_cov_new.T * damping + (1 - damping) * a['ahfhat'][ :, :, :, 0, 1 ]
    a['ahfhat'][ :, :, :, 1, 0 ] = vTilde_cov_new.T * damping + (1 - damping) * a['ahfhat'][ :, :, :, 1, 0 ]
    a['bhfhat'][ :, :, :, 0 ] = mTilde_obs_new.T * damping + (1 - damping) * a['bhfhat'][ :, :, :, 0 ]
    a['bhfhat'][ :, :, :, 1 ] = mTilde_pset_new.T * damping + (1 - damping) * a['bhfhat'][ :, :, :, 1 ]
    a['a_c_hfhat'][ :, :, : ] = a_c_hfHatNew.T * damping + (1 - damping) * a['a_c_hfhat'][ :, :, : ]
    a['b_c_hfhat'][ :, :, : ] = b_c_hfHatNew.T * damping + (1 - damping) * a['b_c_hfhat'][ :, :, : ]

    # Second we update the factors corresponding to the pareto set

    # We compute an "old" distribution

    m_pset1 = np.zeros((q, n_pset, n_pset))
    m_pset2 = np.zeros((q, n_pset, n_pset))
    v_pset1 = np.zeros((q, n_pset, n_pset))
    v_pset2 = np.zeros((q, n_pset, n_pset))
    v_cov = np.zeros((q, n_pset, n_pset))

    c_m_pset = np.zeros((c, n_pset, n_pset))
    c_v_pset = np.zeros((c, n_pset, n_pset))

    n_task = 0
    for obj in all_tasks:
        m_pset1[ n_task, :, : ] = np.tile(a['m'][ obj ][ 0 : n_pset ], n_pset).reshape((n_pset, n_pset))
        m_pset2[ n_task, :, : ] = np.tile(a['m'][ obj ][ 0 : n_pset ], n_pset).reshape((n_pset, n_pset)).T
        v_cov[ n_task, :, : ] = a['V'][ obj ][ 0 : n_pset, 0 : n_pset ]
        v_cov[ n_task, :, : ] = v_cov[ n_task, :, : ] - np.diag(np.diag(v_cov[ n_task, :, : ]))
        v_pset1[ n_task, :, : ] = np.tile(np.diag(a['V'][ obj ])[ 0 : n_pset ], n_pset).reshape((n_pset, n_pset))
        v_pset2[ n_task, :, : ] = np.tile(np.diag(a['V'][ obj ])[ 0 : n_pset ], n_pset).reshape((n_pset, n_pset)).T
        n_task += 1

    n_task = 0
    for cons in all_constraints:
        c_m_pset[ n_task, :, : ] = a['m_cons'][ cons ][ 0 : n_pset ]
        c_v_pset[ n_task, :, : ] = np.diag(a['V_cons'][ cons ])[0 : n_pset]
        n_task += 1

    vTilde_pset1 = a['chfhat'][ :, :, :, 0, 0 ].T
    vTilde_pset2 = a['chfhat'][ :, :, :, 1, 1 ].T
    covTilde = a['chfhat'][ :, :, :, 0, 1 ].T
    mTilde_pset1 = a['dhfhat'][ :, :, :, 0 ].T
    mTilde_pset2 = a['dhfhat'][ :, :, :, 1 ].T

    c_vTilde_pset = a['c_c_hfhat'][ :, :, : ].T
    c_mTilde_pset = a['d_c_hfhat'][ :, :, : ].T

    inv_v_pset1, inv_v_pset2, inv_v_cov = two_by_two_symmetric_matrix_inverse(v_pset1, v_pset2, v_cov)

    inv_vOld_pset1 = inv_v_pset1 - vTilde_pset1
    inv_vOld_pset2 = inv_v_pset2 - vTilde_pset2
    inv_vOld_cov =  inv_v_cov - covTilde

    vOld_pset1, vOld_pset2, vOld_cov = two_by_two_symmetric_matrix_inverse(inv_vOld_pset1, inv_vOld_pset2, inv_vOld_cov)
    c_vOld_pset = 1.0 / (1.0 / c_v_pset - c_vTilde_pset)

    mOld_pset1, mOld_pset2  = two_by_two_symmetric_matrix_product_vector(inv_v_pset1, inv_v_pset2, inv_v_cov, m_pset1, m_pset2)
    mOld_pset1 = mOld_pset1 - mTilde_pset1
    mOld_pset2 = mOld_pset2 - mTilde_pset2
    mOld_pset1, mOld_pset2  = two_by_two_symmetric_matrix_product_vector(vOld_pset1, vOld_pset2, vOld_cov, mOld_pset1, mOld_pset2)

    c_mOld_pset = c_vOld_pset * (c_m_pset / c_v_pset - c_mTilde_pset)

    s = vOld_pset1 + vOld_pset2 - 2 * vOld_cov
    s_cons = c_vOld_pset

    if np.any(vOld_pset1  < 0):
        raise npla.linalg.LinAlgError("Negative value in the sqrt!")

    if np.any(vOld_pset2  < 0):
        raise npla.linalg.LinAlgError("Negative value in the sqrt!")

    if np.any(c_vOld_pset < 0):
        raise npla.linalg.LinAlgError("Negative value in the sqrt!")

    alpha_cons = c_mOld_pset / np.sqrt(c_vOld_pset)

    scale = 1.0 - 1e-4
    while np.any(s / (vOld_pset1 + vOld_pset2) < 1e-6):
        print "Reducing scale to guarantee positivity!"
        scale = scale**2
        s = vOld_pset1 + vOld_pset2 - 2 * vOld_cov * scale

    alpha = (mOld_pset1 - mOld_pset2) / np.sqrt(s) * sgn

    log_phi = logcdf_robust(alpha)
    log_phi_cons = logcdf_robust(alpha_cons)

    logZ_orig = log_1_minus_exp_x(np.sum(log_phi, axis = 0))

    logZ_term1 = np.sum(log_phi_cons, axis = 0) + logZ_orig
    logZ_term2 = log_1_minus_exp_x(np.sum(log_phi_cons, axis = 0))

    # TODO: This should be done robustly

    logZ = np.tile(np.log(np.exp(logZ_term1) + np.exp(logZ_term2)), q).reshape((n_pset, q, n_pset)).swapaxes(0, 1)
    logZ_cons = np.tile(np.log(np.exp(logZ_term1) + np.exp(logZ_term2)), c).reshape((n_pset, c, n_pset)).swapaxes(0, 1)

    log_phi_sum = np.tile(np.sum(log_phi, axis = 0), q).reshape((n_pset, q, n_pset)).swapaxes(0, 1)
    log_phi_sum_cons = np.tile(np.sum(log_phi_cons, axis = 0), q).reshape((n_pset, q, n_pset)).swapaxes(0, 1)

    ratio = - np.exp(sps.norm.logpdf(alpha) - logZ + log_phi_sum - logcdf_robust(alpha) + log_phi_sum_cons)

    logZ_orig_cons = np.tile(logZ_orig, c).reshape((n_pset, c, n_pset)).swapaxes(0, 1)
    log_phi_sum_cons = np.tile(np.sum(log_phi_cons, axis = 0), c).reshape((n_pset, c, n_pset)).swapaxes(0, 1)

    ratio_cons = np.exp(sps.norm.logpdf(alpha_cons) - logZ_cons + logZ_orig_cons + log_phi_sum_cons - logcdf_robust(alpha_cons)) - \
        np.exp(sps.norm.logpdf(alpha_cons) - logZ_cons + log_phi_sum_cons - logcdf_robust(alpha_cons))

    # Derivatives, non vector form.

    dlogZdmfOld_pset1 = ratio / np.sqrt(s) * sgn
    dlogZdmfOld_pset2 = ratio / np.sqrt(s) * -1.0 * sgn

    dlogZdVfOld_pset1 = -0.5 * ratio * alpha / s
    dlogZdVfOld_pset2 = -0.5 * ratio * alpha / s
    dlogZdVfOld_cov = -0.5 * ratio * alpha / s * -1.0

    dlogZdmcOld_pset = ratio_cons / np.sqrt(s_cons)
    dlogZdVcOld_pset = -0.5 * ratio_cons * alpha_cons / s_cons

    # The following lines compute the updates in parallel C = dmdm - 2 dv
    # First the first natural parameter

    c_11 = dlogZdmfOld_pset1 * dlogZdmfOld_pset1 - 2 * dlogZdVfOld_pset1
    c_22 = dlogZdmfOld_pset2 * dlogZdmfOld_pset2 - 2 * dlogZdVfOld_pset2
    c_12 = dlogZdmfOld_pset2 * dlogZdmfOld_pset1 - 2 * dlogZdVfOld_cov

    cp_11 = c_11 * vOld_pset1 + c_12 * vOld_cov
    cp_12 = c_11 * vOld_cov + c_12 * vOld_pset2
    cp_21 = c_12 * vOld_pset1 + c_22 * vOld_cov
    cp_22 = c_12 * vOld_cov + c_22 * vOld_pset2

    vNew_pset1 = vOld_pset1 - (vOld_pset1 * cp_11 + vOld_cov * cp_21)
    vNew_pset2 = vOld_pset2 - (vOld_cov * cp_12 + vOld_pset2 * cp_22)
    vNew_cov = vOld_cov - (vOld_pset1 * cp_12 + vOld_cov * cp_22)

    vNew_inv_pset1, vNew_inv_pset2, vNew_inv_cov = two_by_two_symmetric_matrix_inverse(vNew_pset1, vNew_pset2, vNew_cov)

    # This is the approx factor

    vTilde_pset1_new = (vNew_inv_pset1 - inv_vOld_pset1)
    vTilde_pset2_new = (vNew_inv_pset2 - inv_vOld_pset2)
    vTilde_cov_new = (vNew_inv_cov - inv_vOld_cov)

    v_1 = mOld_pset1 + vOld_pset1 * dlogZdmfOld_pset1 + vOld_cov * dlogZdmfOld_pset2
    v_2 = mOld_pset2 + vOld_cov * dlogZdmfOld_pset1 + vOld_pset2 * dlogZdmfOld_pset2

    # Now the second natural parameter = A~ (mOld + Vold dlogz_dm) + dlogz_dm

    mcNew_pset = c_mOld_pset + c_vOld_pset * dlogZdmcOld_pset
    vcNew_pset = c_vOld_pset - c_vOld_pset * (dlogZdmcOld_pset**2 - 2.0 * dlogZdVcOld_pset) * c_vOld_pset

    mTilde_pset1_new, mTilde_pset2_new = two_by_two_symmetric_matrix_product_vector(vTilde_pset1_new, vTilde_pset2_new, vTilde_cov_new, v_1, v_2)
    mTilde_pset1_new = mTilde_pset1_new + dlogZdmfOld_pset1
    mTilde_pset2_new = mTilde_pset2_new + dlogZdmfOld_pset2

    vTilde_cons_pset = 1.0 / vcNew_pset - 1.0 / c_vOld_pset
    mTilde_cons_pset = mcNew_pset / vcNew_pset - c_mOld_pset / c_vOld_pset

    n_task = 0
    for obj in all_tasks:
        vTilde_pset1_new[ n_task, :, : ] -= np.diag(np.diag(vTilde_pset1_new[ n_task, :, :, ]))
        vTilde_pset2_new[ n_task, :, : ] -= np.diag(np.diag(vTilde_pset2_new[ n_task, :, :, ]))
        vTilde_cov_new[ n_task, :, : ] -= np.diag(np.diag(vTilde_cov_new[ n_task, :, : ]))
        mTilde_pset1_new[ n_task, :, : ] -= np.diag(np.diag(mTilde_pset1_new[ n_task, :, : ]))
        mTilde_pset2_new[ n_task, :, : ] -= np.diag(np.diag(mTilde_pset2_new[ n_task, :, : ]))
        n_task += 1

    finite = np.logical_and(np.logical_and(np.logical_and(np.logical_and(np.isfinite(vTilde_pset1_new), np.isfinite(vTilde_pset2_new)), \
        np.isfinite(vTilde_cov_new)), np.isfinite(mTilde_pset1_new)), np.isfinite(mTilde_pset2_new))

    c_finite = np.logical_and(np.isfinite(vTilde_cons_pset),np.isfinite(mTilde_cons_pset))

    neg1 = np.where(np.logical_or(vTilde_pset1_new < 0, np.logical_not(finite)))
    neg2 = np.where(np.logical_or(vTilde_pset2_new < 0, np.logical_not(finite)))
    c_neg = np.where(np.logical_or(vTilde_cons_pset < 0, np.logical_not(c_finite)))

    vTilde_pset1_new[ neg1 ] = 0.0
    vTilde_pset1_new[ neg2 ] = 0.0
    vTilde_pset2_new[ neg1 ] = 0.0
    vTilde_pset2_new[ neg2 ] = 0.0
    vTilde_cov_new[ neg1 ] = 0.0
    vTilde_cov_new[ neg2 ] = 0.0
    mTilde_pset1_new[ neg1 ] = 0.0
    mTilde_pset1_new[ neg2 ] = 0.0
    mTilde_pset2_new[ neg1 ] = 0.0
    mTilde_pset2_new[ neg2 ] = 0.0
    vTilde_cons_pset[ c_neg ] = 0.0
    mTilde_cons_pset[ c_neg ] = 0.0

    # We do the actual update

    c_c_hfHatNew = vTilde_cons_pset
    d_c_hfHatNew = mTilde_cons_pset

    #i not equal to j condition.

    for i in range(0,n_pset,1):
        c_c_hfHatNew[:,i,i] = 0.0
        d_c_hfHatNew[:,i,i] = 0.0

    a['chfhat'][ :, :, :, 0, 0 ] = vTilde_pset1_new.T * damping + (1 - damping) * a['chfhat'][ :, :, :, 0, 0 ]
    a['chfhat'][ :, :, :, 1, 1 ] = vTilde_pset2_new.T * damping + (1 - damping) * a['chfhat'][ :, :, :, 1, 1 ]
    a['chfhat'][ :, :, :, 0, 1 ] = vTilde_cov_new.T * damping + (1 - damping) * a['chfhat'][ :, :, :, 0, 1 ]
    a['chfhat'][ :, :, :, 1, 0 ] = vTilde_cov_new.T * damping + (1 - damping) * a['chfhat'][ :, :, :, 1, 0 ]
    a['dhfhat'][ :, :, :, 0 ] = mTilde_pset1_new.T * damping + (1 - damping) * a['dhfhat'][ :, :, :, 0 ]
    a['dhfhat'][ :, :, :, 1 ] = mTilde_pset2_new.T * damping + (1 - damping) * a['dhfhat'][ :, :, :, 1 ]
    a['c_c_hfhat'][ :, :, : ] = c_c_hfHatNew.T * damping + (1 - damping) * a['c_c_hfhat'][ :, :, : ]
    a['d_c_hfhat'][ :, :, : ] = d_c_hfHatNew.T * damping + (1 - damping) * a['d_c_hfhat'][ :, :, : ]

    return a

def gp_prediction_given_chol_K(X, Xtest, chol_star, cholV, m, model, jitter):
# computes the predictive distributions. but the chol of the kernel matrix and the
# chol of the test matrix are already provided.

    Kstar = model.noiseless_kernel.cross_cov(X, Xtest)
    mf = np.dot(Kstar.T, spla.cho_solve((chol_star, False), m))
    aux = spla.cho_solve((chol_star, False), Kstar)
    # vf = model.params['amp2'].value * (1.0 + jitter) - \
    #     np.sum(spla.solve_triangular(chol_star.T, Kstar, lower=True)**2, axis=0) + \
    #     np.sum(np.dot(cholV, aux)**2, axis=0)
    vf = model.params['amp2'].value - \
        np.sum(spla.solve_triangular(chol_star.T, Kstar, lower=True)**2, axis=0) + \
        np.sum(np.dot(cholV, aux)**2, axis=0) + \
        jitter

    if np.any(vf < 0.0):
        raise Exception("Encountered negative variance: %f" % np.min(vf))

    return Kstar, mf, vf

# Method that approximates the predictive distribution at a particular location.

def predictEP_multiple_iter(obj_models, a, pareto_set, Xtest, damping = 1, n_iters = 5, no_negatives = True, minimize=True):

	# used to switch between minimizing and maximizing

	sgn = -1.0 if minimize else 1.0

	objs = a['objs']
	all_tasks = objs

	n_obs = a['n_obs']
	n_pset = a['n_pset']
	n_total = a['n_total']
	n_test = Xtest.shape[ 0 ]
	q = a['q']

	Kstar = dict()
	mf = dict()
	mP = dict()
	mPset = dict()
	vf = dict()
	vP = dict()
	cov = dict()
	vPset = dict()

	# This is used for the comutation of the variance of the predictive distribution

	ahfHatNew = dict()
	bhfHatNew = dict()

	mfOld = dict()
	VfOld = dict()
	ahfHatNew = dict()
	bhfHatNew = dict()

	for obj in all_tasks:
		mfOld[ obj ] = np.zeros((n_pset, 2))
		VfOld[ obj ] = np.zeros((n_pset, 2, 2))
		ahfHatNew[ obj ] = np.zeros((n_pset, 2, 2))
		bhfHatNew[ obj ] = np.zeros((n_pset, 2))

	# First data includes the pareto set. Then, the test point

	Xtest_ext = np.vstack((a['X'][ 0 : n_pset, : ], Xtest))

	for obj in all_tasks:

		# We compute the means and variances of each point (test and pareto set)

		Kstar[ obj ], mP[ obj ], vP[ obj ] = gp_prediction_given_chol_K(a['X'], Xtest_ext,
			a['cholKstarstar'][ obj ], a['cholV'][ obj ], a['m'][ obj ], all_tasks[ obj ], a['jitter'][obj])
		vf[ obj ] = vP[ obj ][ n_pset : (n_pset + n_test) ]
		vPset[ obj ] = vP[ obj ][ 0 : n_pset ]
		mPset[ obj ] = mP[ obj ][ 0 : n_pset ]
		mf[ obj ] = mP[ obj ][ n_pset : (n_pset + n_test) ]

		# Now we compute the covariances between the test data and the pareto set

		Kstarstar = obj_models[ obj ].noiseless_kernel.cross_cov(Xtest_ext[ 0 : n_pset, : ], Xtest_ext[ n_pset : (n_pset + n_test), : ])
		aux1 = spla.solve_triangular(a['cholKstarstar'][ obj ].T, Kstar[ obj ][ : , 0 : n_pset  ], lower=True)
		aux2 = spla.solve_triangular(a['cholKstarstar'][ obj ].T, Kstar[ obj ][ :, n_pset : (n_pset + n_test) ], lower=True)
		aux11 = np.dot(a['cholV'][ obj ], spla.solve_triangular(a['cholKstarstar'][ obj ], aux1, lower=False))
		aux12 = np.dot(a['cholV'][ obj ], spla.solve_triangular(a['cholKstarstar'][ obj ], aux2, lower=False))
		cov[ obj ] = Kstarstar - np.dot(aux1.transpose(), aux2) + np.dot(aux11.transpose(), aux12)

	# scale things for stability

#	for obj in all_tasks:
#		scale = (1.0 - 1e-4) * np.ones(cov[ obj ].shape)
#		vf_tmp = np.repeat(vf[ obj ], cov[ obj ].shape[ 0 ]).reshape(cov[ obj ].shape[ ::-1 ]).transpose()
#		vpset_tmp = np.repeat(vPset[ obj ], cov[ obj ].shape[ 1 ]).reshape(cov[ obj ].shape)
#		index = vf_tmp + vpset_tmp -  2.0 * scale * cov[ obj ] < 1e-10
#
#		while np.any(index):
#			scale[ index ] = scale[ index ]**2
#			index = vf_tmp + vpset_tmp -  2.0 * scale * cov[ obj ] < 1e-10
#
#   		cov[ obj ] = scale * cov[ obj ]

	# We update the predictive distribution to take into account that it has to be dominated by the paretoset
	# For this we use a single parallel update of the factors

	# We set the approximate factors to be uniform

	mTilde_pset = np.zeros((q, n_pset, n_test))
	mTilde_test = np.zeros((q, n_pset, n_test))
	vTilde_pset = np.zeros((q, n_pset, n_test))
	vTilde_test = np.zeros((q, n_pset, n_test))
	vTilde_cov = np.zeros((q, n_pset, n_test))

	# We compute a "new" distribution

	mOld_pset = np.zeros((q, n_pset, n_test))
	mOld_test = np.zeros((q, n_pset, n_test))
	vOld_pset = np.zeros((q, n_pset, n_test))
	vOld_test = np.zeros((q, n_pset, n_test))
	covOld = np.zeros((q, n_pset, n_test))

	mNew_pset = np.zeros((q, n_pset, n_test))
	mNew_test = np.zeros((q, n_pset, n_test))
	vNew_pset = np.zeros((q, n_pset, n_test))
	vNew_test = np.zeros((q, n_pset, n_test))
	vNew_cov = np.zeros((q, n_pset, n_test))
	covOrig = np.zeros((q, n_pset, n_test))

	vfNew = dict()
	mfNew = dict()

	n_task = 0
	for obj in all_tasks:
		mNew_pset[ n_task, :, : ] = np.repeat(mPset[ obj ], n_test).reshape(((n_pset, n_test)))
		mNew_test[ n_task, :, : ] = np.repeat(mf[ obj ], n_pset).reshape(((n_test, n_pset))).transpose()
		vNew_pset[ n_task, :, : ] = np.repeat(vPset[ obj ], n_test).reshape(((n_pset, n_test)))
		vNew_test[ n_task, :, : ] = np.repeat(vf[ obj ], n_pset).reshape(((n_test, n_pset))).transpose()
		vNew_cov[ n_task, :, : ] = cov[ obj ]
		covOrig[ n_task, :, : ] = cov[ obj ]
		n_task += 1

	# We compute the predictive distribution over the points in the pareto set

	vOld_full_pset = dict()

	for obj in all_tasks:
		Kstarstar = obj_models[ obj ].noiseless_kernel.cross_cov(a['X'][ 0 : n_pset, : ], a['X'][ 0 : n_pset, : ])
		Kstar = obj_models[ obj ].noiseless_kernel.cross_cov(a['X'], a['X'][ 0 : n_pset, : ])
		aux1 = spla.solve_triangular(a['cholKstarstar'][ obj ].T, Kstar, lower=True)
		aux2 = spla.solve_triangular(a['cholKstarstar'][ obj ].T, Kstar, lower=True)
		aux11 = np.dot(a['cholV'][ obj ], spla.solve_triangular(a['cholKstarstar'][ obj ], aux1, lower=False))
		aux12 = np.dot(a['cholV'][ obj ], spla.solve_triangular(a['cholKstarstar'][ obj ], aux2, lower=False))
		vOld_full_pset[ obj ] = Kstarstar - np.dot(aux1.transpose(), aux2) + np.dot(aux11.transpose(), aux12) + \
			np.eye(n_pset) * a['jitter'][obj]

	n_task = 0
	for obj in all_tasks:
		vfNew[ obj ] = np.zeros( n_test )
		mfNew[ obj ] = np.zeros( n_test )

	for k in range(n_iters):

		change = 0

		# We compute an old distribution by substracting the approximate factors

		det = vNew_test * vNew_pset - vNew_cov * vNew_cov
		vNew_inv_test = 1.0 / det * vNew_pset
		vNew_inv_pset = 1.0 / det * vNew_test
		vNew_inv_cov = 1.0 / det * - vNew_cov

		vOld_inv_test = vNew_inv_test - vTilde_test
		vOld_inv_pset = vNew_inv_pset - vTilde_pset
		vOld_inv_cov = vNew_inv_cov - vTilde_cov

		det = vOld_inv_test * vOld_inv_pset - vOld_inv_cov * vOld_inv_cov
		vOld_test = 1.0 / det * vOld_inv_pset
		vOld_pset = 1.0 / det * vOld_inv_test
		covOld = 1.0  / det * - vOld_inv_cov

		m_nat_old_test = vNew_inv_test * mNew_test + vNew_inv_cov * mNew_pset - mTilde_test
		m_nat_old_pset = vNew_inv_cov * mNew_test + vNew_inv_pset * mNew_pset - mTilde_pset

		mOld_test = vOld_test * m_nat_old_test + covOld * m_nat_old_pset
		mOld_pset = covOld * m_nat_old_test + vOld_pset * m_nat_old_pset

		# We comupte a new distribution

		s = vOld_pset + vOld_test - 2 * covOld
		alpha = (mOld_test - mOld_pset) / np.sqrt(s) * sgn

		if np.any(s < 0):
			raise npla.linalg.LinAlgError("Negative value in the sqrt!")

		log_phi = logcdf_robust(alpha)
       		logZ = np.repeat(log_1_minus_exp_x(np.sum(log_phi, axis = 0)).transpose(), q).reshape((n_test, n_pset, q)).transpose()
		log_phi_sum = np.repeat(np.sum(log_phi, axis = 0).transpose(), q).reshape((n_test, n_pset, q)).transpose()

		ratio = - np.exp(sps.norm.logpdf(alpha) - logZ + log_phi_sum - log_phi)

		dlogZdmfOld_test = ratio / np.sqrt(s) * sgn
		dlogZdmfOld_pset = ratio / np.sqrt(s) * sgn * -1.0

		dlogZdVfOld_test = -0.5 * ratio * alpha / s
		dlogZdVfOld_pset = -0.5 * ratio * alpha / s
		dlogZdVfOld_cov = -0.5 * ratio * alpha / s * -1.0

		# The following lines compute the updates in parallel C = dmdm - 2 dv
		# First the first natural parameter

		c_11 = dlogZdmfOld_test * dlogZdmfOld_test - 2 * dlogZdVfOld_test
		c_22 = dlogZdmfOld_pset * dlogZdmfOld_pset - 2 * dlogZdVfOld_pset
		c_12 = dlogZdmfOld_pset * dlogZdmfOld_test - 2 * dlogZdVfOld_cov

		cp_11 = c_11 * vOld_test + c_12 * covOld
		cp_12 = c_11 * covOld + c_12 * vOld_pset
		cp_21 = c_12 * vOld_test + c_22 * covOld
		cp_22 = c_12 * covOld + c_22 * vOld_pset

		vNew_test = vOld_test - (vOld_test * cp_11 + covOld * cp_21)
		vNew_cov = covOld - (vOld_test * cp_12 + covOld * cp_22)
		vNew_pset = vOld_pset - (covOld * cp_12 + vOld_pset * cp_22)

		det = vNew_test * vNew_pset - vNew_cov * vNew_cov
		vNew_inv_test = 1.0 / det * vNew_pset
		vNew_inv_pset = 1.0 / det * vNew_test
		vNew_inv_cov = 1.0 / det * - vNew_cov

		det = vOld_test * vOld_pset - covOld * covOld
		vOld_inv_test = 1.0 / det * vOld_pset
		vOld_inv_pset = 1.0 / det * vOld_test
		vOld_inv_cov = 1.0 / det * - covOld

		# This is the approx factor

		vTilde_test_new = (vNew_inv_test - vOld_inv_test)
		vTilde_pset_new = (vNew_inv_pset - vOld_inv_pset)
		vTilde_cov_new = (vNew_inv_cov - vOld_inv_cov)

		if no_negatives:
			neg = np.where(vTilde_test_new < 0)
			vTilde_test_new[ neg ] = 0
			vTilde_pset_new[ neg ] = 0
			vTilde_cov_new[ neg ] = 0

		# We avoid negative variances in the approximate factors. This avoids non PSD cov matrices

#		neg = np.where(vTilde_test < 0)
#		vTilde_test[ neg ] = 0
#		vTilde_pset[ neg ] = 0
#		vTilde_cov[ neg ] = 0

		# Now the second natural parameter = A~ (mOld + Vold dlogz_dm) + dlogz_dm

		v_1 = mOld_test + vOld_test * dlogZdmfOld_test + covOld * dlogZdmfOld_pset
		v_2 = mOld_pset + covOld * dlogZdmfOld_test + vOld_pset * dlogZdmfOld_pset

		mTilde_test_new = vTilde_test_new * v_1 + vTilde_cov_new * v_2 + dlogZdmfOld_test
		mTilde_pset_new = vTilde_cov_new * v_1 + vTilde_pset_new * v_2 + dlogZdmfOld_pset

		# We damp the updates

#		max_change = 0
#
#		max_change = np.max((max_change, np.max(np.abs(vTilde_test_new - vTilde_test))))
#		max_change = np.max((max_change, np.max(np.abs(vTilde_pset_new - vTilde_pset))))
#		max_change = np.max((max_change, np.max(np.abs(vTilde_cov_new - vTilde_cov))))
#		max_change = np.max((max_change, np.max(np.abs(mTilde_test_new - mTilde_test))))
#		max_change = np.max((max_change, np.max(np.abs(mTilde_pset_new - mTilde_pset))))

#		print(max_change)

		vTilde_test = vTilde_test_new * damping + (1 - damping) * vTilde_test
		vTilde_pset = vTilde_pset_new * damping + (1 - damping) * vTilde_pset
		vTilde_cov = vTilde_cov_new * damping + (1 - damping) * vTilde_cov
		mTilde_test = mTilde_test_new * damping + (1 - damping) * mTilde_test
		mTilde_pset = mTilde_pset_new * damping + (1 - damping) * mTilde_pset


		# After computing the first natural parameter of the approximate factors we recontruct the
		# predictive distribution. We do the actual computation of the predictive distribution

		# This is the most expensive part (the reconstruction of the posterior)

		n_task = 0
		for obj in all_tasks:

			A = vOld_full_pset[ obj ]
			Ainv = matrixInverse(vOld_full_pset[ obj ])

			for i in range(n_test):

				if ((i % np.ceil(n_test / 100)) == 0):
					sys.stdout.write(".")
					sys.stdout.flush()

				B = covOrig[ n_task, :, i ]
				C = covOrig[ n_task, :, i ].transpose()
				D = vf[ obj ][ i ]

				# We invert the matrix using block inversion

				Anew = Ainv + np.outer(np.dot(Ainv, B), np.dot(C, Ainv)) * 1.0 / (D - np.sum(C * np.dot(Ainv, B)))
				Dnew = 1.0 / (D - np.dot(np.dot(C, Ainv), B))
				Bnew = - np.dot(Ainv, B) * Dnew
				Cnew = - 1.0 / D * np.dot(C, Anew)

				# We add the contribution of the approximate factors

				V = np.vstack((np.hstack((Anew, Bnew.reshape((n_pset, 1)))), np.append(Cnew, Dnew).reshape((1, n_pset + 1))))
				m = np.dot(V, np.append(mPset[ obj ], mf[ obj ][ i ]))

				mnew = (m + np.append(mTilde_pset[ n_task, :, i ], np.sum(mTilde_test[ n_task, :, i ])))

				Anew = (Anew + np.diag(vTilde_pset[ n_task, :, i ]))
				Bnew = (Bnew + vTilde_cov[ n_task, :, i ])
				Cnew = (Cnew + vTilde_cov[ n_task, :, i ])
				Dnew = (Dnew + np.sum(vTilde_test[ n_task, : , i ]))

				# We perform the computation of D by inverting the V matrix after adding the params of the approx factors

				Anew_inv = matrixInverse(Anew)

				D = 1.0 / (Dnew - np.sum(Bnew * np.dot(Anew_inv, Cnew)))
				aux = np.outer(np.dot(Anew_inv, Bnew), np.dot(Cnew, Anew_inv))
				A = Anew_inv +  aux * 1.0 / (Dnew - np.sum(Cnew * np.dot(Anew_inv, Bnew)))
				B = - np.dot(Anew_inv, Bnew) * D
				C = - 1.0 / Dnew * np.dot(Cnew, A)

				V = np.vstack((np.hstack((A, B.reshape((n_pset, 1)))), np.append(C, D).reshape((1, n_pset + 1))))

				mean = np.dot(V, mnew)

				mNew_pset[ n_task, : , i ] = mean[ 0 : n_pset ]
				mNew_test[ n_task, : , i ] = mean[ n_pset ]
				vNew_pset[ n_task, : , i ] = np.diag(V)[ 0 : n_pset ]
				vNew_test[ n_task, : , i ] = D
				vNew_cov[ n_task, : , i ] = V[ n_pset, 0 : n_pset ]

				change = np.max((change, np.max(np.abs(vfNew[ obj ][ i ] - D))))
				change = np.max((change, np.max(np.abs(mfNew[ obj ][ i ] - mean[ n_pset ]))))

				vfNew[ obj ][ i ] = D
				mfNew[ obj ][ i ] = mean[ n_pset ]

			n_task += 1
			print ''

		print(change)

	for obj in all_tasks:
		if np.any(vfNew[ obj ] <= 0):
			raise Exception("vfnew is negative: %g at index %d" % (np.min(vfNew[ obj ]), np.argmin(vfNew[ obj ])))
		if np.any(np.isnan(vfNew[ obj ])):
			raise Exception("vfnew constrains nan")

	return {'mf': mfNew, 'vf':vfNew, 'mfo': mf, 'vfo': vf}

	# don't bother computing mf and mc since they are not used in the acquisition function
	# m = mean, v = var, f = objective, c = constraint


# Method that approximates the predictive distribution at a particular location.

def predictEP_unconditioned(obj_models, con_models, a, pareto_set, Xtest):

    # used to switch between minimizing and maximizing
    objs = a['objs']
    cons = a['cons']
    all_tasks = objs
    all_constraints = cons

    n_obs = a['n_obs']
    n_pset = a['n_pset']
    n_total = a['n_total']
    n_test = Xtest.shape[ 0 ]
    q = a['q']
    c = a['c']

    Kstar = dict()
    mf = dict()
    mP = dict()
    mPset = dict()
    vf = dict()
    vP = dict()
    cov = dict()
    vPset = dict()
    mc = dict()
    vc = dict()

    # This is used for the comutation of the variance of the predictive distribution

    ahfHatNew = dict()
    bhfHatNew = dict()
    c_ahfHatNew = dict()
    c_bhfHatNew = dict()

    mfOld = dict()
    VfOld = dict()

    mcOld = dict()
    VcOld = dict()

    for obj in all_tasks:
        mfOld[ obj ] = np.zeros((n_pset, 2))
        VfOld[ obj ] = np.zeros((n_pset, 2, 2))
        ahfHatNew[ obj ] = np.zeros((n_pset, 2, 2))
        bhfHatNew[ obj ] = np.zeros((n_pset, 2))

    for cons in all_constraints:
        mcOld[ cons ] = np.zeros((n_pset))
        VcOld[ cons ] = np.zeros((n_pset))
        c_ahfHatNew[ cons ] = np.zeros((n_pset))
        c_bhfHatNew[ cons ] = np.zeros((n_pset))

    # First data includes the pareto set. Then, the test point

    Xtest_ext = np.vstack((a['X'][ 0 : n_pset, : ], Xtest))

    for obj in all_tasks:

        # We compute the means and variances of each point (test and pareto set)

	Kstar[ obj ], mP[ obj ], vP[ obj ] = gp_prediction_given_chol_K(a['X'], Xtest_ext,
        	a['cholKstarstar'][ obj ], a['cholV'][ obj ], a['m'][ obj ], all_tasks[ obj ], a['jitter'][obj])
	vf[ obj ] = vP[ obj ][ n_pset : (n_pset + n_test) ]
	mf[ obj ] = mP[ obj ][ n_pset : (n_pset + n_test) ]

    for cons in all_constraints:

        # We compute the means and variances of each point (test and pareto set)

	Kstar[ cons ], mP[ cons ], vP[ cons ] = gp_prediction_given_chol_K(a['X'], Xtest_ext,
        	a['cholKstarstar_cons'][ cons ], a['cholV_cons'][ cons ], a['m_cons'][ cons ], all_constraints[ cons ], a['jitter'][cons])
	vc[ cons ] = vP[ cons ][ n_pset : (n_pset + n_test) ]
	mc[ cons ] = mP[ cons ][ n_pset : (n_pset + n_test) ]

    mfNew = dict()
    vfNew = dict()

    mcNew = dict()
    vcNew = dict()

    for obj in all_tasks:
        vfNew[ obj ] = vf[ obj ]
        mfNew[ obj ] = mf[ obj ]

    for cons in all_constraints:
        vcNew[ cons ] = vc[ cons ]
        mcNew[ cons ] = mc[ cons ]

    for obj in all_tasks:
        if np.any(vfNew[ obj ] <= 0):
            raise Exception("vfnew is negative: %g at index %d" % (np.min(vfNew[ obj ]), np.argmin(vfNew[ obj ])))
        if np.any(np.isnan(vfNew[ obj ])):
            raise Exception("vfnew constrains nan")

    for cons in all_constraints:
        if np.any(vcNew[ cons ] <= 0):
            raise Exception("vcnew is negative: %g at index %d" % (np.min(vcNew[ cons ]), np.argmin(vcNew[ cons ])))
        if np.any(np.isnan(vcNew[ cons ])):
            raise Exception("vcnew constrains nan")

    return {'mf': mfNew, 'vf':vfNew, 'mfo': mf, 'vfo': vf, 'mc': mcNew, 'vc': vcNew, 'mcc': mc, 'vcc': vc}

    # don't bother computing mf and mc since they are not used in the acquisition function
    # m = mean, v = var, f = objective, c = constraint

# computes the predictive distributions. but the chol of the kernel matrix and the
# chol of the test matrix are already provided.

# Method that approximates the predictive distribution at a particular location.

def predictEP_multiple_iter_optim_robust(obj_models, con_models, a, pareto_set, Xtest, damping = 1, n_iters = 5, no_negatives = True, minimize=True):

    # used to switch between minimizing and maximizing

    sgn = -1.0 if minimize else 1.0

    objs = a['objs']
    all_tasks = objs
    cons = a['cons']
    all_constraints = cons

    n_obs = a['n_obs']
    n_pset = a['n_pset']
    n_total = a['n_total']
    n_test = Xtest.shape[ 0 ]
    q = a['q']
    c = a['c']

    Kstar = dict()
    mf = dict()
    mc = dict()
    mP = dict()
    mP_cons = dict()
    mPset = dict()
    mPset_cons = dict()
    vf = dict()
    vc = dict()
    vP = dict()
    vP_cons = dict()
    cov = dict()
    vPset = dict()
    vPset_cons = dict()

    # First data includes the pareto set. Then, the test point

    Xtest_ext = np.vstack((a['X'][ 0 : n_pset, : ], Xtest))

    for obj in all_tasks:

        # We compute the means and variances of each point (test and pareto set)

        Kstar[ obj ], mP[ obj ], vP[ obj ] = gp_prediction_given_chol_K(a['X'], Xtest_ext,
            a['cholKstarstar'][ obj ], a['cholV'][ obj ], a['m'][ obj ], all_tasks[ obj ], a['jitter'][obj])
        vf[ obj ] = vP[ obj ][ n_pset : (n_pset + n_test) ]
        vPset[ obj ] = vP[ obj ][ 0 : n_pset ]
        mPset[ obj ] = mP[ obj ][ 0 : n_pset ]
        mf[ obj ] = mP[ obj ][ n_pset : (n_pset + n_test) ]

        # Now we compute the covariances between the test data and the pareto set

        Kstarstar = obj_models[ obj ].noiseless_kernel.cross_cov(Xtest_ext[ 0 : n_pset, : ], Xtest_ext[ n_pset : (n_pset + n_test), : ])
        aux1 = spla.solve_triangular(a['cholKstarstar'][ obj ].T, Kstar[ obj ][ : , 0 : n_pset  ], lower=True)
        aux2 = spla.solve_triangular(a['cholKstarstar'][ obj ].T, Kstar[ obj ][ :, n_pset : (n_pset + n_test) ], lower=True)
        aux11 = np.dot(a['cholV'][ obj ], spla.solve_triangular(a['cholKstarstar'][ obj ], aux1, lower=False))
        aux12 = np.dot(a['cholV'][ obj ], spla.solve_triangular(a['cholKstarstar'][ obj ], aux2, lower=False))
        cov[ obj ] = Kstarstar - np.dot(aux1.transpose(), aux2) + np.dot(aux11.transpose(), aux12)

    for cons in all_constraints:

        # We compute the means and variances of each point (test and pareto set)

        Kstar[ cons ], mP_cons[ cons ], vP_cons[ cons ] = gp_prediction_given_chol_K(a['X'], Xtest_ext,
            a['cholKstarstar_cons'][ cons ], a['cholV_cons'][ cons ], a['m_cons'][ cons ], all_constraints[ cons ], a['jitter'][cons])
        vc[ cons ] = vP_cons[ cons ][ n_pset : (n_pset + n_test) ]
        mc[ cons ] = mP_cons[ cons ][ n_pset : (n_pset + n_test) ]

    # scale things for stability

    for obj in all_tasks:
        cov[ obj ] = cov[ obj ] * 0.95

    # We update the predictive distribution to take into account that it has to be dominated by the paretoset
    # For this we use a single parallel update of the factors

    # We set the approximate factors to be uniform

    mTilde_pset = np.zeros((q, n_pset, n_test))
    mTilde_test = np.zeros((q, n_pset, n_test))
    vTilde_pset = np.zeros((q, n_pset, n_test))
    vTilde_test = np.zeros((q, n_pset, n_test))
    vTilde_cov = np.zeros((q, n_pset, n_test))

    mTilde_test_cons = np.zeros((c, n_pset, n_test))
    vTilde_test_cons = np.zeros((c, n_pset, n_test))

    # We compute a "new" distribution

    mOld_pset = np.zeros((q, n_pset, n_test))
    mOld_test = np.zeros((q, n_pset, n_test))
    vOld_pset = np.zeros((q, n_pset, n_test))
    vOld_test = np.zeros((q, n_pset, n_test))
    covOld = np.zeros((q, n_pset, n_test))

    mOld_cons = np.zeros((c, n_pset, n_test))
    vOld_cons = np.zeros((c, n_pset, n_test))

    mNew_pset = np.zeros((q, n_pset, n_test))
    mNew_test = np.zeros((q, n_pset, n_test))
    vNew_pset = np.zeros((q, n_pset, n_test))
    vNew_test = np.zeros((q, n_pset, n_test))
    vNew_cov = np.zeros((q, n_pset, n_test))
    covOrig = np.zeros((q, n_pset, n_test))

    # DHL: XXX The approximate factors depend on the constrains and are replicated over the pareto points

    mTilde_cons = np.zeros((c, n_pset, n_test))
    vTilde_cons = np.zeros((c, n_pset, n_test))

    mOld_test_cons = np.zeros((c, n_pset, n_test))
    vOld_test_cons = np.zeros((c, n_pset, n_test))

    mNew_test_cons = np.zeros((c, n_pset, n_test))
    vNew_test_cons = np.zeros((c, n_pset, n_test))

    vfNew = dict()
    mfNew = dict()

    vcNew = dict()
    mcNew = dict()

    n_task = 0
    for obj in all_tasks:
        mNew_pset[ n_task, :, : ] = np.repeat(mPset[ obj ], n_test).reshape(((n_pset, n_test)))
        mNew_test[ n_task, :, : ] = np.repeat(mf[ obj ], n_pset).reshape(((n_test, n_pset))).transpose()
        vNew_pset[ n_task, :, : ] = np.repeat(vPset[ obj ], n_test).reshape(((n_pset, n_test)))
        vNew_test[ n_task, :, : ] = np.repeat(vf[ obj ], n_pset).reshape(((n_test, n_pset))).transpose()
        vNew_cov[ n_task, :, : ] = cov[ obj ]
        covOrig[ n_task, :, : ] = cov[ obj ]
        n_task += 1

    n_task = 0
    for cons in all_constraints:
        mNew_test_cons[ n_task, :, : ] = np.outer(np.ones(n_pset), mc[ cons ])
        vNew_test_cons[ n_task, :, : ] = np.outer(np.ones(n_pset), vc[ cons ])
        n_task += 1

    # We compute the predictive distribution over the points in the pareto set

    vOld_full_pset = dict()
    vOld_full_pset_cons = dict()

    for obj in all_tasks:
        Kstarstar = obj_models[ obj ].noiseless_kernel.cross_cov(a['X'][ 0 : n_pset, : ], a['X'][ 0 : n_pset, : ])
        Kstar = obj_models[ obj ].noiseless_kernel.cross_cov(a['X'], a['X'][ 0 : n_pset, : ])
        aux1 = spla.solve_triangular(a['cholKstarstar'][ obj ].T, Kstar, lower=True)
        aux2 = spla.solve_triangular(a['cholKstarstar'][ obj ].T, Kstar, lower=True)
        aux11 = np.dot(a['cholV'][ obj ], spla.solve_triangular(a['cholKstarstar'][ obj ], aux1, lower=False))
        aux12 = np.dot(a['cholV'][ obj ], spla.solve_triangular(a['cholKstarstar'][ obj ], aux2, lower=False))
        vOld_full_pset[ obj ] = Kstarstar - np.dot(aux1.transpose(), aux2) + np.dot(aux11.transpose(), aux12) + \
            np.eye(n_pset) * a['jitter'][obj]

    n_task = 0
    for obj in all_tasks:
        vfNew[ obj ] = np.zeros( n_test )
        mfNew[ obj ] = np.zeros( n_test )

    for cons in all_constraints:
        vcNew[ cons ] = np.zeros( n_test )
        mcNew[ cons ] = np.zeros( n_test )

    # Here starts the EP algorithm

    for k in range(n_iters):

        change = 0

        # We compute an old distribution by substracting the approximate factors

        det = vNew_test * vNew_pset - vNew_cov * vNew_cov
        vNew_inv_test = 1.0 / det * vNew_pset
        vNew_inv_pset = 1.0 / det * vNew_test
        vNew_inv_cov = 1.0 / det * - vNew_cov

        vOld_inv_test = vNew_inv_test - vTilde_test
        vOld_inv_pset = vNew_inv_pset - vTilde_pset
        vOld_inv_cov = vNew_inv_cov - vTilde_cov

        det = vOld_inv_test * vOld_inv_pset - vOld_inv_cov * vOld_inv_cov
        vOld_test = 1.0 / det * vOld_inv_pset
        vOld_pset = 1.0 / det * vOld_inv_test
        covOld = 1.0  / det * - vOld_inv_cov

        m_nat_old_test = vNew_inv_test * mNew_test + vNew_inv_cov * mNew_pset - mTilde_test
        m_nat_old_pset = vNew_inv_cov * mNew_test + vNew_inv_pset * mNew_pset - mTilde_pset

        mOld_test = vOld_test * m_nat_old_test + covOld * m_nat_old_pset
        mOld_pset = covOld * m_nat_old_test + vOld_pset * m_nat_old_pset

	vOld_cons = 1.0 / (1.0 / vNew_test_cons - vTilde_cons)
	mOld_cons = vOld_cons * (mNew_test_cons / vNew_test_cons - mTilde_cons)

        # We comupte a new distribution

        s = vOld_pset + vOld_test - 2 * covOld

        if np.any(vOld_pset < 0):
            raise npla.linalg.LinAlgError("Negative value in the sqrt!")

        if np.any(vOld_test < 0):
            raise npla.linalg.LinAlgError("Negative value in the sqrt!")

        scale = 1.0 - 1e-4
        while np.any(s / (vOld_pset + vOld_test) < 1e-6):
            print "Reducing scale to guarantee positivity!"
            scale = scale**2
            s = vOld_pset + vOld_test - 2 * covOld * scale

        alpha = (mOld_test - mOld_pset) / np.sqrt(s) * sgn

        if np.any(vOld_cons < 0):
            raise npla.linalg.LinAlgError("Negative value in the sqrt!")

	alpha_cons = mOld_cons / np.sqrt(vOld_cons)

	log_phi = logcdf_robust(alpha)
	log_phi_cons = logcdf_robust(alpha_cons)

	logZ_orig = log_1_minus_exp_x(np.sum(log_phi, axis = 0))

        if np.any(np.logical_not(logZ_orig == -np.inf)):
            sel = (logZ_orig == -np.inf)
            logZ_orig[ sel ] = logcdf_robust(-np.min(alpha[ :, sel ], axis = 0))

	logZ_term1 = np.sum(log_phi_cons, axis = 0) + logZ_orig
	logZ_term2 = log_1_minus_exp_x(np.sum(log_phi_cons, axis = 0))

        if np.any(np.logical_not(logZ_term2 == -np.inf)):
            sel = (logZ_term2 == -np.inf)
            logZ_term2[ sel ] = logcdf_robust(-np.min(alpha_cons[ :, sel ], axis = 0))

        max_value = np.maximum(logZ_term1, logZ_term2)

	logZ = np.tile(np.log(np.exp(logZ_term1 - max_value) + np.exp(logZ_term2 - max_value)) + \
            max_value, q).reshape((n_pset, q, n_test)).swapaxes(0, 1)

	logZ_cons = np.tile(np.log(np.exp(logZ_term1 - max_value) + np.exp(logZ_term2 - max_value)) + \
            max_value, c).reshape((n_pset, c, n_test)).swapaxes(0, 1)

	log_phi_sum = np.tile(np.sum(log_phi, axis = 0), q).reshape((n_pset, q, n_test)).swapaxes(0, 1)
	log_phi_sum_cons = np.tile(np.sum(log_phi_cons, axis = 0), q).reshape((n_pset, q, n_test)).swapaxes(0, 1)

	ratio = - np.exp(sps.norm.logpdf(alpha) - logZ + log_phi_sum - logcdf_robust(alpha) + log_phi_sum_cons)

	logZ_orig_cons = np.tile(logZ_orig, c).reshape((n_pset, c, n_test)).swapaxes(0, 1)
	log_phi_sum_cons = np.tile(np.sum(log_phi_cons, axis = 0), c).reshape((n_pset, c, n_test)).swapaxes(0, 1)

	ratio_cons = np.exp(sps.norm.logpdf(alpha_cons) - logZ_cons + logZ_orig_cons + log_phi_sum_cons - logcdf_robust(alpha_cons)) - \
		np.exp(sps.norm.logpdf(alpha_cons) - logZ_cons + log_phi_sum_cons - logcdf_robust(alpha_cons))

        dlogZdmfOld_test = ratio / np.sqrt(s) * sgn
        dlogZdmfOld_pset = ratio / np.sqrt(s) * sgn * -1.0

        dlogZdmfOld_test2 = - ratio / s * (alpha + ratio)
        dlogZdmfOld_pset2 = - ratio / s * (alpha + ratio)
        dlogZdmfOld_cov2 = - ratio / s * (alpha + ratio) * -1.0

	dlogZdmcOld = ratio_cons / np.sqrt(vOld_cons)
        dlogZdmcOld2 = - ratio_cons / vOld_cons * (alpha_cons + ratio_cons)

        a_VfOld_times_dlogZdmfOld2 = vOld_test * dlogZdmfOld_test2 + covOld * dlogZdmfOld_cov2 + 1.0
        b_VfOld_times_dlogZdmfOld2 = vOld_test * dlogZdmfOld_cov2 + covOld * dlogZdmfOld_pset2
        c_VfOld_times_dlogZdmfOld2 = covOld * dlogZdmfOld_test2 + vOld_pset * dlogZdmfOld_cov2
        d_VfOld_times_dlogZdmfOld2 = covOld * dlogZdmfOld_cov2 + vOld_pset * dlogZdmfOld_pset2 + 1.0

        a_inv, b_inv, c_inv, d_inv = two_by_two_matrix_inverse(a_VfOld_times_dlogZdmfOld2, b_VfOld_times_dlogZdmfOld2, \
            c_VfOld_times_dlogZdmfOld2, d_VfOld_times_dlogZdmfOld2)

        vTilde_test_new = - (dlogZdmfOld_test2 * a_inv + dlogZdmfOld_cov2 * c_inv)
        vTilde_pset_new = - (dlogZdmfOld_cov2 * b_inv + dlogZdmfOld_pset2 * d_inv)
        vTilde_cov_new = - (dlogZdmfOld_test2 * b_inv + dlogZdmfOld_cov2 * d_inv)

        v_1, v_2 = two_by_two_symmetric_matrix_product_vector(dlogZdmfOld_test2, \
            dlogZdmfOld_pset2, dlogZdmfOld_cov2, mOld_test, mOld_pset)

        v_1 = dlogZdmfOld_test - v_1
        v_2 = dlogZdmfOld_pset - v_2
        mTilde_test_new = v_1 * a_inv + v_2 * c_inv
        mTilde_pset_new = v_1 * b_inv + v_2 * d_inv

        vTilde_cons_new =  - dlogZdmcOld2 / (1.0 + dlogZdmcOld2 * vOld_cons)
        mTilde_cons_new = (dlogZdmcOld - mOld_cons * dlogZdmcOld2) / (1.0 + dlogZdmcOld2 * vOld_cons)

        if no_negatives:
            neg = np.where(vTilde_test_new < 0.0)
            vTilde_test_new[ neg ] = 0.0
            vTilde_pset_new[ neg ] = 0.0
            vTilde_cov_new[ neg ] = 0.0
            mTilde_test_new[ neg ] = 0.0
            mTilde_pset_new[ neg ] = 0.0

	    neg = np.where(vTilde_cons_new < 0.0)
	    vTilde_cons_new[ neg ] = 0.0
	    mTilde_cons_new[ neg ] = 0.0

        not_finite = np.logical_not(np.logical_and(np.logical_and(np.logical_and(np.logical_and(np.isfinite(vTilde_test_new), \
            np.isfinite(vTilde_pset_new)), np.isfinite(vTilde_cov_new)), np.isfinite(mTilde_test_new)), \
            np.isfinite(mTilde_pset_new)))

        not_finite = np.where(not_finite)

        vTilde_test_new[ not_finite ] = 0.0
        vTilde_pset_new[ not_finite ] = 0.0
        vTilde_cov_new[ not_finite ] = 0.0
        mTilde_test_new[ not_finite ] = 0.0
        mTilde_pset_new[ not_finite ] = 0.0

	not_finite = np.logical_not(np.logical_and(np.isfinite(vTilde_cons_new), np.isfinite(mTilde_cons_new)))
	vTilde_cons_new[ not_finite ] = 0.0
	mTilde_cons_new[ not_finite ] = 0.0

        # We damp the updates

        vTilde_test = vTilde_test_new * damping + (1 - damping) * vTilde_test
        vTilde_pset = vTilde_pset_new * damping + (1 - damping) * vTilde_pset
        vTilde_cov = vTilde_cov_new * damping + (1 - damping) * vTilde_cov
        mTilde_test = mTilde_test_new * damping + (1 - damping) * mTilde_test
        mTilde_pset = mTilde_pset_new * damping + (1 - damping) * mTilde_pset

	vTilde_cons = vTilde_cons_new * damping + (1 - damping) * vTilde_cons
	mTilde_cons = mTilde_cons_new * damping + (1 - damping) * mTilde_cons

	# After computing the first natural parameter of the approximate factors we recontruct the
	# predictive distribution. We do the actual computation of the predictive distribution
	# This is the most expensive part (the reconstruction of the posterior)

	n_task = 0
	for cons in all_constraints:
		vNew_test_cons[ n_task, :, : ] = 1.0 / np.outer(np.ones(n_pset), 1.0 / vc[ cons ] + \
			np.sum(np.sum(vTilde_cons, axis = 0), axis = 0))
		mNew_test_cons[ n_task, :, : ] = vNew_test_cons[ n_task, :, : ] * np.outer(np.ones(n_pset), mc[ cons ] / vc[ cons ] + \
			np.sum(np.sum(mTilde_cons, axis = 0), axis = 0))
		n_task += 1

	n_task = 0
        for obj in all_tasks:
            A = vOld_full_pset[ obj ]
            Ainv = matrixInverse(vOld_full_pset[ obj ])

            Ba = np.dot(Ainv, covOrig[ n_task, :, : ])
            Ca = Ba.T
            Da = vf[ obj ]
            Za = np.sum(Ba * covOrig[ n_task, :, : ], axis = 0)

            for i in range(n_test):

                if Xtest.shape[ 0 ] > 1:
                    if ((i % np.ceil(n_test / 100)) == 0):
                        sys.stdout.write(".")
                        sys.stdout.flush()

                # We invert the matrix using block inversion

                Anew = Ainv + np.outer(Ca[ i, : ], Ca[ i, : ].T) * 1.0 / (Da[ i ] - Za[ i ])
                Dnew = 1.0 / (Da[ i ] - Za[ i ])
                Bnew = - Ca[ i, : ] * Dnew
                Cnew = Bnew.T

                # We add the contribution of the approximate factors

                mnew = np.zeros(n_pset + 1)
                mnew[ 0 : n_pset ] = np.dot(Anew, mPset[ obj ]) + Bnew * mf[ obj ][ i ] + mTilde_pset[ n_task, :, i ]
                mnew[ n_pset ] = np.sum(mPset[ obj ] * Bnew) + mf[ obj ][ i ] * Dnew + np.sum(mTilde_test[ n_task, :, i ])

                Anew = (Anew + np.diag(vTilde_pset[ n_task, :, i ]))
                Bnew = (Bnew + vTilde_cov[ n_task, :, i ])
                Cnew = (Cnew + vTilde_cov[ n_task, :, i ])
                Dnew = (Dnew + np.sum(vTilde_test[ n_task, : , i ]))

                # We perform the computation of D by inverting the V matrix after adding the params of the approx factors

                Anew_inv = matrixInverse(Anew)

                Bv = np.dot(Anew_inv, Cnew)
                Dv = np.sum(Bnew * Bv)

                D = 1.0 / (Dnew - Dv)
                aux = np.outer(Bv, Bv)
                A = Anew_inv +  aux * D
                B = - Bv * D
                C = B.T

                mean = np.zeros(n_pset + 1)
                mean[ 0 : n_pset ] = np.dot(A, mnew[ 0 : n_pset ]) + B * mnew[ n_pset ]
                mean[ n_pset ] = np.sum(mnew[ 0 : n_pset ] * B) + mnew[ n_pset ] * D

                mNew_pset[ n_task, :, i ] = mean[ 0 : n_pset ]
                mNew_test[ n_task, :, i ] = mean[ n_pset ]
                vNew_pset[ n_task, :, i ] = np.diag(A)
                vNew_test[ n_task, : , i ] = D
                vNew_cov[ n_task, :, i ] = B

                change = np.max((change, np.max(np.abs(vfNew[ obj ][ i ] - D))))
                change = np.max((change, np.max(np.abs(mfNew[ obj ][ i ] - mean[ n_pset ]))))

                vfNew[ obj ][ i ] = D
                mfNew[ obj ][ i ] = mean[ n_pset ]

            n_task += 1
            if Xtest.shape[ 0 ] > 1:
                print ''

        if Xtest.shape[ 0 ] > 1:
            print(change)

    n_task = 0
    for cons in all_constraints:
	vcNew[ cons ] = 1.0 / (1.0 / vc[ cons ] + np.sum(np.sum(vTilde_cons, axis = 0), axis = 0))
	mcNew[ cons ] = vcNew[ cons ] * (mc[ cons ] / vc[ cons ] + np.sum(np.sum(mTilde_cons, axis = 0), axis = 0))
	n_task += 1

    for obj in all_tasks:
        if np.any(vfNew[ obj ] <= 0):
            raise Exception("vfnew is negative: %g at index %d" % (np.min(vfNew[ obj ]), np.argmin(vfNew[ obj ])))
        if np.any(np.isnan(vfNew[ obj ])):
            raise Exception("vfnew constrains nan")

    for cons in all_constraints:
        if np.any(vcNew[ cons ] <= 0):
            raise Exception("vcnew is negative: %g at index %d" % (np.min(vcNew[ cons ]), np.argmin(vcNew[ cons ])))
        if np.any(np.isnan(vcNew[ cons ])):
            raise Exception("vcnew constrains nan")

    return {'mf': mfNew, 'vf':vfNew, 'mfo': mf, 'vfo': vf, 'mc': mcNew, 'vc': vcNew, 'mco': mc, 'vco': vc}



# Method that approximates the predictive distribution at a particular location.

def predictEP_multiple_iter_optim(obj_models, con_models, a, pareto_set, Xtest, damping = 1, n_iters = 5, no_negatives = True, minimize=True):

    # used to switch between minimizing and maximizing

    sgn = -1.0 if minimize else 1.0

    objs = a['objs']
    all_tasks = objs
    cons = a['cons']
    all_constraints = cons

    n_obs = a['n_obs']
    n_pset = a['n_pset']
    n_total = a['n_total']
    n_test = Xtest.shape[ 0 ]
    q = a['q']
    c = a['c']

    Kstar = dict()
    mf = dict()
    mc = dict()
    mP = dict()
    mP_cons = dict()
    mPset = dict()
    mPset_cons = dict()
    vf = dict()
    vc = dict()
    vP = dict()
    vP_cons = dict()
    cov = dict()
    vPset = dict()
    vPset_cons = dict()

    # First data includes the pareto set. Then, the test point

    Xtest_ext = np.vstack((a['X'][ 0 : n_pset, : ], Xtest))

    for obj in all_tasks:

        # We compute the means and variances of each point (test and pareto set)

        Kstar[ obj ], mP[ obj ], vP[ obj ] = gp_prediction_given_chol_K(a['X'], Xtest_ext,
            a['cholKstarstar'][ obj ], a['cholV'][ obj ], a['m'][ obj ], all_tasks[ obj ], a['jitter'][obj])
        vf[ obj ] = vP[ obj ][ n_pset : (n_pset + n_test) ]
        vPset[ obj ] = vP[ obj ][ 0 : n_pset ]
        mPset[ obj ] = mP[ obj ][ 0 : n_pset ]
        mf[ obj ] = mP[ obj ][ n_pset : (n_pset + n_test) ]

        # Now we compute the covariances between the test data and the pareto set

        Kstarstar = obj_models[ obj ].noiseless_kernel.cross_cov(Xtest_ext[ 0 : n_pset, : ], Xtest_ext[ n_pset : (n_pset + n_test), : ])
        aux1 = spla.solve_triangular(a['cholKstarstar'][ obj ].T, Kstar[ obj ][ : , 0 : n_pset  ], lower=True)
        aux2 = spla.solve_triangular(a['cholKstarstar'][ obj ].T, Kstar[ obj ][ :, n_pset : (n_pset + n_test) ], lower=True)
        aux11 = np.dot(a['cholV'][ obj ], spla.solve_triangular(a['cholKstarstar'][ obj ], aux1, lower=False))
        aux12 = np.dot(a['cholV'][ obj ], spla.solve_triangular(a['cholKstarstar'][ obj ], aux2, lower=False))
        cov[ obj ] = Kstarstar - np.dot(aux1.transpose(), aux2) + np.dot(aux11.transpose(), aux12)

    for cons in all_constraints:

        # We compute the means and variances of each point (test and pareto set)

        Kstar[ cons ], mP_cons[ cons ], vP_cons[ cons ] = gp_prediction_given_chol_K(a['X'], Xtest_ext,
            a['cholKstarstar_cons'][ cons ], a['cholV_cons'][ cons ], a['m_cons'][ cons ], all_constraints[ cons ], a['jitter'][cons])
        vc[ cons ] = vP_cons[ cons ][ n_pset : (n_pset + n_test) ]
        mc[ cons ] = mP_cons[ cons ][ n_pset : (n_pset + n_test) ]

    # scale things for stability

    for obj in all_tasks:
        cov[ obj ] = cov[ obj ] * 0.95

    # We update the predictive distribution to take into account that it has to be dominated by the paretoset
    # For this we use a single parallel update of the factors

    # We set the approximate factors to be uniform

    mTilde_pset = np.zeros((q, n_pset, n_test))
    mTilde_test = np.zeros((q, n_pset, n_test))
    vTilde_pset = np.zeros((q, n_pset, n_test))
    vTilde_test = np.zeros((q, n_pset, n_test))
    vTilde_cov = np.zeros((q, n_pset, n_test))

    mTilde_test_cons = np.zeros((c, n_pset, n_test))
    vTilde_test_cons = np.zeros((c, n_pset, n_test))

    # We compute a "new" distribution

    mOld_pset = np.zeros((q, n_pset, n_test))
    mOld_test = np.zeros((q, n_pset, n_test))
    vOld_pset = np.zeros((q, n_pset, n_test))
    vOld_test = np.zeros((q, n_pset, n_test))
    covOld = np.zeros((q, n_pset, n_test))

    mOld_cons = np.zeros((c, n_pset, n_test))
    vOld_cons = np.zeros((c, n_pset, n_test))

    mNew_pset = np.zeros((q, n_pset, n_test))
    mNew_test = np.zeros((q, n_pset, n_test))
    vNew_pset = np.zeros((q, n_pset, n_test))
    vNew_test = np.zeros((q, n_pset, n_test))
    vNew_cov = np.zeros((q, n_pset, n_test))
    covOrig = np.zeros((q, n_pset, n_test))

    # DHL: XXX The approximate factors depend on the constrains and are replicated over the pareto points

    mTilde_cons = np.zeros((c, n_pset, n_test))
    vTilde_cons = np.zeros((c, n_pset, n_test))

    mOld_test_cons = np.zeros((c, n_pset, n_test))
    vOld_test_cons = np.zeros((c, n_pset, n_test))

    mNew_test_cons = np.zeros((c, n_pset, n_test))
    vNew_test_cons = np.zeros((c, n_pset, n_test))

    vfNew = dict()
    mfNew = dict()

    vcNew = dict()
    mcNew = dict()

    n_task = 0
    for obj in all_tasks:
        mNew_pset[ n_task, :, : ] = np.repeat(mPset[ obj ], n_test).reshape(((n_pset, n_test)))
        mNew_test[ n_task, :, : ] = np.repeat(mf[ obj ], n_pset).reshape(((n_test, n_pset))).transpose()
        vNew_pset[ n_task, :, : ] = np.repeat(vPset[ obj ], n_test).reshape(((n_pset, n_test)))
        vNew_test[ n_task, :, : ] = np.repeat(vf[ obj ], n_pset).reshape(((n_test, n_pset))).transpose()
        vNew_cov[ n_task, :, : ] = cov[ obj ]
        covOrig[ n_task, :, : ] = cov[ obj ]
        n_task += 1

    n_task = 0
    for cons in all_constraints:
        mNew_test_cons[ n_task, :, : ] = np.outer(np.ones(n_pset), mc[ cons ])
        vNew_test_cons[ n_task, :, : ] = np.outer(np.ones(n_pset), vc[ cons ])
        n_task += 1

    # We compute the predictive distribution over the points in the pareto set

    vOld_full_pset = dict()
    vOld_full_pset_cons = dict()

    for obj in all_tasks:
        Kstarstar = obj_models[ obj ].noiseless_kernel.cross_cov(a['X'][ 0 : n_pset, : ], a['X'][ 0 : n_pset, : ])
        Kstar = obj_models[ obj ].noiseless_kernel.cross_cov(a['X'], a['X'][ 0 : n_pset, : ])
        aux1 = spla.solve_triangular(a['cholKstarstar'][ obj ].T, Kstar, lower=True)
        aux2 = spla.solve_triangular(a['cholKstarstar'][ obj ].T, Kstar, lower=True)
        aux11 = np.dot(a['cholV'][ obj ], spla.solve_triangular(a['cholKstarstar'][ obj ], aux1, lower=False))
        aux12 = np.dot(a['cholV'][ obj ], spla.solve_triangular(a['cholKstarstar'][ obj ], aux2, lower=False))
        vOld_full_pset[ obj ] = Kstarstar - np.dot(aux1.transpose(), aux2) + np.dot(aux11.transpose(), aux12) + \
            np.eye(n_pset) * a['jitter'][obj]

    n_task = 0
    for obj in all_tasks:
        vfNew[ obj ] = np.zeros( n_test )
        mfNew[ obj ] = np.zeros( n_test )

    for cons in all_constraints:
        vcNew[ cons ] = np.zeros( n_test )
        mcNew[ cons ] = np.zeros( n_test )

    # Here starts the EP algorithm

    for k in range(n_iters):

        change = 0

        # We compute an old distribution by substracting the approximate factors

        det = vNew_test * vNew_pset - vNew_cov * vNew_cov
        vNew_inv_test = 1.0 / det * vNew_pset
        vNew_inv_pset = 1.0 / det * vNew_test
        vNew_inv_cov = 1.0 / det * - vNew_cov

        vOld_inv_test = vNew_inv_test - vTilde_test
        vOld_inv_pset = vNew_inv_pset - vTilde_pset
        vOld_inv_cov = vNew_inv_cov - vTilde_cov

        det = vOld_inv_test * vOld_inv_pset - vOld_inv_cov * vOld_inv_cov
        vOld_test = 1.0 / det * vOld_inv_pset
        vOld_pset = 1.0 / det * vOld_inv_test
        covOld = 1.0  / det * - vOld_inv_cov

        m_nat_old_test = vNew_inv_test * mNew_test + vNew_inv_cov * mNew_pset - mTilde_test
        m_nat_old_pset = vNew_inv_cov * mNew_test + vNew_inv_pset * mNew_pset - mTilde_pset

        mOld_test = vOld_test * m_nat_old_test + covOld * m_nat_old_pset
        mOld_pset = covOld * m_nat_old_test + vOld_pset * m_nat_old_pset

	vOld_cons = 1.0 / (1.0 / vNew_test_cons - vTilde_cons)
	mOld_cons = vOld_cons * (mNew_test_cons / vNew_test_cons - mTilde_cons)

        # We comupte a new distribution

        s = vOld_pset + vOld_test - 2 * covOld

        if np.any(vOld_pset < 0):
            raise npla.linalg.LinAlgError("Negative value in the sqrt!")

        if np.any(vOld_test < 0):
            raise npla.linalg.LinAlgError("Negative value in the sqrt!")

        scale = 1.0 - 1e-4
        while np.any(s / (vOld_pset + vOld_test) < 1e-6):
            print "Reducing scale to guarantee positivity!"
            scale = scale**2
            s = vOld_pset + vOld_test - 2 * covOld * scale

        alpha = (mOld_test - mOld_pset) / np.sqrt(s) * sgn

        if np.any(vOld_cons < 0):
            raise npla.linalg.LinAlgError("Negative value in the sqrt!")

	alpha_cons = mOld_cons / np.sqrt(vOld_cons)

	log_phi = logcdf_robust(alpha)
	log_phi_cons = logcdf_robust(alpha_cons)

	logZ_orig = log_1_minus_exp_x(np.sum(log_phi, axis = 0))

        if np.any(np.logical_not(logZ_orig == -np.inf)):
            sel = (logZ_orig == -np.inf)
            logZ_orig[ sel ] = logcdf_robust(-np.min(alpha[ :, sel ], axis = 0))

	logZ_term1 = np.sum(log_phi_cons, axis = 0) + logZ_orig
	logZ_term2 = log_1_minus_exp_x(np.sum(log_phi_cons, axis = 0))

        if np.any(np.logical_not(logZ_term2 == -np.inf)):
            sel = (logZ_term2 == -np.inf)
            logZ_term2[ sel ] = logcdf_robust(-np.min(alpha_cons[ :, sel ], axis = 0))

        max_value = np.maximum(logZ_term1, logZ_term2)

	logZ = np.tile(np.log(np.exp(logZ_term1 - max_value) + np.exp(logZ_term2 - max_value)) + \
            max_value, q).reshape((n_pset, q, n_test)).swapaxes(0, 1)

	logZ_cons = np.tile(np.log(np.exp(logZ_term1 - max_value) + np.exp(logZ_term2 - max_value)) + \
            max_value, c).reshape((n_pset, c, n_test)).swapaxes(0, 1)

	log_phi_sum = np.tile(np.sum(log_phi, axis = 0), q).reshape((n_pset, q, n_test)).swapaxes(0, 1)
	log_phi_sum_cons = np.tile(np.sum(log_phi_cons, axis = 0), q).reshape((n_pset, q, n_test)).swapaxes(0, 1)

	ratio = - np.exp(sps.norm.logpdf(alpha) - logZ + log_phi_sum - logcdf_robust(alpha) + log_phi_sum_cons)

	logZ_orig_cons = np.tile(logZ_orig, c).reshape((n_pset, c, n_test)).swapaxes(0, 1)
	log_phi_sum_cons = np.tile(np.sum(log_phi_cons, axis = 0), c).reshape((n_pset, c, n_test)).swapaxes(0, 1)

	ratio_cons = np.exp(sps.norm.logpdf(alpha_cons) - logZ_cons + logZ_orig_cons + log_phi_sum_cons - logcdf_robust(alpha_cons)) - \
		np.exp(sps.norm.logpdf(alpha_cons) - logZ_cons + log_phi_sum_cons - logcdf_robust(alpha_cons))

        dlogZdmfOld_test = ratio / np.sqrt(s) * sgn
        dlogZdmfOld_pset = ratio / np.sqrt(s) * sgn * -1.0

        dlogZdVfOld_test = -0.5 * ratio * alpha / s
        dlogZdVfOld_pset = -0.5 * ratio * alpha / s
        dlogZdVfOld_cov = -0.5 * ratio * alpha / s * -1.0

	dlogZdmcOld = ratio_cons / np.sqrt(vOld_cons)
	dlogZdVcOld = -0.5 * ratio_cons * alpha_cons / vOld_cons

        # The following lines compute the updates in parallel C = dmdm - 2 dv
        # First the first natural parameter

        c_11 = dlogZdmfOld_test * dlogZdmfOld_test - 2 * dlogZdVfOld_test
        c_22 = dlogZdmfOld_pset * dlogZdmfOld_pset - 2 * dlogZdVfOld_pset
        c_12 = dlogZdmfOld_pset * dlogZdmfOld_test - 2 * dlogZdVfOld_cov

        cp_11 = c_11 * vOld_test + c_12 * covOld
        cp_12 = c_11 * covOld + c_12 * vOld_pset
        cp_21 = c_12 * vOld_test + c_22 * covOld
        cp_22 = c_12 * covOld + c_22 * vOld_pset

        vNew_test = vOld_test - (vOld_test * cp_11 + covOld * cp_21)
        vNew_cov = covOld - (vOld_test * cp_12 + covOld * cp_22)
        vNew_pset = vOld_pset - (covOld * cp_12 + vOld_pset * cp_22)

        det = vNew_test * vNew_pset - vNew_cov * vNew_cov
        vNew_inv_test = 1.0 / det * vNew_pset
        vNew_inv_pset = 1.0 / det * vNew_test
        vNew_inv_cov = 1.0 / det * - vNew_cov

        det = vOld_test * vOld_pset - covOld * covOld
        vOld_inv_test = 1.0 / det * vOld_pset
        vOld_inv_pset = 1.0 / det * vOld_test
        vOld_inv_cov = 1.0 / det * - covOld

	mcTilted = mOld_cons + vOld_cons * dlogZdmcOld
	vcTilted = vOld_cons - vOld_cons * (dlogZdmcOld**2 - 2.0 * dlogZdVcOld) * vOld_cons

	vTilde_cons_new = 1.0 / vcTilted - 1.0 / vOld_cons
	mTilde_cons_new = mcTilted / vcTilted - mOld_cons / vOld_cons

        # This is the approx factor

        vTilde_test_new = (vNew_inv_test - vOld_inv_test)
        vTilde_pset_new = (vNew_inv_pset - vOld_inv_pset)
        vTilde_cov_new = (vNew_inv_cov - vOld_inv_cov)

        if no_negatives:
            neg = np.where(vTilde_test_new < 0.0)
            vTilde_test_new[ neg ] = 0.0
            vTilde_pset_new[ neg ] = 0.0
            vTilde_cov_new[ neg ] = 0.0

	    neg = np.where(vTilde_cons_new < 0.0)
	    vTilde_cons_new[ neg ] = 0.0
	    mTilde_cons_new[ neg ] = 0.0

        # We avoid negative variances in the approximate factors. This avoids non PSD cov matrices

        # Now the second natural parameter = A~ (mOld + Vold dlogz_dm) + dlogz_dm

        v_1 = mOld_test + vOld_test * dlogZdmfOld_test + covOld * dlogZdmfOld_pset
        v_2 = mOld_pset + covOld * dlogZdmfOld_test + vOld_pset * dlogZdmfOld_pset

        mTilde_test_new = vTilde_test_new * v_1 + vTilde_cov_new * v_2 + dlogZdmfOld_test
        mTilde_pset_new = vTilde_cov_new * v_1 + vTilde_pset_new * v_2 + dlogZdmfOld_pset

        not_finite = np.logical_not(np.logical_and(np.logical_and(np.logical_and(np.logical_and(np.isfinite(vTilde_test_new), \
            np.isfinite(vTilde_pset_new)), np.isfinite(vTilde_cov_new)), np.isfinite(mTilde_test_new)), \
            np.isfinite(mTilde_pset_new)))

        not_finite = np.where(not_finite)

        vTilde_test_new[ not_finite ] = 0.0
        vTilde_pset_new[ not_finite ] = 0.0
        vTilde_cov_new[ not_finite ] = 0.0
        mTilde_test_new[ not_finite ] = 0.0
        mTilde_pset_new[ not_finite ] = 0.0

	not_finite = np.logical_not(np.logical_and(np.isfinite(vTilde_cons_new), np.isfinite(mTilde_cons_new)))
	vTilde_cons_new[ not_finite ] = 0.0
	mTilde_cons_new[ not_finite ] = 0.0

        # We damp the updates

        vTilde_test = vTilde_test_new * damping + (1 - damping) * vTilde_test
        vTilde_pset = vTilde_pset_new * damping + (1 - damping) * vTilde_pset
        vTilde_cov = vTilde_cov_new * damping + (1 - damping) * vTilde_cov
        mTilde_test = mTilde_test_new * damping + (1 - damping) * mTilde_test
        mTilde_pset = mTilde_pset_new * damping + (1 - damping) * mTilde_pset

	vTilde_cons = vTilde_cons_new * damping + (1 - damping) * vTilde_cons
	mTilde_cons = mTilde_cons_new * damping + (1 - damping) * mTilde_cons

	# After computing the first natural parameter of the approximate factors we recontruct the
	# predictive distribution. We do the actual computation of the predictive distribution
	# This is the most expensive part (the reconstruction of the posterior)

	n_task = 0
	for cons in all_constraints:
		vNew_test_cons[ n_task, :, : ] = 1.0 / np.outer(np.ones(n_pset), 1.0 / vc[ cons ] + \
			np.sum(np.sum(vTilde_cons, axis = 0), axis = 0))
		mNew_test_cons[ n_task, :, : ] = vNew_test_cons[ n_task, :, : ] * np.outer(np.ones(n_pset), mc[ cons ] / vc[ cons ] + \
			np.sum(np.sum(mTilde_cons, axis = 0), axis = 0))
		n_task += 1

	n_task = 0
        for obj in all_tasks:
            A = vOld_full_pset[ obj ]
            Ainv = matrixInverse(vOld_full_pset[ obj ])

            Ba = np.dot(Ainv, covOrig[ n_task, :, : ])
            Ca = Ba.T
            Da = vf[ obj ]
            Za = np.sum(Ba * covOrig[ n_task, :, : ], axis = 0)

            for i in range(n_test):

                if Xtest.shape[ 0 ] > 1:
                    if ((i % np.ceil(n_test / 100)) == 0):
                        sys.stdout.write(".")
                        sys.stdout.flush()

                # We invert the matrix using block inversion

                Anew = Ainv + np.outer(Ca[ i, : ], Ca[ i, : ].T) * 1.0 / (Da[ i ] - Za[ i ])
                Dnew = 1.0 / (Da[ i ] - Za[ i ])
                Bnew = - Ca[ i, : ] * Dnew
                Cnew = Bnew.T

                # We add the contribution of the approximate factors

                mnew = np.zeros(n_pset + 1)
                mnew[ 0 : n_pset ] = np.dot(Anew, mPset[ obj ]) + Bnew * mf[ obj ][ i ] + mTilde_pset[ n_task, :, i ]
                mnew[ n_pset ] = np.sum(mPset[ obj ] * Bnew) + mf[ obj ][ i ] * Dnew + np.sum(mTilde_test[ n_task, :, i ])

                Anew = (Anew + np.diag(vTilde_pset[ n_task, :, i ]))
                Bnew = (Bnew + vTilde_cov[ n_task, :, i ])
                Cnew = (Cnew + vTilde_cov[ n_task, :, i ])
                Dnew = (Dnew + np.sum(vTilde_test[ n_task, : , i ]))

                # We perform the computation of D by inverting the V matrix after adding the params of the approx factors

                Anew_inv = matrixInverse(Anew)

                Bv = np.dot(Anew_inv, Cnew)
                Dv = np.sum(Bnew * Bv)

                D = 1.0 / (Dnew - Dv)
                aux = np.outer(Bv, Bv)
                A = Anew_inv +  aux * D
                B = - Bv * D
                C = B.T

                mean = np.zeros(n_pset + 1)
                mean[ 0 : n_pset ] = np.dot(A, mnew[ 0 : n_pset ]) + B * mnew[ n_pset ]
                mean[ n_pset ] = np.sum(mnew[ 0 : n_pset ] * B) + mnew[ n_pset ] * D

                mNew_pset[ n_task, :, i ] = mean[ 0 : n_pset ]
                mNew_test[ n_task, :, i ] = mean[ n_pset ]
                vNew_pset[ n_task, :, i ] = np.diag(A)
                vNew_test[ n_task, : , i ] = D
                vNew_cov[ n_task, :, i ] = B

                change = np.max((change, np.max(np.abs(vfNew[ obj ][ i ] - D))))
                change = np.max((change, np.max(np.abs(mfNew[ obj ][ i ] - mean[ n_pset ]))))

                vfNew[ obj ][ i ] = D
                mfNew[ obj ][ i ] = mean[ n_pset ]

            n_task += 1
            if Xtest.shape[ 0 ] > 1:
                print ''

        if Xtest.shape[ 0 ] > 1:
            print(change)

    n_task = 0
    for cons in all_constraints:
	vcNew[ cons ] = 1.0 / (1.0 / vc[ cons ] + np.sum(np.sum(vTilde_cons, axis = 0), axis = 0))
	mcNew[ cons ] = vcNew[ cons ] * (mc[ cons ] / vc[ cons ] + np.sum(np.sum(mTilde_cons, axis = 0), axis = 0))
	n_task += 1

    for obj in all_tasks:
        if np.any(vfNew[ obj ] <= 0):
            raise Exception("vfnew is negative: %g at index %d" % (np.min(vfNew[ obj ]), np.argmin(vfNew[ obj ])))
        if np.any(np.isnan(vfNew[ obj ])):
            raise Exception("vfnew constrains nan")

    for cons in all_constraints:
        if np.any(vcNew[ cons ] <= 0):
            raise Exception("vcnew is negative: %g at index %d" % (np.min(vcNew[ cons ]), np.argmin(vcNew[ cons ])))
        if np.any(np.isnan(vcNew[ cons ])):
            raise Exception("vcnew constrains nan")

    return {'mf': mfNew, 'vf':vfNew, 'mfo': mf, 'vfo': vf, 'mc': mcNew, 'vc': vcNew, 'mco': mc, 'vco': vc}

    # don't bother computing mf and mc since they are not used in the acquisition function
    # m = mean, v = var, f = objective, c = constraint


# computes the predictive distributions. but the chol of the kernel matrix and the
# chol of the test matrix are already provided.


# Method that approximates the predictive distribution at a particular location.

def predictEP(obj_models, a, pareto_set, Xtest, damping = 1, minimize=True):

	# used to switch between minimizing and maximizing

	sgn = -1.0 if minimize else 1.0

	objs = a['objs']
	all_tasks = objs

	n_obs = a['n_obs']
	n_pset = a['n_pset']
	n_total = a['n_total']
	n_test = Xtest.shape[ 0 ]
	q = a['q']

	Kstar = dict()
	mf = dict()
	mP = dict()
	mPset = dict()
	vf = dict()
	vP = dict()
	cov = dict()
	vPset = dict()

	# This is used for the comutation of the variance of the predictive distribution

	ahfHatNew = dict()
	bhfHatNew = dict()

	mfOld = dict()
	VfOld = dict()
	ahfHatNew = dict()
	bhfHatNew = dict()

	for obj in all_tasks:
		mfOld[ obj ] = np.zeros((n_pset, 2))
		VfOld[ obj ] = np.zeros((n_pset, 2, 2))
		ahfHatNew[ obj ] = np.zeros((n_pset, 2, 2))
		bhfHatNew[ obj ] = np.zeros((n_pset, 2))

	# First data includes the pareto set. Then, the test point

	Xtest_ext = np.vstack((a['X'][ 0 : n_pset, : ], Xtest))

	for obj in all_tasks:

		# We compute the means and variances of each point (test and pareto set)

		Kstar[ obj ], mP[ obj ], vP[ obj ] = gp_prediction_given_chol_K(a['X'], Xtest_ext,
			a['cholKstarstar'][ obj ], a['cholV'][ obj ], a['m'][ obj ], all_tasks[ obj ], a['jitter'][obj])
		vf[ obj ] = vP[ obj ][ n_pset : (n_pset + n_test) ]
		vPset[ obj ] = vP[ obj ][ 0 : n_pset ]
		mPset[ obj ] = mP[ obj ][ 0 : n_pset ]
		mf[ obj ] = mP[ obj ][ n_pset : (n_pset + n_test) ]

		# Now we compute the covariances between the test data and the pareto set

		Kstarstar = obj_models[ obj ].noiseless_kernel.cross_cov(Xtest_ext[ 0 : n_pset, : ], Xtest_ext[ n_pset : (n_pset + n_test), : ])
		aux1 = spla.solve_triangular(a['cholKstarstar'][ obj ].T, Kstar[ obj ][ : , 0 : n_pset  ], lower=True)
		aux2 = spla.solve_triangular(a['cholKstarstar'][ obj ].T, Kstar[ obj ][ :, n_pset : (n_pset + n_test) ], lower=True)
		aux11 = np.dot(a['cholV'][ obj ], spla.solve_triangular(a['cholKstarstar'][ obj ], aux1, lower=False))
		aux12 = np.dot(a['cholV'][ obj ], spla.solve_triangular(a['cholKstarstar'][ obj ], aux2, lower=False))
		cov[ obj ] = Kstarstar - np.dot(aux1.transpose(), aux2) + np.dot(aux11.transpose(), aux12)

	# scale things for stability

	for obj in all_tasks:
		scale = (1.0 - 1e-4) * np.ones(cov[ obj ].shape)
		vf_tmp = np.repeat(vf[ obj ], cov[ obj ].shape[ 0 ]).reshape(cov[ obj ].shape[ ::-1 ]).transpose()
		vpset_tmp = np.repeat(vPset[ obj ], cov[ obj ].shape[ 1 ]).reshape(cov[ obj ].shape)
		index = vf_tmp + vpset_tmp -  2.0 * scale * cov[ obj ] < 1e-10

		while np.any(index):
                        print "Reducing scale to guarantee positivity!"
			scale[ index ] = scale[ index ]**2
			index = vf_tmp + vpset_tmp -  2.0 * scale * cov[ obj ] < 1e-10

    		cov[ obj ] = scale * cov[ obj ]

	# We update the predictive distribution to take into account that it has to be dominated by the paretoset
	# For this we use a single parallel update of the factors

	# We compute an "old" distribution which is the unconstrained distribution

	mOld_pset = np.zeros((q, n_pset, n_test))
	mOld_test = np.zeros((q, n_pset, n_test))
	vOld_pset = np.zeros((q, n_pset, n_test))
	vOld_test = np.zeros((q, n_pset, n_test))
	covOld = np.zeros((q, n_pset, n_test))

	n_task = 0
	for obj in all_tasks:
		mOld_pset[ n_task, :, : ] = np.repeat(mPset[ obj ], n_test).reshape(((n_pset, n_test)))
		mOld_test[ n_task, :, : ] = np.repeat(mf[ obj ], n_pset).reshape(((n_test, n_pset))).transpose()
		vOld_pset[ n_task, :, : ] = np.repeat(vPset[ obj ], n_test).reshape(((n_pset, n_test)))
		vOld_test[ n_task, :, : ] = np.repeat(vf[ obj ], n_pset).reshape(((n_test, n_pset))).transpose()
		covOld[ n_task, :, : ] = cov[ obj ]
		n_task += 1

	# We comupte a new distribution

	s = vOld_pset + vOld_test - 2 * covOld
	alpha = (mOld_test - mOld_pset) / np.sqrt(s) * sgn

	if np.any(s < 0):
		raise npla.linalg.LinAlgError("Negative value in the sqrt!")

	log_phi = logcdf_robust(alpha)
       	logZ = np.repeat(log_1_minus_exp_x(np.sum(log_phi, axis = 0)).transpose(), q).reshape((n_test, n_pset, q)).transpose()
	log_phi_sum = np.repeat(np.sum(log_phi, axis = 0).transpose(), q).reshape((n_test, n_pset, q)).transpose()

	ratio = - np.exp(sps.norm.logpdf(alpha) - logZ + log_phi_sum - log_phi)

	dlogZdmfOld_test = ratio / np.sqrt(s) * sgn
	dlogZdmfOld_pset = ratio / np.sqrt(s) * sgn * -1.0

	dlogZdVfOld_test = -0.5 * ratio * alpha / s
	dlogZdVfOld_pset = -0.5 * ratio * alpha / s
	dlogZdVfOld_cov = -0.5 * ratio * alpha / s * -1.0

	# The following lines compute the updates in parallel C = dmdm - 2 dv
	# First the first natural parameter

	c_11 = dlogZdmfOld_test * dlogZdmfOld_test - 2 * dlogZdVfOld_test
	c_22 = dlogZdmfOld_pset * dlogZdmfOld_pset - 2 * dlogZdVfOld_pset
	c_12 = dlogZdmfOld_pset * dlogZdmfOld_test - 2 * dlogZdVfOld_cov

	cp_11 = c_11 * vOld_test + c_12 * covOld
	cp_12 = c_11 * covOld + c_12 * vOld_pset
	cp_21 = c_12 * vOld_test + c_22 * covOld
	cp_22 = c_12 * covOld + c_22 * vOld_pset

	vNew_test = vOld_test - (vOld_test * cp_11 + covOld * cp_21)
	vNew_cov = covOld - (vOld_test * cp_12 + covOld * cp_22)
	vNew_pset = vOld_pset - (covOld * cp_12 + vOld_pset * cp_22)

	det = vNew_test * vNew_pset - vNew_cov * vNew_cov
	vNew_inv_test = 1.0 / det * vNew_pset
	vNew_inv_pset = 1.0 / det * vNew_test
	vNew_inv_cov = 1.0 / det * - vNew_cov

	det = vOld_test * vOld_pset - covOld * covOld
	vOld_inv_test = 1.0 / det * vOld_pset
	vOld_inv_pset = 1.0 / det * vOld_test
	vOld_inv_cov = 1.0 / det * - covOld

	# This is the approx factor

	vTilde_test = vNew_inv_test - vOld_inv_test
	vTilde_pset = vNew_inv_pset - vOld_inv_pset
	vTilde_cov = vNew_inv_cov - vOld_inv_cov

	# We avoid negative variances in the approximate factors. This avoids non PSD cov matrices

#	neg = np.where(vTilde_test < 0)
#	vTilde_test[ neg ] = 0
#	vTilde_pset[ neg ] = 0
#	vTilde_cov[ neg ] = 0

	# Now the second natural parameter = A~ (mOld + Vold dlogz_dm) + dlogz_dm

	v_1 = mOld_test + vOld_test * dlogZdmfOld_test + covOld * dlogZdmfOld_pset
	v_2 = mOld_pset + covOld * dlogZdmfOld_test + vOld_pset * dlogZdmfOld_pset

	mTilde_test = vTilde_test * v_1 + vTilde_cov * v_2 + dlogZdmfOld_test
	mTilde_pset = vTilde_cov * v_1 + vTilde_pset * v_2 + dlogZdmfOld_pset

	# After computing the first natural parameter of the approximate factors we recontruct the
	# predictive distribution. We do the actual computation of the predictive distribution

	# We compute the predictive distribution over the points in the pareto set

	vOld_full_pset = dict()

	for obj in all_tasks:
		Kstarstar = obj_models[ obj ].noiseless_kernel.cross_cov(a['X'][ 0 : n_pset, : ], a['X'][ 0 : n_pset, : ])
		Kstar = obj_models[ obj ].noiseless_kernel.cross_cov(a['X'], a['X'][ 0 : n_pset, : ])
		aux1 = spla.solve_triangular(a['cholKstarstar'][ obj ].T, Kstar, lower=True)
		aux2 = spla.solve_triangular(a['cholKstarstar'][ obj ].T, Kstar, lower=True)
		aux11 = np.dot(a['cholV'][ obj ], spla.solve_triangular(a['cholKstarstar'][ obj ], aux1, lower=False))
		aux12 = np.dot(a['cholV'][ obj ], spla.solve_triangular(a['cholKstarstar'][ obj ], aux2, lower=False))
		vOld_full_pset[ obj ] = Kstarstar - np.dot(aux1.transpose(), aux2) + np.dot(aux11.transpose(), aux12) + \
		np.eye(n_pset) * a['jitter'][obj]

	# This is the most expensive part

	vfNew = dict()
	mfNew = dict()

	n_task = 0
	for obj in all_tasks:

		vfNew[ obj ] = np.zeros( n_test )
		mfNew[ obj ] = np.zeros( n_test )

		A = vOld_full_pset[ obj ]
		Ainv = matrixInverse(vOld_full_pset[ obj ])

		for i in range(n_test):

			if ((i % np.ceil(n_test / 100)) == 0):
				sys.stdout.write(".")
				sys.stdout.flush()

			B = covOld[ n_task, :, i ]
			C = covOld[ n_task, :, i ].transpose()
			D = vf[ obj ][ i ]

			# We invert the matrix using block inversion

			Anew = Ainv + np.outer(np.dot(Ainv, B), np.dot(C, Ainv)) * 1.0 / (D - np.sum(C * np.dot(Ainv, B)))
			Dnew = 1.0 / (D - np.dot(np.dot(C, Ainv), B))
			Bnew = - np.dot(Ainv, B) * Dnew
			Cnew = - 1.0 / D * np.dot(C, Anew)

			# We add the contribution of the approximate factors

			V = np.vstack((np.hstack((Anew, Bnew.reshape((n_pset, 1)))), np.append(Cnew, Dnew).reshape((1, n_pset + 1))))
			m = np.dot(V, np.append(mPset[ obj ], mf[ obj ][ i ]))

			mnew = (m + np.append(mTilde_pset[ n_task, :, i ], np.sum(mTilde_test[ n_task, :, i ]))) * damping + (1 - damping) * m

			Anew = (Anew + np.diag(vTilde_pset[ n_task, :, i ])) * damping + (1 - damping ) * Anew
			Bnew = (Bnew + vTilde_cov[ n_task, :, i ]) * damping + (1 - damping) * Bnew
			Cnew = (Cnew + vTilde_cov[ n_task, :, i ]) * damping + (1 - damping) * Cnew
			Dnew = (Dnew + np.sum(vTilde_test[ n_task, : , i ])) * damping + (1 - damping) * Dnew

			# We perform the computation of D by inverting the V matrix after adding the params of the approx factors

#			Anew_inv = matrixInverse(Anew)
			Anew_inv = np.linalg.inv(Anew)

			D = 1.0 / (Dnew - np.sum(Bnew * np.dot(Anew_inv, Cnew)))
			aux = np.outer(np.dot(Anew_inv, Bnew), np.dot(Cnew, Anew_inv))
			A = Anew_inv +  aux * 1.0 / (Dnew - np.sum(Cnew * np.dot(Anew_inv, Bnew)))
			B = - np.dot(Anew_inv, Bnew) * D
			C = - 1.0 / Dnew * np.dot(Cnew, A)

			V = np.vstack((np.hstack((A, B.reshape((n_pset, 1)))), np.append(C, D).reshape((1, n_pset + 1))))

			vfNew[ obj ][ i ] = D
			mfNew[ obj ][ i ] = np.dot(V, mnew)[ n_pset ]

		n_task += 1
		print ''

	for obj in all_tasks:
		if np.any(vfNew[ obj ] <= 0):
			raise Exception("vfnew is negative: %g at index %d" % (np.min(vfNew[ obj ]), np.argmin(vfNew[ obj ])))
		if np.any(np.isnan(vfNew[ obj ])):
			raise Exception("vfnew constrains nan")

	return {'mf': mfNew, 'vf':vfNew, 'mfo': mf, 'vfo': vf}

	# don't bother computing mf and mc since they are not used in the acquisition function
	# m = mean, v = var, f = objective, c = constraint

# Method that approximates the predictive distribution at a particular location using ADF.

def predictEP_adf(obj_models, a, pareto_set, Xtest, minimize=True):

	# used to switch between minimizing and maximizing

	sgn = -1.0 if minimize else 1.0

	objs = a['objs']
	all_tasks = objs

	n_obs = a['n_obs']
	n_pset = a['n_pset']
	n_total = a['n_total']
	n_test = Xtest.shape[ 0 ]
	q = a['q']

	Kstar = dict()
	mf = dict()
	mP = dict()
	mPset = dict()
	vf = dict()
	vP = dict()
	cov = dict()
	vPset = dict()

	# This is used for the comutation of the variance of the predictive distribution

	ahfHatNew = dict()
	bhfHatNew = dict()

	mfOld = dict()
	VfOld = dict()
	ahfHatNew = dict()
	bhfHatNew = dict()

	for obj in all_tasks:
		mfOld[ obj ] = np.zeros((n_pset, 2))
		VfOld[ obj ] = np.zeros((n_pset, 2, 2))
		ahfHatNew[ obj ] = np.zeros((n_pset, 2, 2))
		bhfHatNew[ obj ] = np.zeros((n_pset, 2))

	# First data includes the pareto set. Then, the test point

	Xtest_ext = np.vstack((a['X'][ 0 : n_pset, : ], Xtest))

	for obj in all_tasks:

		# We compute the means and variances of each point (test and pareto set)

		Kstar[ obj ], mP[ obj ], vP[ obj ] = gp_prediction_given_chol_K(a['X'], Xtest_ext,
			a['cholKstarstar'][ obj ], a['cholV'][ obj ], a['m'][ obj ], all_tasks[ obj ], a['jitter'][obj])
		vf[ obj ] = vP[ obj ][ n_pset : (n_pset + n_test) ]
		vPset[ obj ] = vP[ obj ][ 0 : n_pset ]
		mPset[ obj ] = mP[ obj ][ 0 : n_pset ]
		mf[ obj ] = mP[ obj ][ n_pset : (n_pset + n_test) ]

		# Now we compute the covariances between the test data and the pareto set

		Kstarstar = obj_models[ obj ].noiseless_kernel.cross_cov(Xtest_ext[ 0 : n_pset, : ], Xtest_ext[ n_pset : (n_pset + n_test), : ])
		aux1 = spla.solve_triangular(a['cholKstarstar'][ obj ].T, Kstar[ obj ][ : , 0 : n_pset  ], lower=True)
		aux2 = spla.solve_triangular(a['cholKstarstar'][ obj ].T, Kstar[ obj ][ :, n_pset : (n_pset + n_test) ], lower=True)
		aux11 = np.dot(a['cholV'][ obj ], spla.solve_triangular(a['cholKstarstar'][ obj ], aux1, lower=False))
		aux12 = np.dot(a['cholV'][ obj ], spla.solve_triangular(a['cholKstarstar'][ obj ], aux2, lower=False))
		cov[ obj ] = Kstarstar - np.dot(aux1.transpose(), aux2) + np.dot(aux11.transpose(), aux12)

	# scale things for stability

	for obj in all_tasks:
		cov[ obj ] = cov[ obj ] * 0.95

#	for obj in all_tasks:
#		scale = (1.0 - 1e-6) * np.ones(cov[ obj ].shape)
#		vf_tmp = np.repeat(vf[ obj ], cov[ obj ].shape[ 0 ]).reshape(cov[ obj ].shape[ ::-1 ]).transpose()
#		vpset_tmp = np.repeat(vPset[ obj ], cov[ obj ].shape[ 1 ]).reshape(cov[ obj ].shape)
#		index = vf_tmp + vpset_tmp -  2.0 * scale * cov[ obj ] < 1e-10
#
#		while np.any(index):
#			scale[ index ] = scale[ index ]**2
#			index = vf_tmp + vpset_tmp -  2.0 * scale * cov[ obj ] < 1e-10
#
 #   		cov[ obj ] = scale * cov[ obj ]

	# We update the predictive distribution to take into account that it has to be dominated by the paretoset
	# For this we use a single parallel update of the factors

	# We compute an "old" distribution which is the unconstrained distribution

	mOld_pset = np.zeros((q, n_pset, n_test))
	mOld_test = np.zeros((q, n_pset, n_test))
	vOld_pset = np.zeros((q, n_pset, n_test))
	vOld_test = np.zeros((q, n_pset, n_test))
	covOld = np.zeros((q, n_pset, n_test))

	n_task = 0
	for obj in all_tasks:
		mOld_pset[ n_task, :, : ] = np.repeat(mPset[ obj ], n_test).reshape(((n_pset, n_test)))
		mOld_test[ n_task, :, : ] = np.repeat(mf[ obj ], n_pset).reshape(((n_test, n_pset))).transpose()
		vOld_pset[ n_task, :, : ] = np.repeat(vPset[ obj ], n_test).reshape(((n_pset, n_test)))
		vOld_test[ n_task, :, : ] = np.repeat(vf[ obj ], n_pset).reshape(((n_test, n_pset))).transpose()
		covOld[ n_task, :, : ] = cov[ obj ]
		n_task += 1

	# We comupte a new distribution by procesing each factor

	vfNew = dict()
	mfNew = dict()

	for obj in all_tasks:
		vfNew[ obj ] = np.zeros( n_test )
		mfNew[ obj ] = np.zeros( n_test )

	vOld_full_pset = dict()

	for obj in all_tasks:
		Kstarstar = obj_models[ obj ].noiseless_kernel.cross_cov(a['X'][ 0 : n_pset, : ], a['X'][ 0 : n_pset, : ])
		Kstar = obj_models[ obj ].noiseless_kernel.cross_cov(a['X'], a['X'][ 0 : n_pset, : ])
		aux1 = spla.solve_triangular(a['cholKstarstar'][ obj ].T, Kstar, lower=True)
		aux2 = spla.solve_triangular(a['cholKstarstar'][ obj ].T, Kstar, lower=True)
		aux11 = np.dot(a['cholV'][ obj ], spla.solve_triangular(a['cholKstarstar'][ obj ], aux1, lower=False))
		aux12 = np.dot(a['cholV'][ obj ], spla.solve_triangular(a['cholKstarstar'][ obj ], aux2, lower=False))
		vOld_full_pset[ obj ] = Kstarstar - np.dot(aux1.transpose(), aux2) + np.dot(aux11.transpose(), aux12) + \
		np.eye(n_pset) * a['jitter'][obj]

	for i in range(n_test):

		if ((i % np.ceil(n_test / 100)) == 0):
			sys.stdout.write(".")
			sys.stdout.flush()

		V = dict()
		Vinv = dict()
		m = dict()
		m_nat = dict()

		# We compute the means and covariance matrix of the predictive distribution for each point

		n_task = 0
		for obj in all_tasks:

			A = vOld_full_pset[ obj ].copy()
			Ainv = matrixInverse(A)

			B = covOld[ n_task, :, i ]
			C = covOld[ n_task, :, i ].transpose()
			D = vf[ obj ][ i ]

			V[ obj ] = np.vstack((np.hstack((A, B.reshape((n_pset, 1)))), np.append(C, D).reshape((1, n_pset + 1))))
			m[ obj ] = np.append(mPset[ obj ], mf[ obj ][ i ])

			# We invert the matrix using block inversion

			Anew = Ainv + np.outer(np.dot(Ainv, B), np.dot(C, Ainv)) * 1.0 / (D - np.sum(C * np.dot(Ainv, B)))
			Dnew = 1.0 / (D - np.dot(np.dot(C, Ainv), B))
			Bnew = - np.dot(Ainv, B) * Dnew
			Cnew = - 1.0 / D * np.dot(C, Anew)

			Vinv[ obj ] = np.vstack((np.hstack((Anew, Bnew.reshape((n_pset, 1)))), np.append(Cnew, Dnew).reshape((1, n_pset + 1))))
			m_nat[ obj ] = np.dot(Vinv[ obj ], m[ obj ])

			n_task += 1

		for j in range(n_pset):

			s = vOld_pset[ :, j, i ] + vOld_test[ :, j, i ] - 2 * covOld[ :, j, i ]

			if np.any(np.logical_or(s < 0, s == 0)):
				raise npla.linalg.LinAlgError("Negative or zero value in the sqrt!")

			alpha = (mOld_test[ :, j, i ] - mOld_pset[ :, j, i ]) / np.sqrt(s) * sgn

			log_phi = logcdf_robust(alpha)
		       	logZ = log_1_minus_exp_x(np.sum(log_phi))
			log_phi_sum = np.sum(log_phi)

			ratio = - np.exp(sps.norm.logpdf(alpha) - logZ + log_phi_sum - log_phi)

			dlogZdmfOld_test = ratio / np.sqrt(s) * sgn
			dlogZdmfOld_pset = ratio / np.sqrt(s) * sgn * -1.0

			dlogZdVfOld_test = -0.5 * ratio * alpha / s
			dlogZdVfOld_pset = -0.5 * ratio * alpha / s
			dlogZdVfOld_cov = -0.5 * ratio * alpha / s * -1.0

			# The following lines compute the updates in parallel C = dmdm - 2 dv
			# First the first natural parameter

			c_11 = dlogZdmfOld_test * dlogZdmfOld_test - 2 * dlogZdVfOld_test
			c_22 = dlogZdmfOld_pset * dlogZdmfOld_pset - 2 * dlogZdVfOld_pset
			c_12 = dlogZdmfOld_pset * dlogZdmfOld_test - 2 * dlogZdVfOld_cov

			cp_11 = c_11 * vOld_test[ :, j, i ] + c_12 * covOld[ :, j, i ]
			cp_12 = c_11 * covOld[ :, j, i ] + c_12 * vOld_pset[ :, j, i ]
			cp_21 = c_12 * vOld_test[ :, j, i ] + c_22 * covOld[ :, j, i ]
			cp_22 = c_12 * covOld[ :, j, i ] + c_22 * vOld_pset[ :, j, i ]

			vNew_test = vOld_test[ :, j, i ] - (vOld_test[ :, j, i ] * cp_11 + covOld[ :, j, i ] * cp_21)
			vNew_cov = covOld[ :, j, i ] - (vOld_test[ :, j, i ] * cp_12 + covOld[ :, j, i ] * cp_22)
			vNew_pset = vOld_pset[ :, j, i ] - (covOld[ :, j, i ] * cp_12 + vOld_pset[ :, j, i ] * cp_22)

			det = vNew_test * vNew_pset - vNew_cov * vNew_cov
			vNew_inv_test = 1.0 / det * vNew_pset
			vNew_inv_pset = 1.0 / det * vNew_test
			vNew_inv_cov = 1.0 / det * - vNew_cov

			det = vOld_test[ :, j, i ] * vOld_pset[ :, j, i ] - covOld[ :, j, i ] * covOld[ :, j, i ]
			vOld_inv_test = 1.0 / det * vOld_pset[ :, j, i ]
			vOld_inv_pset = 1.0 / det * vOld_test[ :, j, i ]
			vOld_inv_cov = 1.0 / det * - covOld[ :, j, i ]

			# This is the approx factor

			vTilde_test = vNew_inv_test - vOld_inv_test
			vTilde_pset = vNew_inv_pset - vOld_inv_pset
			vTilde_cov = vNew_inv_cov - vOld_inv_cov

			# Now the second natural parameter = A~ (mOld + Vold dlogz_dm) + dlogz_dm

			v_1 = mOld_test[ :, j, i ] + vOld_test[ :, j, i ] * dlogZdmfOld_test + covOld[ :, j, i ] * dlogZdmfOld_pset
			v_2 = mOld_pset[ :, j, i ] + covOld[ :, j, i ] * dlogZdmfOld_test + vOld_pset[ :, j, i ] * dlogZdmfOld_pset

			mTilde_test = vTilde_test * v_1 + vTilde_cov * v_2 + dlogZdmfOld_test
			mTilde_pset = vTilde_cov * v_1 + vTilde_pset * v_2 + dlogZdmfOld_pset

			# Now we have to update the means and the variances of each task

			vTilde = np.zeros((2 , 2))

			n_task = 0
			for obj in all_tasks:

				# We do the four rank-1 updates of the covariance matrix

				Vinv[ obj ][ j, j ] = Vinv[ obj ][ j, j ] + vTilde_pset[ n_task ]
				Vinv[ obj ][ n_pset, n_pset ] = Vinv[ obj ][ n_pset, n_pset ] + vTilde_test[ n_task ]
				Vinv[ obj ][ n_pset, j ] = Vinv[ obj ][ n_pset, j ] + vTilde_cov[ n_task ]
				Vinv[ obj ][ j, n_pset ] = Vinv[ obj ][ j, n_pset ] + vTilde_cov[ n_task ]

				vTilde[ 0, 0 ] = vTilde_test[ n_task ]
				vTilde[ 1, 0 ] = vTilde_cov[ n_task ]
				vTilde[ 0, 1 ] = vTilde_cov[ n_task ]
				vTilde[ 1, 1 ] = vTilde_pset[ n_task ]

				delta = np.zeros((2, n_pset + 1))
				delta[ 0, j ] = 1
				delta[ 1, n_pset ] = 1
				deltaV = np.dot(delta, V[ obj ])
				vTilde_delta = np.dot(vTilde, delta)
				vTilde_deltaV = np.dot(vTilde, deltaV)
				M = np.linalg.inv(np.eye(2) + np.dot(vTilde_delta, deltaV.T))

				V[ obj ] = V[ obj ] - np.dot(np.dot(deltaV.T, M), vTilde_deltaV)

				# We update the means

				m_nat[ obj ][ j ] = m_nat[ obj ][ j ] + mTilde_pset[ n_task ]
				m_nat[ obj ][ n_pset ] = m_nat[ obj ][ n_pset ] + mTilde_test[ n_task ]
				m[ obj ] = np.dot(V[ obj ], m_nat[ obj ])

				# We update the vectors that store the current approximation

				vOld_pset[ n_task, :, i ] = np.diag(V[ obj ])[ 0 : n_pset ]
				vOld_test[ n_task, :, i ] = np.diag(V[ obj ])[ n_pset ]
				mOld_pset[ n_task, :, i ] = m[ obj ][ 0 : n_pset ]
				mOld_test[ n_task, :, i ] = m[ obj ][ n_pset ]
				covOld[ n_task, :, i ] = V[ obj ][ 0 : n_pset, n_pset ]

				n_task += 1

	print ''

	n_task = 0
	for obj in all_tasks:
		vfNew[ obj ] = vOld_test[ n_task, 0, : ]
		mfNew[ obj ] = mOld_test[ n_task, 0, : ]
		n_task += 1

	for obj in all_tasks:
		if np.any(vfNew[ obj ] <= 0):
			raise Exception("vfnew is negative: %g at index %d" % (np.min(vfNew[ obj ]), np.argmin(vfNew[ obj ])))
		if np.any(np.isnan(vfNew[ obj ])):
			raise Exception("vfnew constrains nan")

	return {'mf': mfNew, 'vf':vfNew, 'mfo': mf, 'vfo': vf}

	# don't bother computing mf and mc since they are not used in the acquisition function
	# m = mean, v = var, f = objective, c = constraint


# Method that approximates the predictive distribution at a particular location using ADF.

def predictEP_adf_parallel(obj_models, a, pareto_set, Xtest, minimize=True):

	# used to switch between minimizing and maximizing

	sgn = -1.0 if minimize else 1.0

	objs = a['objs']
	all_tasks = objs

	n_obs = a['n_obs']
	n_pset = a['n_pset']
	n_total = a['n_total']
	n_test = Xtest.shape[ 0 ]
	q = a['q']

	Kstar = dict()
	mf = dict()
	mP = dict()
	mPset = dict()
	vf = dict()
	vP = dict()
	cov = dict()
	vPset = dict()

	# This is used for the comutation of the variance of the predictive distribution

	ahfHatNew = dict()
	bhfHatNew = dict()

	mfOld = dict()
	VfOld = dict()
	ahfHatNew = dict()
	bhfHatNew = dict()

	for obj in all_tasks:
		mfOld[ obj ] = np.zeros((n_pset, 2))
		VfOld[ obj ] = np.zeros((n_pset, 2, 2))
		ahfHatNew[ obj ] = np.zeros((n_pset, 2, 2))
		bhfHatNew[ obj ] = np.zeros((n_pset, 2))

	# First data includes the pareto set. Then, the test point

	Xtest_ext = np.vstack((a['X'][ 0 : n_pset, : ], Xtest))

	for obj in all_tasks:

		# We compute the means and variances of each point (test and pareto set)

		Kstar[ obj ], mP[ obj ], vP[ obj ] = gp_prediction_given_chol_K(a['X'], Xtest_ext,
			a['cholKstarstar'][ obj ], a['cholV'][ obj ], a['m'][ obj ], all_tasks[ obj ], a['jitter'][obj])
		vf[ obj ] = vP[ obj ][ n_pset : (n_pset + n_test) ]
		vPset[ obj ] = vP[ obj ][ 0 : n_pset ]
		mPset[ obj ] = mP[ obj ][ 0 : n_pset ]
		mf[ obj ] = mP[ obj ][ n_pset : (n_pset + n_test) ]

		# Now we compute the covariances between the test data and the pareto set

		Kstarstar = obj_models[ obj ].noiseless_kernel.cross_cov(Xtest_ext[ 0 : n_pset, : ], Xtest_ext[ n_pset : (n_pset + n_test), : ])
		aux1 = spla.solve_triangular(a['cholKstarstar'][ obj ].T, Kstar[ obj ][ : , 0 : n_pset  ], lower=True)
		aux2 = spla.solve_triangular(a['cholKstarstar'][ obj ].T, Kstar[ obj ][ :, n_pset : (n_pset + n_test) ], lower=True)
		aux11 = np.dot(a['cholV'][ obj ], spla.solve_triangular(a['cholKstarstar'][ obj ], aux1, lower=False))
		aux12 = np.dot(a['cholV'][ obj ], spla.solve_triangular(a['cholKstarstar'][ obj ], aux2, lower=False))
		cov[ obj ] = Kstarstar - np.dot(aux1.transpose(), aux2) + np.dot(aux11.transpose(), aux12)

	# scale things for stability

	for obj in all_tasks:
		scale = (1.0 - 1e-4) * np.ones(cov[ obj ].shape)
		vf_tmp = np.repeat(vf[ obj ], cov[ obj ].shape[ 0 ]).reshape(cov[ obj ].shape[ ::-1 ]).transpose()
		vpset_tmp = np.repeat(vPset[ obj ], cov[ obj ].shape[ 1 ]).reshape(cov[ obj ].shape)
		index = vf_tmp + vpset_tmp -  2.0 * scale * cov[ obj ] < 1e-10

		while np.any(index):
			scale[ index ] = scale[ index ]**2
			index = vf_tmp + vpset_tmp -  2.0 * scale * cov[ obj ] < 1e-10

    		cov[ obj ] = scale * cov[ obj ]

	# We update the predictive distribution to take into account that it has to be dominated by the paretoset
	# For this we use a single parallel update of the factors

	# We compute an "old" distribution which is the unconstrained distribution

	mOld_pset = np.zeros((q, n_pset, n_test))
	mOld_test = np.zeros((q, n_pset, n_test))
	vOld_pset = np.zeros((q, n_pset, n_test))
	vOld_test = np.zeros((q, n_pset, n_test))
	covOld = np.zeros((q, n_pset, n_test))

	n_task = 0
	for obj in all_tasks:
		mOld_pset[ n_task, :, : ] = np.repeat(mPset[ obj ], n_test).reshape(((n_pset, n_test)))
		mOld_test[ n_task, :, : ] = np.repeat(mf[ obj ], n_pset).reshape(((n_test, n_pset))).transpose()
		vOld_pset[ n_task, :, : ] = np.repeat(vPset[ obj ], n_test).reshape(((n_pset, n_test)))
		vOld_test[ n_task, :, : ] = np.repeat(vf[ obj ], n_pset).reshape(((n_test, n_pset))).transpose()
		covOld[ n_task, :, : ] = cov[ obj ]
		n_task += 1

	# We comupte a new distribution by procesing each factor

	vfNew = dict()
	mfNew = dict()

	for obj in all_tasks:
		vfNew[ obj ] = np.zeros( n_test )
		mfNew[ obj ] = np.zeros( n_test )

	vOld_full_pset = dict()
	vOld_full_pset = dict()

	for obj in all_tasks:
		Kstarstar = obj_models[ obj ].noiseless_kernel.cross_cov(a['X'][ 0 : n_pset, : ], a['X'][ 0 : n_pset, : ])
		Kstar = obj_models[ obj ].noiseless_kernel.cross_cov(a['X'], a['X'][ 0 : n_pset, : ])
		aux1 = spla.solve_triangular(a['cholKstarstar'][ obj ].T, Kstar, lower=True)
		aux2 = spla.solve_triangular(a['cholKstarstar'][ obj ].T, Kstar, lower=True)
		aux11 = np.dot(a['cholV'][ obj ], spla.solve_triangular(a['cholKstarstar'][ obj ], aux1, lower=False))
		aux12 = np.dot(a['cholV'][ obj ], spla.solve_triangular(a['cholKstarstar'][ obj ], aux2, lower=False))
		vOld_full_pset[ obj ] = Kstarstar - np.dot(aux1.transpose(), aux2) + np.dot(aux11.transpose(), aux12) + \
		np.eye(n_pset) * a['jitter'][obj]

	# These are the approximate factors

	vTilde_test = np.zeros((q, n_pset, n_test))
	vTilde_pset = np.zeros((q, n_pset, n_test))
	vTilde_cov  = np.zeros((q, n_pset, n_test))
	mTilde_test = np.zeros((q, n_pset, n_test))
	mTilde_pset = np.zeros((q, n_pset, n_test))

	# We precompute the initial distributions for each point and the pareto set

	vA = dict()
	vB = dict()
	vC = dict()
	vD = dict()
	m_mean = dict()

	vinv_A = dict()
	inv_vinv_A = dict()
	vinv_B = dict()
	vinv_C = dict()
	vinv_D = dict()
	m_nat = dict()

	mat_to_repeat = np.tile(np.eye(n_pset), n_test).T

	n_task = 0
	for obj in all_tasks:

		A = vOld_full_pset[ obj ]
		B = covOld[ n_task, :, : ]
		C = B.T
		D = vf[ obj ]

		vA[ obj ] = np.tile(A, n_test).reshape((n_pset, n_test, n_pset)).swapaxes(0, 1)
		vB[ obj ] = B
		vC[ obj ] = C
		vD[ obj ] = D

		Ainv = matrixInverse(A)
		aux1 = np.dot(Ainv, B)
		aux2 = aux1.T
		aux3 =  np.sum(aux1 * C.T, axis = 0)

		Anew = np.tile(Ainv, n_test).reshape((n_pset, n_test, n_pset)).swapaxes(0, 1)
		value1 = np.tile(aux1.T, n_pset).reshape((n_test, n_pset, n_pset)).swapaxes(1, 2)
		value3 = np.tile(1.0 / (D - aux3), n_pset).reshape((n_pset, n_test)).swapaxes(0, 1)
		value2 = np.tile(aux2 * value3, n_pset).reshape((n_test, n_pset, n_pset))

		Anew = Anew + value1 * value2
		Dnew = 1.0 / (D - aux3)
		Bnew = - np.dot(Ainv, B).T * np.tile(Dnew, n_pset).reshape((n_pset, n_test)).T
		Cnew = Bnew

		vinv_A[ obj ] = Anew
		vinv_B[ obj ] = Bnew
		vinv_C[ obj ] = Cnew
		vinv_D[ obj ] = Dnew

		# Now we compute the inverse of Anew which is required later on for the updates

		inv_vinv_A[ obj ] = np.tile(A, n_test).reshape((n_pset, n_test, n_pset)).swapaxes(0, 1)
		value1 = np.tile(B.T, n_pset).reshape((n_test, n_pset, n_pset)).swapaxes(1, 2)
		value3 = np.tile(1.0 / D, n_pset).reshape((n_pset, n_test)).swapaxes(0, 1)
		value2 = np.tile(C * value3, n_pset).reshape((n_test, n_pset, n_pset))

		inv_vinv_A[ obj ] = inv_vinv_A[ obj ] - value1 * value2

		# Now the means and the corresponding natural parameters

		m_nat[ obj ] = np.zeros((n_test, n_pset + 1))
		m_mean[ obj ] = np.hstack((np.tile(mPset[ obj ], n_test).reshape((n_test, n_pset)), mf[ obj ].reshape((n_test, 1))))

		aux = np.tile(m_mean[ obj ][ :, 0 : n_pset ], n_pset).reshape((n_test, n_pset, n_pset)).swapaxes(1,2)
		aux = np.sum(aux * vinv_A[ obj ], axis = 1)
		m_nat[ obj ][ :, 0 : n_pset ] = aux + np.tile(m_mean[ obj ][ :, n_pset ], n_pset).reshape((n_pset, n_test)).T * vinv_B[ obj ]
		m_nat[ obj ][ :, n_pset ] = np.sum(m_mean[ obj ][ :, 0 : n_pset ] * vinv_B[ obj ], axis = 1) \
			+ m_mean[ obj ][ :, n_pset ] * vinv_D[ obj ]

		n_task += 1


	for j in range(n_pset):

		sys.stdout.write(".")
		sys.stdout.flush()

		# We comupte a new distribution

		s = vOld_pset[ :, j, : ] + vOld_test[ :, j, : ] - 2 * covOld[ :, j, : ]
		alpha = (mOld_test[ :, j, : ] - mOld_pset[ :, j, : ]) / np.sqrt(s) * sgn

		if np.any(s < 0):
			raise npla.linalg.LinAlgError("Negative value in the sqrt!")

		log_phi = logcdf_robust(alpha)
       		logZ = np.repeat(log_1_minus_exp_x(np.sum(log_phi, axis = 0)).transpose(), q).reshape((n_test, q)).transpose()
		log_phi_sum = np.repeat(np.sum(log_phi, axis = 0).transpose(), q).reshape((n_test, q)).transpose()

		ratio = - np.exp(sps.norm.logpdf(alpha) - logZ + log_phi_sum - log_phi)

		dlogZdmfOld_test = ratio / np.sqrt(s) * sgn
		dlogZdmfOld_pset = ratio / np.sqrt(s) * sgn * -1.0

		dlogZdVfOld_test = -0.5 * ratio * alpha / s
		dlogZdVfOld_pset = -0.5 * ratio * alpha / s
		dlogZdVfOld_cov = -0.5 * ratio * alpha / s * -1.0

		# The following lines compute the updates in parallel C = dmdm - 2 dv
		# First the first natural parameter

		c_11 = dlogZdmfOld_test * dlogZdmfOld_test - 2 * dlogZdVfOld_test
		c_22 = dlogZdmfOld_pset * dlogZdmfOld_pset - 2 * dlogZdVfOld_pset
		c_12 = dlogZdmfOld_pset * dlogZdmfOld_test - 2 * dlogZdVfOld_cov

		cp_11 = c_11 * vOld_test[ :, j, : ] + c_12 * covOld[ :, j, : ]
		cp_12 = c_11 * covOld[ :, j, : ] + c_12 * vOld_pset[ :, j, : ]
		cp_21 = c_12 * vOld_test[ :, j, : ] + c_22 * covOld[ :, j, : ]
		cp_22 = c_12 * covOld[ :, j, : ] + c_22 * vOld_pset[ :, j, : ]

		vNew_test = vOld_test[ :, j, : ] - (vOld_test[ :, j, : ] * cp_11 + covOld[ :, j, : ] * cp_21)
		vNew_cov = covOld[ :, j, : ] - (vOld_test[ :, j, : ] * cp_12 + covOld[ :, j, : ] * cp_22)
		vNew_pset = vOld_pset[ :, j, : ] - (covOld[ :, j, : ] * cp_12 + vOld_pset[ :, j, : ] * cp_22)

		det = vNew_test * vNew_pset - vNew_cov * vNew_cov
		vNew_inv_test = 1.0 / det * vNew_pset
		vNew_inv_pset = 1.0 / det * vNew_test
		vNew_inv_cov = 1.0 / det * - vNew_cov

		det = vOld_test[ :, j, : ] * vOld_pset[ :, j, : ] - covOld[ :, j, : ] * covOld[ :, j, : ]
		vOld_inv_test = 1.0 / det * vOld_pset[ :, j, : ]
		vOld_inv_pset = 1.0 / det * vOld_test[ :, j, : ]
		vOld_inv_cov = 1.0 / det * - covOld[ :, j, : ]

		# This is the approx factor

		vTilde_test[ :, j, : ] = vNew_inv_test - vOld_inv_test
		vTilde_pset[ :, j, : ] = vNew_inv_pset - vOld_inv_pset
		vTilde_cov[ :, j, : ] = vNew_inv_cov - vOld_inv_cov

		v_1 = mOld_test[ :, j, : ] + vOld_test[ :, j, : ] * dlogZdmfOld_test + covOld[ :, j, : ] * dlogZdmfOld_pset
		v_2 = mOld_pset[ :, j, : ] + covOld[ :, j, : ] * dlogZdmfOld_test + vOld_pset[ :, j, : ] * dlogZdmfOld_pset

		mTilde_test[ :, j, : ] = vTilde_test[ :, j, : ] * v_1 + vTilde_cov[ :, j, : ] * v_2 + dlogZdmfOld_test
		mTilde_pset[ :, j, : ] = vTilde_cov[ :, j, : ] * v_1 + vTilde_pset[ :, j, : ] * v_2 + dlogZdmfOld_pset

		# We now compute the updated means and variances and covariances for each point in parallel

		n_task = 0
		for obj in all_tasks:

			# We update the inverse covariance matrix. For this we use block inversion

			# First we compute inv_vinv_A after the update

			aux = inv_vinv_A[ obj ][ :, :, j ]
			value1 = np.tile(aux, n_pset).reshape((n_test, n_pset, n_pset)).swapaxes(1, 2)
			value3 = np.tile(1.0 / (1.0 / vTilde_pset[ n_task, j, : ] + inv_vinv_A[ obj ][ :, j, j ]), \
				n_pset).reshape((n_pset, n_test)).swapaxes(0, 1)
			value2 = np.tile(aux * value3, n_pset).reshape((n_test, n_pset, n_pset))

			inv_vinv_A[ obj ] = inv_vinv_A[ obj ] - value1 * value2

			# We compute vinv_A after the update

			aux = np.zeros((n_test, n_pset, n_pset))
			aux[ :, j, j ] = vTilde_pset[ n_task, j, : ]
			vinv_A[ obj ] = vinv_A[ obj ] + aux

			aux = np.zeros((n_test, n_pset))
			aux[ :, j ] = vTilde_cov[ n_task, j, : ]
			vinv_B[ obj ] = vinv_B[ obj ] + aux
			vinv_C[ obj ] = vinv_B[ obj ]
			vinv_D[ obj ] = vinv_D[ obj ] + vTilde_test[ n_task, j, : ]

			# We update the covariance matrix

			aux = inv_vinv_A[ obj ] * np.tile(vinv_B[ obj ], n_pset).reshape((n_test, n_pset, n_pset)).swapaxes(1,2)
			aux = np.sum(aux, axis = 1)
			aux2 = np.sum(aux * vinv_B[ obj ], axis = 1)

			value1 = np.tile(aux, n_pset).reshape((n_test, n_pset, n_pset)).swapaxes(1, 2)
			value3 = np.tile(1.0 / (vinv_D[ obj ] - aux2), n_pset).reshape((n_pset, n_test)).swapaxes(0, 1)
			value2 = np.tile(aux * value3, n_pset).reshape((n_test, n_pset, n_pset))

			Anew = inv_vinv_A[ obj ] + value1 * value2
			Dnew = 1.0 / (vinv_D[ obj ] - aux2)
			Bnew = - aux * np.tile(Dnew, n_pset).reshape((n_pset, n_test)).T
			Cnew = Bnew

			vA[ obj ] = Anew
			vB[ obj ] = Bnew
			vC[ obj ] = Bnew
			vD[ obj ] = Dnew

			# Now we update the means and the first natural parameter

			m_nat[ obj ][ :, j ] = m_nat[ obj ][ :, j ] +  mTilde_pset[ n_task, j, : ]
			m_nat[ obj ][ :, n_pset ] = m_nat[ obj ][ :, n_pset ] +  mTilde_test[ n_task, j, : ]

			aux = np.tile(m_nat[ obj ][ :, 0 : n_pset ], n_pset).reshape((n_test, n_pset, n_pset)).swapaxes(1,2)
			aux = np.sum(aux * vA[ obj ], axis = 1)
			m_mean[ obj ][ :, 0 : n_pset ] = aux + np.tile(m_nat[ obj ][ :, n_pset ], n_pset).reshape((n_pset, n_test)).T * vB[ obj ]
			m_mean[ obj ][ :, n_pset ] = np.sum(m_nat[ obj ][ :, 0 : n_pset ] * vB[ obj ], axis = 1) \
				+ m_nat[ obj ][ :, n_pset ] * vD[ obj ]

			# We update the old distribution for the following ADF update

			vOld_test[ n_task, :, : ] = np.tile(vD[ obj ], n_pset).reshape((n_pset, n_test))
			vOld_pset[ n_task, :, : ] = np.sum(vA[ obj ] * np.tile(np.eye(n_pset), \
				n_test).reshape((n_pset, n_test, n_pset)).swapaxes(0,1), axis = 1).T
			covOld[ n_task, :, : ] = vB[ obj ].T

			mOld_test[ n_task, :, : ] = np.tile(m_mean[ obj ][ :, n_pset ], n_pset).reshape((n_pset, n_test))
			mOld_pset[ n_task, :, : ] = m_mean[ obj ][ :, 0 : n_pset ].T

			n_task += 1

	print ''

	n_task = 0
	for obj in all_tasks:
		vfNew[ obj ] = vOld_test[ n_task, 0, : ]
		mfNew[ obj ] = mOld_test[ n_task, 0, : ]
		n_task += 1

	for obj in all_tasks:
		if np.any(vfNew[ obj ] <= 0):
			raise Exception("vfnew is negative: %g at index %d" % (np.min(vfNew[ obj ]), np.argmin(vfNew[ obj ])))
		if np.any(np.isnan(vfNew[ obj ])):
			raise Exception("vfnew constrains nan")

	return {'mf': mfNew, 'vf':vfNew, 'mfo': mf, 'vfo': vf}

	# don't bother computing mf and mc since they are not used in the acquisition function
	# m = mean, v = var, f = objective, c = constraint


"""
See Miguel's paper (http://arxiv.org/pdf/1406.2541v1.pdf) section 2.1 and Appendix A

Returns a function the samples from the approximation...

if testing=True, it does not return the result but instead the random cosine for testing only

We express the kernel as an expectation. But then we approximate the expectation with a weighted sum
theta are the coefficients for this weighted sum. that is why we take the dot product of theta at the end
we also need to scale at the end so that it's an average of the random features.

if use_woodbury_if_faster is False, it never uses the woodbury version
"""
def sample_gp_with_random_features(gp, nFeatures, testing=False, use_woodbury_if_faster=True):

    d = gp.num_dims
    N_data = gp.observed_values.size

    nu2 = gp.noise_value()

    sigma2 = gp.params['amp2'].value  # the kernel amplitude

    # We draw the random features
    if gp.options['kernel'] == "SquaredExp":
        W = npr.randn(nFeatures, d) / gp.params['ls'].value
    elif gp.options['kernel'] == "Matern52":
        m = 5.0/2.0
        W = npr.randn(nFeatures, d) / gp.params['ls'].value / np.sqrt(npr.gamma(shape=m, scale=1.0/m, size=(nFeatures,1)))
    else:
        raise Exception('This random feature sampling is for the squared exp or Matern5/2 kernels and you are using the %s' % gp.options['kernel'])
    b = npr.uniform(low=0, high=2*np.pi, size=nFeatures)[:,None]

    # Just for testing the  random features in W and b... doesn't test the weights theta

    if testing:
        return lambda x: np.sqrt(2 * sigma2 / nFeatures) * np.cos(np.dot(W, gp.noiseless_kernel.transformer.forward_pass(x).T) + b)

    randomness = npr.randn(nFeatures)

    # W has size nFeatures by d
    # tDesignMatrix has size Nfeatures by Ndata
    # woodbury has size Ndata by Ndata
    # z is a vector of length nFeatures

    if gp.has_data:
        tDesignMatrix = np.sqrt(2.0 * sigma2 / nFeatures) * np.cos(np.dot(W, \
		gp.noiseless_kernel.transformer.forward_pass(gp.observed_inputs).T) + b)

        if use_woodbury_if_faster and N_data < nFeatures:
            # you can do things in cost N^2d instead of d^3 by doing this woodbury thing

            # We obtain the posterior on the coefficients
            woodbury = np.dot(tDesignMatrix.T, tDesignMatrix) + nu2*np.eye(N_data)
            chol_woodbury = spla.cholesky(woodbury)
            # inverseWoodbury = chol2inv(chol_woodbury)
            z = np.dot(tDesignMatrix, gp.observed_values / nu2)
            # m = z - np.dot(tDesignMatrix, np.dot(inverseWoodbury, np.dot(tDesignMatrix.T, z)))
            m = z - np.dot(tDesignMatrix, spla.cho_solve((chol_woodbury, False), np.dot(tDesignMatrix.T, z)))
            # (above) alternative to original but with cho_solve

            # z = np.dot(tDesignMatrix, gp.observed_values / nu2)
            # m = np.dot(np.eye(nFeatures) - \
            # np.dot(tDesignMatrix, spla.cho_solve((chol_woodbury, False), tDesignMatrix.T)), z)

            # woodbury has size N_data by N_data
            D, U = npla.eigh(woodbury)
            # sort the eigenvalues (not sure if this matters)
            idx = D.argsort()[::-1] # in decreasing order instead of increasing
            D = D[idx]
            U = U[:,idx]
            R = 1.0 / (np.sqrt(D) * (np.sqrt(D) + np.sqrt(nu2)))
            # R = 1.0 / (D + np.sqrt(D*nu2))

            # We sample from the posterior of the coefficients
            theta = randomness - \
    np.dot(tDesignMatrix, np.dot(U, (R * np.dot(U.T, np.dot(tDesignMatrix.T, randomness))))) + m

        else:
            # all you are doing here is sampling from the posterior of the linear model
            # that approximates the GP
            # Sigma = matrixInverse(np.dot(tDesignMatrix, tDesignMatrix.T) / nu2 + np.eye(nFeatures))
            # m = np.dot(Sigma, np.dot(tDesignMatrix, gp.observed_values / nu2))
            # theta = m + np.dot(randomness, spla.cholesky(Sigma, lower=False)).T

            # Sigma = matrixInverse(np.dot(tDesignMatrix, tDesignMatrix.T) + nu2*np.eye(nFeatures))
            # m = np.dot(Sigma, np.dot(tDesignMatrix, gp.observed_values))
            # theta = m + np.dot(randomness, spla.cholesky(Sigma*nu2, lower=False)).T

            chol_Sigma_inverse = spla.cholesky(np.dot(tDesignMatrix, tDesignMatrix.T) + nu2*np.eye(nFeatures))
            Sigma = chol2inv(chol_Sigma_inverse)
            m = spla.cho_solve((chol_Sigma_inverse, False), np.dot(tDesignMatrix, gp.observed_values))
            theta = m + np.dot(randomness, spla.cholesky(Sigma*nu2, lower=False)).T


    else:
        # We sample from the prior -- same for Matern
        theta = npr.randn(nFeatures)

    def wrapper(x, gradient):
    # the argument "gradient" is
    # not the usual compute_grad that computes BOTH when true
    # here it only computes the objective when true

        if x.ndim == 1:
            x = x[None,:]

        x = gp.noiseless_kernel.transformer.forward_pass(x)

        if not gradient:
            result = np.dot(theta.T, np.sqrt(2.0 * sigma2 / nFeatures) * np.cos(np.dot(W, x.T) + b))
            if result.size == 1:
                result = float(result) # if the answer is just a number, take it out of the numpy array wrapper
                # (failure to do so messed up NLopt and it only gives a cryptic error message)
            return result
        else:
            grad = np.dot(theta.T, -np.sqrt(2.0 * sigma2 / nFeatures) * np.sin(np.dot(W, x.T) + b) * W)
	    return gp.noiseless_kernel.transformer.backward_pass(grad)

    return wrapper

"""
Given some approximations to the GP sample, find a subset of the pareto set
wrapper_functions should be a dict with keys 'objective' and optionally 'constraints'
"""
# find MINIMUM if minimize=True, else find a maximum

def global_optimization_of_GP_approximation(funs, num_dims, inputs, grid_default_chooser, minimize=True):

	moo = MOOP_basis_functions(funs['objectives'], num_dims, funs['constraints'])

	# XXX Currently it is only implemented the grid approach

	assert USE_GRID_ONLY == True

	if USE_GRID_ONLY == True:

#		moo.solve_using_grid(grid = sobol_grid.generate(num_dims, num_dims * GRID_SIZE))

                # We add the observations made

#		grid = np.vstack((sobol_grid.generate(num_dims, num_dims * GRID_SIZE), inputs))

                grid = np.vstack((np.random.uniform(size = ((num_dims * GRID_SIZE, num_dims)))))
#		grid = np.vstack((np.random.uniform(size = ((num_dims * GRID_SIZE, num_dims))), inputs))
#		grid = np.vstack((grid_default_chooser, np.random.uniform(size = ((num_dims * GRID_SIZE, num_dims))), inputs))
#               grid = grid[ np.random.permutation(grid.shape[ 0 ]), :]

                # This is to speed up the optimization and to avoid evaluating the constraints many times
                # on infeasible points

                grid = find_feasible_grid(funs['constraints'], grid)

                if grid is not None:

                    for objective in funs['objectives']:

                        result_to_add = global_optimization_of_GP_approximation_single_obj_multiple_cons( \
                            {'objective': objective, 'constraints': funs['constraints']}, num_dims, grid)

                        if result_to_add is not None:
                            if np.min(cdist(grid, result_to_add)) > 1e-6:
                                grid = np.vstack((grid, result_to_add))
                else:

                    # The problem has no solution! This is to send something to solve_using_grid

                    grid = np.zeros((1, num_dims))

		moo.solve_using_grid(grid)

# 		DHL : Removed because in a constrained setting it does not make sense

#		for i in range(len(funs['objectives'])):
#			result = find_global_optimum_GP_sample(funs['objectives'][ i ], num_dims, grid, minimize)
#			moo.append_to_population(result)

	else:

		assert False

		# TODO

		assert NSGA2_POP > len(funs['objectives']) + 1

		moo.solve_using_grid(grid = sobol_grid.generate(num_dims, num_dims * GRID_SIZE))

		for i in range(len(funs['objectives'])):
			result = find_global_optimum_GP_sample(funs['objectives'][ i ], num_dims, grid, minimize)
			moo.append_to_population(result)

		pareto_set = moo.compute_pareto_front_and_set_summary(NSGA2_POP)['pareto_set']

		moo.initialize_population(np.maximum(NSGA2_POP - pareto_set.shape[ 0 ], 0))

		for i in range(pareto_set.shape[ 0 ]):
			moo.append_to_population(pareto_set[ i, : ])

		moo.evolve_population_only(NSGA2_EPOCHS)

		for i in range(pareto_set.shape[ 0 ]):
			moo.append_to_population(pareto_set[ i, : ])

	result = moo.compute_pareto_front_and_set_summary(PARETO_SET_SIZE)

	return result['pareto_set']



"""
Given some approximations to the GP sample, find its minimum
We do that by first evaluating it on a grid, taking the best, and using that to
initialize an optimization. If nothing on the grid satisfies the constraint, then
we return None

wrapper_functions should be a dict with keys 'objective' and optionally 'constraints'
"""
# find MINIMUM if minimize=True, else find a maximum

def find_feasible_grid(constraints, grid):

    con_evals = np.ones(grid.shape[0]).astype('bool')

    for con_fun in constraints:
        con_evals = np.logical_and(con_evals, con_fun(grid, gradient = False) >= 0)

    if not np.any(con_evals):
        return None
    else:
        return grid[ con_evals, : ]

def global_optimization_of_GP_approximation_single_obj_multiple_cons(funs, num_dims, feasible_grid, minimize=True):

    assert num_dims == feasible_grid.shape[ 1 ]

    num_con = len(funs['constraints'])

    if feasible_grid is None:
        return None

    obj_evals = funs['objective'](feasible_grid, gradient = False)

    if minimize:
        best_guess_index = np.argmin(obj_evals)
        best_guess_value = np.min(obj_evals)
    else:
        best_guess_index = np.argmax(obj_evals)
        best_guess_value = np.max(obj_evals)

    x_initial = feasible_grid[ best_guess_index, : ]

    fun_counter = defaultdict(int)

    assert minimize # todo - can fix later

    f       = lambda x: float(funs['objective'](x, gradient=False))
    f_prime = lambda x: funs['objective'](x, gradient=True).flatten()

    constraint_tol = 1e-6 # my tolerance

    # with SLSQP in scipy, the constraints are written as c(x) >= 0

    # We substract a small value from the constraints to guarantee that we find something feasible

    def g(x):
        g_func = np.zeros(num_con)
        for i,constraint_wrapper in enumerate(funs['constraints']):
            g_func[i] = constraint_wrapper(x, gradient=False)
        return g_func

    def g_prime(x):
        g_grad_func = np.zeros((num_con, num_dims))
        for i,constraint_wrapper in enumerate(funs['constraints']):
            g_grad_func[i,:] = constraint_wrapper(x, gradient=True)
        return g_grad_func

    bounds = [(0.0,1.0)]*num_dims

    opt_x = spo.fmin_slsqp(f, x_initial.copy(), bounds=bounds, disp=0, fprime=f_prime, f_ieqcons=g, fprime_ieqcons=g_prime)

    # make sure bounds are respected

    opt_x[opt_x > 1.0] = 1.0
    opt_x[opt_x < 0.0] = 0.0

    if f(opt_x) < best_guess_value and np.all(g(opt_x)>= 0):
       return opt_x[None]
    else:
        logging.debug('SLSQP failed when optimizing x*')

        # We try to solve the problem again but more carefully (we substract 1e-6 to the constraints)

        def g(x):
            g_func = np.zeros(num_con)
            for i,constraint_wrapper in enumerate(funs['constraints']):
                g_func[i] = constraint_wrapper(x, gradient=False) - 1e-6
            return g_func

        opt_x = spo.fmin_slsqp(f, x_initial.copy(), bounds=bounds, disp=0, fprime=f_prime, f_ieqcons=g, fprime_ieqcons=g_prime)

        opt_x[opt_x > 1.0] = 1.0
        opt_x[opt_x < 0.0] = 0.0

        if f(opt_x) < best_guess_value and np.all(g(opt_x)>= - 1e-6):
            return opt_x[None]
        else:
            logging.debug('SLSQP failed two times when optimizing x*')
            return x_initial[None]

# This functions finds the global optimum of each objective, which could be useful to
# initialize the population in NSGA2

def find_global_optimum_GP_sample(fun, num_dims, grid, minimize = True):

	assert num_dims == grid.shape[ 1 ]

	# First, evaluate on a grid

	obj_evals = fun(grid, gradient = False)

	if minimize:
		best_guess_index = np.argmin(obj_evals)
		best_guess_value = np.min(obj_evals)
	else:
		best_guess_index = np.argmax(obj_evals)
		best_guess_value = np.max(obj_evals)

	x_initial = grid[ best_guess_index ]

	def f(x):
		if x.ndim == 1:
			x = x[None,:]

		a = fun(x, gradient = False)
		a_grad = fun(x, gradient = True)

		return (a, a_grad)

	bounds = [ (0, 1) ] * num_dims
	x_opt, y_opt, opt_info = spo.fmin_l_bfgs_b(f, x_initial, bounds=bounds, disp=0, approx_grad = False)
	# make sure bounds are respected

	x_opt[ x_opt > 1.0 ] = 1.0
	x_opt[ x_opt < 0.0 ] = 0.0

	return x_opt

class MESMC(AbstractAcquisitionFunction):

    def __init__(self, num_dims, verbose=True, input_space=None, grid=None, opt = None):

        global NSGA2_POP
        global NSGA2_EPOCHS
        global PARETO_SET_SIZE
        global NUM_RANDOM_FEATURES
        global GRID_SIZE
        global USE_GRID_ONLY

        # we want to cache these. we use a dict indexed by the state integer

        self.cached_EP_solution = dict()
        self.cached_pareto_front = dict()
        self.cached_acquisition_on_grid = dict()
        self.has_gradients = False
        self.num_dims = num_dims
        self.input_space = input_space

        self.options = PESM_OPTION_DEFAULTS.copy()
        self.options.update(opt)

        PARETO_SET_SIZE = self.options['mesmoc_pareto_set_size']
        NUM_RANDOM_FEATURES = self.options['mesmoc_num_random_features']

        NSGA2_POP = self.options['mesmoc_nsga2_pop']
        NSGA2_EPOCHS = self.options['mesmoc_nsga2_epochs']

        GRID_SIZE = self.options['mesmoc_grid_size']
        USE_GRID_ONLY = self.options['mesmoc_use_grid_only_to_solve_problem']

        # We save the grid that will be used by the default chooser

        self.grid_default_chooser = grid

    # obj_models is a GP
    # con_models is a dict of named constraints and their GPs

    def acquisition(self, obj_models_dict, con_models_dict, cand, current_best, compute_grad, minimize=True, tasks=None, tasks_values=None):


        models = obj_models_dict.values()
        for model in models:
            if not model.options['caching']:
                logging.error("Warning: caching is off while using MESMOC!")

        assert len({model.state for model in models}) == 1, "Models are not all at the same state"
        assert not compute_grad



        key = tuple([obj_models_dict[ obj ].state for obj in obj_models_dict])
        if key not in self.cached_pareto_front:
            pareto_fronts = dict()
            pareto_sets = dict()

            for i in range(int(self.options['mesmoc_samples_per_hyper'])):

                pareto_fronts[ i ] = sample_solution(self.num_dims, obj_models_dict, con_models_dict, self.grid_default_chooser)

                objectives = pareto_fronts[ i ]['objectives']

                one_point = False

                try:
                    n_points = len(objectives[ objectives.keys()[ 0 ] ])
                except:
                    one_point = True

                if one_point == False:

                    permutation = np.random.permutation(n_points)

                    for key_tmp in pareto_fronts[ i ]['objectives'].keys():
                        pareto_fronts[ i ]['objectives'][ key_tmp ] = pareto_fronts[ i ]['objectives'][ key_tmp ][ permutation ]

                    for key_tmp in pareto_fronts[ i ]['constraints'].keys():
                        pareto_fronts[ i ]['constraints'][ key_tmp ] = pareto_fronts[ i ]['constraints'][ key_tmp ][ permutation ]

            self.cached_pareto_front[ key ] = pareto_fronts
        else:
            pareto_fronts = self.cached_pareto_front[ key ]

        NUM_SAMPLES = len(pareto_fronts)
        TAM_CAND = len(cand)
        C = len(con_models_dict)
        K = len(obj_models_dict)

        m_f_old, v_f_old, e_f = get_statistics_in_cand(cand, obj_models_dict)
        m_c_old, v_c_old, e_c = get_statistics_in_cand(cand, con_models_dict)

        acq_dict = dict()
        keys_f_c = obj_models_dict.keys() + con_models_dict.keys()
        for key in keys_f_c:
            acq_dict[ key ] = 0.0

        for pareto_front in pareto_fronts.values():
            _, v_f_new, _, v_c_new = compute_adf(m_f_old, v_f_old, m_c_old, v_c_old, pareto_front)

            vs_old = np.vstack((v_f_old + e_f, v_c_old + e_c))
            vs_new = np.vstack((v_f_new + e_f, v_c_new + e_c))
            for key, v_old, v_new in zip(keys_f_c, vs_old, vs_new):
                #acq_dict[ key ] += 0.5 * np.log(2. * np.pi * np.e * v_old) - 0.5 * np.log(2. * np.pi * np.e * v_new)
                #acq_dict[ key ] += 0.5 * np.log(v_old / v_new)
                acq_dict[ key ] += v_old - v_new


        for key in keys_f_c:
            acq_dict[ key ] /= NUM_SAMPLES

        # By default, sum the MESMOC contribution for all tasks
        if tasks is None:
            tasks = acq_dict.keys()

        # Compute the total acquisition function for the tasks of interests
        total_acq = 0.0
        for task in tasks:
            total_acq += acq_dict[ task ]

        return total_acq

def compute_adf(m_f, v_f, m_c, v_c, pareto_front):

    m_f_new = np.zeros((m_f.shape))
    v_f_new = np.zeros((v_f.shape))
    m_c_new = np.zeros((m_c.shape))
    v_c_new = np.zeros((v_c.shape))

    fs_star = np.atleast_2d(pareto_front['objectives'].values()).T

    for f_star in fs_star:

        gamma_f = (f_star[:,None] - m_f) / np.sqrt(v_f)
        gamma_c = m_c / np.sqrt(v_c)

        log_neg_Z_minus_1 = compute_log_neg_Z_minus_1(gamma_f, gamma_c)

        if np.all(log_neg_Z_minus_1 != 0.0):

            dlogZ_dmf, dlogZ_dmc, dlogZ_dvf, dlogZ_dvc = compute_derivatives(log_neg_Z_minus_1, gamma_f, gamma_c, v_f, v_c)

            m_f = m_f + v_f * dlogZ_dmf
            v_f = v_f - v_f * (dlogZ_dmf * dlogZ_dmf - 2*dlogZ_dvf) * v_f
            m_c = m_c + v_c * dlogZ_dmc
            v_c = v_c - v_c * (dlogZ_dmc * dlogZ_dmc - 2*dlogZ_dvc) * v_c

    return m_f, v_f, m_c, v_c


def compute_log_Z(gamma_f, gamma_c):

    logcdf_gamma_f = sps.norm.logcdf(gamma_f)
    logcdf_gamma_c = sps.norm.logcdf(gamma_c)

    log_Z = np.log1p (-np.exp(np.sum(np.concatenate((logcdf_gamma_f, logcdf_gamma_c)),
                                    axis=0, keepdims=True)))

    return log_Z

def compute_log_neg_Z_minus_1(gamma_f, gamma_c):

    logcdf_gamma_f = sps.norm.logcdf(gamma_f)
    logcdf_gamma_c = sps.norm.logcdf(gamma_c)

    log_neg_Z_minus_1 = np.sum(np.concatenate((logcdf_gamma_f, logcdf_gamma_c)),
                                    axis=0, keepdims=True)

    return log_neg_Z_minus_1

def compute_derivative_m_f(Z_minus_1_div_Z, gamma_f, v_f):
    pdf_div_cdf_gamma_f = np.exp(sps.norm.logpdf(gamma_f) - sps.norm.logcdf(gamma_f))
    return - Z_minus_1_div_Z * pdf_div_cdf_gamma_f / np.sqrt(v_f)

def compute_derivative_m_c(Z_minus_1_div_Z, gamma_c, v_c):
    pdf_div_cdf_gamma_c = np.exp(sps.norm.logpdf(gamma_c) - sps.norm.logcdf(gamma_c))
    return Z_minus_1_div_Z * pdf_div_cdf_gamma_c / np.sqrt(v_c)

def compute_derivative_v_f(Z_minus_1_div_Z, gamma_f, v_f):
    pdf_div_cdf_gamma_f = np.exp(sps.norm.logpdf(gamma_f) - sps.norm.logcdf(gamma_f))
    return - Z_minus_1_div_Z * pdf_div_cdf_gamma_f * gamma_f  / (2*v_f)

def compute_derivative_v_c(Z_minus_1_div_Z, gamma_c, v_c):
    pdf_div_cdf_gamma_c = np.exp(sps.norm.logpdf(gamma_c) - sps.norm.logcdf(gamma_c))
    return - Z_minus_1_div_Z * pdf_div_cdf_gamma_c * gamma_c  / (2*v_c)

def compute_derivatives(log_neg_Z_minus_1, gamma_f, gamma_c, v_f, v_c):

    Z_minus_1_div_Z = -1. / np.expm1(-log_neg_Z_minus_1)

    derivative_m_f = compute_derivative_m_f(Z_minus_1_div_Z, gamma_f, v_f)
    derivative_m_c = compute_derivative_m_c(Z_minus_1_div_Z, gamma_c, v_c)
    derivative_v_f = compute_derivative_v_f(Z_minus_1_div_Z, gamma_f, v_f)
    derivative_v_c = compute_derivative_v_c(Z_minus_1_div_Z, gamma_c, v_c)

    return derivative_m_f, derivative_m_c, derivative_v_f, derivative_v_c

def get_statistics_in_cand(cand, models_dict):
    m = np.zeros((len(models_dict), len(cand)))
    v = np.zeros((len(models_dict), len(cand)))
    e = np.zeros((len(models_dict), 1))

    for i, model in enumerate(models_dict.values()):
        m[ i ], v[ i ] = model.predict(cand)
        e[ i ] = model.noise_value()

    return m, v, e


# Returns the MESMC for each task given the unconstrainedStatistics and sampled pareto_set.

def evaluate_acquisition_function_given_EP_solution(obj_models_dict, cand, epSolution, pareto_set, minimize=True, opt = None, con_models = {}):

    if cand.ndim == 1:
        cand = cand[None]

    unconstrainedVariances = dict()
    constrainedVariances = dict()
    acq = dict()

    for obj in obj_models_dict:
        unconstrainedVariances[ obj ] = obj_models_dict[ obj ].predict(cand)[ 1 ] + obj_models_dict[ obj ].noise_value()

    for cons in con_models:
        unconstrainedVariances[ cons ] = con_models[ cons ].predict(cand)[ 1 ] + con_models[ cons ].noise_value()

    for t in unconstrainedVariances:
        acq[t] = np.zeros(cand.shape[ 0 ])

    # We then evaluate the constrained variances

    for i in range(len(epSolution)):

	if epSolution[ str(i) ] is None:
		continue

        # We check if we have to constrain the predictions or not

        if opt['pesm_not_constrain_predictions'] == True:
            predictionEP = predictEP_unconditioned(obj_models_dict, con_models, epSolution[ str(i) ], pareto_set[ str(i) ], cand)
        else:
            predictionEP = predictEP_multiple_iter_optim_robust(obj_models_dict, con_models, epSolution[ str(i) ], pareto_set[ str(i) ], cand,  \
                n_iters = 1, damping = .1, no_negatives = True, minimize = minimize)

        predictionEP_obj = predictionEP[ 'vf' ]
        predictionEP_cons = predictionEP[ 'vc' ]

        for obj in obj_models_dict:
            constrainedVariances[ obj ] = predictionEP_obj[ obj ] + obj_models_dict[ obj ].noise_value()

        for cons in con_models:
            constrainedVariances[ cons ] = predictionEP_cons[ cons ] + con_models[ cons ].noise_value()

        # We only care about the variances because the means do not affect the entropy

        for t in unconstrainedVariances:
            value = 0.5 * np.log(2 * np.pi * np.e * unconstrainedVariances[t]) - \
                0.5 * np.log(2 * np.pi * np.e * constrainedVariances[t])

            # We set negative values of the acquisition function to zero  because the
            # entropy cannot be increased when conditioning

            value = np.maximum(np.zeros(len(value)), value)
            acq[t] += value

    for t in unconstrainedVariances:
        acq[t] /= len(epSolution)

    for t in acq:
        if np.any(np.isnan(acq[t])):
            raise Exception("Acquisition function containts NaN for task %s" % t)

    return acq



import scipy.spatial as ss
from scipy.special import digamma,gamma
from math import log,pi
import numpy.random as nr
import numpy as np
import random

def entropy(x,k=3,base=2):
  """ The classic K-L k-nearest neighbor continuous entropy estimator
      x should be a list of vectors, e.g. x = [[1.3],[3.7],[5.1],[2.4]]
      if x is a one-dimensional scalar and we have four samples
  """
  assert k <= len(x)-1, "Set k smaller than num. samples - 1"
  d = len(x[0])
  N = len(x)
  intens = 1e-10 #small noise to break degeneracy, see doc.
  x = [list(p + intens*nr.rand(len(x[0]))) for p in x]
  tree = ss.cKDTree(x)
  nn = [tree.query(point,k+1,p=float('inf'))[0][k] for point in x]
  const = digamma(N)-digamma(k) + d*log(2)
  return (const + d*np.mean(map(log,nn)))/log(base)


if __name__ == "__main__":

    print "Nothing to do."


