#!/usr/bin/env python3

import os, sys, subprocess

def main():
  
  # dotnet add package Microsoft.DotNet.ILCompiler -v '1.0.0-alpha-*'
  # dotnet add package Microsoft.AspNetCore.Server.Kestrel -v '2.2.0'

  output_exe = None
  if os.name == 'nt':
    subprocess.run(['dotnet', 'publish', '-r', 'win-x64', '-c', 'release'], check=True)
    output_exe = os.path.join(
      'bin', 'release', 'netcoreapp3.1', 'win-x64', 'publish', 'csharp-hello-world.exe'
    )
  else:
    subprocess.run(['dotnet', 'publish', '-r', 'linux-x64', '-c', 'release'], check=True)
    output_exe = os.path.join(
      'bin', 'release', 'netcoreapp3.1', 'linux-x64', 'publish', 'csharp-hello-world'
    )

  subprocess.run(output_exe, check=True)



if __name__ == '__main__':
  main()

