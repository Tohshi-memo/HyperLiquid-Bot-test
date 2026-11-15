# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T16:52:28.498144+00:00`
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

- `market_context_high->unknown_24h` score `535.3418` n `64` status `ready` deltaP `3.8128` edge `44.5864` maxDD `0.0`
- `news_risk_high->equity_24h` score `45.035` n `50` status `ready` deltaP `50.3917` edge `3.4876` maxDD `-3.6503`
- `market_context_high->equity_24h` score `40.3525` n `64` status `ready` deltaP `46.7667` edge `3.2051` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `33.4645` n `64` status `ready` deltaP `62.0234` edge `2.4829` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `23.4188` n `50` status `ready` deltaP `46.3882` edge `2.8075` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `12.2813` n `50` status `ready` deltaP `39.2195` edge `0.875` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `9.1364` n `50` status `ready` deltaP `18.5234` edge `1.4984` maxDD `-29.0448`
- `market_context_high->index_24h` score `8.1221` n `64` status `ready` deltaP `49.5586` edge `0.3551` maxDD `-0.0251`
- `news_risk_high->commodity_24h` score `6.7535` n `50` status `ready` deltaP `44.714` edge `0.2647` maxDD `0.0`
- `market_context_high->metal_24h` score `6.6403` n `64` status `ready` deltaP `62.7112` edge `0.5224` maxDD `-3.7989`
- `news_risk_high->index_24h` score `6.5279` n `50` status `ready` deltaP `42.2461` edge `0.2927` maxDD `-0.4279`
- `news_risk_high->crypto_major_4h` score `5.2727` n `50` status `ready` deltaP `22.9756` edge `0.4238` maxDD `-9.0062`
- `news_risk_high->metal_4h` score `4.9088` n `50` status `ready` deltaP `44.3841` edge `0.1508` maxDD `-1.0104`
- `market_context_high->crypto_major_24h` score `4.729` n `64` status `ready` deltaP `13.3882` edge `1.2386` maxDD `-69.0352`
- `news_risk_high->crypto_alt_4h` score `4.548` n `50` status `ready` deltaP `26.9939` edge `0.3426` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `3.9732` n `50` status `ready` deltaP `21.1976` edge `0.2528` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.7427` n `50` status `ready` deltaP `34.8963` edge `0.1046` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.6609` n `50` status `ready` deltaP `25.8659` edge `0.0843` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2113` n `50` status `ready` deltaP `25.2934` edge `0.0411` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.2436` n `50` status `ready` deltaP `16.5988` edge `0.0231` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
