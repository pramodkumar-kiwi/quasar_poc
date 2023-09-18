/*
  File: used for application form
  Description: This file contains the implementation of a chatbot.
  Date: June 20, 2023
*/
(function($) {
    'use strict';

    var allData = [];
    var question_type = 0;
    var index = 0;
    var shared_amount = 0;
    var medical_quest = 8;
    var dob;

    $(document).ready(function() {
        var enableForm = false;

        // Disable the textarea and submit button initially
        $("#message-id").prop('disabled', true);
        $("#startRecordingButton").prop('disabled', true);

        // Event listener for "Let’s Do It" button click
        $('.lets-do-btn').on('click', function() {
            // Enable the textarea and submit button
            $("#message-id").prop('disabled', false);
            $("#startRecordingButton").prop('disabled', false);
            enableForm = true;

            // Disable the content section
            $('.lets-go-chat .content').prop('disabled', true);
        });

        var status = false;
        var loginFormId = $('#applicationChatForm');

        loginFormId.validate({
            submitHandler: function(form, event) {
                event.preventDefault();

                // Check if the form is enabled
                if (!enableForm) {
                    return;
                }

                if (status === true) {
                    return true;
                }

                status = true;
                document.getElementById('message-id').placeholder = "Type your message here";
                $('.bot-typing').addClass('active');
                $('.chat-body').addClass('response-generate');
                var formData = loginFormId.serialize();
                var element = document.getElementById("insurance-app-chat");
                var user_message = document.getElementById("message-id").value.trim();
                $("#message-id").val("");
                $("#formButton").prop('disabled', true);
                update_user_html(element, user_message);
                // Submit the form using AJAX
                $.ajax({
                    url: load_constant.api_base_url + 'application-form/?question_type=' + question_type + '&index=' + index + '&shared_amount=' + shared_amount + '&medical_quest=' + medical_quest,
                    type: form.method,
                    data: formData,
                    success: function(response) {
                        update_table_data(response, user_message)
                        update_ai_html(response, element);
                        $('.bot-typing').removeClass('active');
                        $('.chat-body').removeClass('response-generate');
                        status = false;
                        question_type = response.data.question_type;
                        index = response.data.index;
                        shared_amount = response.data.shared_amount || shared_amount;
                        medical_quest = response.data.medical_quest || medical_quest;
                        if (question_type === null) {
                            // Disable the submit button and textarea
                            $("#message-id").prop('disabled', true);
                            $("#startRecordingButton").prop('disabled', true);

                            // Display all questions and answers
                            displayQuestionsAndAnswers();
                        }
                    },
                    error: function(xhr, status, error) {
                        $('.bot-typing').removeClass('active');
                        $('.chat-body').removeClass('response-generate');
                        status = false;
                    }
                });
            },
            rules: {
                answer: {
                    minlength: 1,
                    maxlength: 500,
                    nowhitespace: true
                }
            },
            messages: {
                answer: {
                    minlength: ""
                }
            },
            success: function(error, element) {}
        });

        $.validator.addMethod(
            "nowhitespace",
            function(value, element) {
                var strippedValue = value.replace(/\s/g, '');
                return strippedValue !== '';
            },
            ""
        );

        // Event listener for "Let’s Do It" button click
        $('.lets-do-btn').on('click', function() {
            var element = document.getElementById("insurance-app-chat");
            update_user_html(element, "Let’s do it");
            $('.bot-typing').addClass('active');
            $('.chat-body').addClass('response-generate');
            $('#message-id').focus();
            $("#letsDoButton").prop('disabled', true);

            // Perform API call
            var formData = loginFormId.serialize();
            $.ajax({
                url: load_constant.api_base_url + 'application-form/?question_type=' + question_type + '&index=' + index + '&shared_amount=' + shared_amount + '&medical_quest=' + medical_quest,
                type: 'POST',
                data: formData,
                success: function(response) {
                    update_table_data(response, '')
                    update_ai_html(response, element);
                    $('.bot-typing').removeClass('active');
                    $('.chat-body').removeClass('response-generate');
                    question_type = response.data.question_type;
                    index = response.data.index;
                    shared_amount = response.data.shared_amount || shared_amount;
                    medical_quest = response.data.medical_quest || medical_quest;
                },
                error: function(xhr, status, error) {
                    $('.bot-typing').removeClass('active');
                    $('.chat-body').removeClass('response-generate');
                }
            });
        });
    });

    /**
     * Updates the HTML element with the user's message for chat.
     *
     * @param {HTMLElement} element - The HTML element to update with the user message.
     * @param {string} user_message - The message entered by the user.
     * @returns {boolean} - Returns true if the update was successful.
     */
    function update_user_html(element, user_message) {
            var message_html = '<div class="user-message"><p>' + user_message + '</p></div>';
            element.innerHTML += message_html;
            scrollToBottom(element);

            return true;
        }

        /**
         * Updates the HTML element with the AI's response for chat.
         *
         * @param {object} response - The AI's response object.
         * @param {HTMLElement} element - The HTML element to update with the AI's response.
         * @returns {boolean} - Returns true if the update was successful.
         */
    function update_ai_html(response, element) {
        var htmlContent = '<div class="bot-message"><div class="bot-thumb"><img src="' +
            load_constant.base_url + '/static/images/fred.png" alt="Quasar Market" /></div><p>' +
            response.data.question.replace(/\n/g, '<br>') + '</p></div>';
        element.innerHTML += htmlContent;
        scrollToBottom(element);
        return true;
    }

    /**
     * Scrolls the given element to the bottom.
     *
     * @param {HTMLElement} element - The HTML element to scroll to the bottom.
     */
    function scrollToBottom(element) {
        element.scrollTop = element.scrollHeight;
    }

    document.addEventListener('DOMContentLoaded', function() {
        const textarea = document.getElementById('message-id');
        const loginFormId = $('#applicationChatForm');

        textarea.addEventListener('input', function() {
            textarea.style.height = 'auto';
            textarea.style.height = textarea.scrollHeight + 'px';
        });

        textarea.addEventListener('keydown', function(event) {
            if (event.key === 'Enter') {
                if (!event.shiftKey) {
                    event.preventDefault();
                    loginFormId.submit(); // Submit the form
                } else {
                    // Shift + Enter is pressed
                     textarea.value += '\n';
                     textarea.style.height = 'auto';
                     textarea.style.height = textarea.scrollHeight + 'px';
                     textarea.scrollTop = textarea.scrollHeight;
                }
            }
        });

        loginFormId.on('submit', function(event) {
            event.preventDefault();
        });
    });

    document.addEventListener('DOMContentLoaded', function() {
        document.getElementById('message-id').addEventListener('keyup', function(event) {
            const messageInput = event.target;
            const trimmedValue = messageInput.value.trim();
            if (trimmedValue.length > 0) {
                $('#formButton').prop('disabled', false);
            } else {
                $('#formButton').prop('disabled', true);
            }
        });
    });

    function displayQuestionsAndAnswers() {
        var tableHtml = '<h2 class="data-table-heading">Here is the summary of your responses</h2>';
        tableHtml += '<table class="data-table">';
        for (var i = 0; i < allData.length-1; i++) {
            var question = allData[i].question || '';
            var answer = allData[i].answer || '';
            var user_answer = capitalizeFirstLetterIfValid(answer);
            if (question.includes('date')){
                var formatted_date = calculateAge(answer)
                user_answer = formatted_date.formattedDate
               }
            if (question.includes('Please enter your date of birth'))
                dob = answer;
            if (question.includes('Please enter your Social Security number.')){
              var age = calculateAge(dob);
              tableHtml += '<tr><td>' + 'Your age (Years)' + '</td><td>' + age.age + '</td></tr>';
            }
            if (question.includes('provide the details of your beneficiary')){
                tableHtml += '<tr><td>' + "Beneficiary's type" + '</td><td>' + "Primary" + '</td></tr>';
            }
            if (question.includes('Social Security Number')) {
                user_answer = 'XXX-XX-' + user_answer;
            }
            tableHtml += '<tr><td>' + question + '</td><td>' + user_answer + '</td></tr>';
        }
        tableHtml += '</table>';
        var element = document.getElementById('insurance-app-chat');
        element.innerHTML += tableHtml;
        var summaryHeading = document.querySelector('.data-table-heading');
        if (summaryHeading) {
            var scrollOptions = {
                behavior: 'smooth',
                block: 'start'
            };

            var parentElement = summaryHeading.parentElement;
            var paddingTop = 20;
            parentElement.scrollTo({
                top: summaryHeading.offsetTop - paddingTop,
                ...scrollOptions
            });
        }
    }

    function capitalizeFirstLetterIfValid(answer) {
      if (answer.indexOf('@') === -1 && answer.indexOf('.') === -1) {
        return answer.charAt(0).toUpperCase() + answer.slice(1);
      } else {
        return answer;
      }
    }

    /**
     * Updates table data based on the response and user message.
     * @param {Object} response - The response object containing question and index data.
     *   - response.data.question: The question received from the response.
     *   - response.data.index: The index received from the response.
     *   - response.data.question_type: The question type received from the response.
     * @param {string} user_message - The message provided by the user in response to the question.
     * @returns {boolean} - Indicates the success of the update operation.
    */
    function update_table_data(response, user_message) {
        var question = response.data.question || '';
        var index = response.data.index || 0;
        var question_type = response.data.question_type || 0;
        const count = allData.length;
        if (allData.length === 0) {
           allData.push({ question: question, answer: '', index: index, question_type: question_type });
        }else{

            allData[allData.length - 1].answer = user_message
            const lastElement = allData[allData.length - 1];
            if(lastElement.index === index && lastElement.question_type === question_type){
            }else{
                allData.push({ question: question, answer: '', index: index, question_type: question_type });
            }
        }
        return true
    }

// calculate age with date formate
function calculateAge(dateString) {
  const cleanDateString = dateString.replace(/\D/g, '');
  let day, month, year;
  if (cleanDateString.length === 8) {
    day = cleanDateString.substring(2, 4);
    month = cleanDateString.substring(0, 2);
    year = cleanDateString.substring(4);
  } else {
    const parts = cleanDateString.split(/[^\d]+/);
    day = parts[1];
    month = parts[0];
    year = parts[2];
  }
  const formattedDate = `${month.padStart(2, '0')}-${day.padStart(2, '0')}-${year}`;
  const birthDate = new Date(Date.UTC(year, month - 1, day));
  const today = new Date();
  let age = today.getUTCFullYear() - birthDate.getUTCFullYear();
  const monthDiff = today.getUTCMonth() - birthDate.getUTCMonth();
  if (monthDiff < 0 || (monthDiff === 0 && today.getUTCDate() < birthDate.getUTCDate())) {
    age--;
  }

  return {
    age: age,
    formattedDate: formattedDate
  };
}

})(jQuery);
