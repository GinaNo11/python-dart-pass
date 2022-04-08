import '../abstracts/animal-abstract.dart';

class Dog extends Animal {
  @override
  void printName() {
    print('Dog name :boby');
  }

  @override
  void printSound() {
    print('aooo');
  }
}
