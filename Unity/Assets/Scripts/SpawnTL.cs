using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SpawnTL : MonoBehaviour
{
    [SerializeField] private GameObject TF;
    TLAttr[] TLs;
    public Vector3[] Poslist;

    void Start()
    {
        for(int i = 0; i < 4; i++)
        {
            Poslist[i] = new Vector3(TLs[i].X, 3.5f, TLs[i].Y);
        }
        Instantiate(TF, Poslist[0], Quaternion.identity);
        Instantiate(TF, Poslist[1], Quaternion.identity);
        Instantiate(TF, Poslist[2], Quaternion.identity);
        Instantiate(TF, Poslist[3], Quaternion.identity);
    }
}
