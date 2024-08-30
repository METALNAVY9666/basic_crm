import { useEffect, useState } from "react"
import { datapull } from "./Functions";

export default function Interventions(){
    const [interventions, setInterventions] = useState<Array<Array<string>>>([]);

    useEffect(() => {datapull("get_interventions").then(response => setInterventions(response.data))}, [])
    return <>
    <table>
        <tbody>
                {interventions.map((intervention, interventionIndex) => <tr key={interventionIndex}>{intervention.map((value, index) => <td key={index}>{value}</td>)}</tr>)}
            </tbody>
    </table></>
}