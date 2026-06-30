# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T22:37:28.497017+00:00`
- Price records: `672`
- Market context records: `5292`
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

- `market_context_high->unknown_24h` score `22.8742` n `153` status `ready` deltaP `26.4706` edge `1.7387` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `7.574` n `153` status `ready` deltaP `25.7353` edge `0.8746` maxDD `-26.5332`
- `market_context_high->equity_24h` score `4.4174` n `153` status `ready` deltaP `19.9653` edge `0.7979` maxDD `-40.0306`
- `market_context_high->crypto_alt_4h` score `4.0851` n `181` status `ready` deltaP `15.7661` edge `0.3994` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.9712` n `181` status `ready` deltaP `16.4517` edge `0.4505` maxDD `-14.0065`
- `market_context_high->equity_4h` score `1.3407` n `181` status `ready` deltaP `11.0388` edge `0.202` maxDD `-7.4425`
- `market_context_high->unknown_4h` score `1.0149` n `181` status `ready` deltaP `14.6392` edge `0.0892` maxDD `-5.5109`
- `market_context_high->fx_24h` score `0.5517` n `153` status `ready` deltaP `13.3068` edge `0.0468` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.3153` n `192` status `ready` deltaP `3.9639` edge `0.096` maxDD `-5.0257`
- `market_context_high->index_24h` score `0.2779` n `153` status `ready` deltaP `20.8231` edge `0.0603` maxDD `-7.413`
- `market_context_high->equity_1h` score `0.1539` n `192` status `ready` deltaP `8.3022` edge `0.054` maxDD `-5.0555`
- `market_context_high->crypto_major_1h` score `0.1423` n `192` status `ready` deltaP `5.3112` edge `0.101` maxDD `-6.9639`
- `market_context_high->index_1h` score `-0.0384` n `192` status `ready` deltaP `5.5608` edge `0.0101` maxDD `-1.0296`
- `market_context_high->index_4h` score `-0.29` n `181` status `ready` deltaP `7.1343` edge `0.027` maxDD `-2.9391`
- `market_context_high->metal_1h` score `-0.3677` n `192` status `ready` deltaP `1.9461` edge `0.0074` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.388` n `192` status `ready` deltaP `-0.0904` edge `-0.0002` maxDD `-0.5823`
- `market_context_high->fx_4h` score `-0.7386` n `181` status `ready` deltaP `0.9795` edge `0.0017` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.4476` n `192` status `ready` deltaP `-3.3527` edge `-0.0065` maxDD `-3.3428`
- `market_context_high->metal_4h` score `-1.8013` n `181` status `ready` deltaP `-4.6001` edge `0.0009` maxDD `-9.4268`
- `market_context_high->crypto_alt_24h` score `-2.9062` n `153` status `ready` deltaP `13.3476` edge `0.3794` maxDD `-53.6115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
