# Redis cluster nagios

Python script to check the status of a master/slave redis cluster. 
Considerations:
  - Execute the same script without parameters at master or slave.
  - It use 'redis-cli info | grep' to extract the information.
  - For the moment only works in a two nodes cluster. 
  - We are using this script in check_mk + mrpe.
