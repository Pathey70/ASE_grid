# HW 4 Grid


### Document file for HW4 Main.py file



- To view all command line options run 
    ```python3 Main.py --help True ```

- To Run test cases 
    ```python3 Main.py```


```
Here are the list of options

OPTIONS:
  -d  --dump    on crash, dump stack   = False
  -f  --file    name of file           = ../etc/data/repgrid1.csv
  -g  --go      start-up action        = data
  -h  --help    show help              = False
  -p  --p       distance coefficient   = 2
  -s  --seed    random number seed     = 937162211

To run

python3 Main.py --seed 937162211

```
## Output
```
✅PASS : eg_check_nums
✅PASS : eg_check_syms
b4 {'a': 1, 'b': {'c': 2, 'd': [3]}} 
after {'a': 1, 'b': {'c': 2, 'd': [10000]}}
✅PASS : eg_copy
 70
|..  43
|.. |..  31
|.. |.. |..  BroadbandNetworks
|.. |.. |..  ElectronicPublishing
|.. |..  36
|.. |.. |..  VirtualReality
|.. |.. |..  33
|.. |.. |.. |..  MultimediaAndHypermedia
|.. |.. |.. |..  InformationHighway
|..  71
|.. |..  47
|.. |.. |..  ObjectOrientedSystems
|.. |.. |..  CrossPlatformGUIs
|.. |..  64
|.. |.. |..  IntelligentAgents
|.. |.. |..  53
|.. |.. |.. |..  VisualProgramming
|.. |.. |.. |..  KnowledgeBasedSystems
 72
|..  48
|.. |..  38
|.. |.. |..  TargetedOnInterface:TargetedOnOverallSystem
|.. |.. |..  ConventionalSystem:IntelligentSystem
|.. |..  41
|.. |.. |..  Multimedia:Programming
|.. |.. |..  CommunicationTechnology:ApplicationTechnology
|..  67
|.. |..  54
|.. |.. |..  DevelopmentTool:Application
|.. |.. |..  ConventionalCommunication:NovelCommunication
|.. |..  57
|.. |.. |..  HumanOrientedTool:SystemTool
|.. |.. |..  OnlyActAsProgrammed:Semi-autonomous

A ElectronicPublishing
B VirtualReality
C MultimediaAndHypermedia
D VisualProgramming
E CrossPlatformGUIs
F ObjectOrientedSystems
G KnowledgeBasedSystems
H IntelligentAgents
I InformationHighway
J BroadbandNetworks

{ J                           F           }
{                                         }
{                                         }
{ I                                       }
{                                         }
{ C                                       }
{   A                                     }
{                 E                       }
{ B         D       G                     }
{                                         }
{                                         }
{           H                             }
✅PASS : eg_every

A ElectronicPublishing
B VirtualReality
C MultimediaAndHypermedia
D VisualProgramming
E CrossPlatformGUIs
F ObjectOrientedSystems
G KnowledgeBasedSystems
H IntelligentAgents
I InformationHighway
J BroadbandNetworks

{ J                           F           }
{                                         }
{                                         }
{ I                                       }
{                                         }
{ C                                       }
{   A                                     }
{                 E                       }
{ B         D       G                     }
{                                         }
{                                         }
{           H                             }
✅PASS : eg_position
 70
|..  43
|.. |..  31
|.. |.. |..  BroadbandNetworks
|.. |.. |..  ElectronicPublishing
|.. |..  36
|.. |.. |..  VirtualReality
|.. |.. |..  33
|.. |.. |.. |..  MultimediaAndHypermedia
|.. |.. |.. |..  InformationHighway
|..  71
|.. |..  47
|.. |.. |..  ObjectOrientedSystems
|.. |.. |..  CrossPlatformGUIs
|.. |..  64
|.. |.. |..  IntelligentAgents
|.. |.. |..  53
|.. |.. |.. |..  VisualProgramming
|.. |.. |.. |..  KnowledgeBasedSystems
✅PASS : eg_prototype
{'a': 'Num', 'at': 0, 'hi': 5, 'id': 140302087592400, 'lo': 1, 'm2': 13.5, 'mu': 1.75, 'n': 8, 'txt': 'Num0', 'w': 1}
{'a': 'Num', 'at': 1, 'hi': 5, 'id': 140302356996592, 'lo': 1, 'm2': 17.875, 'mu': 2.375, 'n': 8, 'txt': 'Num1', 'w': 1}
{'a': 'Num', 'at': 2, 'hi': 3, 'id': 140302356996544, 'lo': 1, 'm2': 6.000000000000001, 'mu': 1.5, 'n': 8, 'txt': 'Num2', 'w': 1}
{'a': 'Num', 'at': 3, 'hi': 5, 'id': 140302356469408, 'lo': 1, 'm2': 18.875, 'mu': 2.125, 'n': 8, 'txt': 'Num3', 'w': 1}
{'a': 'Num', 'at': 4, 'hi': 5, 'id': 140302356469216, 'lo': 1, 'm2': 14.874999999999998, 'mu': 1.8749999999999998, 'n': 8, 'txt': 'Num4', 'w': 1}
{'a': 'Num', 'at': 5, 'hi': 5, 'id': 140302356469168, 'lo': 1, 'm2': 32.0, 'mu': 3.0, 'n': 8, 'txt': 'Num5', 'w': 1}
{'a': 'Num', 'at': 6, 'hi': 5, 'id': 140302356469360, 'lo': 1, 'm2': 20.000000000000004, 'mu': 3.5, 'n': 8, 'txt': 'Num6', 'w': 1}
{'a': 'Num', 'at': 7, 'hi': 5, 'id': 140302087398496, 'lo': 2, 'm2': 10.874999999999998, 'mu': 4.125, 'n': 8, 'txt': 'Num7', 'w': 1}
{'a': 'Num', 'at': 8, 'hi': 5, 'id': 140302087399312, 'lo': 1, 'm2': 16.0, 'mu': 2.5, 'n': 8, 'txt': 'Num8', 'w': 1}
{'a': 'Num', 'at': 9, 'hi': 5, 'id': 140302087398832, 'lo': 1, 'm2': 15.875, 'mu': 2.375, 'n': 8, 'txt': 'Num9', 'w': 1}
{'a': 'Sym', 'at': 10, 'has': defaultdict(<class 'int'>, {}), 'id': 140302087398064, 'mode': None, 'most': 0, 'n': 0, 'txt': 'thingX'}
{'a': 'Row', 'cells': [5, 3, 3, 1, 1, 1, 1, 3, 5, 5, 'DevelopmentTool:Application', 'DevelopmentTool:Application'], 'id': 140302087592592}
{'a': 'Row', 'cells': [2, 1, 1, 5, 5, 5, 5, 5, 1, 2, 'Multimedia:Programming', 'Multimedia:Programming'], 'id': 140302357259456}
{'a': 'Row', 'cells': [1, 3, 1, 3, 2, 5, 4, 3, 1, 1, 'CommunicationTechnology:ApplicationTechnology', 'CommunicationTechnology:ApplicationTechnology'], 'id': 140302357259552}
{'a': 'Row', 'cells': [2, 1, 1, 1, 3, 5, 3, 2, 2, 2, 'HumanOrientedTool:SystemTool', 'HumanOrientedTool:SystemTool'], 'id': 140302357259600}
{'a': 'Row', 'cells': [1, 5, 3, 4, 1, 1, 4, 5, 4, 4, 'ConventionalCommunication:NovelCommunication', 'ConventionalCommunication:NovelCommunication'], 'id': 140302357259696}
{'a': 'Row', 'cells': [1, 4, 1, 1, 1, 1, 1, 5, 3, 1, 'OnlyActAsProgrammed:Semi-autonomous', 'OnlyActAsProgrammed:Semi-autonomous'], 'id': 140302357259744}
{'a': 'Row', 'cells': [1, 1, 1, 1, 1, 1, 5, 5, 1, 1, 'ConventionalSystem:IntelligentSystem', 'ConventionalSystem:IntelligentSystem'], 'id': 140302357259792}
{'a': 'Row', 'cells': [1, 1, 1, 1, 1, 5, 5, 5, 3, 3, 'TargetedOnInterface:TargetedOnOverallSystem'], 'id': 140302357259840}
✅PASS : eg_repcols
{'a': 'Num', 'at': 0, 'hi': 5, 'id': 140302356469216, 'lo': 1, 'm2': 27.6, 'mu': 2.8, 'n': 10, 'txt': 'DevelopmentTool:Application', 'w': 1}
{'a': 'Num', 'at': 1, 'hi': 5, 'id': 140302356469168, 'lo': 1, 'm2': 33.6, 'mu': 3.2, 'n': 10, 'txt': 'Multimedia:Programming', 'w': 1}
{'a': 'Num', 'at': 2, 'hi': 5, 'id': 140302356469360, 'lo': 1, 'm2': 18.4, 'mu': 2.4, 'n': 10, 'txt': 'CommunicationTechnology:ApplicationTechnology', 'w': 1}
{'a': 'Num', 'at': 3, 'hi': 5, 'id': 140302087398496, 'lo': 1, 'm2': 13.599999999999998, 'mu': 2.2000000000000006, 'n': 10, 'txt': 'HumanOrientedTool:SystemTool', 'w': 1}
{'a': 'Num', 'at': 4, 'hi': 5, 'id': 140302087399312, 'lo': 1, 'm2': 23.6, 'mu': 3.2, 'n': 10, 'txt': 'ConventionalCommunication:NovelCommunication', 'w': 1}
{'a': 'Num', 'at': 5, 'hi': 5, 'id': 140302087398832, 'lo': 1, 'm2': 20.9, 'mu': 1.9, 'n': 10, 'txt': 'OnlyActAsProgrammed:Semi-autonomous', 'w': -1}
{'a': 'Num', 'at': 6, 'hi': 5, 'id': 140302087398064, 'lo': 1, 'm2': 25.6, 'mu': 1.8, 'n': 10, 'txt': 'ConventionalSystem:IntelligentSystem', 'w': 1}
{'a': 'Num', 'at': 7, 'hi': 5, 'id': 140302087592400, 'lo': 1, 'm2': 30.4, 'mu': 2.5999999999999996, 'n': 10, 'txt': 'TargetedOnInterface:TargetedOnOverallSystem', 'w': 1}
{'a': 'Sym', 'at': 8, 'has': defaultdict(<class 'int'>, {}), 'id': 140302087592592, 'mode': None, 'most': 0, 'n': 0, 'txt': 'thingX'}
{'a': 'Row', 'cells': [5, 2, 1, 2, 1, 1, 1, 1, 'ElectronicPublishing'], 'id': 140302356469408}
{'a': 'Row', 'cells': [3, 1, 3, 1, 5, 4, 1, 1, 'VirtualReality'], 'id': 140302356493024}
{'a': 'Row', 'cells': [3, 1, 1, 1, 3, 1, 1, 1, 'MultimediaAndHypermedia'], 'id': 140302356493168}
{'a': 'Row', 'cells': [1, 5, 3, 1, 4, 1, 1, 1, 'VisualProgramming'], 'id': 140302356493072}
{'a': 'Row', 'cells': [1, 5, 2, 3, 1, 1, 1, 1, 'CrossPlatformGUIs'], 'id': 140302357259456}
{'a': 'Row', 'cells': [1, 5, 5, 5, 1, 1, 1, 5, 'ObjectOrientedSystems'], 'id': 140302357259552}
{'a': 'Row', 'cells': [1, 5, 4, 3, 4, 1, 5, 5, 'KnowledgeBasedSystems'], 'id': 140302357259600}
{'a': 'Row', 'cells': [3, 5, 3, 2, 5, 5, 5, 5, 'IntelligentAgents'], 'id': 140302357259696}
{'a': 'Row', 'cells': [5, 1, 1, 2, 4, 3, 1, 3, 'InformationHighway'], 'id': 140302357259744}
{'a': 'Row', 'cells': [5, 2, 1, 2, 4, 1, 1, 3, 'BroadbandNetworks'], 'id': 140302357259792}
✅PASS : eg_reprows
 72
|..  48
|.. |..  38
|.. |.. |..  TargetedOnInterface:TargetedOnOverallSystem
|.. |.. |..  ConventionalSystem:IntelligentSystem
|.. |..  41
|.. |.. |..  Multimedia:Programming
|.. |.. |..  CommunicationTechnology:ApplicationTechnology
|..  67
|.. |..  54
|.. |.. |..  DevelopmentTool:Application
|.. |.. |..  ConventionalCommunication:NovelCommunication
|.. |..  57
|.. |.. |..  HumanOrientedTool:SystemTool
|.. |.. |..  OnlyActAsProgrammed:Semi-autonomous
✅PASS : eg_synonyms
{'dump': False, 'file': '../etc/data/repgrid1.csv', 'go': 'data', 'help': False, 'p': 2, 'seed': 937162211}
✅PASS : eg_the

```