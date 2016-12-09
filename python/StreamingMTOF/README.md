# Python Streaming MultipleTextOutputFormat
Implementation of MultipleTextOutputFormat in Python Streaming

Python Streaming 多路输出

方法一：使用-libjars添加java自定义MultipleTextOutputFormat

注：使用该方法首先需要设置环境变量：export HADOOP_CLASSPATH=$HADOOP_CLASSPATH:./StreamingMTOF.jar

该方法在输出目录中添加flag标识,如：

/user/product/joe/temp/testMultioutput_out/A/part-00000

/user/product/joe/temp/testMultioutput_out/B/part-00000


方法二：使用Streaming自带SuffixMultipleTextOutputFormat

该方法在输出文件名part后添加flag标识,如：

/user/product/joe/temp/testMultioutput_out/part-00000-A

/user/product/joe/temp/testMultioutput_out/part-00000-B


