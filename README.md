# Miele-cli

A program that uses the Miele Logic API (kind, uses curl idk) to check the progress of the dryers and washers at my student complex. 

The authentication header in the curl command is not included, because I don't know if that is a security risk or not. Better safe than sorry.

## Example output
![Example of output](/assets/miele-example.png)

## Usage

You can use `miele` to get the status of Grønneviksøren 54, the default. Or use `miele 52` to see the status of Grønneviksøren 52.

Included is a .py and .sh. The bash script depends on [jq](https://github.com/stedolan/jq). JQ can be download through you package manager.

Feedback is very much appreciated. :)
