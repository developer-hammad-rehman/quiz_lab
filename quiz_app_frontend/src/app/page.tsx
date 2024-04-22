import React from 'react'
import { BackgroundBoxes } from './components/Hero'
import { AnimatedPin } from './components/cards'

export default function Home() {
  return (
    <div className='overflow-x-hidden bg-gray-900'>
      <BackgroundBoxes/>
      <h4 className='text-center text-5xl font-bold text-white py-7'>Topices</h4>
      <AnimatedPin/>
    </div>
  )
}
