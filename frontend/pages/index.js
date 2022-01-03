import { useState, useEffect } from 'react'
var xmlrpc = require('xmlrpc')
import Swal from 'sweetalert2'

export default function Home() {
  var client = xmlrpc.createClient({
    host: 'localhost',
    port: 8008,
    path: '/RPC2',
    cookies: true
  })

  var initial_data = {
    nik: "",
    nama_pelapor: "",
    nama_terduga: "",
    gejala: "",
    alamat: ""
  }

  const [Forms, setForms] = useState(initial_data)

  useEffect(() => {
    console.log(Forms)
  }, [Forms])
  
  const submitHandler = (e) => {
    e.preventDefault()
    client.methodCall('report', [Forms.nik], (err, val) => {
      if (err) {
        console.log(err)
        return
      }
      if (val.status != 'failed'){
        setForms(initial_data)
        Swal.fire({
          title: 'Permintaan Berhasil Terlaporkan',
          text: val.message,
          icon: 'success',
          confirmButtonText: 'Okay'
        })
      } else {
        Swal.fire({
          title: 'Permintaan Gagal',
          text: val.message,
          icon: 'error',
          confirmButtonText: 'Okay'
        })
      }
    })
  }

  return (
    <div className=" h-full w-full flex flex-row justify-center">
      <div className="py-8 px-5 max-w-[640px] sm:w-[35%]">
        <h1 className="font-bold text-[24px] text-center">
          Form Pelaporan Kasus COVID-19
        </h1>
        <div className="h-[40px]"></div>
        <form className="w-full max-w-lg" onSubmit={submitHandler}>
        <div className="flex flex-wrap -mx-3 mb-6">
          <div className="w-full md:w-1/2 px-3 mb-6 md:mb-0">
            <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2">
              NIK Pelapor
            </label>
            <input onChange={e => { setForms({ ...Forms, nik: e.target.value }) }} value={Forms.nik} className="appearance-none block w-full bg-gray-200 text-gray-700 border rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white" id="" type="number" />
          </div>
          <div className="w-full md:w-1/2 px-3">
            <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2">
              Nama Pelapor
            </label>
            <input onChange={e => { setForms({ ...Forms, nama_pelapor: e.target.value }) }} value={Forms.nama_pelapor}   className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="" type="text" />
          </div>
        </div>
        <div className="flex flex-wrap -mx-3 mb-6">
          <div className="w-full px-3">
            <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2">
              Nama Terduga
            </label>
            <input onChange={e => { setForms({ ...Forms, nama_terduga: e.target.value }) }} value={Forms.nama_terduga} className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="" type="text" />
          </div>
        </div>
        <div className="flex flex-wrap -mx-3 mb-6">
          <div className="w-full px-3">
            <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2">
              Gejala yang Dirasakan
            </label>
            <textarea onChange={e => { setForms({ ...Forms, gejala: e.target.value }) }} value={Forms.gejala} className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="" type="text" />
          </div>
        </div>
        <div className="flex flex-wrap -mx-3 mb-6">
          <div className="w-full px-3">
            <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2">
              Alamat Terduga
            </label>
            <textarea onChange={e => { setForms({ ...Forms, alamat: e.target.value }) }} value={Forms.alamat} className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="" type="text" />
          </div>
        </div>
        <div className="flex flex-wrap -mx-3 mb-6">
          <div className="w-full px-3 text-center">
            <button className=" bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded" type="submit">
              Laporkan
            </button>
          </div>
        </div>
      </form>
      </div>
    </div>    
  )
}
