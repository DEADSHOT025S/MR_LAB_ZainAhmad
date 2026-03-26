from setuptools import find_packages, setup

package_name = 'my_turtle_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='your_name',
    maintainer_email='your_email@domain.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'square_node = my_turtle_package.move_turtle_square:main',
            'circle_node = my_turtle_package.move_turtle_circle:main',
            'triangle_node = my_turtle_package.move_turtle_triangle:main',
            'goal_node = my_turtle_package.move_turtle_goal:main'
        ],
    },
)