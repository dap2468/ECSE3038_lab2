
1) update_todo_by_id(), handles incoming `PATCH` requests from the demo site. The function accepts the ID of the todo that should be updated and a todo request object that has the desired changes. The function then search for the matching todo object in your todo list and update it with the received changes.

The PATCH handler responds with the entire todo object as it exists after being updated along with the `200 OK` status code. 

If there exists no todo object with the provided ID, the PATCH handler responds with a `404 Not Found` status code.




2) delete_todo_by_id(), handles incoming `DELETE` requests from the demo site. The function accept the ID of the todo that should be deleted. The function should then search for the matching todo object in your todo list and remove it.

The DELETE handler responds with a JSON object indicating that an object has been successfully deleted along with the `200 OK` status code. 

If there exists no todo object with the provided ID, the DELETE handler responds with a `404 Not Found` status code.



REASON FOR WRITTING CODE IS FOR LAB 2


Arceus - Arceus is an equine being similar to a Qilin. Its body color is white with a gray, vertically-striated underside, the pattern of which has similar recurrences on the underside of Arceus's mane, tail, and face, and Arceus's pointed feet are tipped with gold hooves. Its mane is quite long, jutting away from its head, and its face is gray, with green eyes and red pupils, and a green circular pattern below its eyes.
   