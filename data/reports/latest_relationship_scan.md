# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T17:22:34.360705+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11696`

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

- `market_context_high->equity_24h` score `1.6444` n `136` status `ready` deltaP `4.9827` edge `0.4172` maxDD `-21.0709`
- `market_context_high->commodity_4h` score `0.774` n `171` status `ready` deltaP `11.2591` edge `0.0609` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.7176` n `179` status `ready` deltaP `9.6745` edge `0.0296` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.7011` n `136` status `ready` deltaP `18.7634` edge `0.0141` maxDD `-1.4613`
- `market_context_high->fx_4h` score `-0.1007` n `171` status `ready` deltaP `6.628` edge `0.0074` maxDD `-0.4647`
- `market_context_high->fx_1h` score `-0.1388` n `179` status `ready` deltaP `4.0294` edge `0.0005` maxDD `-0.613`
- `market_context_high->index_24h` score `-0.1942` n `136` status `ready` deltaP `4.5991` edge `0.1063` maxDD `-5.9181`
- `market_context_high->index_1h` score `-0.5858` n `179` status `ready` deltaP `-3.5836` edge `-0.0035` maxDD `-0.8168`
- `market_context_high->metal_24h` score `-0.74` n `136` status `ready` deltaP `1.5585` edge `0.0561` maxDD `-2.9193`
- `market_context_high->metal_1h` score `-0.8173` n `179` status `ready` deltaP `-4.7812` edge `-0.0093` maxDD `-2.0884`
- `market_context_high->equity_1h` score `-0.9868` n `179` status `ready` deltaP `-2.8677` edge `-0.0157` maxDD `-5.0023`
- `market_context_high->index_4h` score `-1.1861` n `171` status `ready` deltaP `-1.3791` edge `-0.0114` maxDD `-1.26`
- `market_context_high->crypto_alt_1h` score `-1.8116` n `179` status `ready` deltaP `-10.2984` edge `-0.0467` maxDD `-6.3518`
- `market_context_high->metal_4h` score `-2.0562` n `171` status `ready` deltaP `-7.3242` edge `-0.0384` maxDD `-6.1111`
- `market_context_high->crypto_major_24h` score `-3.206` n `136` status `ready` deltaP `1.2693` edge `-0.0262` maxDD `-14.2873`
- `market_context_high->equity_4h` score `-3.2228` n `171` status `ready` deltaP `-11.0657` edge `-0.1208` maxDD `-8.4888`
- `market_context_high->crypto_alt_24h` score `-3.7804` n `136` status `ready` deltaP `-10.1744` edge `-0.1029` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-3.8416` n `171` status `ready` deltaP `-11.498` edge `-0.1401` maxDD `-15.3937`
- `market_context_high->crypto_major_1h` score `-3.9506` n `179` status `ready` deltaP `-11.0544` edge `-0.0651` maxDD `-11.9002`
- `market_context_high->commodity_24h` score `-8.8073` n `136` status `ready` deltaP `-5.5485` edge `-0.2206` maxDD `-52.3908`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
