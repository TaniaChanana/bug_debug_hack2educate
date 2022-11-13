import React, { Fragment, useState } from 'react'
import "antd/dist/antd.min.css";
import { Typography } from 'antd';
import { Input } from 'antd';
import './Homepage.css'
import ReactPlayer from 'react-player/youtube'
import LanguageCard from './LangaugeCard';
import ReactWebMediaPlayer from 'react-web-media-player';
import { LoadingOutlined } from '@ant-design/icons';
import { Spin } from 'antd';
const { Search } = Input;
const { Title } = Typography;
const antIcon = <LoadingOutlined style={{ fontSize: 56 }} spin />;
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
    // const [loading, setLoading] = useState(false);
    const [dubFilter, setDubFilter] = useState(false);
    const onSearch = (value) => {
        setVideoUrl(value);
        setDubFilter(false);
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

                    {videoUrl.length ? <Fragment>
                        <div className="video__container">
                            {!dubFilter ? <ReactPlayer url={videoUrl} />
                                :
                                <ReactWebMediaPlayer
                                    width={640}
                                    height={360}
                                    autoplay
                                    title="My own video player"
                                    video="http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4"
                                    thumbnail="https://any-link.com/video-thumbnail.jpg"
                                />}
                        </div>

                        <div className="language__options">
                            {
                                languages.map((language, idex) => (
                                    <LanguageCard image={language} key={idex} setDubFilter={setDubFilter} />
                                ))
                            }
                        </div>
                    </Fragment>:
                    <Typography>Enter a valid Url to continue dubbing</Typography>
                    
                }
                </div>
                <Spin indicator={antIcon} />

            </div>
        </Fragment>
    )
}

export default Homepage