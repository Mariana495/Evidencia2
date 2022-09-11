using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;

[Serializable]
public class TLAttr : MonoBehaviour
{
    public string kind { set; get; }
    public int id { set; get; }
    public float X { set; get; }
    public float Y { set; get; }

    public string color { set; get; }

    public string nextColor { set; get; }

    public Light trafficLight;
    Color colorRed, colorGreen;

    [SerializeField] List<GameObject> semPrefabs;

    void Start()
    {
        nextColor = color;
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

