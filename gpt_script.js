class NutrientTable {
    constructor() {
        this.nutriKeys = ["water", "Kcal", "Protein", "Tryptophan", "Threonine", "Isoleucine", "Leucine", "Lysine", "Methionine", "Cystine", "Phenylalanine", "Tyrosine", "Valine", "Arginine", "Histidine", "Alanine", "Aspartic_acid", "Glutamic_acid", "Glycine", "Proline", "Serine", "Fat", "ala", "epa", "dpa", "dha", "omega6", "omega3", "Carb", "Fiber", "Sugar", "Ca", "Fe", "Mg", "P", "K", "Na", "Zn", "Cu", "Mn", "Se", "V_c", "B1", "B2", "B3", "B6", "B9", "B12", "V_a", "V_e", "V_k", "tsFat", "tmsFat", "tpusFat", "transFat", "cholest", "cname", "caffine", "alcho", "hydroxyproline", "laz", "V_d", "sucrose", "glucose", "frutose", "lactose", "maltose", "galctose", "strach", "id", "name", "sname", "group"];
        this.nutriArr = [];
        this.table = this.initializeTable();
    }

    initializeTable() {
        let table = {};
        this.nutriKeys.forEach(key => {
            table[key] = { data: [], high: 0, unit: 0 };
        });
        table.pop = this.removeLast;
        return table;
    }

    // Utility to remove the last item from nutriArr
    removeLast() {
        console.log("remove last func called");
        this.nutriArr.pop();
    }

    // Create the table
    createTable() {
        this.nutriArr.forEach(nutrient => {
            this.nutriKeys.forEach(key => {
                if (nutrient[key] !== undefined) {
                    if (['name', 'id', 'sname', 'group', 'cname'].includes(key)) {
                        this.table[key].data.push(nutrient[key]);
                    } else {
                        this.table[key].data.push(nutrient[key].v);
                        this.table[key].unit = nutrient[key].u;
                    }
                } else {
                    this.table[key].data.push('-');
                }
            });
        });
    }

    // Flush table data (reset everything)
    flushTableJSON() {
        this.table = this.initializeTable();
    }

    // Flush table header
    flushTableHeader() {
        const headerRow = document.getElementById('table-header-row');
        while (headerRow.children.length > 1) {
            headerRow.lastChild.remove();
        }
    }

    // Render the table header dynamically
    renderTableHeader() {
        this.flushTableHeader();
        this.table.name.data.forEach((name, index) => {
            const headerCell = document.createElement('th');
            headerCell.id = `header-${index}`;
            headerCell.innerHTML = `${name} <span onClick="nutrientTable.removeFood(event)" click_i="${index}">&#9421;</span>`;
            document.getElementById('table-header-row').appendChild(headerCell);
        });
    }

    // Flush the table body (clear all rows)
    flushTableBody() {
        this.nutriKeys.forEach(key => {
            const row = document.getElementById(`${key}-row`);
            while (row.children.length > 0) {
                row.lastChild.remove();
            }
        });
    }

    // Remove table data at a specific index
    removeTableIndexData(index) {
        this.nutriKeys.forEach(key => {
            this.table[key].data.splice(index, 1);
        });
    }

    // Remove nutrient data at a specific index
    removeNutrIndexData(index) {
        this.nutriArr.splice(index, 1);
    }

    // Remove food row from the table
    removeFood(event) {
        const index = event.target.getAttribute('click_i');
        this.removeTableIndexData(index);
        this.removeNutrIndexData(index);
        this.renderTableHeader();
        this.renderTableBody();
        this.showHigh();
    }

    // Show highest value in each nutrient column
    showHigh() {
        if (this.nutriArr.length > 1) {
            this.nutriKeys.forEach(key => {
                const arr = this.table[key].data;
                const highIndex = arr.reduce((maxIdx, curr, idx, arr) => (curr > arr[maxIdx] ? idx : maxIdx), 0);
                this.table[key].high = highIndex;
                document.getElementById(`${key}-value-${highIndex}`).style.fontWeight = '600';
                document.getElementById(`${key}-value-${highIndex}`).style.color = '#970d2e';
            });
        }
    }

    // Render the table body
    renderTableBody() {
        this.flushTableBody();
        this.nutriKeys.forEach(key => {
            const rowLength = this.table[key].data.length;
            const unit = this.table[key].unit ? this.table[key].unit : '';
            for (let i = 0; i < rowLength; i++) {
                const cell = document.createElement('td');
                cell.id = `${key}-value-${i}`;
                cell.classList.add('nutrient-value');
                cell.innerHTML = this.table[key].data[i] === '-' ? '' : `${this.table[key].data[i]} ${unit}`;
                document.getElementById(`${key}-row`).appendChild(cell);
            }
        });
    }

    // Check if an ID exists in the nutrient array
    idExist(id) {
        return this.nutriArr.some(item => item.id === id);
    }

    // Add new nutrient data from the API
    addNutrientData(url, id) {
        if (!this.idExist(id)) {
            fetch(`${url}?q=${id}`)
                .then(response => response.json())
                .then(data => {
                    if (data.result === 0) {
                        document.getElementById('result_status').innerText = `No result for ${id}`;
                    } else {
                        this.nutriArr.push(data);
                        this.flushTableJSON();
                        this.createTable();
                        this.renderTableHeader();
                        this.renderTableBody();
                        this.showHigh();
                        document.getElementById('result_status').innerText = `Result for ${id} added to array`;
                    }
                })
                .catch(error => console.error('Error:', error));
        } else {
            console.log("ID already exists");
        }
    }
}

// Create an instance of the NutrientTable class
const nutrientTable = new NutrientTable();

// Fetch nutrient data using a button click
document.getElementById("json").onclick = () => {
    fetch('http://localhost/php/request.php')
        .then(response => response.json())
        .then(data => {
            nutrientTable.nutriArr.push(JSON.parse(data));
            console.log(data);
        })
        .catch(error => console.error('Error:', error));
};

// Add search functionality
document.getElementById("search_submit").onclick = () => {
    const searchId = document.getElementById('search').value;
    nutrientTable.addNutrientData('http://localhost/php/request.php', searchId);
};
