import './Navbar.css'
import { PageData } from './PageData'


function Navbar() {

    return (
        <nav className="navbar">
            <h1 className="nav-title">
                <a href='/'>
                    Platform Computing
                </a>
            </h1>
            <ul className='page-item'>
            {PageData.map((item, index) => {
                return (
                    <li key={index}>
                        <a href={item.path} className={item.cName}>
                        {item.title}
                        </a>
                    </li>
                );
            })}
            </ul>
      </nav>
    )
}

export default Navbar