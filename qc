#!/usr/bin/bash

# python环境检查
check_python(){
  PYTHON_MAIN_VERSION=$(python --version | awk '{print $2}' | awk -F '.' '{print $1}')
  if [[ ${PYTHON_MAIN_VERSION} != 3 ]];then
    echo "未安装python3"
    exit
  fi
}

# pip环境检查
check_pip(){
  PIP_VERSION=$(pip --version | awk '{print $2}')
  if [[ ${PIP_VERSION}x = "x" ]];then
    echo "未安装pip"
    exit
  fi
}

# paramiko环境检查
check_paramiko(){
  PARAMIKO_VERSION=$(pip list | grep paramiko | awk '{print $2}')
  if [[ ${PARAMIKO_VERSION}x = "x" ]];then
    echo "未检测到paramiko，即将安装..."
    pip install paramiko -i https://pypi.tuna.tsinghua.edu.cn/simple --user
    PARAMIKO_VERSION=$(pip list | grep paramiko | awk '{print $2}')
  fi
}

check_python
check_pip
check_paramiko

PYTHONPATH=$(dirname "$0")
export PYTHONPATH

cd "${PYTHONPATH}/src"
python3 -B main.py "$1"