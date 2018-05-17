Feature: calculating lscpu from server
    Scenario Outline: ssh to server
        Given establish ssh to a server
        When execute lscpu on a server
        Then feature "<feature>" with "<availability>"
    

    Examples:ssh to server
          | feature            | availability |
          | Architecture       |  x86_64      |
          | Model              |   13         |
          | L2 cache           |   512K       |
