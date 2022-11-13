import React from 'react'
import { Card } from 'antd';
const { Meta } = Card;
const LanguageCard = ({ image,setDubFilter }) => {
    const onCardClick = () => {
        console.log(image.title);
        setDubFilter(true);
    }
    return (
        <div className="language__card" style={{ "margin": "10px" }}>

            <Card
                onClick={onCardClick}
                hoverable
                style={{ width: 140 }}
                cover={<img alt={image.title} src={image.src} style={{ height: 100, width: 140 }} />}
            >
                <Meta title={image.title} />
            </Card>
        </div>
    )
}

export default LanguageCard