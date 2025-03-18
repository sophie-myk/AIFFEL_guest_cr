import 'package:flutter/material.dart';

class ImageDetailScreen extends StatelessWidget {
  final String imagePath;
  final String imageName;

  const ImageDetailScreen({
    super.key,
    required this.imagePath,
    required this.imageName,
  });

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(imageName)),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Image.asset(imagePath, width: 250, height: 250, fit: BoxFit.contain),
            const SizedBox(height: 20),
            Text(
              imageName,
              style: const TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
            ),
          ],
        ),
      ),
    );
  }
}
