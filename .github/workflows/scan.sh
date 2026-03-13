#!/bin/bash
curl -fsSL https://raw.githubusercontent.com/ZupIT/horusec/master/deployments/scripts/install.sh | bash
./horusec start -p="./" -e="true"