#include <stdio.h>
#include <string.h>
#include <stdlib.h>
struct node 
{
  int data;
  struct node *left,*right;
};

struct node* create(struct node* root){
    int x;
                                                                           //here try to allocate the  memory after the condition user wants newnode 
    // struct node*newnode;                                                 //or not because if user press -1  and u had already allocated the memory above then memory is waste :(         
    // newnode=(struct node*)malloc(sizeof(struct node));     
    printf("enter data : press -1 for no node\n");     
    scanf("%d",&x);
    if(x==-1){                                           //here condition to return null is -1 so in printf function write press -1 for no node 
        return 0;
    }
    else{                                                           //as u passed the root as pointer here u will allocate the memory for it so u don't need anyother pointer   
        root=(struct node*)malloc(sizeof(struct node));           //here now user wants a node so u created , definitely no memory wastage
        root->data=x;
        printf("enter left child of %d\n",x);
        root->left=create(root->left);                          // here now root memory is allocated and for the left pointer it again called create function recrusively to create node at left
        printf("enter right child of %d\n",x);
        root->right=create(root->right);                         // same for the right pointer                              
    }
    return root;     
}

//i have written this function to check whether the tree create or not
void display( struct node *root)           ////basically this is preorder traveral of binary tree
{
    if(root== NULL)
    return;
    printf("%d ",root->data);
    display(root->left);
    display(root->right);
}


int main()
{
    struct node* root = NULL;

    //here in create function u need to pass the root node so that u can create the root node and recursively create all other nodes
    // as root here is just a pointer u didn't allocated memory for it
    root= create(root);
    display(root);
    return 0;
}