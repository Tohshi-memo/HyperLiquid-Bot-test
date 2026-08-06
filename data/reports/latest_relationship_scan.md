# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-06T22:52:37.310110+00:00`
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

- `market_context_high->unknown_24h` score `41.283` n `109` status `ready` deltaP `3.7571` edge `3.4195` maxDD `-0.0104`
- `market_context_high->commodity_4h` score `1.1593` n `119` status `ready` deltaP `13.1004` edge `0.0939` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.9172` n `109` status `ready` deltaP `3.7004` edge `0.1686` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.5395` n `109` status `ready` deltaP `21.4854` edge `0.0465` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.5063` n `120` status `ready` deltaP `8.0988` edge `0.0298` maxDD `-1.3282`
- `market_context_high->fx_1h` score `-0.0171` n `120` status `ready` deltaP `5.5539` edge `-0.0042` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.3922` n `119` status `ready` deltaP `5.5374` edge `-0.0012` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5529` n `120` status `ready` deltaP `-2.2255` edge `-0.0066` maxDD `-1.6224`
- `market_context_high->crypto_alt_1h` score `-0.791` n `120` status `ready` deltaP `-3.1437` edge `-0.0094` maxDD `-3.0178`
- `market_context_high->index_1h` score `-1.0851` n `120` status `ready` deltaP `-3.2734` edge `-0.0152` maxDD `-1.6054`
- `market_context_high->crypto_alt_4h` score `-1.2208` n `119` status `ready` deltaP `2.0522` edge `-0.0312` maxDD `-5.7857`
- `market_context_high->metal_4h` score `-1.2967` n `119` status `ready` deltaP `1.4418` edge `0.0058` maxDD `-3.211`
- `market_context_high->index_24h` score `-1.3635` n `109` status `ready` deltaP `-4.218` edge `0.0728` maxDD `-7.8922`
- `market_context_high->equity_1h` score `-1.3732` n `120` status `ready` deltaP `3.498` edge `-0.0429` maxDD `-10.5179`
- `market_context_high->index_4h` score `-1.7278` n `119` status `ready` deltaP `-8.4564` edge `-0.0397` maxDD `-4.7021`
- `market_context_high->crypto_major_1h` score `-2.6381` n `120` status `ready` deltaP `-6.7515` edge `-0.0375` maxDD `-7.6533`
- `market_context_high->crypto_alt_24h` score `-2.9779` n `109` status `ready` deltaP `-5.8124` edge `-0.0651` maxDD `-4.5445`
- `market_context_high->equity_4h` score `-6.2062` n `119` status `ready` deltaP `-0.628` edge `-0.2626` maxDD `-34.9766`
- `market_context_high->commodity_24h` score `-6.2651` n `109` status `ready` deltaP `9.8099` edge `0.0079` maxDD `-52.7876`
- `market_context_high->crypto_major_4h` score `-7.2884` n `119` status `ready` deltaP `-6.4308` edge `-0.1433` maxDD `-27.3622`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
