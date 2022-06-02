//Окунев Жданов БПМ20-2
#include <iostream>

struct node {
    int key_value;
    node* left;
    node* right;
};

class btree {
public:
    btree();
    ~btree();

    void insert(int key);
    bool search(int key);
    void destroy_tree();
    void treeprint();

private:
    void treeprint(node* leaf);
    void destroy_tree(node* leaf);
    void insert(int key, node* leaf);
    node* search(int key, node* leaf);

    node* root;
};


btree::btree() {
    root = NULL;
}

btree::~btree() {
    destroy_tree();
}

void btree::destroy_tree(node* leaf) {
    if (leaf != NULL) {
        destroy_tree(leaf->left);
        destroy_tree(leaf->right);
        delete leaf;
    }
}

void btree::treeprint(node* leaf) {
    if (leaf != NULL) {
        treeprint(leaf->left);
        std::cout << leaf->key_value << " ";
        treeprint(leaf->right);
    }
    
}

void btree::insert(int key, node* leaf) {
    if (key < leaf->key_value) {
        if (leaf->left != NULL) {
            insert(key, leaf->left);
        }
        else {
            leaf->left = new node;
            leaf->left->key_value = key;
            leaf->left->left = NULL;
            leaf->left->right = NULL;
        }

    }
    else if (key >= leaf->key_value) {
        if (leaf->right != NULL) {
            insert(key, leaf->right);
        }
        else {
            leaf->right = new node;
            leaf->right->key_value = key;
            leaf->right->left = NULL;
            leaf->right->right = NULL;
        }
    }
}

node* btree::search(int key, node* leaf) {
    if (leaf != NULL) {
        if (key == leaf->key_value) {
            return leaf;
        }
        if (key < leaf->key_value) {
            return search(key, leaf->left);
        }
        else {
            return search(key, leaf->right);
        }
    }
    else {
        return NULL;
    }
}

void btree::insert(int key) {
    if (root != NULL) {
        insert(key, root);
    }
    else {
        root = new node;
        root->key_value = key;
        root->left = NULL;
        root->right = NULL;
    }
}

bool btree::search(int key) {
    if (search(key, root))
        return true;
    else return false;
}

void btree::destroy_tree() {
    destroy_tree(root);
}

void btree::treeprint()
{
    treeprint(root);
}



int main()
{
    btree a;
    a.insert(105);
    a.insert(18);
    a.insert(7);
    a.insert(296);
    a.insert(9);
    a.insert(51);
    a.treeprint();
    std::cout << "\n";
    std::cout << (a.search(9) ? "Yes" : "No");
    
}
