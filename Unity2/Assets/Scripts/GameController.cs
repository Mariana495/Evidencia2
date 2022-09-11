using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GameController : MonoBehaviour
{
    public List<GameObject> actCars;
    public List<GameObject> actTLs;

    public jsonController jCont;
    private jsonDataClass Data;
    public List<carList> carros;
    public List<semList> semaforos;

    [SerializeField] List<GameObject> carrosPrefabs;

    bool start = true;

    void Update()
    {
        
        if (start)
        {
            jCont = GetComponent<jsonController>();

            Debug.Log(carros.Count);
            CreateCars();
            start = false;
        }
        Debug.Log(semaforos.Count);
        carros = Data.Carro;
        semaforos = Data.Semaforo;
        TLsChange();
        carsChange();
        
    }
    void TLsChange(){
        for(int i = 0; i < semaforos.Count; i++)
        {
            Debug.Log("Entra");
            if(semaforos[i].X == 43 && semaforos[i].Y == -300)
            {
                Debug.Log("1");
                actTLs[0].GetComponent<TLAttr>().color = semaforos[i].color;
            }
            else if(semaforos[i].X == 43 && semaforos[i].Y == -31)
            {
                Debug.Log("2");
                actTLs[1].GetComponent<TLAttr>().color = semaforos[i].color;
            }
            else if(semaforos[i].X == 320 && semaforos[i].Y == -31)
            {
                Debug.Log("3");
                actTLs[2].GetComponent<TLAttr>().color = semaforos[i].color;
            }
            else if(semaforos[i].X == 320 && semaforos[i].Y == -300)
            {
                Debug.Log("4");
                actTLs[3].GetComponent<TLAttr>().color = semaforos[i].color;
            }
        }
    }
    void carsChange()
    {
        Debug.Log(actCars.Count);
        for(int i= 0; i < actCars.Count;i++)
        {
            actCars[i].GetComponent<carAttr>().nextX = carros[i].X;
            actCars[i].GetComponent<carAttr>().nextY = carros[i].Y;
        }
    }
    
    void CreateCars()
    {
        int n = carros.Count;
        for(int i = 0; i<n; i++)
        {
            int rand = Random.Range(0,carrosPrefabs.Count);
            actCars.Add(Instantiate(carrosPrefabs[rand], new Vector3((float)carros[i].X, 3.5f, (float)carros[i].Y), new Quaternion(0,0,0,0)));
        }
    }
    /*
    void CreateTF()
    {
        int n = semaforos.Count;
        for(int i = 0; i < n; i++)
        {
            actTLs.Add(Instantiate(semaforoPrefab, new Vector3((float)semaforos[i].X, 3.5f, (float)semaforos[i].Y), new Quaternion(0, 0, 0, 0)));
        }
    }*/
}
