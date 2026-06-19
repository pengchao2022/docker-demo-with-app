# Diff between CMD and EMTRYPOINT in Dockerfile
In this demo, I will write 3 Dockerfiles to test the following cases:

  - Only cmd in Dockerfile
  - Only entrypoint in Dockerfile
  - Both cmd and entrypoint in Dockerfile


## Usage

### Only CMD in Dockerfile

- Dockerfile code
```shell
FROM ubuntu:22.04

CMD ["echo", "Hello, CMD!"]

```
- Build image
```shell
 docker build -f Dockerfile -t maxwell-test-cmd:1.1.2 .

 ```

 - run the image to create the container only cmd 

 ```shell
 allen@192 dockerfile-cmd % docker run maxwell-test-cmd:1.1.2
Hello, CMD!
```
- you can see the outputs with "Hello, CMD!"

- now we will run with args like this:

```shell
allen@192 dockerfile-cmd % docker run maxwell-test-cmd:1.1.2 echo "I love China"
I love China
```
- you can see the output is "I love China" without "Hello, CMD"


