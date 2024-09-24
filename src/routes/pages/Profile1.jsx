import React from "react";
import "./Profile1.css";
import Header from "./Header";
import HeartImage from "../images/ic_round-heart-broken.png";

function Profile1() {
  return (
    <div className="Profile1">
      <Header isAuthenticated={true} />
      {/* Передаем isAuthenticated в Header */}
      <div className="avatar"></div>
      {/* <img className="avatar" src="path_to_avatar" alt="User Avatar" /> */}
      <p className="name">Максим Максимович</p>
      <h1>Username</h1>
      <h3>
        Повседневная практика показывает, что внедрение современных методик
        напрямую зависит от инновационных методов
      </h3>
      <nav>
        <ul>
          <li>
            <a href="#added-articles">Добавленные статьи</a>
          </li>
          <li>
            <a href="#saved-drafts">Сохраненные черновики</a>
          </li>
          <li>
            <a href="#liked-articles">Лайкнутые статьи</a>
          </li>
        </ul>
      </nav>
      <hr />
      <div className="ProfileText">
        <div className="LittleAvatar"></div>
        <h4 className="username1">Username</h4>
        <h4 className="ProfileTime">10 минут назад</h4>
      </div>
      <div className="HeartVector">
        <img className="Heart" src={HeartImage} alt="HeartImage"></img>
      </div>
    </div>
  );
}

export default Profile1;
