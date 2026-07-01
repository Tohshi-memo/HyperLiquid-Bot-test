# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T01:37:26.349326+00:00`
- Price records: `672`
- Market context records: `5306`
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

- `market_context_high->unknown_24h` score `20.5139` n `153` status `ready` deltaP `24.3872` edge `1.5559` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `7.5428` n `153` status `ready` deltaP `25.7353` edge `0.872` maxDD `-26.5332`
- `market_context_high->equity_24h` score `5.243` n `153` status `ready` deltaP `19.9653` edge `0.8667` maxDD `-40.0306`
- `market_context_high->crypto_alt_4h` score `3.3781` n `192` status `ready` deltaP `12.8684` edge `0.3598` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.2307` n `192` status `ready` deltaP `13.2113` edge `0.4104` maxDD `-14.0065`
- `market_context_high->equity_4h` score `1.9226` n `192` status `ready` deltaP `10.6326` edge `0.2532` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.5385` n `153` status `ready` deltaP `13.3068` edge `0.0457` maxDD `-0.8294`
- `market_context_high->equity_1h` score `0.4822` n `194` status `ready` deltaP `8.7614` edge `0.0783` maxDD `-5.0555`
- `market_context_high->index_24h` score `0.3208` n `153` status `ready` deltaP `20.8231` edge `0.0658` maxDD `-7.413`
- `market_context_high->crypto_alt_1h` score `0.288` n `194` status `ready` deltaP `3.4431` edge `0.0972` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.1857` n `194` status `ready` deltaP `5.5389` edge `0.1031` maxDD `-6.9639`
- `market_context_high->index_1h` score `0.0454` n `194` status `ready` deltaP `6.3677` edge `0.0117` maxDD `-1.0296`
- `market_context_high->unknown_4h` score `-0.1777` n `192` status `ready` deltaP `11.687` edge `0.0095` maxDD `-5.5109`
- `market_context_high->metal_1h` score `-0.3187` n `194` status `ready` deltaP `2.6946` edge `0.0087` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.4194` n `194` status `ready` deltaP `-0.6327` edge `-0.0006` maxDD `-0.5823`
- `market_context_high->index_4h` score `-0.4899` n `192` status `ready` deltaP `4.2048` edge `0.0209` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.6555` n `192` status `ready` deltaP `2.3374` edge `0.0033` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.4335` n `194` status `ready` deltaP `-3.1761` edge `-0.0065` maxDD `-3.3428`
- `market_context_high->metal_4h` score `-2.2635` n `192` status `ready` deltaP `-6.9741` edge `-0.0107` maxDD `-11.9729`
- `market_context_high->crypto_alt_24h` score `-2.9694` n `153` status `ready` deltaP `13.3476` edge `0.3713` maxDD `-53.6115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
