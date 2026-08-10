# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T19:22:28.633189+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11712`

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

- `market_context_high->equity_24h` score `1.2601` n `141` status `ready` deltaP `3.7096` edge `0.4145` maxDD `-21.0709`
- `market_context_high->commodity_4h` score `0.8798` n `176` status `ready` deltaP `12.0566` edge `0.0644` maxDD `-2.7169`
- `market_context_high->fx_24h` score `0.8338` n `141` status `ready` deltaP `19.7021` edge `0.0189` maxDD `-1.4613`
- `market_context_high->commodity_1h` score `0.6712` n `184` status `ready` deltaP `9.2294` edge `0.0287` maxDD `-0.7439`
- `market_context_high->fx_1h` score `-0.1193` n `184` status `ready` deltaP `4.465` edge `0.0001` maxDD `-0.613`
- `market_context_high->fx_4h` score `-0.1869` n `176` status `ready` deltaP `5.6402` edge `0.0068` maxDD `-0.4647`
- `market_context_high->index_24h` score `-0.2904` n `141` status `ready` deltaP `3.4563` edge `0.1059` maxDD `-5.9181`
- `market_context_high->index_1h` score `-0.5957` n `184` status `ready` deltaP `-3.7588` edge `-0.0036` maxDD `-0.8168`
- `market_context_high->metal_24h` score `-0.7474` n `141` status `ready` deltaP `1.883` edge `0.0576` maxDD `-2.9283`
- `market_context_high->index_4h` score `-0.7972` n `176` status `ready` deltaP `-2.0926` edge `-0.01` maxDD `-1.26`
- `market_context_high->metal_1h` score `-0.8189` n `184` status `ready` deltaP `-4.7676` edge `-0.0096` maxDD `-2.0884`
- `market_context_high->equity_1h` score `-1.0048` n `184` status `ready` deltaP `-3.1697` edge `-0.0128` maxDD `-5.2573`
- `market_context_high->crypto_alt_1h` score `-1.8212` n `184` status `ready` deltaP `-10.4465` edge `-0.0441` maxDD `-6.5795`
- `market_context_high->metal_4h` score `-2.0046` n `176` status `ready` deltaP `-6.7212` edge `-0.0358` maxDD `-6.1111`
- `market_context_high->equity_4h` score `-3.2273` n `176` status `ready` deltaP `-11.3775` edge `-0.0984` maxDD `-10.1608`
- `market_context_high->crypto_major_24h` score `-3.3985` n `141` status `ready` deltaP `0.2569` edge `-0.0355` maxDD `-14.2873`
- `market_context_high->crypto_major_1h` score `-3.8261` n `184` status `ready` deltaP `-10.248` edge `-0.0601` maxDD `-11.9002`
- `market_context_high->crypto_alt_24h` score `-4.1434` n `141` status `ready` deltaP `-11.291` edge `-0.1257` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-6.0553` n `176` status `ready` deltaP `-11.7932` edge `-0.1346` maxDD `-16.6446`
- `market_context_high->commodity_24h` score `-8.5707` n `141` status `ready` deltaP `-5.214` edge `-0.1925` maxDD `-52.3908`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
