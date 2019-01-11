from invoke import task

@task
def triggerjob(c, branchname, jiraticket, extra=''):
    print("That will trigger Jenkins job for %s branch %s ticket number is %s" % ("componentA", branchname, jiraticket))
    jobUrl = "http://localhost:8080/job/componentA/job/integration%252FJIRA-1234/build?token=mytoken"
    c.run("curl --user jenkins:117fdb366df85accd3e8841d8eea7e9041 -X POST http://localhost:8080/job/componentA/job/integration%252FJIRA-1234/buildWithParameters?PARAMETER=null")
    # These options are for verification job
    # By the branch name it should walk through projects directories (?) That could be never used branches in components we dont need
    # Make a request to JIRA/BitBucket about opened PR by Jira number.
    # Next case is integration
    # There are no other chose how we can find component need to run but by using artifactory
    # Only parameter we need is Jira ticket number. Make a request to Artifactory to find all artifacts contains this ticket
    # Collect ["component_name":"commit ID", ...] And run integration job on those commits if they are on project/integration
    # Problems: This should be a queue organized. All commits on project/integration should be tagged. Maybe even merge itself should be done
    # here.
