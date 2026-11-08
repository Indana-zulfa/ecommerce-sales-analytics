# Business Insights & Recommendations

## Brazilian E-Commerce Sales Analytics

### 1. Overview

This document presents the key business insights and recommendations derived from the analysis of the Brazilian E-Commerce Public Dataset by Olist.

The analysis focuses on sales performance, customer behavior, product performance, payment behavior, delivery and customer satisfaction, and seller performance.

The objective is to identify business patterns, evaluate operational performance, and provide data-driven recommendations to support business improvement and decision-making.

---

### 2. Sales Performance

#### Key Findings

- The dataset contains **99,441 orders** and **112,650 order items**.
- The total recorded item sales value is **R$13,591,643.70**, excluding freight.
- The average order value (AOV) is approximately **R$136.68**.
- Health & Beauty generated the highest recorded category sales value at **R$1,258,681.34**.
- Watches & Gifts ranked second with **R$1,205,005.68**, followed by Bed, Bath & Table with **R$1,036,988.68**.

#### Business Insights

Sales performance is concentrated in several major product categories, particularly Health & Beauty, Watches & Gifts, and Bed, Bath & Table.

These categories represent important contributors to the marketplace's recorded item sales value and may provide opportunities for further business growth.

The distribution of sales across product categories also indicates that customer purchasing activity varies depending on product type. Understanding these differences can help the business make more informed decisions regarding product assortment, pricing, and promotional strategies.

#### Recommendations

- Prioritize high-performing categories when planning promotional campaigns.
- Evaluate product assortment and pricing strategies in categories with strong sales contributions.
- Investigate lower-performing categories to identify opportunities for product improvement and targeted marketing.
- Monitor monthly sales trends to support inventory and promotional planning.

_Data Interpretation Note: The recorded item sales value includes items across all order statuses and excludes freight. It should not be interpreted as net revenue or realized revenue._

---

### 3. Customer Behavior

#### Key Findings

- The dataset contains approximately **96,096 unique customers**.
- Approximately **93,099 customers** made only one recorded purchase.
- Approximately **2,997 customers** made more than one recorded purchase.
- The repeat purchase rate is approximately **3.12%**.

#### Business Insights

The majority of customers in the dataset made only one recorded purchase.

This indicates a potential opportunity to improve customer retention and encourage repeat purchases.

The relatively small proportion of repeat customers suggests that customer engagement and post-purchase strategies could be further improved to encourage customers to return.

However, the repeat purchase rate is calculated across the available dataset and all recorded order statuses. It does not represent a complete customer retention or cohort analysis.

#### Recommendations

- Introduce customer loyalty programs and repeat-purchase incentives.
- Develop personalized promotions based on previous purchasing behavior.
- Implement post-purchase engagement campaigns to encourage customers to return.
- Analyze customer purchasing frequency and behavior to identify valuable customer segments.

---

### 4. Product Performance

#### Key Findings

- Bed, Bath & Table recorded the highest number of items sold, with approximately **11,115 items**.
- Health & Beauty recorded approximately **9,670 items sold**.
- Sports & Leisure recorded approximately **8,641 items sold**.
- Computers had the highest average item price among the analyzed categories, at approximately **R$1,098.34**.

#### Business Insights

Product categories demonstrate different sales characteristics.

Some categories generate high sales volume, while others have higher average item prices. This suggests that product performance should be evaluated using multiple indicators rather than sales value alone.

Categories with high sales volume may require greater inventory attention, while categories with higher average item prices may provide opportunities for targeted marketing and pricing strategies.

#### Recommendations

- Maintain sufficient inventory for categories with high sales volume.
- Develop cross-selling and product bundling strategies for complementary products.
- Evaluate pricing and promotional strategies for high-value product categories.
- Review products with no recorded sales to determine whether they require improved visibility, pricing adjustments, or assortment changes.

---

### 5. Payment Behavior

