Debugging and refactoring trick
===============================

This is a cute decorator for logging the inputs and outputs of a function to a debug folder.
You can run your script and get :code:`(input, output)` tuples.

* Stores files in the :code:`debug` folder
* Stores :code:`<function name>__<id>__<input/output>.pickle`
  * Choose to store the input and output separately, so if function crashes, we can capture the inputs and reproduce
  * The corresponding input and output have the same id
  * The id is the timestamp right before the function is called


The code
--------


.. code::python

    import time
    import pickle
    
    
    def log_inputs_and_outputs(f):
        def wrapper(*args, **kwargs):
            timestamp = time.time_ns()
            input_filename = f'debug/{f.__name__}__{timestamp}__input.pickle'
            to_save = locals()
            pickle.dump({'args': to_save['args'], 'kwargs': to_save['kwargs']}, open(input_filename, 'wb'))
            ret_val = f(*args, **kwargs)
            output_filename = f'debug/{f.__name__}__{timestamp}__output.pickle'
            pickle.dump(ret_val, open(output_filename, 'wb'))
            return ret_val
        return wrapper

To use

.. code::python

    import pickle
    import pathlib
    import client_behavior_heuristics.scripts.create_tool as c
    from pandas.testing import assert_frame_equal
    
    def pairings(func):
        files = set(str(p) for p in pathlib.Path('debug').glob('*.pickle'))
        pairing = {}
        for file in files:
            if file.startswith(func.__name__) and file.endswith('__input.pickle') and file.replace('input', 'output') in files:
                pairing[file] = file.replace('input', 'output')
        return pairing
    
    
    def check_expectations(input_file, outfile):
        args = pickle.load(open(input_file, 'rb'))['kwargs']
        ret_val = pickle.load(open(outfile, 'rb'))
        return args, ret_val
    
    
    def check_function(input_file, outfile, func):
        args, ret_val = check_expectations(input_file, outfile)
        assert_frame_equal(func(**args), ret_val)
    
    
    def test_all(func, n_limit=None):
        pair = list(pairings(func).items())
        if n_limit:
            pair = pair[:n_limit]
        for index, (input_file, output_file) in enumerate(pair):
            print(f'On {index+1} of {len(pair)} pairing tests')
            check_function(input_file, output_file, func)


This example is picked assuming that our function returns a dataframe, you can modify this pattern for other return types.
