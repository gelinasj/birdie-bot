# Birdie Bot

This repository provides a generic tool for creating a Twitter bot that tweets phrases trained on the provided training data. The machine learning model employed by the tool is inspired by a Markov Chain model to predict likely and, ideally, appropriate words to occur next in a given phrases. Below you can see an instance of the tool in action mimicking a fan favorite...

# Michael Gary Bot

"You miss 100% of the shots you don't take" -Michael Scott. Well, he didn't actually say that. Nor did he say any of the quotes posted by our [Twitter bot](https://twitter.com/MichaelGaryBot). While it doesn't have the same impulse to deliver a classic "that's what she said" joke, the tweet generator powering this account strives to emulate the speech and likeness of Steve Carell's iconic character. [Some tweets](https://twitter.com/MichaelGaryBot/status/1270901824707493895) turned out pretty funny. [Others](https://twitter.com/MichaelGaryBot/status/1272109779859767296), not so much.

# Create Your Own Bot

If you would like to use the Birdie Bot yourself, after cloning the repository, there are simply 7 prerequisite actions before you can set your bot free!

1. Place all the data files you want the bot to learn from in the `example_data/` directory
2. Package your code by running the following command from the project root: `zip -r9 function.zip; zip -g function.zip *.py example_data/*`
3. Create an AWS account and through the UI create your own twitter bot [AWS Lambda](https://aws.amazon.com/lambda/) function
4. Push your code to the AWS Lambda function by running the following command from the project root: `aws lambda update-function-code --function-name <insert_lambda_name_here> --zip-file fileb://function.zip`
5. Apply for a developer Twitter account and create your first app [here](https://developer.twitter.com)
6. Update your AWS Lambda function's `CONSUMER_KEY`, `CONSUMER_SECRET_KEY`, `ACCESS_TOKEN`, and `ACCESS_SECRET_TOKEN` environment variables with the values of your recently created Twitter app's `API key`, `API secret key`, `Access token`, and `Access token secret` respectively
7. Finally, create a [AWS CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html) event that triggers your Lambda as frequently as you wish

At this point, your bot is out of your control... with great power comes great responsibility!

![](michael.gif)
