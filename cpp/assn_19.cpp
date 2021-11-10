#include<iostream>
using namespace std;
struct node
{
	string name;
	int PRN;
	node *next, *head=NULL;
	void accept();
	void display();
	void del();
}ob;

void node::accept() 
{
	node *ptr, *temp;
	ptr=new node;
	if(head==NULL)
	{
		cout<<"Enter President's Name and PRN: ";
		cin>>ptr->name;
		cin>>ptr->PRN;
		ptr->next=NULL;
		head=ptr;
	}
	else
	{
		if(head->next==NULL)
		{
			cout<<"Enter Secretary's Name and PRN: ";
			cin>>ptr->name;
			cin>>ptr->PRN;
			ptr->next=NULL;
			head->next=ptr;
		}
		else
		{
			cout<<"Enter Member's Name and PRN: ";
			cin>>ptr->name;
			cin>>ptr->PRN;
			ptr->next=NULL;
			temp=head;

			while(temp->next->next!=NULL)
			{
				temp=temp->next;
			}

			ptr->next=temp->next;
			temp->next=ptr;
		}
	}
}

void node::display()
{
	node *temp;
	cout<<"\nThe Pinnacle Club information is:"<< endl;
	temp=head;
	while(temp!=NULL)
	{
		cout<<temp->name<<" ";
		cout<<temp->PRN<<" "<<endl;
		temp=temp->next;
	}

}

int main()
{
	int ch, n;
	char choice;
	do
	{
		cout<<"Press 1 to insert president,secretary and members:"<< endl;
		cout<<"Press 2 to Display Members of the club:"<< endl;
		cin>>ch;
		switch(ch)
		{
			case 1:
				cout<< "Enter number of members to add: ";
				cin>> n;
				for(int i = 0; i < n; i++) ob.accept();
				cout<< "Successfully Added!"<< endl;
				break;
			case 2:
				ob.display();
				break;
		}
		cout<<"\nDo you want to continue? (press y or n): ";
		cin>>choice;
		cout<< endl;
	}while(choice=='Y'|| choice=='y');
}