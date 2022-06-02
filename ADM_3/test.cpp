#include<iostream>
using namespace std;

class Stack
{
   public:
   Stack()
   {
      size = 0;
      head = nullptr;
   };
   void push(int arg)
   {
      if (size == 0)
      {
         head = new Node(arg);
      }
      else
      {
         Node* temp = head;
         while (temp->pNext != nullptr)
         {
            temp = temp->pNext;
         }
         temp->pNext = new Node(arg);
      }
      size++;
   };
   void pop()
   {
      if (size == 0)
      {
         cout << "Error" << endl;
      }
      else
      {
         if (size == 1)
      {
         Node* temp = head;
         head = nullptr;
         delete temp;
      }
      else
      {
         Node* temp = head;
         for (int i = 1; i < getsize()-1; i++)
         {
            temp = temp->pNext;
         }
         Node* del = temp->pNext;
         temp->pNext = nullptr;
         delete del;
      }
      size--;
      }
   };
   int top()
   {
      if (size == 0)
      {
         cout << "Error" << endl;
      }
      else
      {
         Node* temp = head;
         while (temp->pNext != nullptr)
         {
            temp = temp->pNext;
         }
         return temp->data;
      }
   }
   int getsize()
   {
      return size;
   };
   void print()
   {
      if (size == 0)
      {
         cout << "Stack is empty";
      }
      else
      {
         Node*temp = head;
         while(temp != nullptr)
         {
            cout << temp->data << endl;
            temp = temp->pNext;
         }
      }
   }

   private:
   struct Node
   {
      int data;
      Node* pNext;
      Node(int data = int(), Node*pNext = nullptr)
      {
         this->data = data;
         this->pNext = pNext;
      }
   };
   Node* head;
   int size;
};

int main()
{
   Stack test;
   int i = 0;
   string command;
   int arg;
   while(command != "stop")
   {
      cin >> command;
      if (command == "push")
      {
         cin >> arg;
         test.push(arg);
         cout << "--------------------" << endl;
         test.print();
         cout << "--------------------" << endl;
      }
      else if (command == "pop")
      {
         test.pop();
         cout << "--------------------" << endl;
         test.print();
         cout << "--------------------" << endl;
      }
      else if (command == "top")
      {
         cout << test.top() << endl;
      }
      else if (command == "size")
      {
         cout << test.getsize() << endl;
      }
   }
   cout << "OK";
}

