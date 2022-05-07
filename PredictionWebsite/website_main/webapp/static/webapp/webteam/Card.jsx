import React from 'react'
import img from './boy.jpg';

import { Container, Col, Row, Button ,Card} from "react-bootstrap";

import { AiFillInstagram,AiFillLinkedin } from "react-icons/ai";

import './WebTeam.css';
import styles from './webcards.module.css';
function CardFunc(props) {
    return (
        <div style={{ margin:"30px" }}>
            <Card className={styles.card} style={{ width: '14rem', textAlign:'center', borderRadius:"5px"}}>
            <Card.Img  style={{height:'12rem'}} className="ourteamimg" variant="top" src={props.webimg}/>
            <Card.Body>
                <Card.Title style={{fontStyle:"bold"}} >{props.name}</Card.Title>
                <Card.Text style={{fontStyle:"italic"}} >
                {props.post}
                <Container>
                <Row>
                <ul style={{listStyle:"none",display:"flex",position:"relative",marginLeft:"1rem"}}>
                    <li>
                    <a href={props.insta} target="_blank" style={{ color: "blue" , textAlign: "center"}} className="icons"><AiFillInstagram size="2em"/></a>
                    </li>
                    <li>
                    <a href={props.linkd} target="_blank" style={{ color: "blue" , textAlign: "center"}} className="icons"><AiFillLinkedin size="2em"/></a>
                    </li>
                </ul>
                
                
              
                
                
                </Row>
                </Container>
                
                </Card.Text>
            </Card.Body>
            </Card>
        </div>
    )
}

export default CardFunc;
