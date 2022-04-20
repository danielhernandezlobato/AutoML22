* Instructions to use the implementation of MESMOC+ described in this paper.

Note that MESMOC+ has been included in the version of Spearmint corresponding to the implementation 
of PESMOC, as described by Garrido-Merchán, E. C. and Hernández-Lobato, D., 2019. Therefore, that
version of Spearmint is required.

    1.- Download or clone the github repository corresponding to PESMOC: https://github.com/EduardoGarrido90/Spearmint 
	
    2.- Install the required software following the README.md that you can found in that repository.

    3.- To enable MESMOC+ in that version of Spearmint:

        3.1.- Remove the following file from Spearmint:

            - spearmint/acquisition_functions/random.py

        3.2.- Copy the following files from this zip to their corresponding folder:

            - parsing.py:         cp parsing.py         <path/to/Spearmint/spearmint/utils/parsing.py>
            - default_chooser.py: cp default_chooser.py <path/to/Spearmint/spearmint/choosers/default_chooser.py>
            - __init__.py:        cp __init__.py        <path/to/Spearmint/spearmint/acquisition_functions/__init__.py>
            - randomAcq.py:       cp randomAcq.py       <path/to/Spearmint/spearmint/acquisition_functions/randomAcq.py>

    5.- Add to the folder spearmint/acquisition_functions/ this file from this zip:

        - max_value_entropy_search_multiobjective_constraints.py
	
    6.- Install Spearmint:

        - pip install -e <path/to/Spearmint>

To run a the toy problem of this zip on which to test MESMOC+, follow this instructions:

    1.- Start the mongod service (if it is not already running):
        - service mongod start

    2.- Go to the path where the example of this zip is (the example of this zip is in the folder moocon_mesmoc):
        - cd <path/to/moocon_mesmoc/>

    3.- Clean the experiment to be run from the database (this step is only necessary if this experiment has been launched before):
        - python <path/to/Spearmint/spearmint/cleanup.py> <path/to/experiment/>

    4.- Execute the experiment:
        - python <path/to/Spearmint/spearmint/main.py> <path/to/experiment/>

    5.- Compute the results:
        - python <path/to/moocon_mesmoc/generate_hypervolumes.py> <path/to/experiment/>

