# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T22:52:17.139989+00:00`
- Price records: `672`
- Market context records: `1263`
- Flow alert records: `5545`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8809`

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

- `market_context_high->crypto_major_24h` score `17.9605` n `128` status `ready` deltaP `41.5798` edge `1.3327` maxDD `-8.0553`
- `market_context_high->metal_24h` score `9.3945` n `128` status `ready` deltaP `4.5139` edge `0.9195` maxDD `-6.3373`
- `market_context_high->unknown_4h` score `8.1828` n `128` status `ready` deltaP `5.6784` edge `0.7657` maxDD `-6.7322`
- `market_context_high->crypto_alt_24h` score `8.1661` n `128` status `ready` deltaP `23.8715` edge `0.723` maxDD `-15.1306`
- `market_context_high->index_24h` score `4.6501` n `128` status `ready` deltaP `25.5208` edge `0.326` maxDD `-5.3574`
- `market_context_high->equity_4h` score `3.6458` n `128` status `ready` deltaP `18.9214` edge `0.244` maxDD `-3.6396`
- `market_context_high->equity_24h` score `3.5507` n `128` status `ready` deltaP `23.6111` edge `0.5305` maxDD `-14.2815`
- `market_context_high->commodity_24h` score `2.5041` n `128` status `ready` deltaP `-10.7639` edge `0.4286` maxDD `-6.8535`
- `market_context_high->unknown_24h` score `2.2842` n `128` status `ready` deltaP `1.5625` edge `0.4529` maxDD `-10.1706`
- `market_context_high->index_4h` score `1.7678` n `128` status `ready` deltaP `14.958` edge `0.1159` maxDD `-2.1308`
- `market_context_high->metal_4h` score `0.7304` n `128` status `ready` deltaP `17.7401` edge `0.0857` maxDD `-6.4478`
- `market_context_high->index_1h` score `0.7099` n `134` status `ready` deltaP `10.1171` edge `0.0234` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.6894` n `134` status `ready` deltaP `6.5287` edge `0.0508` maxDD `-1.2834`
- `market_context_high->metal_1h` score `0.3837` n `134` status `ready` deltaP `11.7772` edge `0.0145` maxDD `-2.2164`
- `market_context_high->crypto_major_4h` score `0.2593` n `128` status `ready` deltaP `8.2889` edge `0.1701` maxDD `-8.3693`
- `market_context_high->fx_24h` score `0.1258` n `128` status `ready` deltaP `3.9063` edge `0.0309` maxDD `-0.3831`
- `market_context_high->fx_1h` score `-0.2813` n `134` status `ready` deltaP `3.5749` edge `-0.0017` maxDD `-0.3124`
- `market_context_high->crypto_alt_4h` score `-0.3422` n `128` status `ready` deltaP `9.3178` edge `0.1905` maxDD `-16.7194`
- `market_context_high->crypto_alt_1h` score `-0.3772` n `134` status `ready` deltaP `0.5876` edge `0.032` maxDD `-3.4088`
- `market_context_high->crypto_major_1h` score `-0.6144` n `134` status `ready` deltaP `0.7463` edge `0.0025` maxDD `-4.8999`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
