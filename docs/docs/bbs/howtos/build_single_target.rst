.. _bbs-build-single-target_top:

-----------------------------------
Build a Single Package or Component
-----------------------------------
This build mode in intended for developers who are modifying a single
component or group of components.

General workflow
----------------
After :doc:`setting up the build environment <build_bde_basic>`, you can
configure the library with a simple:

.. code-block:: shell
    
   $ bbs_build configure

This command will generate build target for **all** libraries and **all** test
drivers in the current build repository or workspace.

* To build (only) an individual target, you should specify the name of the
  target in the build command:

  .. code-block:: shell
    
     $ bbs_build build --target bsls  # Build bsls package library 
     $ bbs_build build --target bal   # Build bal package group library 

     $ bbs_build build --target all.t  # Build all test drivers
     $ bbs_build build --test build    # Build all test drivers

     $ bbs_build build --target bslmt.t             # Build test drivers for bslmt package
     $ bbs_build build --target bslmt --test build  # Build test drivers for bslmt package

* To build and run test drivers:

  .. code-block:: shell
    
     $ bbs_build build --test run    # Build and run all test drivers

     $ bbs_build build --target bslmt --test run  # Build and run test drivers for bslmt package

Optimized workflow
------------------
When working on a single component, we want to minimize the number of the
targets generated by CMake by filtering out unused tests targets.  This can
significantly reduce the configuration, dependency check and build time of the
underlying build system.

* Specify the regex for the component you want to have test drivers
  (``bsls_platform`` in the example below):

  .. code-block:: shell
    
     $ bbs_build configure --regex "bsls_platform$"

  In a similar fashion you can provide a regex to enable tests for the whole
  package or even package groups:

  .. code-block:: shell
    
     $ bbs_build configure --regex "bsls"

  .. note::
     Misspeling regex can lead to the test driver set to be empty. 

* Building and running test drivers is done with the following commands:

  This command builds **all** library targets, but only links and executes
  the tests matching the regex supplied at the ``configure`` step.

  .. code-block:: shell

     $ bbs_build build --tests run

  This command builds only direct dependencies of the ``bsls_platform`` test
  driver (and thus is much faster than the command above):

  .. code-block:: shell

      $ bbs_build build --target bsls_platform.t --tests run

  This command builds only direct dependencies of the tests in ``bsls``
  package. For the regex ``bsls_platform$`` it also runs a single test
  driver:

  .. code-block:: shell

      $ bbs_build build --target bsls.t --tests run
