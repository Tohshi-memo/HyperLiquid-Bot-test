# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T18:45:14.887203+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5932`

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

- `news_risk_high->unknown_24h` score `5189.8455` n `60` status `ready` deltaP `33.5413` edge `432.3056` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `17.2017` n `53` status `ready` deltaP `55.711` edge `1.1018` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `6.3641` n `61` status `ready` deltaP `23.3907` edge `0.4341` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.6032` n `61` status `ready` deltaP `22.9333` edge `0.0831` maxDD `-0.191`
- `market_context_high->commodity_24h` score `1.9588` n `53` status `ready` deltaP `29.2175` edge `0.2422` maxDD `-10.2019`
- `news_risk_high->crypto_major_4h` score `0.9996` n `61` status `ready` deltaP `7.2996` edge `0.1751` maxDD `-4.9822`
- `market_context_high->crypto_alt_4h` score `0.6192` n `53` status `ready` deltaP `9.0428` edge `0.1148` maxDD `-5.323`
- `news_risk_high->equity_1h` score `0.6062` n `68` status `ready` deltaP `8.5946` edge `0.0755` maxDD `-2.916`
- `news_risk_high->crypto_alt_4h` score `0.3168` n `61` status `ready` deltaP `11.4554` edge `0.1133` maxDD `-6.5912`
- `market_context_high->fx_4h` score `0.2383` n `53` status `ready` deltaP `14.1682` edge `0.0157` maxDD `-1.3685`
- `news_risk_high->fx_4h` score `0.2253` n `61` status `ready` deltaP `13.5496` edge `0.0242` maxDD `-0.6604`
- `news_risk_high->crypto_alt_1h` score `0.1544` n `68` status `ready` deltaP `7.08` edge `0.0408` maxDD `-3.1233`
- `news_risk_high->metal_4h` score `0.1451` n `61` status `ready` deltaP `4.7855` edge `0.0343` maxDD `-0.8085`
- `market_context_high->fx_1h` score `0.0091` n `53` status `ready` deltaP `7.502` edge `0.001` maxDD `-0.6874`
- `market_context_high->commodity_1h` score `-0.0854` n `53` status `ready` deltaP `4.0278` edge `0.0163` maxDD `-1.3282`
- `news_risk_high->index_1h` score `-0.0917` n `68` status `ready` deltaP `1.8669` edge `0.0081` maxDD `-0.5845`
- `news_risk_high->fx_1h` score `-0.0957` n `68` status `ready` deltaP `2.3688` edge `0.0042` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1092` n `68` status `ready` deltaP `2.9148` edge `0.0069` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.1532` n `68` status `ready` deltaP `2.6682` edge `0.0346` maxDD `-3.762`
- `market_context_high->fx_24h` score `-0.1761` n `53` status `ready` deltaP `5.3268` edge `0.0399` maxDD `-2.506`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
