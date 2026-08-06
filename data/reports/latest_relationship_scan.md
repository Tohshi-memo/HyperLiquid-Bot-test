# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-06T21:55:49.649602+00:00`
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

- `market_context_high->unknown_24h` score `50.295` n `109` status `ready` deltaP `3.7571` edge `4.1705` maxDD `-0.0104`
- `market_context_high->commodity_4h` score `1.17` n `119` status `ready` deltaP `13.2494` edge `0.0938` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.9376` n `109` status `ready` deltaP `3.7004` edge `0.1703` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.534` n `109` status `ready` deltaP `21.4854` edge `0.0458` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4977` n `120` status `ready` deltaP `8.0216` edge `0.0296` maxDD `-1.3282`
- `market_context_high->fx_1h` score `-0.0127` n `120` status `ready` deltaP `5.6371` edge `-0.0042` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.3922` n `119` status `ready` deltaP `5.5369` edge `-0.0012` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5559` n `120` status `ready` deltaP `-2.2826` edge `-0.0066` maxDD `-1.6224`
- `market_context_high->crypto_alt_1h` score `-0.7957` n `120` status `ready` deltaP `-3.2042` edge `-0.0096` maxDD `-3.0178`
- `market_context_high->index_1h` score `-1.0774` n `120` status `ready` deltaP `-3.1768` edge `-0.0152` maxDD `-1.6054`
- `market_context_high->crypto_alt_4h` score `-1.2428` n `119` status `ready` deltaP `1.7636` edge `-0.0321` maxDD `-5.7857`
- `market_context_high->metal_4h` score `-1.3235` n `119` status `ready` deltaP `1.182` edge `0.0053` maxDD `-3.211`
- `market_context_high->equity_1h` score `-1.3785` n `120` status `ready` deltaP `3.4563` edge `-0.0433` maxDD `-10.5179`
- `market_context_high->index_24h` score `-1.4201` n `109` status `ready` deltaP `-4.8858` edge `0.07` maxDD `-7.8922`
- `market_context_high->index_4h` score `-1.7484` n `119` status `ready` deltaP `-8.7324` edge `-0.0405` maxDD `-4.7021`
- `market_context_high->crypto_major_1h` score `-2.6623` n `120` status `ready` deltaP `-6.9784` edge `-0.038` maxDD `-7.6533`
- `market_context_high->crypto_alt_24h` score `-2.8656` n `109` status `ready` deltaP `-5.1446` edge `-0.0602` maxDD `-4.5445`
- `market_context_high->commodity_24h` score `-6.2252` n `109` status `ready` deltaP `9.9769` edge `0.0119` maxDD `-52.7876`
- `market_context_high->equity_4h` score `-6.2572` n `119` status `ready` deltaP `-0.8906` edge `-0.2674` maxDD `-34.9766`
- `market_context_high->crypto_major_4h` score `-7.3139` n `119` status `ready` deltaP `-6.5996` edge `-0.1443` maxDD `-27.3622`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
