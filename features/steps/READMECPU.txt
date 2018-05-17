PROJECT TITLE:
Write a python api to get all the parameters from “lscpu”output and  Using behave framework to write test-cases to fetch lscpu data from remote server.

PREREQUISITES:
Openstack instance should be in active state and running.
PARAMIKO package
PYHAMCREST


PROCESS:
 The python api to fetch lscpu from a remote server and use BDD framework to write test-cases to fetch lscpu data from remote  server.


USAGE:
     The program is useful in finding the CPU information of  a remote instance in openstack and checking its feature availability.The behave framework is helpful in easy understanding of working of each functional block in step implementation.


SAMPLE OUTPUT:
USER INPUT:
 behave -D hostname=10.0.4.13 -D username=cirros -D password=gocubsgo

OUTPUT:
feature: calculating lscpu from server # features/lscpu.feature:1

  Scenario Outline: ssh to server -- @1.1 ssh to server  # features/lscpu.feature:10
    Given establish ssh to a server                      # features/steps/lscpu_info.py:14 1.163s
    When execute lscpu on a server                       # features/steps/lscpu_info.py:33 0.062s
    Then feature "Architecture" with "x86_64"            # features/steps/lscpu_info.py:59 0.000s

  Scenario Outline: ssh to server -- @1.2 ssh to server  # features/lscpu.feature:11
    Given establish ssh to a server                      # features/steps/lscpu_info.py:14 0.222s
    When execute lscpu on a server                       # features/steps/lscpu_info.py:33 0.059s
    Then feature "Model" with "13"                       # features/steps/lscpu_info.py:59 0.000s

  Scenario Outline: ssh to server -- @1.3 ssh to server  # features/lscpu.feature:12
    Given establish ssh to a server                      # features/steps/lscpu_info.py:14 0.233s
    When execute lscpu on a server                       # features/steps/lscpu_info.py:33 0.071s
    Then feature "L2 cache" with "512K"                  # features/steps/lscpu_info.py:59 0.000s

1 feature passed, 0 failed, 0 skipped
3 scenarios passed, 0 failed, 0 skipped
9 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m1.811s


