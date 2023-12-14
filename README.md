## Autify Backend Engineer

#### How to run complete code
```commandline
./fetch.sh https://www.google.com https://autify.com <...>
```
#### To Print metadata
```commandline
chmod +x fetch.sh
./fetch.sh --metadata https://www.google.com
```

### GIST of Script
* Bash script has way to build and run docker and container is remove after succesful run

### GIST of Code

* Code entry point is from main.py
* Code is written to keep very lean service layers and heavy models
* Followed strict dependency inversion and single responsibility
* All external dependency interactions are through interfaces
