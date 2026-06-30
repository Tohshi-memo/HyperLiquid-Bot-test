# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T20:22:27.228908+00:00`
- Price records: `672`
- Market context records: `5282`
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

- `market_context_high->unknown_24h` score `24.8261` n `153` status `ready` deltaP `27.8595` edge `1.8921` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `7.4972` n `153` status `ready` deltaP `25.7353` edge `0.8682` maxDD `-26.5332`
- `market_context_high->crypto_alt_4h` score `4.2635` n `176` status `ready` deltaP `16.4357` edge `0.4098` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.9628` n `176` status `ready` deltaP `16.0477` edge `0.4525` maxDD `-14.0065`
- `market_context_high->equity_24h` score `3.8486` n `153` status `ready` deltaP `19.9653` edge `0.7505` maxDD `-40.0306`
- `market_context_high->equity_4h` score `1.0064` n `176` status `ready` deltaP `10.1441` edge `0.1801` maxDD `-7.4425`
- `market_context_high->unknown_4h` score `0.754` n `176` status `ready` deltaP `14.648` edge `0.0674` maxDD `-5.5109`
- `market_context_high->fx_24h` score `0.5661` n `153` status `ready` deltaP `13.3068` edge `0.048` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.507` n `183` status `ready` deltaP `5.0563` edge `0.1047` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.3269` n `183` status `ready` deltaP `6.2539` edge `0.1101` maxDD `-6.9639`
- `market_context_high->index_24h` score `0.235` n `153` status `ready` deltaP `20.8231` edge `0.0548` maxDD `-7.413`
- `market_context_high->equity_1h` score `0.1291` n `183` status `ready` deltaP `7.4073` edge `0.0579` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.0038` n `183` status `ready` deltaP `5.8727` edge `0.0109` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.2281` n `183` status `ready` deltaP `2.9155` edge `0.0105` maxDD `-2.0682`
- `market_context_high->index_4h` score `-0.2763` n `176` status `ready` deltaP `7.4418` edge `0.0267` maxDD `-2.9391`
- `market_context_high->fx_1h` score `-0.3407` n `183` status `ready` deltaP `0.76` edge `0.0002` maxDD `-0.5823`
- `market_context_high->fx_4h` score `-0.7218` n `176` status `ready` deltaP `1.3026` edge `0.0017` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.3516` n `183` status `ready` deltaP `-2.212` edge `-0.0061` maxDD `-3.3428`
- `market_context_high->metal_4h` score `-1.6939` n `176` status `ready` deltaP `-3.423` edge `0.006` maxDD `-9.3609`
- `market_context_high->unknown_1h` score `-2.5963` n `183` status `ready` deltaP `6.8085` edge `-0.1976` maxDD `-2.7986`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
