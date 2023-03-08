export interface Product {
  id: number;
  name: string;
  price: number;
  description: string;

  imge: string;
}

export const products = [
  {
    id: 1,
    name: 'Phone XL',
    price: 799,
    imge: "https://www.celladorales.com/wp-content/uploads/2016/12/ShippingBox_sq.jpg",
    description: 'A large phone with one of the best screens'
  },
  {
    id: 2,
    name: 'Phone Mini',
    price: 699,
    imge: "https://www.celladorales.com/wp-content/uploads/2016/12/ShippingBox_sq.jpg",
    description: 'A great phone with one of the best cameras'
  },
  {
    id: 3,
    name: 'Phone Standard',
    price: 299,
    imge: "https://www.celladorales.com/wp-content/uploads/2016/12/ShippingBox_sq.jpg",
    description: ''
  }
];
