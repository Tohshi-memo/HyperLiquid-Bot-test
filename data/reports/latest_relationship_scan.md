# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T04:07:27.096177+00:00`
- Price records: `672`
- Market context records: `5316`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9648`

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

- `market_context_high->unknown_24h` score `18.9945` n `153` status `ready` deltaP `22.8247` edge `1.4397` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `7.2355` n `153` status `ready` deltaP `25.3881` edge `0.8487` maxDD `-26.5332`
- `market_context_high->equity_24h` score `5.1268` n `153` status `ready` deltaP `19.0972` edge `0.8628` maxDD `-40.0306`
- `market_context_high->crypto_alt_4h` score `3.1627` n `194` status `ready` deltaP `12.0364` edge `0.3474` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.1303` n `194` status `ready` deltaP `13.3361` edge `0.4012` maxDD `-14.0065`
- `market_context_high->equity_4h` score `2.1164` n `194` status `ready` deltaP `11.4643` edge `0.2638` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.5229` n `153` status `ready` deltaP `13.3068` edge `0.0444` maxDD `-0.8294`
- `market_context_high->equity_1h` score `0.4918` n `194` status `ready` deltaP `8.462` edge `0.0811` maxDD `-5.0555`
- `market_context_high->index_24h` score `0.4153` n `153` status `ready` deltaP `21.1703` edge `0.0756` maxDD `-7.413`
- `market_context_high->crypto_alt_1h` score `0.047` n `194` status `ready` deltaP `2.2455` edge `0.0851` maxDD `-5.0257`
- `market_context_high->index_1h` score `0.0274` n `194` status `ready` deltaP `6.218` edge `0.0112` maxDD `-1.0296`
- `market_context_high->crypto_major_1h` score `-0.0289` n `194` status `ready` deltaP `4.491` edge `0.0922` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.335` n `194` status `ready` deltaP `2.3952` edge `0.0086` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.3789` n `194` status `ready` deltaP `0.1158` edge `-0.0004` maxDD `-0.5823`
- `market_context_high->index_4h` score `-0.4694` n `194` status `ready` deltaP `4.8497` edge `0.0234` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.6296` n `194` status `ready` deltaP `2.7454` edge `0.0039` maxDD `-1.567`
- `market_context_high->unknown_4h` score `-0.7201` n `194` status `ready` deltaP `9.8897` edge `-0.0077` maxDD `-6.126`
- `market_context_high->commodity_1h` score `-1.4347` n `194` status `ready` deltaP `-3.1761` edge `-0.0066` maxDD `-3.3428`
- `market_context_high->metal_4h` score `-2.3235` n `194` status `ready` deltaP `-6.0048` edge `-0.0054` maxDD `-12.8631`
- `market_context_high->crypto_alt_24h` score `-3.1316` n `153` status `ready` deltaP `13.3476` edge `0.3505` maxDD `-53.6115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
