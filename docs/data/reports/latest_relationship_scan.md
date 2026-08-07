# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T01:22:27.095641+00:00`
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

- `market_context_high->unknown_24h` score `18.7374` n `109` status `ready` deltaP `3.7571` edge `1.5407` maxDD `-0.0104`
- `market_context_high->commodity_4h` score `1.1912` n `120` status `ready` deltaP `13.4094` edge `0.0945` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.9028` n `109` status `ready` deltaP `3.7004` edge `0.1674` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.5621` n `109` status `ready` deltaP `21.4854` edge `0.0494` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4895` n `120` status `ready` deltaP `7.9491` edge `0.0294` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0141` n `120` status `ready` deltaP `6.1527` edge `-0.0042` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.3798` n `120` status `ready` deltaP `5.6849` edge `-0.0006` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5155` n `120` status `ready` deltaP `-1.6267` edge `-0.0058` maxDD `-1.6224`
- `market_context_high->crypto_alt_1h` score `-0.7902` n `120` status `ready` deltaP `-3.1437` edge `-0.0093` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.9988` n `120` status `ready` deltaP `-2.3752` edge `-0.014` maxDD `-1.6054`
- `market_context_high->index_24h` score `-1.2197` n `109` status `ready` deltaP `-2.5486` edge `0.0801` maxDD `-7.8922`
- `market_context_high->metal_4h` score `-1.2858` n `120` status `ready` deltaP `1.4878` edge `0.0064` maxDD `-3.211`
- `market_context_high->equity_1h` score `-1.3171` n `120` status `ready` deltaP `3.7974` edge `-0.0377` maxDD `-10.5179`
- `market_context_high->index_4h` score `-1.6594` n `120` status `ready` deltaP `-7.4392` edge `-0.0377` maxDD `-4.7021`
- `market_context_high->crypto_alt_4h` score `-1.8463` n `120` status `ready` deltaP `2.344` edge `-0.0305` maxDD `-5.7857`
- `market_context_high->crypto_major_1h` score `-2.6129` n `120` status `ready` deltaP `-6.6018` edge `-0.0364` maxDD `-7.6533`
- `market_context_high->crypto_alt_24h` score `-3.1579` n `109` status `ready` deltaP `-7.148` edge `-0.0712` maxDD `-4.5445`
- `market_context_high->equity_4h` score `-6.0077` n `120` status `ready` deltaP `0.2777` edge `-0.2432` maxDD `-34.9766`
- `market_context_high->commodity_24h` score `-6.3267` n `109` status `ready` deltaP `9.8099` edge `0.0` maxDD `-52.7876`
- `market_context_high->crypto_major_4h` score `-7.237` n `120` status `ready` deltaP `-6.1187` edge `-0.1411` maxDD `-27.3622`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
