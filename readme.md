
# Building

```bash
dotnet publish -r linux-x64 -c release
dotnet publish -r win-x64 -c release
python build.py # does a build + runs the output file
```

# Goals

 - [x] Compile `c#` to a native `.exe`
 - [-] Run a web server
 - [ ] Store user data sent to the web server in a sqlite database file


