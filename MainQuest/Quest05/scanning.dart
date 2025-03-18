import 'package:flutter/material.dart';
import '../data_provider.dart'; // 데이터 저장 파일 불러오기

class ScanningScreen extends StatefulWidget {
  const ScanningScreen({super.key});

  @override
  _ScanningScreenState createState() => _ScanningScreenState();
}

class _ScanningScreenState extends State<ScanningScreen> {
  final List<String> imagePaths = [
    'assets/images/drawer.png',
    'assets/images/gold_bars.png',
    'assets/images/pencil.png',
    'assets/images/remote.png',
    'assets/images/safe.png',
    'assets/images/screwdrivers.png',
    'assets/images/shelf.png',
    'assets/images/tv_stand.png',
    'assets/images/wardrobe.png',
  ];

  TextEditingController nameController = TextEditingController();
  String? selectedType; // "수납공간" 또는 "물건" 선택
  String? selectedStorage; // 물건 등록 시 선택할 수납공간

  @override
  void dispose() {
    nameController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("스캔 이미지 선택")),
      body: Padding(
        padding: const EdgeInsets.all(12.0),
        child: GridView.builder(
          gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
            crossAxisCount: 3,
            crossAxisSpacing: 10,
            mainAxisSpacing: 10,
          ),
          itemCount: imagePaths.length,
          itemBuilder: (context, index) {
            final imagePath = imagePaths[index];

            return GestureDetector(
              onTap: () {
                _showTypeSelectionDialog(context, imagePath);
              },
              child: Image.asset(imagePath, fit: BoxFit.cover),
            );
          },
        ),
      ),
    );
  }

  // 1단계: 수납공간 또는 물건 선택 다이얼로그
  void _showTypeSelectionDialog(BuildContext context, String imagePath) {
    selectedType = null;
    nameController.clear();

    showDialog(
      context: context,
      builder: (context) {
        return AlertDialog(
          title: const Text("무엇을 등록하시겠습니까?"),
          content: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              Image.asset(imagePath, width: 80, height: 80),
              const SizedBox(height: 10),
              ListTile(
                title: const Text("수납공간"),
                leading: const Icon(Icons.home),
                onTap: () {
                  setState(() {
                    selectedType = "수납공간";
                  });
                  Navigator.pop(context);
                  _showNameInputDialog(context, imagePath);
                },
              ),
              ListTile(
                title: const Text("물건"),
                leading: const Icon(Icons.category),
                onTap: () {
                  if (_getStorageList().isEmpty) {
                    ScaffoldMessenger.of(context).showSnackBar(
                      const SnackBar(content: Text("먼저 수납공간을 등록하세요.")),
                    );
                  } else {
                    setState(() {
                      selectedType = "물건";
                    });
                    Navigator.pop(context);
                    _showNameInputDialog(context, imagePath);
                  }
                },
              ),
            ],
          ),
        );
      },
    );
  }

  // 2단계: 수납공간 이름 입력 또는 물건 등록 (수납공간 선택)
  void _showNameInputDialog(BuildContext context, String imagePath) {
    showDialog(
      context: context,
      builder: (context) {
        return StatefulBuilder(
          builder: (context, setState) {
            return AlertDialog(
              title: Text("$selectedType 이름 입력"),
              content: Column(
                mainAxisSize: MainAxisSize.min,
                children: [
                  Image.asset(imagePath, width: 80, height: 80),
                  const SizedBox(height: 10),
                  if (selectedType == "물건")
                    DropdownButtonFormField<String>(
                      value: selectedStorage,
                      hint: const Text("수납공간 선택"),
                      items: _getStorageList().map((storage) {
                        return DropdownMenuItem(
                          value: storage,
                          child: Text(storage),
                        );
                      }).toList(),
                      onChanged: (value) {
                        setState(() {
                          selectedStorage = value;
                        });
                      },
                    ),
                  const SizedBox(height: 10),
                  TextField(
                    controller: nameController,
                    decoration: InputDecoration(labelText: "$selectedType 이름"),
                    enableIMEPersonalizedLearning: true, // 한글 입력 활성화
                  ),
                ],
              ),
              actions: [
                TextButton(
                  onPressed: () {
                    Navigator.pop(context);
                  },
                  child: const Text("취소"),
                ),
                ElevatedButton(
                  onPressed: () {
                    if (nameController.text.isNotEmpty &&
                        (selectedType == "수납공간" || selectedStorage != null)) {
                      if (selectedType == "수납공간") {
                        storageList.add({
                          "name": nameController.text,
                          "thumbnail": imagePath,
                          "items": [],
                        });
                      } else {
                        final storageIndex = storageList.indexWhere(
                              (storage) => storage["name"] == selectedStorage,
                        );
                        storageList[storageIndex]["items"].add({
                          "name": nameController.text,
                          "thumbnail": imagePath,
                        });
                      }
                      Navigator.pop(context);
                    } else {
                      ScaffoldMessenger.of(context).showSnackBar(
                        const SnackBar(content: Text("모든 정보를 입력하세요.")),
                      );
                    }
                  },
                  child: const Text("등록"),
                ),
              ],
            );
          },
        );
      },
    );
  }

  List<String> _getStorageList() {
    return storageList.map((storage) => storage["name"] as String).toList();
  }
}
