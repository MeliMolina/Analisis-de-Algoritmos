package com.example.rubmchaves.myapplication;

import java.util.*;
import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import java.util.ArrayList;


public class AlgoritmoOrdenamiento extends ActionBarActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_algoritmo_ordenamiento);
    }


    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_algoritmo_ordenamiento, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }

        private static int N;
        /* Sort Function */
        public static void sort(int arr[])
        {
            heapify(arr);
            for (int i = N; i > 0; i--)
            {
                swap(arr,0, i);
                N = N-1;
                maxheap(arr, 0);
            }
        }
        /* Function to build a heap */
        public static void heapify(int arr[])
        {
            N = arr.length-1;
            for (int i = N/2; i >= 0; i--)
                maxheap(arr, i);
        }
        /* Function to swap largest element in heap */
        public static void maxheap(int arr[], int i)
        {
            int left = 2*i ;
            int right = 2*i + 1;
            int max = i;
            if (left <= N && arr[left] > arr[i])
                max = left;
            if (right <= N && arr[right] > arr[max])
                max = right;

            if (max != i)
            {
                swap(arr, i, max);
                maxheap(arr, max);
            }
        }
        /* Function to swap two numbers in an array */
        public static void swap(int arr[], int i, int j)
        {
            int tmp = arr[i];
            arr[i] = arr[j];
            arr[j] = tmp;
        }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    public void clickBotonSort(View v, ArrayList<int> arr) {
        sort(arr);
    }
}
