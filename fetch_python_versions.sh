#!/bin/bash

min_version="3.8.0"

versions=$(curl -s https://raw.githubusercontent.com/actions/python-versions/main/versions-manifest.json | jq -r ".[] | select(.version | startswith(\"${min_version}\") or (.version | version) >= \"${min_version}\" | version) | .version")

echo "["

first=true
for version in $versions; do
  if [ "$first" = true ]; then
    first=false
  else
    echo ","
  fi
  echo -n "\"$version\""
done

echo "]"
