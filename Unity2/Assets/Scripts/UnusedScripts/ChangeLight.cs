using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ChangeLight : MonoBehaviour
{
    Light trafficLight;
    public string color;
    Color colorRed, colorGreen;

    void Start()
    {
        trafficLight = GetComponent<Light>();
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
    }
}
