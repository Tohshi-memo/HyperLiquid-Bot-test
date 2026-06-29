# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T07:22:27.960299+00:00`
- Price records: `672`
- Market context records: `5122`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5560`

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

- `market_context_high->unknown_24h` score `26.2264` n `67` status `ready` deltaP `28.8583` edge `2.0274` maxDD `-1.4072`
- `market_context_high->unknown_1h` score `8.4379` n `126` status `ready` deltaP `7.9817` edge `0.7141` maxDD `-2.7986`
- `market_context_high->unknown_4h` score `7.1809` n `116` status `ready` deltaP `20.0747` edge `0.5668` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `5.3481` n `116` status `ready` deltaP `14.8182` edge `0.5068` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.7396` n `116` status `ready` deltaP `12.5368` edge `0.4573` maxDD `-14.0065`
- `market_context_high->crypto_alt_1h` score `0.9356` n `126` status `ready` deltaP `6.708` edge `0.1294` maxDD `-5.0257`
- `market_context_high->equity_1h` score `0.7343` n `126` status `ready` deltaP `8.0411` edge `0.0669` maxDD `-2.745`
- `market_context_high->crypto_major_1h` score `0.7158` n `126` status `ready` deltaP `7.7702` edge `0.1324` maxDD `-6.9639`
- `market_context_high->commodity_24h` score `0.4139` n `67` status `ready` deltaP `16.5423` edge `0.1051` maxDD `-8.319`
- `market_context_high->equity_4h` score `0.2583` n `116` status `ready` deltaP `7.0017` edge `0.1503` maxDD `-7.4425`
- `market_context_high->metal_1h` score `0.2273` n `126` status `ready` deltaP `8.0102` edge `0.0272` maxDD `-1.4501`
- `market_context_high->index_1h` score `0.0332` n `126` status `ready` deltaP `5.7053` edge `0.0151` maxDD `-1.0296`
- `market_context_high->index_4h` score `-0.4456` n `116` status `ready` deltaP `3.9161` edge `0.0285` maxDD `-2.9391`
- `market_context_high->metal_4h` score `-0.5686` n `116` status `ready` deltaP `2.0448` edge `0.0545` maxDD `-4.6157`
- `market_context_high->fx_1h` score `-0.6565` n `126` status `ready` deltaP `-2.7707` edge `-0.0016` maxDD `-0.7944`
- `market_context_high->commodity_1h` score `-0.9377` n `126` status `ready` deltaP `0.2091` edge `-0.0026` maxDD `-2.155`
- `market_context_high->fx_4h` score `-1.0266` n `116` status `ready` deltaP `-3.7532` edge `0.0007` maxDD `-1.9169`
- `market_context_high->fx_24h` score `-1.5363` n `67` status `ready` deltaP `-3.2105` edge `-0.0097` maxDD `-1.4206`
- `market_context_high->metal_24h` score `-1.8553` n `67` status `ready` deltaP `-1.3319` edge `0.1093` maxDD `-20.3954`
- `market_context_high->commodity_4h` score `-2.5262` n `116` status `ready` deltaP `-1.1985` edge `-0.0301` maxDD `-7.4611`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
