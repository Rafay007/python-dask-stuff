from distributed import Client,LocalCluster


if __name__=='__main__':
    cluster= LocalCluster()
    client=Client(cluster)
    print(client)