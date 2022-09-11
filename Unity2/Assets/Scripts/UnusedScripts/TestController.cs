/*
using UnityEngine;
using UnityEngine.Networking;

public class TestController : MonoBehaviour
{
    public void TestGet()
    {
        var url = "";

        using var www = UnityWebRequest.Get(url);

        www.SetRequestHeader("Content-Type", "application/JsonUtility");

        var operation = www.SendWebRequest();

        while (!operation.isDone)
            await Task.Yield();
    }
}
*/