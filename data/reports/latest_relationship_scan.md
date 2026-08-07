# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T00:52:25.861753+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11765`

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

- `market_context_high->unknown_24h` score `23.2566` n `109` status `ready` deltaP `3.7571` edge `1.9173` maxDD `-0.0104`
- `market_context_high->commodity_4h` score `1.1754` n `120` status `ready` deltaP `13.2574` edge `0.0942` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.904` n `109` status `ready` deltaP `3.7004` edge `0.1675` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.5566` n `109` status `ready` deltaP `21.4854` edge `0.0487` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4619` n `120` status `ready` deltaP `7.6497` edge `0.0291` maxDD `-1.3282`
- `market_context_high->fx_1h` score `-0.0031` n `120` status `ready` deltaP `5.8533` edge `-0.0044` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.3894` n `120` status `ready` deltaP `5.5311` edge `-0.0008` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5241` n `120` status `ready` deltaP `-1.7764` edge `-0.0059` maxDD `-1.6224`
- `market_context_high->crypto_alt_1h` score `-0.7918` n `120` status `ready` deltaP `-3.1437` edge `-0.0095` maxDD `-3.0178`
- `market_context_high->index_1h` score `-1.0288` n `120` status `ready` deltaP `-2.6746` edge `-0.0145` maxDD `-1.6054`
- `market_context_high->index_24h` score `-1.2457` n `109` status `ready` deltaP `-2.8825` edge `0.079` maxDD `-7.8922`
- `market_context_high->metal_4h` score `-1.2844` n `120` status `ready` deltaP `1.5061` edge `0.0064` maxDD `-3.211`
- `market_context_high->equity_1h` score `-1.3529` n `120` status `ready` deltaP `3.498` edge `-0.0403` maxDD `-10.5179`
- `market_context_high->index_4h` score `-1.6683` n `120` status `ready` deltaP `-7.581` edge `-0.0379` maxDD `-4.7021`
- `market_context_high->crypto_alt_4h` score `-1.863` n `120` status `ready` deltaP `2.1952` edge `-0.0309` maxDD `-5.7857`
- `market_context_high->crypto_major_1h` score `-2.6129` n `120` status `ready` deltaP `-6.6018` edge `-0.0364` maxDD `-7.6533`
- `market_context_high->crypto_alt_24h` score `-3.1036` n `109` status `ready` deltaP `-6.8141` edge `-0.0689` maxDD `-4.5445`
- `market_context_high->equity_4h` score `-6.0374` n `120` status `ready` deltaP `0.1429` edge `-0.2461` maxDD `-34.9766`
- `market_context_high->commodity_24h` score `-6.3204` n `109` status `ready` deltaP `9.8099` edge `0.0008` maxDD `-52.7876`
- `market_context_high->crypto_major_4h` score `-7.2573` n `120` status `ready` deltaP `-6.2822` edge `-0.1417` maxDD `-27.3622`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
