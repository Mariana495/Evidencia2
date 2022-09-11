using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;

[Serializable]
public class carAttr : MonoBehaviour
{
    public string kind;
    public int id;
    public float X = 0;
    public float Y = 0;

    public float nextX;
    public float nextY;

    private Vector3 initPos;

    public float moveDuration = 2;
    void Start()
    {
        initPos = transform.position;
        nextX = X;
        nextY = Y;
    }

    void Update()
    {
        if (transform.position.x > -780 && transform.position.x < 270 && transform.position.z > -750 && transform.position.z < 350)
        {
            gameObject.transform.position = initPos;
        }
        else
        {
            StartCoroutine(StartMove(new Vector3(nextX, 3.5f, nextY)));
        }
    }

    IEnumerator StartMove(Vector3 np)
    {
        initPos = transform.position;
        float timeElapsed = 0;
        while (timeElapsed < moveDuration)
        {
            transform.position = Vector3.Lerp(initPos, np, timeElapsed / moveDuration);
            yield return null;
            timeElapsed += Time.deltaTime;
        }
    }
}

