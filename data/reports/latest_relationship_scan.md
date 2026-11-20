# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-20T05:52:28.775559+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2790`

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

- `market_context_high->unknown_1h` score `11990.5796` n `108` status `ready` deltaP `1.1367` edge `999.2272` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `7452.1797` n `108` status `ready` deltaP `-0.0903` edge `621.044` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `13.3425` n `102` status `ready` deltaP `30.77` edge `1.3327` maxDD `-29.4102`
- `market_context_high->crypto_alt_24h` score `7.0772` n `102` status `ready` deltaP `16.8812` edge `1.0812` maxDD `-43.6516`
- `market_context_high->crypto_major_4h` score `1.4994` n `108` status `ready` deltaP `4.5505` edge `0.3765` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `1.3649` n `108` status `ready` deltaP `6.2274` edge `0.2798` maxDD `-12.9396`
- `market_context_high->metal_4h` score `0.8391` n `108` status `ready` deltaP `20.0034` edge `0.071` maxDD `-6.4211`
- `market_context_high->metal_1h` score `-0.0284` n `108` status `ready` deltaP `6.2874` edge `0.0222` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.2312` n `108` status `ready` deltaP `3.8645` edge `0.0058` maxDD `-1.2295`
- `market_context_high->crypto_major_1h` score `-0.3311` n `108` status `ready` deltaP `4.5465` edge `0.0669` maxDD `-6.5061`
- `market_context_high->crypto_alt_1h` score `-0.7473` n `108` status `ready` deltaP `-1.7853` edge `0.0383` maxDD `-5.4428`
- `market_context_high->equity_1h` score `-1.0799` n `108` status `ready` deltaP `6.792` edge `0.0426` maxDD `-10.8962`
- `market_context_high->fx_1h` score `-1.5965` n `108` status `ready` deltaP `-11.2497` edge `-0.0021` maxDD `-0.4757`
- `market_context_high->index_4h` score `-1.8284` n `108` status `ready` deltaP `-2.2245` edge `-0.0032` maxDD `-4.7471`
- `market_context_high->fx_4h` score `-2.3747` n `108` status `ready` deltaP `-14.7979` edge `-0.0042` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.4091` n `108` status `ready` deltaP `-9.6696` edge `-0.0281` maxDD `-3.9892`
- `market_context_high->metal_24h` score `-5.1107` n `102` status `ready` deltaP `14.5425` edge `0.0735` maxDD `-37.7071`
- `market_context_high->fx_24h` score `-6.4611` n `102` status `ready` deltaP `-16.0233` edge `-0.0043` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-8.0822` n `108` status `ready` deltaP `-28.8053` edge `-0.1122` maxDD `-15.5426`
- `market_context_high->equity_4h` score `-9.2983` n `108` status `ready` deltaP `-6.8992` edge `-0.0467` maxDD `-44.2396`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
