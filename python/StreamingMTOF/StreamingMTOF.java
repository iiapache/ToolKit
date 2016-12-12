import java.io.IOException;

import org.apache.hadoop.mapred.JobConf;
import org.apache.hadoop.mapred.RecordWriter;
import org.apache.hadoop.mapred.TextOutputFormat;
import org.apache.hadoop.mapred.lib.MultipleTextOutputFormat;
import org.apache.hadoop.util.Progressable;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.io.Text;

public class StreamingMTOF extends MultipleTextOutputFormat<Text, Text>{
     
     private TextOutputFormat<Text, Text> output = null;
     
      @Override
     protected RecordWriter<Text, Text> getBaseRecordWriter(
          FileSystem fs, JobConf job, String name, Progressable arg3)
          throws IOException {
        if (output == null) {
          output = new TextOutputFormat<Text, Text>();
        }
        return output.getRecordWriter(fs, job, name, arg3);
     }
     
     @Override
     protected String generateFileNameForKeyValue(Text key, Text value, String filename) {
           String strValue = value.toString();
           int markerIndex = strValue.lastIndexOf("#");
           if(-1 != markerIndex) {
               String newValue = strValue.substring(0, markerIndex);
               value.set(newValue);
               String pathFlag = strValue.substring(markerIndex + 1);
               return pathFlag + "/" + filename;
           }
           return filename;
     }

}
