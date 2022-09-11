using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;

[Serializable]
public class TLAttr : MonoBehaviour
{
    public string kind;
    public int id;
    public float X;
    public float Y;
    public string color;

    Renderer rend;
    Material m1, m2;

    private void Start()
    {
        rend = GetComponent<Renderer>();

    }

    private void Update()
    {
        /*
        Debug.Log(kind);
        Debug.Log(id);
        Debug.Log(color);
        Debug.Log(X);
        Debug.Log(Y);
        */
        if (color == "red")
        {
            rend.material = m1;
        }else if(color == "green")
        {
            rend.material = m2;
        }
    }

    /*
    

    public Light trafficLight;
    Color colorRed, colorGreen;


    
    void Start()
    {
        ColorUtility.TryParseHtmlString("FF0000", out colorRed);
        ColorUtility.TryParseHtmlString("00FF0C", out colorGreen);
    }

    void Update()
    {
        if (color == "red")
        {
            trafficLight.color = colorRed;
        }
        else if (color == "green")
        {
            trafficLight.color = colorGreen;
        }
    }*/
}

