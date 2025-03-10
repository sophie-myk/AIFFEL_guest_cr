import 'package:flutter/material.dart';

class ThirdPage extends StatefulWidget {
  @override
  _ThirdPageState createState() => _ThirdPageState();
}

class _ThirdPageState extends State<ThirdPage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.black,

      appBar: AppBar(
        automaticallyImplyLeading: false,
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

      body: Center(
        child: Image.asset(
          'assets/images/thirdpage.png',
          width: MediaQuery.of(context).size.width,
          height: MediaQuery.of(context).size.height,
          fit: BoxFit.fill,
        ),
      ),
    );
  }
}
