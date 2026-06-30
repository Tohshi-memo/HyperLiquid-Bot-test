# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T22:52:33.648307+00:00`
- Price records: `672`
- Market context records: `5294`
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

- `market_context_high->unknown_24h` score `22.6011` n `153` status `ready` deltaP `26.297` edge `1.7171` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `7.5812` n `153` status `ready` deltaP `25.7353` edge `0.8752` maxDD `-26.5332`
- `market_context_high->equity_24h` score `4.487` n `153` status `ready` deltaP `19.9653` edge `0.8037` maxDD `-40.0306`
- `market_context_high->crypto_alt_4h` score `4.0923` n `181` status `ready` deltaP `15.7661` edge `0.4` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.993` n `181` status `ready` deltaP `16.6041` edge `0.4513` maxDD `-14.0065`
- `market_context_high->equity_4h` score `1.4115` n `181` status `ready` deltaP `11.0388` edge `0.2079` maxDD `-7.4425`
- `market_context_high->unknown_4h` score `0.9273` n `181` status `ready` deltaP `14.6392` edge `0.0819` maxDD `-5.5109`
- `market_context_high->fx_24h` score `0.5505` n `153` status `ready` deltaP `13.3068` edge `0.0467` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.2847` n `193` status `ready` deltaP `3.7022` edge `0.0952` maxDD `-5.0257`
- `market_context_high->index_24h` score `0.2833` n `153` status `ready` deltaP `20.8231` edge `0.061` maxDD `-7.413`
- `market_context_high->equity_1h` score `0.1359` n `193` status `ready` deltaP `8.1226` edge `0.0537` maxDD `-5.0555`
- `market_context_high->crypto_major_1h` score `0.1274` n `193` status `ready` deltaP `5.1992` edge `0.1005` maxDD `-6.9639`
- `market_context_high->index_1h` score `-0.0213` n `193` status `ready` deltaP `5.774` edge `0.0101` maxDD `-1.0296`
- `market_context_high->index_4h` score `-0.2892` n `181` status `ready` deltaP `7.1343` edge `0.0271` maxDD `-2.9391`
- `market_context_high->metal_1h` score `-0.3613` n `193` status `ready` deltaP `2.0555` edge `0.0075` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.3952` n `193` status `ready` deltaP `-0.2133` edge `-0.0003` maxDD `-0.5823`
- `market_context_high->fx_4h` score `-0.7299` n `181` status `ready` deltaP `1.1319` edge `0.0018` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.4697` n `193` status `ready` deltaP `-3.5982` edge `-0.0067` maxDD `-3.3428`
- `market_context_high->metal_4h` score `-1.8013` n `181` status `ready` deltaP `-4.6001` edge `0.0009` maxDD `-9.4268`
- `market_context_high->crypto_alt_24h` score `-2.9086` n `153` status `ready` deltaP `13.3476` edge `0.3791` maxDD `-53.6115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
