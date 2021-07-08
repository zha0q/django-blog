import axiosInstance from "./index"

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

export const postLogin = (name, psw) =>{
  return axios.post("/api/token/", {
    'username': name,
    'password': psw,
  })
}

export const postBlog = (title, content, token) =>{
  return axios.post("/api/article/", {
    'a_title': title,
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
