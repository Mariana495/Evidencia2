using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class NewCarSpawner : MonoBehaviour
{
    [SerializeField] private GameObject carPrefab;
    private List<GameObject> actCarList;
    private List<carAttr> carsList;
    public int numCar = 0;
    private int ID, actNumCar = 0;
    public int[] IDList;
    private bool create = true;

    /*
    private void Start()
    {
        car = GetComponent<carAttr>();
        for (int i = 0; i < IDList.Length; i++)
        {
            SpawnCar(carPosInit[i]);
        }
    }
    void Update()
    {
        CarList = GameObject.FindGameObjectsWithTag("car");
        actNumCar = CarList.Length;
        while (numCar > actNumCar)
        {
            foreach (GameObject c in CarList)
            {
                car = c.GetComponent<CarMovement2>();
                foreach (int idel in IDList)
                {
                    if (idel == car.id)
                    {
                        create = false;
                    }
                }
                ID = car.id;
            }
            if (create)
            {
                IDList[IDList.Length] = ID;
                SpawnCar(carPosInit[numCar]);
                numCar++;
            }
            create = true;
        }
    }
    */
    /*
    void SpawnCar(Vector3 Pos)
    {

        Instantiate(carPrefab, Pos, Quaternion.identity);
        car = carPrefab.GetComponent<CarMovement2>();
        car.id = ID;
    */
        /*
        if (Pos.z > -670 && Pos.z < -570 && Pos.x > -370 && Pos.x < -270) // == InitX1)
        {
            //Debug.Log(Pos);
            //Debug.Log(Vector3.back);
            car.Dir = Vector3.back;
        }
        else if (Pos.z > 170 && Pos.z < 300 && Pos.x > -270 && Pos.x < -170)// == InitX2)
        {
            //Debug.Log(Pos);
            //Debug.Log(Vector3.left);
            car.Dir = Vector3.left;
        }
        else if (Pos.x > -710 && Pos.x < -610 && Pos.z > -290 && Pos.z < -220) //== InitY1)
        {
            //Debug.Log(Pos);
            //Debug.Log(Vector3.forward);
            car.Dir = Vector3.forward;
        }
        else if (Pos.x > 120 && Pos.x < 220 && Pos.z > -200 && Pos.z < -100) //== InitY2)
        {
            //Debug.Log(Pos);
            //Debug.Log(Vector3.right);
            car.Dir = Vector3.right;
        }
        else
        {
            Destroy(carPrefab);
            car.Dir = Vector3.zero;
            //Debug.Log(Pos);
        }
        */
    //}
}
