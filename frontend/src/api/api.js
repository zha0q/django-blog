import axiosInstance from "./index"

//4


const axios = axiosInstance

export const getBlogs = (url) => {
  return axios.get(url)
}

export const postUser = (name, psw) =>{
  return axios.post("/api/user/", {
    'username': name,
    'password': psw,
  })
}

export const postUserChange = (url, name, psw, token) =>{
  return axios.patch(url, {
    'username': name,
    'password': psw,
  }, {
    headers: {Authorization: 'Bearer ' + token}
  })
}

export const postSubscribe = (fans, blogger) =>{
  return axios.post("/api/subscribe/", {
    'fans': fans,
    'blogger': blogger,
  })
}

export const postLogin = (name, psw) =>{
  return axios.post("/api/token/", {
    'username': name,
    'password': psw,
  })
}

export const postImg = (data) =>{
  return axios.post("/api/avatar/",
    data, {
    headers: {
            'Content-Type': 'multipart/form-data',
            // 'Authorization': 'Bearer ' + token
          }})
}

export const postBlog = (title, image, content, token) =>{
  return axios.post("/api/article/", {
    'a_title': title,
    'avatar_id': image,
    'a_content': content,
  },{
    headers: {Authorization: 'Bearer ' + token}
  })
}

export const postComment = (content, article, token) =>{
  return axios.post("/api/comment/", {
    'c_content': content,
    'article': article,
  },{
    headers: {Authorization: 'Bearer ' + token}
  })
}
