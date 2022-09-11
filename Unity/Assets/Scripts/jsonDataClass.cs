using System;
using System.Collections.Generic;

[Serializable]
public class jsonDataClass
{
    public List<carList> Carro; 
    public List<semList> Semaforo;
}

[Serializable]
public class carList
{
    public string kind;
    public int id;
    public int X;
    public int Y;
}

[Serializable]
public class semList
{
    public string kind;
    public int id;
    public int X;
    public int Y;
    public string color;
}