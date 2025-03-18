import 'package:flutter/material.dart';

class StorageDetailScreen extends StatelessWidget {
  final Map<String, dynamic> storage;

  const StorageDetailScreen({super.key, required this.storage});

  @override
  Widget build(BuildContext context) {
    List<Map<String, String>> items = List<Map<String, String>>.from(storage["items"]);

    return Scaffold(
      appBar: AppBar(title: Text(storage["name"])),
      body: items.isEmpty
          ? const Center(
        child: Text(
          "등록된 물건이 없습니다.",
          style: TextStyle(fontSize: 16, color: Colors.grey),
        ),
      )
          : Padding(
        padding: const EdgeInsets.all(12.0),
        child: GridView.builder(
          gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
            crossAxisCount: 3, // 한 줄에 3개씩 표시
            crossAxisSpacing: 10,
            mainAxisSpacing: 10,
          ),
          itemCount: items.length,
          itemBuilder: (context, index) {
            final item = items[index];
            return GestureDetector(
              onTap: () {
                _showItemDialog(context, item["name"]!, storage["name"]!);
              },
              child: Image.asset(item["thumbnail"]!, fit: BoxFit.cover),
            );
          },
        ),
      ),
    );
  }

  // 물건 클릭 시 다이얼로그 표시
  void _showItemDialog(BuildContext context, String itemName, String storageName) {
    showDialog(
      context: context,
      builder: (context) {
        return AlertDialog(
          title: const Text("물건 정보"),
          content: Text("$itemName이(가) $storageName에 보관 중"),
          actions: [
            TextButton(
              onPressed: () {
                Navigator.pop(context);
              },
              child: const Text("확인"),
            ),
          ],
        );
      },
    );
  }
}
