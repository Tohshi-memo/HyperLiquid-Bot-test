# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-20T06:37:25.863822+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2754`

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

- `market_context_high->unknown_1h` score `11992.508` n `108` status `ready` deltaP `0.987` edge `999.3889` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `7440.4329` n `108` status `ready` deltaP `-0.0903` edge `620.0651` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `13.3797` n `102` status `ready` deltaP `30.77` edge `1.3358` maxDD `-29.4102`
- `market_context_high->crypto_alt_24h` score `7.2476` n `102` status `ready` deltaP `16.8812` edge `1.0954` maxDD `-43.6516`
- `market_context_high->crypto_major_4h` score `1.521` n `108` status `ready` deltaP `4.5505` edge `0.3783` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `1.4513` n `108` status `ready` deltaP `6.2274` edge `0.287` maxDD `-12.9396`
- `market_context_high->metal_4h` score `0.7821` n `108` status `ready` deltaP `19.5461` edge `0.0693` maxDD `-6.4211`
- `market_context_high->metal_1h` score `-0.0943` n `108` status `ready` deltaP `5.8383` edge `0.0197` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.2561` n `108` status `ready` deltaP `3.4154` edge `0.0056` maxDD `-1.2295`
- `market_context_high->crypto_major_1h` score `-0.3475` n `108` status `ready` deltaP `4.5465` edge `0.0648` maxDD `-6.5061`
- `market_context_high->crypto_alt_1h` score `-0.7473` n `108` status `ready` deltaP `-1.7853` edge `0.0383` maxDD `-5.4428`
- `market_context_high->equity_1h` score `-1.1482` n `108` status `ready` deltaP `6.3429` edge `0.0399` maxDD `-10.8962`
- `market_context_high->fx_1h` score `-1.6085` n `108` status `ready` deltaP `-11.3994` edge `-0.0021` maxDD `-0.4757`
- `market_context_high->index_4h` score `-1.815` n `108` status `ready` deltaP `-2.072` edge `-0.0031` maxDD `-4.7471`
- `market_context_high->fx_4h` score `-2.3739` n `108` status `ready` deltaP `-14.7979` edge `-0.0041` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.3936` n `108` status `ready` deltaP `-9.5199` edge `-0.0278` maxDD `-3.9892`
- `market_context_high->metal_24h` score `-5.0519` n `102` status `ready` deltaP `14.5425` edge `0.0784` maxDD `-37.7071`
- `market_context_high->fx_24h` score `-6.5112` n `102` status `ready` deltaP `-16.5441` edge `-0.005` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-8.0506` n `108` status `ready` deltaP `-28.5004` edge `-0.1116` maxDD `-15.5426`
- `market_context_high->equity_4h` score `-9.2789` n `108` status `ready` deltaP `-6.7468` edge `-0.0461` maxDD `-44.2396`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
