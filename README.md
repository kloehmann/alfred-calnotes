# Alfred Calendar notes

This workflow helps you manage notes for your appointments.
It reads all org files in a directory and lists all files for upcoming appointments, so they can be easily opened fro alfred when needed

## Setup
1. Download workflow
2. Install in alfred
3. Set folder for your notes files


## File structure
All org files in the given directory are scanned. For org files to be recognized by this workflow, the first top-level node in the files must be scheduled with a time.
Headlines that are scheduled or scheduled without time are ignored.

**Example**
``` org
* My meeting
  SCHEDULED: <2023-11-08 Wed 12:00> 
  C'mon this is lunchtime
```
