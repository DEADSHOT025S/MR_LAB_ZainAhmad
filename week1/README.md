Week 1 Lab: Linux Onboarding and ROS 2 Basics

Description
This folder contains my submission for the Week 1 Mobile Robotics lab. The objective was to set up a ROS 2 Humble workspace (ros2_ws_zain), create a custom Python package named my_first_pkg, and write a simple ROS 2 node. The node was progressively enhanced to include a file-based run counter and handle dynamic ROS 2 parameters from the terminal.

Commands Used
`mkdir -p ~/ros2_ws_zain/src` - Created the workspace directory structure.
`colcon build` - Compiled the workspace and generated the build/install/log folders.
`source install/setup.bash` - Sourced the ROS 2 environment variables.
`ros2 pkg create --build-type ament_python my_first_pkg` - Created the Python package.
`chmod +x simple_node.py` - Made the Python node file executable.
`ros2 run my_first_pkg simple_node` - Executed the basic node.
`ros2 run my_first_pkg simple_node --ros-args -p student_name:="Zain"` - Executed the node with a custom parameter.

Problems Faced & Solutions
Problem: When attempting my first GitHub commit, Git blocked the action with an Author identity unknown error.
Solution: I used the `git config --global user.email` and `user.name` commands to link my terminal to my GitHub identity.
Problem: I needed to ensure the node remembered its run count even though nodes don't save their state after shutting down.
 Solution: I utilized the Python `os` module to read from and write to a `counter.txt` file located directly inside the package directory, updating it securely on each run.

Reflection
This first lab provided a highly practical foundation for understanding the ROS 2 architecture and the Linux terminal. Transitioning from standard Python scripts to ROS 2 nodes required a mental shift, particularly in understanding how a workspace separates source code from build artifacts. Learning to use `colcon build` and consistently sourcing the environment highlighted the importance of environment variables for system pathing. The programming tasks involving the file-based counter and the `student_name` parameter were especially insightful; they demonstrated how nodes can maintain external state and accept dynamic configurations without modifying the underlying code. Overall, getting hands-on with package creation and `setup.py` entry points has made the ROS 2 framework feel much more approachable.
