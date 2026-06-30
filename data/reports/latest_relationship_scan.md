# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T18:22:27.565238+00:00`
- Price records: `672`
- Market context records: `5273`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9652`

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

- `market_context_high->unknown_24h` score `26.3592` n `153` status `ready` deltaP `29.2484` edge `2.0106` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `7.6988` n `153` status `ready` deltaP `25.7353` edge `0.885` maxDD `-26.5332`
- `market_context_high->crypto_alt_4h` score `4.3224` n `168` status `ready` deltaP `15.8972` edge `0.4183` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.762` n `168` status `ready` deltaP `14.6777` edge `0.4449` maxDD `-14.0065`
- `market_context_high->equity_24h` score `3.6746` n `153` status `ready` deltaP `19.9653` edge `0.736` maxDD `-40.0306`
- `market_context_high->unknown_4h` score `1.1308` n `168` status `ready` deltaP `15.5633` edge `0.0927` maxDD `-5.5109`
- `market_context_high->equity_4h` score `0.8212` n `168` status `ready` deltaP `9.0592` edge `0.1719` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.5793` n `153` status `ready` deltaP `13.3068` edge `0.0491` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.5036` n `177` status `ready` deltaP `4.9376` edge `0.1052` maxDD `-5.0257`
- `market_context_high->index_24h` score `0.2733` n `153` status `ready` deltaP `21.1703` edge `0.0574` maxDD `-7.413`
- `market_context_high->crypto_major_1h` score `0.2405` n `177` status `ready` deltaP `5.4882` edge `0.108` maxDD `-6.9639`
- `market_context_high->equity_1h` score `0.0325` n `177` status `ready` deltaP `6.4101` edge `0.0565` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.0039` n `177` status `ready` deltaP `5.8789` edge `0.0115` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.3215` n `177` status `ready` deltaP `3.2088` edge `0.011` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.327` n `177` status `ready` deltaP `0.4127` edge `0.0001` maxDD `-0.5823`
- `market_context_high->index_4h` score `-0.5401` n `168` status `ready` deltaP `6.1701` edge `0.0256` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.6787` n `168` status `ready` deltaP `1.9963` edge `0.0026` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.424` n `177` status `ready` deltaP `-3.1073` edge `-0.007` maxDD `-3.2759`
- `market_context_high->metal_4h` score `-1.5834` n `168` status `ready` deltaP `-1.989` edge `0.0106` maxDD `-9.3609`
- `market_context_high->unknown_1h` score `-1.9512` n `177` status `ready` deltaP `6.608` edge `-0.1425` maxDD `-2.7986`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
