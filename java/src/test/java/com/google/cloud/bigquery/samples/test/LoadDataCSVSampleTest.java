package com.google.cloud.bigquery.samples.test;

import com.google.gson.JsonIOException;
import com.google.gson.JsonSyntaxException;
import com.google.cloud.bigquery.samples.LoadDataCSVSample;

import org.junit.Test;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

/**
 * TODO: Insert description here. (generated by elibixby)
 */
public class LoadDataCSVSampleTest extends BigquerySampleTest {

  /**
   * @throws JsonSyntaxException
   * @throws JsonIOException
   * @throws FileNotFoundException
   */
  public LoadDataCSVSampleTest() throws JsonSyntaxException, JsonIOException, FileNotFoundException {
    // TODO(elibixby): Auto-generated constructor stub
    super();
  }
  
  @Test
  public void testLoadData() throws IOException, InterruptedException{
    LoadDataCSVSample.run(
        CONSTANTS.getGcsInputURI(), 
        CONSTANTS.getProjectId(),
        CONSTANTS.getDatasetId(),
        CONSTANTS.getNewTableId(),
        new FileReader(new File(RESOURCE_PATH.resolve("schema.json").toString())),
        5000L);
  }
  

}