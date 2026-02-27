# Post-Lab Questions & Answers

1.Node: A process that performs computation, such as a controller or sensor driver.
Topic: A named communication channel used for streaming messages between nodes.
Package: A folder containing ROS 2 code, its dependencies, and build information.
Workspace: A main folder that holds one or more ROS 2 packages along with their build outputs.

2.Sourcing is required to update your terminal's environment variables so that ROS 2 knows where to find your built packages and executables. If you do not source a workspace, ROS 2 will not recognize your custom packages, commands like ros2 run will fail.

3.The purpose of colcon build is to compile your workspace, processing your packages and preparing them to be run. When run in an empty workspace, it generates three new folders: build/, install/, and log/.

4.The entry_points console script acts as a map for ROS 2; it tells the system exactly which Python function inside which specific file should be executed when a user types a command name in the terminal.

5.
+-----------------------+                     +-----------------------+
|       Node A          |                     |        Node B         |
|  (Publisher)          |                     |   (Subscriber)        |
|                       |                     |                       |
| publishes Twist msgs  |   /cmd_vel topic    | receives Twist msgs   |
| at 10 Hz              +-------------------->| and acts on them      |
+-----------------------+                     +-----------------------+
