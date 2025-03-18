import 'package:flutter/material.dart';
import '../data_provider.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  _HomeScreenState createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  TextEditingController searchController = TextEditingController();
  String? selectedItem; // 드롭다운에서 선택한 물건
  String? searchResult; // 검색 결과 메시지

  @override
  void dispose() {
    searchController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    List<Map<String, dynamic>> allItems = _getAllItems();
    List<String> itemNames = allItems.map((item) => item["name"] as String).toList();

    return Scaffold(
      appBar: AppBar(title: const Text("물건 검색")),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            // 물건이 없으면 검색 불가 메시지 표시
            if (itemNames.isEmpty)
              const Center(
                child: Text(
                  "등록된 물건이 없습니다.",
                  style: TextStyle(fontSize: 18, color: Colors.grey),
                ),
              )
            else
              Column(
                children: [
                  // 텍스트 필드로 검색
                  TextField(
                    controller: searchController,
                    decoration: InputDecoration(
                      labelText: "물건 이름 입력",
                      suffixIcon: IconButton(
                        icon: const Icon(Icons.search),
                        onPressed: () {
                          _searchItem(searchController.text);
                        },
                      ),
                    ),
                  ),
                  const SizedBox(height: 20),

                  // 드롭다운으로 물건 선택
                  DropdownButtonFormField<String>(
                    value: selectedItem,
                    hint: const Text("물건 선택"),
                    items: itemNames.map((name) {
                      return DropdownMenuItem(
                        value: name,
                        child: Text(name),
                      );
                    }).toList(),
                    onChanged: (value) {
                      setState(() {
                        selectedItem = value;
                        _searchItem(value!);
                      });
                    },
                  ),
                ],
              ),

            const SizedBox(height: 20),

            // 검색 결과 출력
            if (searchResult != null)
              Text(
                searchResult!,
                style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
              ),
          ],
        ),
      ),
    );
  }

  // 모든 물건 리스트 가져오기
  List<Map<String, String>> _getAllItems() {
    List<Map<String, String>> items = [];
    for (var storage in storageList) {
      for (var item in storage["items"]) {
        items.add({
          "name": item["name"],
          "storage": storage["name"],
        });
      }
    }
    return items;
  }

  // 검색 기능 (텍스트 검색 또는 드롭다운 선택)
  void _searchItem(String itemName) {
    List<Map<String, String>> allItems = _getAllItems();
    var foundItem = allItems.firstWhere(
          (item) => item["name"] == itemName,
      orElse: () => {},
    );

    if (foundItem.isNotEmpty) {
      setState(() {
        searchResult = "${foundItem["name"]}이(가) ${foundItem["storage"]}에 보관 중";
      });
    } else {
      setState(() {
        searchResult = "해당 물건이 없습니다.";
      });
    }
  }
}
