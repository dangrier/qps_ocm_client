# QPS Online Crime Map Client

This project is not in any way affiliated with the Queensland Police Service.

This client provides access to the same data used in the Queensland Police Service's Online Crime Map, available here: https://qps-ocm.s3-ap-southeast-2.amazonaws.com/index.html

## Usage

An example of usage can be found in [example.py](./example.py):

```shell
> python .\example.py
Which type of area will you be searching for offences in [Suburb]? 
Which Suburb do you want to search for offences in [Brisbane City]? 
Search from how many days ago [90]? 

There were 2478 offences in Brisbane City (Suburb) in the last 90 days:
Other Theft (excl. Unlawful Entry): 846
Drug Offences: 436
Good Order Offences: 399
Assault: 132
Handling Stolen Goods: 93
Unlawful Entry: 77
Traffic & Related Offences: 73
Fraud: 69
Weapons Act Offences: 66
Trespassing & Vagrancy: 29
Robbery: 23
Other Offences Against the Person: 18
Liquor (excl. Drunkenness): 18
Unlawful Use of Motor Vehicle: 10

```


## Future plans

I plan to create another project for a Home Assistant Add-On which can generate events and use the data for crime in your area, in a way which can be extended to support other jurisdictions.
