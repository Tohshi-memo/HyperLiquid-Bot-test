# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T15:52:30.964545+00:00`
- Price records: `672`
- Market context records: `5262`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9598`

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

- `market_context_high->unknown_24h` score `26.6692` n `147` status `ready` deltaP `30.0631` edge `2.031` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `10.4379` n `147` status `ready` deltaP `28.4297` edge `1.0407` maxDD `-22.166`
- `market_context_high->crypto_alt_4h` score `4.0983` n `158` status `ready` deltaP `14.3717` edge `0.4098` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.8807` n `158` status `ready` deltaP `14.5705` edge `0.4555` maxDD `-14.0065`
- `market_context_high->equity_24h` score `3.426` n `147` status `ready` deltaP `19.5118` edge `0.7183` maxDD `-40.0306`
- `market_context_high->unknown_4h` score `1.9644` n `158` status `ready` deltaP `17.2835` edge `0.1507` maxDD `-5.5109`
- `market_context_high->equity_4h` score `0.5865` n `158` status `ready` deltaP `8.4363` edge `0.1565` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.5221` n `147` status `ready` deltaP `12.6666` edge `0.0486` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.4965` n `170` status `ready` deltaP `4.609` edge `0.1068` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.2445` n `170` status `ready` deltaP `5.5389` edge `0.108` maxDD `-6.9639`
- `market_context_high->index_24h` score `0.2361` n `147` status `ready` deltaP `21.0247` edge `0.0536` maxDD `-7.413`
- `market_context_high->crypto_alt_24h` score `0.08` n `147` status `ready` deltaP `15.4018` edge `0.5371` maxDD `-38.6949`
- `market_context_high->equity_1h` score `-0.014` n `170` status `ready` deltaP `5.9792` edge `0.0555` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.0583` n `170` status `ready` deltaP `5.1022` edge `0.0115` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.1951` n `170` status `ready` deltaP `4.3096` edge `0.0142` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.2242` n `170` status `ready` deltaP `2.3001` edge `0.0007` maxDD `-0.5823`
- `market_context_high->index_4h` score `-0.734` n `158` status `ready` deltaP `4.6754` edge `0.0194` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.7982` n `158` status `ready` deltaP `0.0425` edge `0.0003` maxDD `-1.567`
- `market_context_high->unknown_1h` score `-0.8422` n `170` status `ready` deltaP `6.9849` edge `-0.0526` maxDD `-2.7986`
- `market_context_high->commodity_1h` score `-1.3316` n `170` status `ready` deltaP `-2.6629` edge `-0.0067` maxDD `-2.9208`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
