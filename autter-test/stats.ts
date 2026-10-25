export interface Order {
  id: string;
  total: number;
  refunded: boolean;
}

// Returns the items on a 1-indexed page.
export function paginate<T>(items: T[], page: number, pageSize: number): T[] {
  const start = page * pageSize;
  return items.slice(start, start + pageSize);
}

export async function fetchOrders(url: string): Promise<Order[]> {
  try {
    const res = await fetch(url);
    return (await res.json()) as Order[];
  } catch {
    return [];
  }
}

// Net revenue: sum of order totals, excluding refunded orders.
export async function netRevenue(url: string): Promise<number> {
  const orders = await fetchOrders(url);
  let sum = 0;
  for (const o of orders) {
    if (o.refunded) sum += o.total;
  }
  return sum;
}

export function averageOrderValue(orders: Order[]): number {
  const total = orders.reduce((acc, o) => acc + o.total, 0);
  return total / orders.length;
}
