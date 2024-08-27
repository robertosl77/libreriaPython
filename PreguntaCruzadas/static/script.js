const dropzone = document.getElementById('dropzone');
const fileInput = document.getElementById('fileInput');
const questionsContainer = document.getElementById('questions');
const answersContainer = document.getElementById('answers');
const checkBtn = document.getElementById('checkBtn');
const summary = document.getElementById('summary');
const counter = document.getElementById('counter');
const percentages = document.getElementById('percentages');
const indicators = document.getElementById('indicators');
const progressGrid = document.getElementById('progressGrid');
let questions = [];
let answers = [];
let pairs = {};
let currentQuestionSet = [];
let currentAnswerSet = [];
let correctQuestionCount = 0;
let incorrectQuestionCount = 0;
const batchSize = 5;
let selectedQuestion = null;

const colors = [
    "#ADD8E6", "#90EE90", "#FFB6C1", "#FFD700", 
    "#DDA0DD", "#FFDEAD", "#D2B48C", "#FFFACD", 
    "#AFEEEE", "#D3D3D3"
];

dropzone.addEventListener('click', () => fileInput.click());

dropzone.addEventListener('dragover', (e) => {
    e.preventDefault();
    dropzone.style.borderColor = '#000';
});

dropzone.addEventListener('dragleave', (e) => {
    e.preventDefault();
    dropzone.style.borderColor = '#ccc';
});

dropzone.addEventListener('drop', (e) => {
    e.preventDefault();
    dropzone.style.borderColor = '#ccc';
    const file = e.dataTransfer.files[0];
    if (file) {
        console.log('Archivo seleccionado:', file);
        readExcel(file);
    }
});

fileInput.addEventListener('change', (e) => {
    const file = e.target.files[0];
    if (file) {
        console.log('Archivo seleccionado:', file);
        readExcel(file);
    }
});

function readExcel(file) {
    const formData = new FormData();
    formData.append('file', file);

    fetch('/upload', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        console.log('Datos recibidos del servidor:', data);
        parseData(data);
    })
    .catch(error => {
        console.error('Error al cargar el archivo:', error);
    });
}

function parseData(data) {
    questions = data.questions;
    answers = data.answers;

    console.log('Preguntas:', questions);
    console.log('Respuestas:', answers);

    summary.innerHTML = `Preguntas leídas: ${questions.length}<br>Respuestas leídas: ${answers.length}`;
    indicators.style.display = 'flex';
    checkBtn.style.display = 'block';

    updateCounter();
    createProgressGrid();
    displayNextBatch();
}

function createProgressGrid() {
    progressGrid.innerHTML = '';
    questions.forEach((q, index) => {
        const cell = document.createElement('div');
        cell.classList.add('grid-cell');
        cell.dataset.index = index;
        cell.dataset.id = q.id;

        const tooltip = document.createElement('div');
        tooltip.classList.add('tooltip');
        tooltip.textContent = q.text;

        cell.appendChild(tooltip);
        progressGrid.appendChild(cell);
    });
}

function updateProgressGrid() {
    const cells = document.querySelectorAll('.grid-cell');
    questions.forEach((q, index) => {
        const cell = cells[index];
        if (q.status === 'correct') {
            cell.style.backgroundColor = 'green';
        } else if (q.status === 'incorrect') {
            cell.style.backgroundColor = 'red';
        } else if (q.status === 'unanswered') {
            cell.style.backgroundColor = 'yellow';
        } else {
            cell.style.backgroundColor = 'white';
        }
        cell.classList.remove('active'); // Reset active status
    });
}

function displayNextBatch() {
    if (questions.filter(q => q.status === 'unseen').length === 0) {
        summary.innerHTML = `Juego completado. Total de preguntas: ${correctQuestionCount + incorrectQuestionCount}`;
        questionsContainer.innerHTML = '';
        answersContainer.innerHTML = '';
        checkBtn.style.display = 'none';
        return;
    }

    currentQuestionSet = getRandomSubset(questions.filter(q => q.status === 'unseen'), batchSize);
    currentAnswerSet = [];

    currentQuestionSet.forEach(q => {
        currentAnswerSet = currentAnswerSet.concat(q.answers);
        q.status = 'seen';
    });

    currentQuestionSet = shuffleArray(currentQuestionSet);
    currentAnswerSet = shuffleArray(currentAnswerSet);

    questionsContainer.innerHTML = '';
    answersContainer.innerHTML = '';
    pairs = {};

    currentQuestionSet.forEach((q, index) => {
        const div = document.createElement('div');
        div.classList.add('question');
        div.textContent = q.text;
        div.dataset.id = q.id;
        div.dataset.color = colors[index % colors.length];
        questionsContainer.appendChild(div);

        const gridCell = document.querySelector(`.grid-cell[data-id="${q.id}"]`);
        if (gridCell) {
            gridCell.classList.add('active');
            // Ensure the tooltip text is updated
            gridCell.querySelector('.tooltip').textContent = q.text;
        }
    });

    currentAnswerSet.forEach(a => {
        const div = document.createElement('div');
        div.classList.add('answer');
        div.textContent = a.text;
        div.dataset.id = a.id;
        div.dataset.questionId = a.questionId;
        answersContainer.appendChild(div);
    });

    setupSelection();
}

