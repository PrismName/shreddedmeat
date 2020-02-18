#### Shredded meat
An audit of shredded meat based on the scratch vulnerability


#### Requirements
* Linux -- I haven't tested this on Windows.
* Python 3.7.x or above
* Sccrapy 1.8.0 or above


#### Install shedded meat
`pip3 install scrapy`

`git clone https://github.com/prisnName/shreddedmeat.git`


#### Usage
`cd shreddedmeat/`
`scrapy crawl rsspider -a domain=exmpale.com`


#### Exporting
`scrapy crawl rsspider -a domain=exmpale.com -t json -o exmpale.json`

#### ToDo
1. vulnerability audit undone
2. crawler url done


---
that's all
