import 'package:flutter/material.dart';

class ScanningDetailScreen extends StatelessWidget {
  final String imagePath;

  const ScanningDetailScreen({super.key, required this.imagePath});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("상세 정보 등록")),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Image.asset(imagePath, width: 150, height: 150),
            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: () {
                _showRegistrationDialog(context);
              },
              child: const Text("등록하기"),
            ),
          ],
        ),
      ),
    );
  }

  // 등록 다이얼로그
  void _showRegistrationDialog(BuildContext context) {
    TextEditingController storageController = TextEditingController();
    TextEditingController itemController = TextEditingController();

    showDialog(
      context: context,
      builder: (context) {
        return AlertDialog(
          title: const Text("등록하시겠습니까?"),
          content: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              TextField(
                controller: storageController,
                decoration: const InputDecoration(labelText: "수납공간"),
              ),
              TextField(
                controller: itemController,
                decoration: const InputDecoration(labelText: "물건명"),
              ),
            ],
          ),
          actions: [
            TextButton(
              onPressed: () {
                Navigator.pop(context); // 다이얼로그 닫기
              },
              child: const Text("취소"),
            ),
            ElevatedButton(
              onPressed: () {
                // 입력값 저장 (콘솔 출력)
                print("수납공간: ${storageController.text}, 물건명: ${itemController.text}");
                Navigator.pop(context); // 다이얼로그 닫기
              },
              child: const Text("등록"),
            ),
          ],
        );
      },
    );
  }
}
