# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T16:07:24.879609+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `9998`

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

- `market_context_high->unknown_24h` score `535.0598` n `64` status `ready` deltaP `3.8128` edge `44.5629` maxDD `0.0`
- `news_risk_high->equity_24h` score `44.831` n `50` status `ready` deltaP `50.3917` edge `3.4706` maxDD `-3.6503`
- `market_context_high->equity_24h` score `40.1485` n `64` status `ready` deltaP `46.7667` edge `3.1881` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `33.2969` n `64` status `ready` deltaP `61.5035` edge `2.4724` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `23.4664` n `50` status `ready` deltaP `46.3882` edge `2.8136` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `12.2463` n `50` status `ready` deltaP `39.0671` edge `0.8731` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `9.0274` n `50` status `ready` deltaP `18.0035` edge `1.4879` maxDD `-29.0448`
- `market_context_high->index_24h` score `8.1005` n `64` status `ready` deltaP `49.5586` edge `0.3533` maxDD `-0.0251`
- `news_risk_high->commodity_24h` score `6.8167` n `50` status `ready` deltaP `45.234` edge `0.2665` maxDD `0.0`
- `market_context_high->metal_24h` score `6.5891` n `64` status `ready` deltaP `62.1913` edge `0.5193` maxDD `-3.7989`
- `news_risk_high->index_24h` score `6.5063` n `50` status `ready` deltaP `42.2461` edge `0.2909` maxDD `-0.4279`
- `news_risk_high->crypto_major_4h` score `5.2103` n `50` status `ready` deltaP `22.9756` edge `0.4186` maxDD `-9.0062`
- `news_risk_high->metal_4h` score `4.8686` n `50` status `ready` deltaP `43.9268` edge `0.1505` maxDD `-1.0104`
- `market_context_high->crypto_major_24h` score `4.8022` n `64` status `ready` deltaP `13.3882` edge `1.2447` maxDD `-69.0352`
- `news_risk_high->crypto_alt_4h` score `4.4868` n `50` status `ready` deltaP `26.9939` edge `0.3375` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `3.9972` n `50` status `ready` deltaP `21.3473` edge `0.2538` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.7463` n `50` status `ready` deltaP `34.8963` edge `0.1049` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.6597` n `50` status `ready` deltaP `25.8659` edge `0.0842` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2245` n `50` status `ready` deltaP `25.4431` edge `0.0412` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.2567` n `50` status `ready` deltaP `16.7485` edge `0.0232` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