#### Key Findings

- Credit card was the most frequently recorded payment method, with **76,795 payment records**.
- Boleto recorded **19,784 payment records**.
- Voucher recorded **5,775 payment records**.
- Debit card recorded **1,529 payment records**.
- Credit card represented the highest recorded payment value, totaling **R$12,542,084.19**.

#### Business Insights

Credit card payments dominate the recorded payment activity in the dataset, both in transaction count and payment value.

This suggests that credit card functionality is an important component of the marketplace payment experience.

Other payment methods also contribute to the overall payment mix and should remain accessible to customers with different payment preferences.

Understanding payment preferences can help the business maintain a convenient checkout experience and identify opportunities to improve payment services.

#### Recommendations

- Maintain a reliable and convenient credit card payment experience.
- Monitor payment success rates and potential payment failures.
- Evaluate alternative payment methods to support different customer preferences.
- Analyze installment usage to understand customer payment behavior and purchasing preferences.

_Data Interpretation Note: Payment transaction counts refer to individual payment records, not necessarily unique orders. Some orders may contain multiple payment records._

---

### 6. Delivery & Customer Satisfaction

#### Key Findings

- The dataset contains **96,478 delivered orders**.
- Average actual delivery time was **12.56 days**.
- Average estimated delivery time was **23.74 days**.
- A total of **88,649 orders** were delivered on time, representing approximately **91.89%** of orders with classified delivery performance.
- A total of **7,827 orders** were delivered late, representing approximately **8.11%** of classified orders.
- The average delivery delay among late orders was **9.55 days**.
- The overall average customer review score was **4.09 out of 5**, based on **99,224 review records**.
- The average review score for on-time deliveries was **4.29**, based on **88,658 review records**.
- The average review score for late deliveries was **2.57**, based on **7,701 review records**.
- Delivery performance varied across customer regions. Roraima (RR) recorded the longest average delivery time at **29.39 days**, while São Paulo (SP) recorded the shortest at **8.76 days**.

#### Business Insights

The delivery analysis indicates that most classified orders were delivered on time. Approximately 91.89% of orders with available delivery performance classifications met their estimated delivery dates, while 8.11% experienced delays.

The average actual delivery time was 12.56 days, compared with an estimated delivery time of 23.74 days. This represents an average difference of 11.18 days, indicating that deliveries were completed earlier than the estimated delivery dates on average.

However, delivery delays were associated with noticeably lower customer satisfaction. Orders delivered on time received an average review score of 4.29, whereas late deliveries received an average score of 2.57. This difference suggests a strong relationship between delivery performance and customer experience.

Regional analysis also reveals considerable differences in delivery duration. São Paulo had the shortest average delivery time, while Roraima had the longest. This suggests that geographical location may be an important factor when evaluating logistics performance.

Overall, delivery reliability appears to be an important aspect of customer satisfaction. Improving delivery performance, particularly in regions with longer delivery times, may help enhance the overall customer experience.

#### Recommendations

- Monitor delivery performance against estimated delivery dates to identify and reduce late shipments.
- Investigate operational factors contributing to delivery delays, particularly in regions with longer average delivery times.
- Evaluate logistics performance across customer regions to identify opportunities for improving delivery efficiency.
- Prioritize improvements in regions with longer delivery durations and lower customer satisfaction.
- Use customer reviews to identify recurring delivery-related issues and improve service quality.
- Strengthen coordination between sellers and logistics providers to improve delivery reliability.

_Data Interpretation Note: Delivery performance percentages are calculated using 96,476 orders classified as either on-time or late. This is slightly lower than the total of 96,478 delivered orders, indicating that two delivered orders did not have a usable delivery performance classification. Review scores by delivery performance are based only on available review records. The findings indicate an association between delivery performance and customer satisfaction, not proof of causation._

---

### 7. Seller Performance

#### Key Findings

