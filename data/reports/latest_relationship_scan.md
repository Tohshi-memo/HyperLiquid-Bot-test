# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-20T10:52:28.259978+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2612`

## Conditions

- `news_risk_high`: News Risk is elevated.
- `macro_risk_high`: Macro Risk is elevated.
- `risk_on_high`: Risk-On score is elevated.
- `market_context_high`: Market Context is supportive.
- `polymarket_volume_spike`: Polymarket 24h volume z-score is elevated.
- `flow_alert_high`: Flow Alert score is elevated.
- `news_and_polymarket`: News Risk and Polymarket volume spike happen together.
- `risk_on_and_context`: Risk-On and Market Context are both supportive.
- `macro_and_flow`: Macro Risk and Flow Alert are elevated together.

## Top Patterns

- `market_context_high->unknown_1h` score `11387.4975` n `113` status `ready` deltaP `1.5196` edge `948.9678` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `7455.7721` n `108` status `ready` deltaP `0.5194` edge `621.3393` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `13.4373` n `102` status `ready` deltaP `30.77` edge `1.3406` maxDD `-29.4102`
- `market_context_high->crypto_alt_24h` score `7.6244` n `102` status `ready` deltaP `16.8812` edge `1.1268` maxDD `-43.6516`
- `market_context_high->crypto_major_4h` score `1.8753` n `108` status `ready` deltaP `5.7701` edge `0.3997` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `1.6068` n `108` status `ready` deltaP `6.8371` edge `0.2959` maxDD `-12.9396`
- `market_context_high->metal_4h` score `0.5752` n `108` status `ready` deltaP `18.1741` edge `0.0612` maxDD `-6.4211`
- `market_context_high->metal_1h` score `-0.103` n `113` status `ready` deltaP `5.2461` edge `0.0183` maxDD `-2.6517`
- `market_context_high->crypto_major_1h` score `-0.3194` n `113` status `ready` deltaP `4.6208` edge `0.0679` maxDD `-6.5061`
- `market_context_high->index_1h` score `-0.4058` n `113` status `ready` deltaP `3.463` edge `0.0043` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-1.1171` n `113` status `ready` deltaP `-1.5739` edge `0.0396` maxDD `-5.4428`
- `market_context_high->equity_1h` score `-1.1903` n `113` status `ready` deltaP `6.5669` edge `0.0349` maxDD `-10.8962`
- `market_context_high->fx_1h` score `-1.4635` n `113` status `ready` deltaP `-9.6617` edge `-0.0016` maxDD `-0.4757`
- `market_context_high->index_4h` score `-1.7043` n `108` status `ready` deltaP `-0.8525` edge `-0.002` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.3578` n `113` status `ready` deltaP `-8.6403` edge `-0.0257` maxDD `-4.3877`
- `market_context_high->fx_4h` score `-2.3621` n `108` status `ready` deltaP `-14.6454` edge `-0.0036` maxDD `-1.794`
- `market_context_high->metal_24h` score `-4.6883` n `102` status `ready` deltaP `14.5425` edge `0.1087` maxDD `-37.7071`
- `market_context_high->fx_24h` score `-6.5491` n `102` status `ready` deltaP `-16.7177` edge `-0.007` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-7.8499` n `108` status `ready` deltaP `-27.2809` edge `-0.103` maxDD `-15.5426`
- `market_context_high->equity_4h` score `-8.8611` n `108` status `ready` deltaP `-4.7651` edge `-0.0245` maxDD `-44.2396`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
