# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T00:22:30.133726+00:00`
- Price records: `672`
- Market context records: `5301`
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

- `market_context_high->unknown_24h` score `21.4425` n `153` status `ready` deltaP `25.2553` edge `1.6275` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `7.622` n `153` status `ready` deltaP `25.7353` edge `0.8786` maxDD `-26.5332`
- `market_context_high->equity_24h` score `4.9754` n `153` status `ready` deltaP `19.9653` edge `0.8444` maxDD `-40.0306`
- `market_context_high->crypto_alt_4h` score `3.6705` n `187` status `ready` deltaP `14.004` edge `0.3766` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.5715` n `187` status `ready` deltaP `14.771` edge `0.4284` maxDD `-14.0065`
- `market_context_high->equity_4h` score `1.8218` n `187` status `ready` deltaP `11.6669` edge `0.2379` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.5433` n `153` status `ready` deltaP `13.3068` edge `0.0461` maxDD `-0.8294`
- `market_context_high->unknown_4h` score `0.5126` n `187` status `ready` deltaP `13.581` edge `0.0544` maxDD `-5.5109`
- `market_context_high->index_24h` score `0.3122` n `153` status `ready` deltaP `20.8231` edge `0.0647` maxDD `-7.413`
- `market_context_high->crypto_alt_1h` score `0.2904` n `194` status `ready` deltaP `3.5928` edge `0.0964` maxDD `-5.0257`
- `market_context_high->equity_1h` score `0.1979` n `194` status `ready` deltaP `8.3123` edge `0.0576` maxDD `-5.0555`
- `market_context_high->crypto_major_1h` score `0.1426` n `194` status `ready` deltaP `5.2395` edge `0.1015` maxDD `-6.9639`
- `market_context_high->index_1h` score `0.001` n `194` status `ready` deltaP `5.9186` edge `0.011` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.3405` n `194` status `ready` deltaP `2.3952` edge `0.0079` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.4007` n `194` status `ready` deltaP `-0.3333` edge `-0.0002` maxDD `-0.5823`
- `market_context_high->index_4h` score `-0.4033` n `187` status `ready` deltaP `5.39` edge `0.0241` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.7215` n `187` status `ready` deltaP `1.279` edge `0.0019` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.4718` n `194` status `ready` deltaP `-3.6252` edge `-0.0067` maxDD `-3.3428`
- `market_context_high->metal_4h` score `-2.069` n `187` status `ready` deltaP `-5.9296` edge `-0.0063` maxDD `-10.8876`
- `market_context_high->crypto_alt_24h` score `-2.907` n `153` status `ready` deltaP `13.3476` edge `0.3793` maxDD `-53.6115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