- The dataset contains **3,095 registered sellers**.
- São Paulo (SP) has the largest seller presence, with **1,849 sellers**, representing approximately **59.76%** of all registered sellers.
- São Paulo recorded **70,188 orders** and **80,342 items sold**.
- São Paulo generated the highest recorded item sales value of **R$8,753,396.21**, accounting for approximately **64.40%** of the overall recorded item sales value.
- Paraná (PR) ranked second with **R$1,261,887.21**, followed by Minas Gerais (MG) with **R$1,011,564.74**.
- The top-performing seller by recorded sales value generated **R$229,472.63** from 1,132 orders and 1,156 items sold.
- Another seller recorded the highest order volume among the top 10 sellers, with 1,806 orders and R$200,472.92 in recorded sales value.
- Acre (AC) recorded one seller, one order, one item sold, and R$267.00 in sales value.

#### Business Insights

Seller performance varies across individual sellers and geographical regions.

São Paulo dominates marketplace activity in terms of seller concentration, order volume, items sold, and recorded sales value. This indicates that the region plays a significant role in the marketplace's overall commercial activity.

The comparison between seller order volume and sales value also demonstrates that a higher number of orders does not necessarily result in the highest sales value. Differences in product prices and the number of items sold per order may influence individual seller performance.

Additionally, the distribution of seller activity across regions highlights differences in marketplace participation and sales contribution.

#### Recommendations

- Maintain strong engagement with high-performing sellers through seller support and performance-based programs.
- Evaluate the business practices of top-performing sellers to identify strategies that may be replicated across the marketplace.
- Explore opportunities to expand seller participation in regions with lower marketplace activity.
- Monitor seller performance using multiple indicators, including order volume, items sold, and recorded sales value.
- Consider seller locations and freight costs when evaluating marketplace expansion and logistics strategies.

_Data Interpretation Note: Seller sales value is calculated from recorded item prices, excludes freight, and includes items across all recorded order statuses. It should not be interpreted as seller profit or net revenue._

---

### 8. Overall Business Recommendations

Based on the completed analysis, the following strategic priorities are recommended:

| Business Area | Recommended Priority                                                    |
| ------------- | ----------------------------------------------------------------------- |
| Sales         | Strengthen high-performing product categories and monitor sales trends. |
| Customer      | Improve customer retention and encourage repeat purchases.              |
| Product       | Optimize product assortment, pricing, and inventory.                    |
| Payment       | Maintain reliable payment options and monitor payment behavior.         |
| Delivery      | Improve delivery reliability and monitor late deliveries.               |
| Seller        | Strengthen seller performance monitoring and marketplace participation. |

---

### 9. Conclusion

The analysis provides an overview of the marketplace's sales performance, customer behavior, product activity, payment preferences, delivery operations, and seller performance.

The findings highlight several opportunities for business improvement, particularly in customer retention, product category management, payment experience, delivery performance, and seller engagement.

The analysis also demonstrates the importance of evaluating business performance through multiple indicators, including sales value, order volume, customer purchasing behavior, delivery efficiency, and customer feedback.

By using data-driven insights to guide business decisions, the marketplace can identify operational improvement opportunities, enhance customer experience, and support sustainable business growth.

---

### 10. Analysis Limitations

The following limitations should be considered when interpreting the findings:

- The dataset represents historical marketplace transactions rather than real-time business activity.
- Recorded item sales value is calculated from item prices and excludes freight.
- Sales calculations include items across all recorded order statuses unless explicitly filtered.
- Repeat purchase rate is based on recorded orders and does not represent a full cohort retention analysis.
- Delivery analysis includes delivered orders with valid delivery timestamps and available delivery performance classifications.
- Review score analysis by delivery performance is based on available review records, which may not cover all delivered orders.
- Seller performance is evaluated using recorded order items and does not directly represent seller profitability.
- Business recommendations are based on observed dataset patterns and should be validated with additional operational context before implementation.
