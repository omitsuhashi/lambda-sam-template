#!/bin/bash
function error() {
    echo "Error: $1"
    exit 1
}
[[ -n "$1" ]] || error "Missing environment name (eg, dev, stg, qa, prod)"
env_type=$1

if [ "$env_type" = "dev" ]; then
    export s3_bucket="todo"
    export stack_name="todo"
elif [ "$env_type" = "prod" ]; then
    export s3_bucket="todo"
    export stack_name="todo"
else
    error "Argument not allowed, environment name (eg, dev, qa, prod)"
fi

sam build

aws cloudformation package \
    --template .aws-sam/build/template.yaml \
    --s3-bucket $s3_bucket \
    --output-template-file packaged-template.yml

sam deploy --template-file packaged-template.yml \
    --stack-name $stack_name \
    --s3-bucket $s3_bucket \
    --capabilities CAPABILITY_NAMED_IAM \
    --parameter-overrides Env="$env_type"
