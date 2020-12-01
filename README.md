# DiscoDungeonBot/dungeonbot

This is our DnD discord bot that handles dice rolls, splash damage, and a few
other odds and ends. It builds into a Docker Container that can be run
anywhere, but will come with support for AWS Fargate on ECS.

## Running

1. Build the container

    ``` bash
    docker build -t dungeonbot .
    ```

1. Run the container

    ``` bash
    docker run --rm -it -e DISCORD_TOKEN=<YOURTOKEN> dungeonbot
    ```
