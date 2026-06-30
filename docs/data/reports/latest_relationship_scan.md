# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T20:52:30.843559+00:00`
- Price records: `672`
- Market context records: `5284`
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

- `market_context_high->unknown_24h` score `24.4359` n `153` status `ready` deltaP `27.5122` edge `1.8619` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `7.5104` n `153` status `ready` deltaP `25.7353` edge `0.8693` maxDD `-26.5332`
- `market_context_high->crypto_alt_4h` score `4.2922` n `177` status `ready` deltaP `16.8096` edge `0.4097` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.01` n `177` status `ready` deltaP `16.2628` edge `0.455` maxDD `-14.0065`
- `market_context_high->equity_24h` score `3.9698` n `153` status `ready` deltaP `19.9653` edge `0.7606` maxDD `-40.0306`
- `market_context_high->equity_4h` score `1.0414` n `177` status `ready` deltaP `10.3271` edge `0.1818` maxDD `-7.4425`
- `market_context_high->unknown_4h` score `0.7543` n `177` status `ready` deltaP `14.8021` edge `0.0664` maxDD `-5.5109`
- `market_context_high->fx_24h` score `0.5625` n `153` status `ready` deltaP `13.3068` edge `0.0477` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.4501` n `185` status `ready` deltaP `4.7945` edge `0.1017` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.276` n `185` status `ready` deltaP `5.9921` edge `0.1076` maxDD `-6.9639`
- `market_context_high->index_24h` score `0.2443` n `153` status `ready` deltaP `20.8231` edge `0.056` maxDD `-7.413`
- `market_context_high->equity_1h` score `0.1478` n `185` status `ready` deltaP `7.6712` edge `0.0577` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.0345` n `185` status `ready` deltaP `5.5341` edge `0.0106` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.2505` n `185` status `ready` deltaP `2.6655` edge `0.0093` maxDD `-2.0682`
- `market_context_high->index_4h` score `-0.2752` n `177` status `ready` deltaP `7.4032` edge `0.0271` maxDD `-2.9391`
- `market_context_high->fx_1h` score `-0.3298` n `185` status `ready` deltaP `0.9686` edge `0.0002` maxDD `-0.5823`
- `market_context_high->fx_4h` score `-0.724` n `177` status `ready` deltaP `1.2608` edge `0.0017` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.3944` n `185` status `ready` deltaP `-2.7318` edge `-0.0062` maxDD `-3.3428`
- `market_context_high->metal_4h` score `-1.7119` n `177` status `ready` deltaP `-3.6637` edge `0.0053` maxDD `-9.3609`
- `market_context_high->unknown_1h` score `-2.7264` n `185` status `ready` deltaP `7.2221` edge `-0.2112` maxDD `-2.7986`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
