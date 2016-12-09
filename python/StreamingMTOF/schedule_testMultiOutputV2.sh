#!/bin/sh

CUR_PATH=$(cd `dirname $0`; pwd)
echo ${CUR_PATH}

HADOOP="/home/work/tools/hadoop/hadoop-client-1.5.5/hadoop/bin/hadoop"
PYTHON_DIR="hdfs:///user/rp-product/chenjianrong/thirdparty/python2.7.tar.gz"

JOB_NAME="testMultiOutputV2"

MAP_FILE="${JOB_NAME}_map.py"
RED_FILE="${JOB_NAME}_red.py"

INPUT_DIR="/user/rp-product/chenjianrong/temp/testMultioutput/"
OUTPUT_DIR="/user/rp-product/chenjianrong/temp/testMultioutput_out/"

$HADOOP fs -rmr $OUTPUT_DIR

$HADOOP jar /home/work/tools/hadoop/hadoop-client-1.5.5/hadoop/lib/streaming-3.14.0.jar -libjars "/home/work/chenjianrong/backup/chenjianrong/survey/tools/streaming_code/StreamingMTOF.jar" \
    -jobconf mapred.job.name=\"$JOB_NAME\" \
    -jobconf mapred.job.queue.name=rp-bda  \
    -jobconf mapred.map.over.capacity.allowed=true \
    -jobconf ares.user=\"chenjianrong\" \
    -jobconf mapred.job.map.capacity=500 \
    -jobconf mapred.job.reduce.capacity=100 \
    -jobconf mapred.map.tasks=200 \
    -jobconf mapred.reduce.tasks=2 \
    -jobconf mapred.job.priority=NORMAL \
    -jobconf stream.non.zero.exit.is.failure=false \
    -inputformat org.apache.hadoop.mapred.TextInputFormat \
    -outputformat mypackage.streaming.mtof.StreamingMTOF \
    -file $MAP_FILE \
    -file $RED_FILE \
    -cacheArchive ${PYTHON_DIR}#py27 \
    -mapper "py27/python/bin/python ${MAP_FILE}" \
    -reducer "py27/python/bin/python ${RED_FILE}" \
    -input $INPUT_DIR \
    -output $OUTPUT_DIR 


if [ $? -eq 0 ]; then
    $HADOOP fs -touchz "${OUTPUT_DIR}done"
fi

exit 0
