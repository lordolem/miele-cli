# Miele-cli

Program that uses the Miele Logic API to check the status/progress of dryers and washers at my student housing. You need your account token for this program to work.

## Example output

![Example of output](/assets/miele-example.png)

## Usage

You can use `miele` to get the status of Grønneviksøren 54, the default. Or use `miele 52` to see the status of Grønneviksøren 52.

Included is a .py and .sh. The bash script depends on [jq](https://github.com/stedolan/jq). JQ can be download through you package manager.

This project is dead. My student housing now uses Miele appWash. I have made two projects related to appWash.

- [Appwash CLI (Python)](https://github.com/omfj/appwash-cli)
- [Appwash rust (Rust)](https://github.com/omfj/appwash-rs)
