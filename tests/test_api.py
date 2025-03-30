import pytest
import httpx

BASE_URL = "https://webapp-ocr-p7-b2d0cuafdhgyf8fx.canadacentral-01.azurewebsites.net/"

@pytest.mark.asyncio
async def test_negative_tweet_prediction():
    tweet = "I hate my family"
   
    async with httpx.AsyncClient(timeout=10.0) as client:
        try:
            response = await client.post(f"{BASE_URL}/predict", params={"tweet": tweet})
            print(f"Status code : {response.status_code}")
            print(f"Response : {response.json}")
        except Exception as e:
            print(f"Request failed: {e}")
            assert False
       
    assert response.status_code == 200
    data = response.json()
    assert 'prediction' in data
    assert data['prediction'] == 0, f"Expected prediction to be 0, but got {data['prediction']}"

@pytest.mark.asyncio
async def test_positive_tweet_prediction():
    tweet = "I love my family"
   
    async with httpx.AsyncClient(timeout=10.0) as client:
        try:
            response = await client.post(f"{BASE_URL}/predict", params={"tweet": tweet})
            print(f"Status code : {response.status_code}")
            print(f"Response : {response.json}")
        except Exception as e:
            print(f"Request failed: {e}")
            assert False
       
    assert response.status_code == 200
    data = response.json()
    assert 'prediction' in data
    assert data['prediction'] == 1, f"Expected prediction to be 1, but got {data['prediction']}"
