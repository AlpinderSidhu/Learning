### Docker and K8s Perspective

| Docker Field Name | Kubernetes Field Name | Description                           |
| ----------------- | --------------------- | ------------------------------------- |
| ENTRYPOINT        | command               | Command that will be run by container |
| CMD               | args                  | Argument passed to container          |

### Commands and Args in Kubernetes

| Image Entrypoint | Image Entrypoint | Container Commands  | Container Argument | Result              |
| ---------------- | ---------------- | ------------------- | ------------------ | ------------------- |
| sleep            | 3600             | `<not-set>`         | `<not-set>`        | sleep 3600          |
| sleep            | 3600             | `<not-set>`         | 5000               | sleep 5000          |
| sleep            | 3600             | ping -c5 google.com | `<not-set>`        | ping -c5 google.com |
| sleep            | 3600             | ping                | yahoo.com          | ping yahoo.com      |
