import '../abstracts/animal-abstract.dart';

class Cat extends Animal {
  @override
  void printName() {
    print('Cat name :besa');
  }

  @override
  void printSound() {
    print('mew');
  }
}
