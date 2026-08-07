# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T12:52:38.342223+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11740`

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

- `market_context_high->commodity_4h` score `1.1995` n `119` status `ready` deltaP `13.4825` edge `0.0947` maxDD `-2.7703`
- `market_context_high->commodity_1h` score `0.5715` n `121` status `ready` deltaP `8.8991` edge `0.0299` maxDD `-1.3282`
- `market_context_high->fx_24h` score `0.4886` n `112` status `ready` deltaP `20.0304` edge `0.0488` maxDD `-4.2424`
- `market_context_high->metal_24h` score `0.2839` n `112` status `ready` deltaP `0.1356` edge `0.1324` maxDD `-2.4386`
- `market_context_high->fx_1h` score `0.0913` n `121` status `ready` deltaP `7.1745` edge `-0.0035` maxDD `-0.9376`
- `market_context_high->fx_4h` score `-0.1314` n `119` status `ready` deltaP `9.5781` edge `0.0053` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5482` n `121` status `ready` deltaP `-2.1972` edge `-0.0071` maxDD `-1.5489`
- `market_context_high->index_1h` score `-0.587` n `121` status `ready` deltaP `-1.8978` edge `-0.0092` maxDD `-1.6054`
- `market_context_high->crypto_alt_1h` score `-0.8069` n `121` status `ready` deltaP `-3.1796` edge `-0.0112` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.1067` n `121` status `ready` deltaP `4.9476` edge `-0.0184` maxDD `-10.5179`
- `market_context_high->crypto_alt_4h` score `-1.4154` n `119` status `ready` deltaP `0.123` edge `-0.0433` maxDD `-5.7857`
- `market_context_high->index_4h` score `-1.5286` n `119` status `ready` deltaP `-6.2205` edge `-0.0295` maxDD `-4.6675`
- `market_context_high->metal_4h` score `-1.8158` n `119` status `ready` deltaP `-3.1448` edge `-0.0135` maxDD `-3.0147`
- `market_context_high->index_24h` score `-1.8175` n `112` status `ready` deltaP `-1.7381` edge `0.0705` maxDD `-7.4964`
- `market_context_high->crypto_major_1h` score `-2.5742` n `121` status `ready` deltaP `-6.0486` edge `-0.04` maxDD `-7.4022`
- `market_context_high->crypto_alt_24h` score `-3.7322` n `112` status `ready` deltaP `-10.1717` edge `-0.0989` maxDD `-4.5445`
- `market_context_high->equity_4h` score `-5.9905` n `119` status `ready` deltaP `0.2049` edge `-0.2405` maxDD `-34.9766`
- `market_context_high->commodity_24h` score `-6.0167` n `112` status `ready` deltaP `11.2106` edge `0.0304` maxDD `-52.7876`
- `market_context_high->crypto_major_4h` score `-7.6899` n `119` status `ready` deltaP `-8.1395` edge `-0.1765` maxDD `-26.4717`
- `market_context_high->unknown_1h` score `-8.1334` n `121` status `ready` deltaP `1.1741` edge `-0.6409` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
