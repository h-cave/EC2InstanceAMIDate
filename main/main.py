import boto3


def extract_date(ec2_data):
    image_ids = []
    instance_ids = []
    launch_times = []
    instance_name = []

    for details in ec2_data['Reservations']:
        for instance_details in details['Instances']:
            instance_ids.append((instance_details['InstanceId']))
            image_ids.append((instance_details['ImageId']))
            launch_times.append((instance_details['LaunchTime']))
            for tags in instance_details['Tags']:
                instance_name.append((tags['Value']))

    return image_ids, instance_ids, launch_times, instance_name


def format_times(instance_launch_times):
    instance_launch_times = [time.strftime('%m/%d/%Y, %H:%M:%S') for time in instance_launch_times]
    return instance_launch_times


if __name__ == "__main__":
    # stuff only to run when not called via 'import' here
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()
    print('Response: ', response)

    print(response)

    image_ids, instance_ids, launch_times, instance_name = extract_date(response)
    launch_times = format_times(launch_times)
    print(image_ids)
    print(instance_ids)
    print(launch_times)
    print(instance_name)

