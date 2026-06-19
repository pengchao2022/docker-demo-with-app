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

### Only ENTRYPOINT in Dockerfile

- Dockerfile code
```shell
FROM ubuntu:22.04

ENTRYPOINT [ "echo", "Hello, Entrypoint!" ]

```
- build the image
```shell
docker build -f Dockerfile.py -t maxwell-test-entrypoint:1.2.3 .

```
- run the image to create container
```shell
allen@192 dockerfile-entrypoint % docker run maxwell-test-entrypoint:1.2.3
Hello, Entrypoint!

```
- you can see with "Hello, Entrypoint!"

- now we run the image with args like "echo "I love China""

```shell
allen@192 dockerfile-entrypoint % docker run maxwell-test-entrypoint:1.2.3 echo "I love China"
Hello, Entrypoint! echo I love China

```
- you can see it print "Hello, Entrypoint!" and new added args "I love China"

### here you can see the difference between cmd and entrypoint is ：

- CMD in Dckerfile will Overwrite the original args with new args 
  the args written in Dckerfile will not execute anymore and will replaced by new args 

  - CMD in Dockerfile 覆盖 --- Overwrite

- ENTRYPOINT in Dockerfile will Append the args
  the args written in Dockerfile will still be executed and new args will be exectuted also

  - ENTRYPOINT in Dockerfile 追加 --- Append


### The best practices shoud be using both

- ENTRYPOINT 固定命令 

- CMD 传递参数

- Here's the Dockerfile both using CMD and ENTRYPOINT

```shell
FROM ubuntu:22.04

ENTRYPOINT [ "echo" ]

CMD [ "Hello, CMD and ENTRYPOINT as default !" ]

```
- build the image
```shell
 docker build -f Dockerfile -t maxwell-test-both:1.2.4 .  

 ```
- run the image to create container
```shell
allen@192 dockerfile-cmd-entrypoint % docker run maxwell-test-both:1.2.4  
Hello, CMD and ENTRYPOINT as default !

```
- you can see the outputs, now we add args like "I love China"

```shell
allen@192 dockerfile-cmd-entrypoint % docker run maxwell-test-both:1.2.4 "I love China"
I love China

```
- Please see the command carefully and we no need to write command "echo" just give the args






