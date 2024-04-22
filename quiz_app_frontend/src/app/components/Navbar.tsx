import Link from 'next/link'
import React from 'react'

export default function Navbar() {
  return (
    <header className='py-8 px-7 flex justify-between bg-purple-300'>
        <h1 className='text-4xl font-bold text-yellow-200'>Quizii Hub</h1>
        <div className='flex gap-6'>
            <Link  className='bg-gradient-to-tr from-red-400 to-yellow-200 text-white py-3 px-7 rounded-lg' href={'/login'}>Sigin</Link>
            <Link className='bg-gradient-to-tr from-red-400 to-yellow-200 text-white py-3 px-7 rounded-lg' href={'/register'}>Sigin UP</Link>
        </div>
    </header>
  )
}
