import 'package:flutter/material.dart';
import 'storage_detail.dart';
import '../data_provider.dart';

class ListScreen extends StatefulWidget {
  const ListScreen({super.key});

  @override
  _ListScreenState createState() => _ListScreenState();
}

class _ListScreenState extends State<ListScreen> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("수납공간 목록")),
      body: ListView.builder(
        itemCount: storageList.length,
        itemBuilder: (context, index) {
          final storage = storageList[index];
          return Card(
            child: ListTile(
              leading: Image.asset(storage["thumbnail"], width: 50, height: 50, fit: BoxFit.cover),
              title: Text(storage["name"]),
              onTap: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (context) => StorageDetailScreen(storage: storage)),
                );
              },
            ),
          );
        },
      ),
    );
  }
}
