using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class jsonController : MonoBehaviour
{
    public string jsonURL = "http://localhost:8585/";
    jsonDataClass jsnData;

    void Start()
    {
        StartCoroutine(getData());
    }

    IEnumerator getData()
    {
        Debug.Log("Processing Data, Please Wait");

        WWW _www = new WWW(jsonURL);
        yield return _www;
        if(_www.error == null)
        {
            processJsonData(_www.text);
        }
        else
        {
            Debug.Log("Oops something went wrong");
        }
    }

    private void processJsonData(string _url)
    {
        jsnData = JsonUtility.FromJson<jsonDataClass>(_url);

        foreach(carList car in jsnData.Carro)
        {/*   Debug.Log(car.kind);
            Debug.Log(car.id);
            Debug.Log(car.X);
            Debug.Log(car.Y);*/
        }
        foreach (semList semaforo in jsnData.Semaforo)
        {/*
            Debug.Log(semaforo.kind);
            Debug.Log(semaforo.id);
            Debug.Log(semaforo.X);
            Debug.Log(semaforo.Y);
            Debug.Log(semaforo.color);*/
        }
    }
}
