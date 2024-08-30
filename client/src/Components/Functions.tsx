import { apiUrl } from "./Constants";
import axios from "axios";

export async function datapull(query_key: string){
    return axios.get(apiUrl + "datapull/" + query_key)
}