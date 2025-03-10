import 'package:flutter/material.dart';
import 'secondpage.dart'; // ✅ SecondPage import

class FirstPage extends StatefulWidget {
  @override
  _FirstPageState createState() => _FirstPageState();
}

class _FirstPageState extends State<FirstPage> {
  int _selectedIndex = 0; // 현재 선택된 인덱스

  void _onItemTapped(int index) {
    setState(() {
      _selectedIndex = index; // 선택된 인덱스 업데이트
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.black, // ✅ 배경색 검정

      // ✅ 앱바 추가
      appBar: AppBar(
        backgroundColor: Colors.black, // ✅ 앱바 배경색 검정
        elevation: 0, // ✅ 그림자 제거
        title: Row(
          children: [
            Icon(Icons.play_circle_fill, color: Colors.red, size: 30),
            SizedBox(width: 8),
            Text("Music", style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold, color: Colors.grey)),
          ],
        ),
        actions: [
          IconButton(icon: Icon(Icons.notifications), onPressed: () {}),
          IconButton(icon: Icon(Icons.search), onPressed: () {}),
          CircleAvatar(
            backgroundColor: Colors.green,
            child: Text("B", style: TextStyle(color: Colors.white)),
          ),
          SizedBox(width: 10),
        ],
      ),

      body: Stack(
        children: [
          Center(
            child: Image.asset(
              'assets/images/home.png',
              width: MediaQuery.of(context).size.width,
              height: MediaQuery.of(context).size.height,
              fit: BoxFit.fill,
            ),
          ),

          // ✅ "Presenting Alan Walker" 박스 클릭 가능하게 만들기
          Positioned(
            top: MediaQuery.of(context).size.height * 0.33,
            left: MediaQuery.of(context).size.width * 0.07,
            child: GestureDetector(
              onTap: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (context) => SecondPage()), // ✅ SecondPage로 이동
                );
              },
              child: Container(
                width: MediaQuery.of(context).size.width * 0.42,
                height: MediaQuery.of(context).size.height * 0.17,
                color: Colors.transparent, // ✅ 보이지 않지만 클릭 가능
              ),
            ),
          ),
        ],
      ),
    );
  }
}
