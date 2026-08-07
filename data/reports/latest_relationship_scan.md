# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T01:37:31.602229+00:00`
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

- `market_context_high->unknown_24h` score `16.4778` n `109` status `ready` deltaP `3.7571` edge `1.3524` maxDD `-0.0104`
- `market_context_high->commodity_4h` score `1.1997` n `120` status `ready` deltaP `13.4857` edge `0.0947` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.9004` n `109` status `ready` deltaP `3.7004` edge `0.1672` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.5644` n `109` status `ready` deltaP `21.4854` edge `0.0497` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.5063` n `120` status `ready` deltaP `8.0988` edge `0.0298` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0226` n `120` status `ready` deltaP `6.3024` edge `-0.0041` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.375` n `120` status `ready` deltaP `5.7622` edge `-0.0005` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5249` n `120` status `ready` deltaP `-1.7764` edge `-0.006` maxDD `-1.6224`
- `market_context_high->crypto_alt_1h` score `-0.791` n `120` status `ready` deltaP `-3.1437` edge `-0.0094` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.9832` n `120` status `ready` deltaP `-2.2255` edge `-0.0137` maxDD `-1.6054`
- `market_context_high->index_24h` score `-1.2072` n `109` status `ready` deltaP `-2.3817` edge `0.0806` maxDD `-7.8922`
- `market_context_high->metal_4h` score `-1.2939` n `120` status `ready` deltaP `1.4024` edge `0.0063` maxDD `-3.211`
- `market_context_high->equity_1h` score `-1.3007` n `120` status `ready` deltaP `3.9471` edge `-0.0366` maxDD `-10.5179`
- `market_context_high->index_4h` score `-1.6541` n `120` status `ready` deltaP `-7.3679` edge `-0.0375` maxDD `-4.7021`
- `market_context_high->crypto_alt_4h` score `-1.8356` n `120` status `ready` deltaP `2.4187` edge `-0.0301` maxDD `-5.7857`
- `market_context_high->crypto_major_1h` score `-2.6309` n `120` status `ready` deltaP `-6.7515` edge `-0.0369` maxDD `-7.6533`
- `market_context_high->crypto_alt_24h` score `-3.1941` n `109` status `ready` deltaP `-7.3149` edge `-0.0731` maxDD `-4.5445`
- `market_context_high->equity_4h` score `-5.991` n `120` status `ready` deltaP `0.3455` edge `-0.2415` maxDD `-34.9766`
- `market_context_high->commodity_24h` score `-6.3282` n `109` status `ready` deltaP `9.8099` edge `-0.0002` maxDD `-52.7876`
- `market_context_high->crypto_major_4h` score `-7.2245` n `120` status `ready` deltaP `-6.0366` edge `-0.1406` maxDD `-27.3622`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
