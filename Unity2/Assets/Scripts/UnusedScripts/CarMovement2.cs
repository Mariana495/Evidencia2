using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CarMovement2 : MonoBehaviour
{
    public int id;
    private Vector3 initPos;
    private Vector3 nextPos;
    public Vector3 Dir;
    public float distanceT;
    public float moveDuration;
    public Light[] TFL;
    public ChangeLight letPass0;
    public ChangeLight letPass1;
    public ChangeLight letPass2;
    public ChangeLight letPass3;
    private bool check = true;


    void Update()
    {
        if(transform.position.x > -780 && transform.position.x < 270 && transform.position.z > -750 && transform.position.z < 350)
        {
            Destroy(gameObject);
        }
        else
        {
            StartCoroutine(StartMove(nextPos));
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