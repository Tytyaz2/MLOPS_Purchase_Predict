from google.cloud import storage


def test_list_bucket_files():
    client = storage.Client()

    bucket = client.bucket("mlops-ia")

    blobs = list(bucket.list_blobs(prefix="data-test.csv"))

    print("\nFichiers trouvés dans le bucket :")

    for blob in blobs:
        print(blob.name)

    assert len(blobs) > 0


test_list_bucket_files()
