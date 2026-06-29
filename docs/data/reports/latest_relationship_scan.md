# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T19:07:32.585331+00:00`
- Price records: `672`
- Market context records: `5172`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5650`

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

- `market_context_high->unknown_24h` score `26.5799` n `71` status `ready` deltaP `32.5606` edge `2.0169` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `9.2106` n `71` status `ready` deltaP `21.5571` edge `0.99` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `8.4716` n `71` status `ready` deltaP `23.0047` edge `0.8913` maxDD `-23.4292`
- `market_context_high->unknown_4h` score `6.0807` n `147` status `ready` deltaP `20.6322` edge `0.4714` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `5.0183` n `147` status `ready` deltaP `15.4813` edge `0.4749` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.6299` n `147` status `ready` deltaP `14.4257` edge `0.5189` maxDD `-14.0065`
- `market_context_high->unknown_1h` score `2.9564` n `154` status `ready` deltaP `10.5918` edge `0.2399` maxDD `-2.7986`
- `market_context_high->equity_4h` score `1.2934` n `147` status `ready` deltaP `9.1722` edge `0.2105` maxDD `-7.4425`
- `market_context_high->crypto_major_1h` score `0.6488` n `154` status `ready` deltaP `7.3373` edge `0.1297` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `0.5872` n `154` status `ready` deltaP `4.5435` edge `0.1148` maxDD `-5.0257`
- `market_context_high->equity_1h` score `0.3422` n `154` status `ready` deltaP `8.391` edge `0.0691` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.0246` n `154` status `ready` deltaP `5.7936` edge `0.0138` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.0381` n `154` status `ready` deltaP `5.3406` edge `0.0187` maxDD `-2.0682`
- `market_context_high->commodity_24h` score `-0.2025` n `71` status `ready` deltaP `13.2629` edge `0.0958` maxDD `-9.4808`
- `market_context_high->fx_24h` score `-0.2229` n `71` status `ready` deltaP `8.5583` edge `0.0139` maxDD `-0.8294`
- `market_context_high->fx_1h` score `-0.257` n `154` status `ready` deltaP `1.7984` edge `0.0003` maxDD `-0.6194`
- `market_context_high->index_4h` score `-0.4197` n `147` status `ready` deltaP `6.0395` edge `0.0365` maxDD `-2.9391`
- `market_context_high->metal_24h` score `-0.4447` n `71` status `ready` deltaP `-3.35` edge `0.1798` maxDD `-9.4921`
- `market_context_high->fx_4h` score `-0.5599` n `147` status `ready` deltaP `3.7072` edge `0.0069` maxDD `-1.6047`
- `market_context_high->commodity_1h` score `-0.5872` n `154` status `ready` deltaP `0.8982` edge `-0.0004` maxDD `-2.4692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
