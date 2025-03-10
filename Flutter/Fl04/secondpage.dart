import 'package:flutter/material.dart';
import 'thirdpage.dart'; // ✅ ThirdPage import 추가

class SecondPage extends StatefulWidget {
  @override
  _SecondPageState createState() => _SecondPageState();
}

class _SecondPageState extends State<SecondPage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.black,

      // ✅ 앱바 추가
      appBar: AppBar(
        automaticallyImplyLeading: false, // ✅ 뒤로가기 버튼 제거
        backgroundColor: Colors.black,
        elevation: 0,
        title: Row(
          children: [
            Icon(Icons.play_circle_fill, color: Colors.red, size: 30),
            SizedBox(width: 8),
            Text("Music", style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold, color: Colors.grey)),
          ],
        ),
      ),

      body: Stack(
        alignment: Alignment.center,
        children: [
          Center(
            child: Image.asset(
              'assets/images/secondpage.png',
              width: MediaQuery.of(context).size.width,
              height: MediaQuery.of(context).size.height,
              fit: BoxFit.fill,
            ),
          ),

          // ✅ 플레이 버튼이 있는 영역 감지하여 클릭 가능하게 만들기
          Positioned(
            top: MediaQuery.of(context).size.height * 0.52,
            left: MediaQuery.of(context).size.width * 0.4,
            child: GestureDetector(
              onTap: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (context) => ThirdPage()), // ✅ ThirdPage로 이동
                );
              },
              child: Container(
                width: MediaQuery.of(context).size.width * 0.2,
                height: MediaQuery.of(context).size.height * 0.1,
                color: Colors.transparent,
              ),
            ),
          ),
        ],
      ),
    );
  }
}
