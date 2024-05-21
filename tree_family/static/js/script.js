// family_tree.js
document.addEventListener('DOMContentLoaded', () => {
    const familyTree = document.getElementById('family-tree');
    const parentNodes = familyTree.querySelectorAll('.parent-node');

    parentNodes.forEach((node) => {
        node.addEventListener('click', () => {
            node.classList.toggle('expanded');
            node.classList.toggle('collapsed');
        });
    });
});
