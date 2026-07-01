# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T00:37:26.058038+00:00`
- Price records: `672`
- Market context records: `5302`
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

- `market_context_high->unknown_24h` score `21.2439` n `153` status `ready` deltaP `25.0817` edge `1.6121` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `7.6028` n `153` status `ready` deltaP `25.7353` edge `0.877` maxDD `-26.5332`
- `market_context_high->equity_24h` score `5.0246` n `153` status `ready` deltaP `19.9653` edge `0.8485` maxDD `-40.0306`
- `market_context_high->crypto_alt_4h` score `3.6063` n `188` status `ready` deltaP `13.6968` edge `0.3733` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.5016` n `188` status `ready` deltaP `14.4525` edge `0.4247` maxDD `-14.0065`
- `market_context_high->equity_4h` score `1.843` n `188` status `ready` deltaP `11.4524` edge `0.2411` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.5433` n `153` status `ready` deltaP `13.3068` edge `0.0461` maxDD `-0.8294`
- `market_context_high->unknown_4h` score `0.3713` n `188` status `ready` deltaP `13.1941` edge `0.0452` maxDD `-5.5109`
- `market_context_high->index_24h` score `0.3122` n `153` status `ready` deltaP `20.8231` edge `0.0647` maxDD `-7.413`
- `market_context_high->crypto_alt_1h` score `0.2916` n `194` status `ready` deltaP `3.5928` edge `0.0965` maxDD `-5.0257`
- `market_context_high->equity_1h` score `0.2015` n `194` status `ready` deltaP `8.3123` edge `0.0579` maxDD `-5.0555`
- `market_context_high->crypto_major_1h` score `0.163` n `194` status `ready` deltaP `5.3892` edge `0.1022` maxDD `-6.9639`
- `market_context_high->index_1h` score `-0.0002` n `194` status `ready` deltaP `5.9186` edge `0.0109` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.3311` n `194` status `ready` deltaP `2.5449` edge `0.0081` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.4092` n `194` status `ready` deltaP `-0.483` edge `-0.0003` maxDD `-0.5823`
- `market_context_high->index_4h` score `-0.423` n `188` status `ready` deltaP `5.0856` edge `0.0236` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.7094` n `188` status `ready` deltaP `1.4952` edge `0.002` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.4587` n `194` status `ready` deltaP `-3.4755` edge `-0.0066` maxDD `-3.3428`
- `market_context_high->metal_4h` score `-2.1001` n `188` status `ready` deltaP `-6.143` edge `-0.007` maxDD `-11.0368`
- `market_context_high->crypto_alt_24h` score `-2.9242` n `153` status `ready` deltaP `13.3476` edge `0.3771` maxDD `-53.6115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
