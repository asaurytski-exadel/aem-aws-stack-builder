# aem-aws-stack-builder
Cloudformation templates (yaml) for creating an AEM Stack

Network (shared) Stacks:
* vpc
* network

AEM Application (specific) Stacks:
* roles (can be shared across stacks)
* security-groups
* messaging
* publish-dispatcher
* publish
* author
* author-dispatcher
* orchestrator
* chaos-monkey

Prerequisites:
* ec2 key pair
* ssl server certificate
* ami images for publish-dispatcher, publish, author, author-dispatcher, orchestrator, chaos-monkey (with component and version tags)
* dns hosted zone
* provisioning init script accessible via s3 bucket
* inbound_from_bastion_host_security_group
* nat gateway / internet proxy


## Installation

Requirements:

* Run `make deps` to install [AWS CLI](http://docs.aws.amazon.com/cli/latest/userguide/installing.html), [Ansible](http://docs.ansible.com/ansible/intro_installation.html), and [Boto 3](https://boto3.readthedocs.io/en/latest/).
* [Configure](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html#cli-quick-configuration) AWS CLI.

## Usage

Requirements:

* Set up SSL certificate in [AWS IAM](https://aws.amazon.com/iam), check out `create-cert`, `upload-cert`, and `delete-cert` targets in the Makefile for examples.
* Set up [EC2 key pair](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html). The key pair name should be configured in `ansible/inventory/group_vars/apps.yaml` at `compute.key_pair_name` field.

To create the network setup (VPC, subnets, etc):

    STACK_PREFIX=mynetwork make create-network-stacks

To delete the network setup:

    STACK_PREFIX=mynetwork make delete-network-stacks

To create AEM infrastructure:

    STACK_PREFIX=myaem make create-aem-stacks

It is also possible to specify custom configuration files:

    STACK_PREFIX=myaem CONFIG_PATH=/path/to/myconf make create-aem-stacks

To delete AEM infrastructure:

    STACK_PREFIX=myaem make delete-aem-stacks

Environment variables:

| Name         | Description                                      |
|--------------|--------------------------------------------------|
| STACK_PREFIX | Prefix string added to all stack names           |
| CONFIG_PATH  | Path to directory containing configuration files |

It is also possible to create specific components without the complete set. Check out the Makefile for the complete list of targets.

## Configuration

|--------------------------------------------|------|
| Name                                       | Description | Default value |
|--------------------------------------------|------|
| publish_dispatcher.stack_name              | TODO |
| publish_dispatcher.instance_profile        | TODO |
| publish_dispatcher.instance_type           | TODO |
| publish_dispatcher.min_size                | TODO |
| publish_dispatcher.max_size                | TODO |
| publish_dispatcher.load_balancer.tag_name  | TODO |
| publish_dispatcher.tag_name                | TODO |
| publish_dispatcher.elb_health_check        | TODO |
| publish_dispatcher.route53_record_set_name | TODO |
| chaos_monkey.stack_name                    | TODO |
| chaos_monkey.ami_id                        | TODO |
| chaos_monkey.instance_profile              | TODO |
| chaos_monkey.instance_type                 | TODO |
| chaos_monkey.tag_name                      | TODO |
|--------------------------------------------|------|

## Development

Requirements:

* Install [ShellCheck](https://github.com/koalaman/shellcheck#user-content-installing)

Check shell scripts, validate CloudFormation templates, check Ansible playbooks syntax:
```
make lint
```