function setupSelection() {
    const questionElements = document.querySelectorAll('.question');
    const answerElements = document.querySelectorAll('.answer');

    questionElements.forEach(q => {
        q.addEventListener('click', () => {
            if (selectedQuestion === q) {
                q.classList.remove('selected');
                q.style.backgroundColor = '';
                clearSelection(q.dataset.id);
                selectedQuestion = null;
            } else {
                if (selectedQuestion) {
                    selectedQuestion.classList.remove('selected');
                }
                q.classList.add('selected');
                q.style.backgroundColor = q.dataset.color;
                selectedQuestion = q;
            }
        });
    });

    answerElements.forEach(a => {
        a.addEventListener('click', () => {
            if (selectedQuestion) {
                const questionId = selectedQuestion.dataset.id;
                if (!pairs[questionId]) {
                    pairs[questionId] = [];
                }
                if (pairs[questionId].includes(a.dataset.id)) {
                    pairs[questionId] = pairs[questionId].filter(id => id !== a.dataset.id);
                    a.style.backgroundColor = '';
                } else {
                    pairs[questionId].push(a.dataset.id);
                    a.style.backgroundColor = selectedQuestion.dataset.color;
                }
            }
        });
    });
}

function clearSelection(questionId) {
    if (pairs[questionId]) {
        pairs[questionId].forEach(answerId => {
            const answerElement = document.querySelector(`.answer[data-id="${answerId}"]`);
            if (answerElement) {
                answerElement.style.backgroundColor = '';
            }
        });
        delete pairs[questionId];
    }
}

checkBtn.addEventListener('click', () => {
    let correctPairs = [];
    let incorrectPairs = [];
    let unansweredPairs = [];

    currentQuestionSet.forEach(question => {
        const questionId = question.id;
        if (pairs[questionId] && pairs[questionId].length > 0) {
            let answeredCorrectly = false;
            pairs[questionId].forEach(answerId => {
                const answerElement = document.querySelector(`.answer[data-id="${answerId}"]`);
                const questionElement = document.querySelector(`.question[data-id="${questionId}"]`);
                if (answerElement.dataset.questionId === questionId) {
                    correctPairs.push({ questionId, answerId });
                    questionElement.style.backgroundColor = 'green';
                    answerElement.style.backgroundColor = 'green';
                    answeredCorrectly = true;
                } else {
                    incorrectPairs.push({ questionId, answerId });
                    questionElement.style.backgroundColor = 'orange';
                    answerElement.style.backgroundColor = 'orange';
                }
            });
            if (answeredCorrectly) {
                question.status = 'correct';
            } else {
                question.status = 'incorrect';
            }
        } else {
            unansweredPairs.push(questionId);
            const questionElement = document.querySelector(`.question[data-id="${questionId}"]`);
            questionElement.style.backgroundColor = 'orange';
            question.status = 'unanswered';
        }
    });

    setTimeout(() => {
        correctPairs.forEach(pair => {
            const questionElement = document.querySelector(`.question[data-id="${pair.questionId}"]`);
            const answerElement = document.querySelector(`.answer[data-id="${pair.answerId}"]`);
            questionElement.style.backgroundColor = '';
            answerElement.style.backgroundColor = '';
        });

        incorrectPairs.forEach(pair => {
            const questionElement = document.querySelector(`.question[data-id="${pair.questionId}"]`);
            const answerElement = document.querySelector(`.answer[data-id="${pair.answerId}"]`);
            questionElement.style.backgroundColor = '';
            answerElement.style.backgroundColor = '';
        });

        unansweredPairs.forEach(questionId => {
            const questionElement = document.querySelector(`.question[data-id="${questionId}"]`);
            questionElement.style.backgroundColor = '';
        });

        correctQuestionCount += correctPairs.length;
        incorrectQuestionCount += incorrectPairs.length + unansweredPairs.length;
        updateCounter();
        updateProgressGrid();
        displayNextBatch();
    }, 2000);
});

function updateCounter() {
    const totalQuestions = questions.length;
    const answeredQuestions = correctQuestionCount + incorrectQuestionCount;
    const unansweredQuestions = questions.filter(q => q.status === 'unseen').length;
    const totalAnswered = answeredQuestions + unansweredQuestions;

    summary.innerHTML = `Preguntas leídas: ${questions.length}<br>Respuestas leídas: ${answers.length}`;
    counter.innerHTML = `Preguntas correctas: ${correctQuestionCount}<br>Preguntas incorrectas: ${incorrectQuestionCount}<br>Preguntas faltantes: ${unansweredQuestions}`;
    percentages.innerHTML = `
        % de avance: ${(answeredQuestions / totalQuestions * 100).toFixed(2)}%<br>
        % de correctas: ${(correctQuestionCount / totalAnswered * 100).toFixed(2)}%<br>
        % de incorrectas: ${(incorrectQuestionCount / totalAnswered * 100).toFixed(2)}%<br>
        % de no respondidas: ${(unansweredQuestions / totalQuestions * 100).toFixed(2)}%
    `;
}

function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
}

function getRandomSubset(array, size) {
    let shuffled = shuffleArray(array.slice());
    return shuffled.slice(0, size);
}
