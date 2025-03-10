import 'package:flutter/material.dart';
import 'firstpage.dart'; // ✅ 첫 번째 페이지 import

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: FirstPage(), // ✅ 첫 화면을 FirstPage로 설정
    );
  }
}
