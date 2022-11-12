import React, { Fragment, useState } from 'react'
import "antd/dist/antd.min.css";
import { Typography } from 'antd';
import { Input } from 'antd';
import './Homepage.css'
import ReactPlayer from 'react-player'
import LanguageCard from './LangaugeCard';

const { Search } = Input;
const { Title } = Typography;

const languages = [
    {
        title: "Hindi",
        src: "https://upload.wikimedia.org/wikipedia/commons/b/bc/Flag_of_India.png",
    },
    {
        title: "Spanish",
        src: "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/2560px-Flag_of_Spain.svg.png",
    },
    {
        title: "German",
        src: "https://upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/2560px-Flag_of_Germany.svg.png",
    },
    {
        title: "English",
        src: "https://upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/2560px-Flag_of_the_United_States.svg.png",
    },
    {
        title: "Russian",
        src: "https://upload.wikimedia.org/wikipedia/en/thumb/f/f3/Flag_of_Russia.svg/2560px-Flag_of_Russia.svg.png",
    },
    {
        title: "italan",
        src: "https://toppng.com/uploads/preview/indian-flag-11551056347wdhxdrdrmw.png",
    },
    {
        title: "SWISS",
        src: "https://toppng.com/uploads/preview/indian-flag-11551056347wdhxdrdrmw.png",
    },
]
const Homepage = () => {

    const [videoUrl, setVideoUrl] = useState("");
    const onSearch = (value) => {
        setVideoUrl(value)
        console.log(value);
    }

    return (
        <Fragment>
            <div className="homepage">
                <div className="homepage__container">
                    <div className="homepage__container--heading">
                        <Title>AUDIO DUBBING FOR YOUTUBE VIDEOS</Title>
                    </div>
                    <div className="video__searchbar">
                        <Search placeholder="Enter youtube url to continue dubbing" enterButton size='large' onSearch={onSearch} />
                    </div>

                    <div className="video__container">
                        <ReactPlayer url={videoUrl} />
                    </div>

                    <div className="language__options">
                        {
                            languages.map((language, idex) => (
                                <LanguageCard image={language} key={idex} />
                            ))
                        }
                    </div>
                </div>
            </div>
        </Fragment>
    )
}

export default Homepage