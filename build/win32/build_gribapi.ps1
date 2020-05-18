param(
    [switch]$Rebuild,
    [switch]$Debug,
	[switch]$Verbose,
	[string]$PlatformToolset = "v142",
    [string]$PackageVersion
)

Set-StrictMode -Version 3.0
$ErrorActionPreference = "Stop"

$build = If ($Rebuild) {"Clean,Build"} Else {"Build"}
$config = If ($Debug) {"Debug"} Else {"Release"}
$output = if ($Verbose) {'Out-Default'} else {'Out-Null'}

If ((Get-Command "msbuild.exe" -ErrorAction SilentlyContinue) -eq $null) {
  Write-Warning "msbuild.exe was not found in the PATH. "
  Write-Warning "Run this script from an Developer Powershell For VS"
  Write-Warning "or have msbuild.exe in your PATH"
  exit 1
}

If ((Get-Command "bash.exe" -ErrorAction SilentlyContinue) -eq $null) {
  Write-Warning "bash.exe was not found in the PATH. "
  Write-Warning "E.g. install WSL"
  exit 1
}

$scriptDir = Split-Path $script:MyInvocation.MyCommand.Path
$baseDir = "$scriptDir\..\.."

### Apply patches
If (!(Select-String -Path "$baseDir\grib_api\src\grib_api.h" -SimpleMatch -Quiet -Pattern "grib_set_exit_proc")) {
  Write-Host "Patching grib_api_h"
  git apply "$baseDir\patches\grib_api_h.patch"
}

If (!(Select-String -Path "$baseDir\grib_api\src\grib_errors.c" -SimpleMatch -Quiet -Pattern "grib_set_exit_proc")) {
  Write-Host "Patching grib_errors.c"
  git apply "$baseDir\patches\grib_errors_c.patch"
}

If (!(Select-String -Path "$baseDir\grib_api\windows\msvc\grib_api_lib\grib_api_lib.vcxproj" -SimpleMatch -Quiet -Pattern "ext\jasper")) {
  Write-Host "Patching grib_api_lib.vcxproj"
  git apply "$baseDir\patches\grib_api_lib_vcxproj.patch"
}

If ($Rebuild) {
  Remove-Item -Recurse -Force -ErrorAction Ignore "$baseDir\grib_api\build"
  Remove-Item -Recurse -Force -ErrorAction Ignore "$baseDir\lib\x64"
  Remove-Item -Recurse -Force -ErrorAction Ignore "$baseDir\lib\x86"
}

New-Item -Path "$baseDir\grib_api" -Name build -ItemType "directory" -Force | & $output
Push-Location "$baseDir\grib_api\build"
try {
  If(!(Test-Path ../src/eccodes_version.h) -Or $Rebuild) {
    Write-Host "Generating eccodes_version.h"
    bash -c "cmake .. -DENABLE_INSTALL_ECCODES_DEFINITIONS=OFF -DENABLE_TESTS=OFF -DENABLE_EXAMPLES=OFF -DENABLE_INSTALL_ECCODES_SAMPLES=OFF -DENABLE_LARGE_FILE_SUPPORT=OFF -DENABLE_FORTRAN=OFF -DENABLE_NETCDF=OFF -DENABLE_PYTHON=OFF -DENABLE_PNG=OFF -DENABLE_JPG=OFF" | & $output
	cp src/eccodes_version.h ../src/eccodes_version.h 
  }
}
Finally {
  Pop-Location
}

######## X64

Write-Host "Building Grib.Api.XP x64"
msbuild "$baseDir\grib_api\windows\msvc\grib_api_lib\grib_api_lib.vcxproj" /p:Configuration="$config" /p:Platform="x64" /p:PlatformToolset="$PlatformToolset" /t:"$build" | & $output

######## X86

Write-Host "Building Grib.Api.XP x86"
msbuild "$baseDir\grib_api\windows\msvc\grib_api_lib\grib_api_lib.vcxproj" /p:Configuration="$config" /p:Platform="Win32" /p:PlatformToolset="$PlatformToolset" /t:"$build" | & $output

If ($PackageVersion) {
  Write-Host "Packaging choco"
  & "$scriptDir\build_choco.cmd" $PackageVersion $config
}