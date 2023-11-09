package Coding;

import java.util.Scanner;

public class Myprogram{


	public static void main(String[] args) {
		
		 Scanner in = new Scanner(System.in);
	     boolean status = true;
		do{
			
			System.out.println("Please select number 1-3 to run the program, or press 0 to quit:");
			int number = in.nextInt();			
			
			if(number == 1) {
				System.out.println("Please insert number to the program and press 0 to to calculate the Max, Min, and Average value:");
				// TODO: Task 1: Write a program to enter the numbers until pressing 0 to stop,
				int num;
				int count = 0;
				int temp =0;

				int max =Integer.MIN_VALUE;
				int min = Integer.MAX_VALUE;

				do {
				Scanner in_num = new Scanner(System.in);
				num = in_num.nextInt();

				temp+=num;
				count++;
				if(num ==0) {
				count--;
				}
				if(num != 0) {
				if(num < min) {
				min = num;
				}
				if(num > max) {
				max = num;
				}
				}
				}while(num != 0);

				double Average=(double)temp/(double)count;
				if(count==0) {
				System.out.println("Max= 0");
				System.out.println("Min= 0");
				break;
				}
				System.out.println("Max"+max);
				System.out.println("Min"+min);
				System.out.println("Average"+Average);

				//then the program should calculate and display the largest (Max), smallest (Min), and Average numbers entered.
				
			}else if(number == 2) {
				System.out.println("Please insert any number as a high of the triangle:");
				// TODO: Task 2: Write a program to print the following triangle where height h is given by user.
				int h;
                Scanner hh = new Scanner(System.in);
                h = hh.nextInt();
                int i, j, k, p;
                for (i = 0; i < h; i++) {
                    for (j = i - 1; j <= h; j++) {
                        System.out.print(" ");
                    }
                    for (k = 0; k <= i; k++) {
                        System.out.print(i);
                    }
                    for (p = k - 1; p >= 1; p--) {
                        System.out.print(i);
                    }
                    System.out.println("");
                }

					
			}else if(number ==3) {
				// TODO: Task 3: Write a program to print the following Roman 3 number.	
				for (int i = 0; i <= 7; i++) {
                    if (i > 1 && i <= 7) {
                        System.out.println(" *     *       * ");
                    }
                    if (i == 0 || i == 7) {
                        System.out.println("***   ***     ***");
                    }
                }
			}else {
				if(number == 0) status=false;
				else System.out.println("invalid number");
			}
			
		}while(status);

	}

}
