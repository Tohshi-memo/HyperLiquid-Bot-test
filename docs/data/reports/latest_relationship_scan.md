# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T22:52:26.650065+00:00`
- Price records: `672`
- Market context records: `5190`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5644`

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

- `market_context_high->unknown_24h` score `20.5612` n `86` status `ready` deltaP `33.196` edge `1.5111` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `13.544` n `86` status `ready` deltaP `27.3054` edge `1.3128` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `10.5357` n `86` status `ready` deltaP `28.016` edge `1.0299` maxDD `-23.4292`
- `market_context_high->unknown_4h` score `5.4923` n `155` status `ready` deltaP `19.7266` edge `0.4284` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `4.3677` n `155` status `ready` deltaP `12.7793` edge `0.4387` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.3186` n `155` status `ready` deltaP `13.4599` edge `0.4994` maxDD `-14.0065`
- `market_context_high->unknown_1h` score `2.6072` n `155` status `ready` deltaP `9.4369` edge `0.2185` maxDD `-2.7986`
- `market_context_high->equity_4h` score `1.1486` n `155` status `ready` deltaP `8.9221` edge `0.2001` maxDD `-7.4425`
- `market_context_high->crypto_alt_1h` score `0.5037` n `155` status `ready` deltaP `4.2042` edge `0.1101` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.4937` n `155` status `ready` deltaP `6.2536` edge `0.124` maxDD `-6.9639`
- `market_context_high->fx_24h` score `0.2636` n `86` status `ready` deltaP `11.8499` edge `0.0325` maxDD `-0.8294`
- `market_context_high->equity_1h` score `0.2381` n `155` status `ready` deltaP `7.4657` edge `0.0666` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.0106` n `155` status `ready` deltaP `5.6336` edge `0.0137` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.0615` n `155` status `ready` deltaP `5.0096` edge `0.0179` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.265` n `155` status `ready` deltaP `1.6593` edge `0.0002` maxDD `-0.6194`
- `market_context_high->index_4h` score `-0.4408` n `155` status `ready` deltaP `6.2107` edge `0.0336` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.4839` n `155` status `ready` deltaP `5.1682` edge `0.0069` maxDD `-1.6047`
- `market_context_high->commodity_1h` score `-0.5884` n `155` status `ready` deltaP `0.875` edge `-0.0004` maxDD `-2.4692`
- `market_context_high->index_24h` score `-0.9812` n `86` status `ready` deltaP `8.0709` edge `-0.0161` maxDD `-7.413`
- `market_context_high->metal_4h` score `-1.2625` n `155` status `ready` deltaP `0.5074` edge `0.0351` maxDD `-9.3609`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
