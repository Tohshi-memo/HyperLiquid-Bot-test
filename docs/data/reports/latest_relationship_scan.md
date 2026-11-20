# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-20T09:52:26.467672+00:00`
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

- `market_context_high->unknown_1h` score `11729.8215` n `110` status `ready` deltaP `1.2058` edge `977.4969` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `7450.5845` n `108` status `ready` deltaP `0.5194` edge `620.907` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `13.4541` n `102` status `ready` deltaP `30.77` edge `1.342` maxDD `-29.4102`
- `market_context_high->crypto_alt_24h` score `7.5764` n `102` status `ready` deltaP `16.8812` edge `1.1228` maxDD `-43.6516`
- `market_context_high->crypto_major_4h` score `1.7439` n `108` status `ready` deltaP `5.3127` edge `0.3918` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `1.5054` n `108` status `ready` deltaP `6.3798` edge `0.2905` maxDD `-12.9396`
- `market_context_high->metal_4h` score `0.5872` n `108` status `ready` deltaP `18.1741` edge `0.0622` maxDD `-6.4211`
- `market_context_high->metal_1h` score `-0.1499` n `110` status `ready` deltaP `4.7795` edge `0.0154` maxDD `-2.6517`
- `market_context_high->crypto_major_1h` score `-0.4051` n `110` status `ready` deltaP `4.0528` edge `0.0607` maxDD `-6.5061`
- `market_context_high->index_1h` score `-0.4774` n `110` status `ready` deltaP `2.6728` edge `0.0036` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-1.1509` n `110` status `ready` deltaP `-2.0114` edge `0.0397` maxDD `-5.4428`
- `market_context_high->equity_1h` score `-1.3689` n `110` status `ready` deltaP `5.8492` edge `0.0248` maxDD `-10.8962`
- `market_context_high->fx_1h` score `-1.4314` n `110` status `ready` deltaP `-9.306` edge `-0.0013` maxDD `-0.4757`
- `market_context_high->index_4h` score `-1.7323` n `108` status `ready` deltaP `-1.1574` edge `-0.0023` maxDD `-4.7471`
- `market_context_high->fx_4h` score `-2.3723` n `108` status `ready` deltaP `-14.7979` edge `-0.0039` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.3861` n `110` status `ready` deltaP `-9.1454` edge `-0.0264` maxDD `-4.2513`
- `market_context_high->metal_24h` score `-4.7687` n `102` status `ready` deltaP `14.5425` edge `0.102` maxDD `-37.7071`
- `market_context_high->fx_24h` score `-6.5455` n `102` status `ready` deltaP `-16.7177` edge `-0.0067` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-7.8921` n `108` status `ready` deltaP `-27.4333` edge `-0.1055` maxDD `-15.5426`
- `market_context_high->equity_4h` score `-8.9723` n `108` status `ready` deltaP `-5.3748` edge `-0.0297` maxDD `-44.2396`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
