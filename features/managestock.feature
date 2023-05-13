Feature: Manage Stock
  https://app.jubelio.com/login

  Scenario: Arrange and Managing Stock Item Amount
    Given User is Already logged in
    When User Click on "Barang", Select "Katalog" and "In Review" Menu
    And User Enter SKU Code with "HJUEID" in Search
    Then User Will See a Desired Item
    When User Select and Click on the Item
    Then User Will Redirected to "In Review" Page
    And User Will Edit and Enter the desired Value in "Batas Stok Menipis" Field
    And User will Click on "Simpan" and Will be notify with "Data Berhasil Disimpan"