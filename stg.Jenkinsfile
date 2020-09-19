intelQAAutomation {
  machine          = 'prod'
  trigger          = '00 22 * * *'
  html_pattern     =  [
                            [keepAll: true, reportDir: "reports/", reportFiles: "*.html", reportName: "Performance_report"],
                      ]
  automation_script   = '''
                     current_timestamp=`date +"%Y_%m_%d_%H_%M_%S"`
                     docker build -t automation_image_${current_timestamp} .
                     docker run --rm  -v $(pwd):/code automation_image_${current_timestamp} bash -x trigger_run.sh
                     docker rmi automation_image_${current_timestamp}
                     '''
  email_options = [
  to: '',
  subject: 'QA Performance  : Test Suite Report',
  body: '''
        Please refer to the detailed test report at:
        ${BUILD_URL}/Automation_Reports/
        <br>
        <h2>Short Summary:</h2>
        ${FILE,path="reports/summary.html"}
        '''
  ]
}
