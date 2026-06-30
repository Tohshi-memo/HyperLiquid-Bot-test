# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T23:52:25.766241+00:00`
- Price records: `672`
- Market context records: `5298`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9650`

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

- `market_context_high->unknown_24h` score `21.8375` n `153` status `ready` deltaP `25.6025` edge `1.6581` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `7.622` n `153` status `ready` deltaP `25.7353` edge `0.8786` maxDD `-26.5332`
- `market_context_high->equity_24h` score `4.8302` n `153` status `ready` deltaP `19.9653` edge `0.8323` maxDD `-40.0306`
- `market_context_high->crypto_alt_4h` score `3.8189` n `185` status `ready` deltaP `14.6284` edge `0.3848` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.7241` n `185` status `ready` deltaP `15.4185` edge `0.4368` maxDD `-14.0065`
- `market_context_high->equity_4h` score `1.7384` n `185` status `ready` deltaP `11.7197` edge `0.2306` maxDD `-7.4425`
- `market_context_high->unknown_4h` score `0.7939` n `185` status `ready` deltaP `14.3672` edge `0.0726` maxDD `-5.5109`
- `market_context_high->fx_24h` score `0.5445` n `153` status `ready` deltaP `13.3068` edge `0.0462` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.3215` n `194` status `ready` deltaP `3.8922` edge `0.097` maxDD `-5.0257`
- `market_context_high->index_24h` score `0.3075` n `153` status `ready` deltaP `20.8231` edge `0.0641` maxDD `-7.413`
- `market_context_high->equity_1h` score `0.1931` n `194` status `ready` deltaP `8.3123` edge `0.0572` maxDD `-5.0555`
- `market_context_high->crypto_major_1h` score `0.1474` n `194` status `ready` deltaP `5.2395` edge `0.1019` maxDD `-6.9639`
- `market_context_high->index_1h` score `0.001` n `194` status `ready` deltaP `5.9186` edge `0.011` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.3389` n `194` status `ready` deltaP `2.3952` edge `0.0081` maxDD `-2.0682`
- `market_context_high->index_4h` score `-0.3618` n `185` status `ready` deltaP `6.0085` edge `0.0253` maxDD `-2.9391`
- `market_context_high->fx_1h` score `-0.3921` n `194` status `ready` deltaP `-0.1836` edge `-0.0001` maxDD `-0.5823`
- `market_context_high->fx_4h` score `-0.7451` n `185` status `ready` deltaP `0.8396` edge `0.0018` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.4587` n `194` status `ready` deltaP `-3.4755` edge `-0.0066` maxDD `-3.3428`
- `market_context_high->metal_4h` score `-1.9713` n `185` status `ready` deltaP `-5.4961` edge `-0.0033` maxDD `-10.3565`
- `market_context_high->crypto_alt_24h` score `-2.9023` n `153` status `ready` deltaP `13.3476` edge `0.3799` maxDD `-53.6115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
