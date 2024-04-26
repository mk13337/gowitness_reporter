## About the project

This is a project that uses python3 and jinja2. By communicating with the gowitness API it retrieves screenshot information and produces more convenient static reports.


Current features:
- Screenshot filtering by status codes 
- Grouping screenshots by similarity based on perception hashes
- Viewing a screenshot through a separate modal window

![](https://raw.githubusercontent.com/mk13337/gowitness/master/images/main_demo.gif)


## Project Usage

### Via Docker

Docker is the main way to run this utility. You can see instructions in my [fork of the gowitness project](https://github.com/mk13337/gowitness/).

### Separately

To run separately, you need to:

1) Run gowitness in screenshot mode
2) Run gowitness in server mode
3) Copy the screenshots directory to the project directory.
4) Run main.py


