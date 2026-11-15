# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T16:22:32.108538+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10008`

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

- `market_context_high->unknown_24h` score `535.1798` n `64` status `ready` deltaP `3.8128` edge `44.5729` maxDD `0.0`
- `news_risk_high->equity_24h` score `44.897` n `50` status `ready` deltaP `50.3917` edge `3.4761` maxDD `-3.6503`
- `market_context_high->equity_24h` score `40.2145` n `64` status `ready` deltaP `46.7667` edge `3.1936` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `33.3479` n `64` status `ready` deltaP `61.6768` edge `2.4755` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `23.4516` n `50` status `ready` deltaP `46.3882` edge `2.8117` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `12.2681` n `50` status `ready` deltaP `39.2195` edge `0.8739` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `9.0606` n `50` status `ready` deltaP `18.1768` edge `1.491` maxDD `-29.0448`
- `market_context_high->index_24h` score `8.1077` n `64` status `ready` deltaP `49.5586` edge `0.3539` maxDD `-0.0251`
- `news_risk_high->commodity_24h` score `6.7945` n `50` status `ready` deltaP `45.0607` edge `0.2658` maxDD `0.0`
- `market_context_high->metal_24h` score `6.6051` n `64` status `ready` deltaP `62.3646` edge `0.5202` maxDD `-3.7989`
- `news_risk_high->index_24h` score `6.5135` n `50` status `ready` deltaP `42.2461` edge `0.2915` maxDD `-0.4279`
- `news_risk_high->crypto_major_4h` score `5.2319` n `50` status `ready` deltaP `22.9756` edge `0.4204` maxDD `-9.0062`
- `news_risk_high->metal_4h` score `4.882` n `50` status `ready` deltaP `44.0793` edge `0.1506` maxDD `-1.0104`
- `market_context_high->crypto_major_24h` score `4.7794` n `64` status `ready` deltaP `13.3882` edge `1.2428` maxDD `-69.0352`
- `news_risk_high->crypto_alt_4h` score `4.5048` n `50` status `ready` deltaP `26.9939` edge `0.339` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `3.996` n `50` status `ready` deltaP `21.3473` edge `0.2537` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.7451` n `50` status `ready` deltaP `34.8963` edge `0.1048` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.6609` n `50` status `ready` deltaP `25.8659` edge `0.0843` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2245` n `50` status `ready` deltaP `25.4431` edge `0.0412` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.2567` n `50` status `ready` deltaP `16.7485` edge `0.0232` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
