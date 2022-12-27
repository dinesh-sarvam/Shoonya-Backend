<View> 


  <Labels name="labels" toName="audio_url" className="ignore_assertion"> 
    {speaker_0_details ? <Label value="Speaker 0" />  : null} 
    {speaker_1_details ? <Label value="Speaker 1" />  : null}
  </Labels> 
  <AudioPlus name="audio_url" value="$audio_url"/> 
  
  <View visibleWhen="region-selected"> 
    <Header value="Provide Transcription" /> 
  </View> 
  
  <TextArea name="transcribed_json" toName="audio_url" 
            rows="2" editable="true" 
            perRegion="true" required="true" /> 
              
  {reference_raw_transcript ? <Header value="Reference Transcript" /> 
   <Text name="reference_raw_transcript" 
    value="$reference_raw_transcript"/> : null}

   <Header value="Speaker Details" />          
   {speaker_0_details ?
   <Text name="speaker_0_details" className="ignore_assertion"
    value="$speaker_0_details"/> : null} 
   {speaker_1_details ?
   <Text name="speaker_1_details" className="ignore_assertion"
    value="$speaker_1_details"/> : null}
   
</View> 
 
