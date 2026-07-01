# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T01:07:27.395223+00:00`
- Price records: `672`
- Market context records: `5304`
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

- `market_context_high->unknown_24h` score `20.8765` n `153` status `ready` deltaP `24.7345` edge `1.5838` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `7.5704` n `153` status `ready` deltaP `25.7353` edge `0.8743` maxDD `-26.5332`
- `market_context_high->equity_24h` score `5.1206` n `153` status `ready` deltaP `19.9653` edge `0.8565` maxDD `-40.0306`
- `market_context_high->crypto_alt_4h` score `3.5171` n `190` status `ready` deltaP `13.466` edge `0.3674` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.3603` n `190` status `ready` deltaP `13.8254` edge `0.4171` maxDD `-14.0065`
- `market_context_high->equity_4h` score `1.884` n `190` status `ready` deltaP `11.0349` edge `0.2473` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.5409` n `153` status `ready` deltaP `13.3068` edge `0.0459` maxDD `-0.8294`
- `market_context_high->index_24h` score `0.313` n `153` status `ready` deltaP `20.8231` edge `0.0648` maxDD `-7.413`
- `market_context_high->equity_1h` score `0.2974` n `194` status `ready` deltaP `8.462` edge `0.0649` maxDD `-5.0555`
- `market_context_high->crypto_alt_1h` score `0.2796` n `194` status `ready` deltaP `3.4431` edge `0.0965` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.1905` n `194` status `ready` deltaP `5.5389` edge `0.1035` maxDD `-6.9639`
- `market_context_high->unknown_4h` score `0.086` n `190` status `ready` deltaP `12.4326` edge `0.0265` maxDD `-5.5109`
- `market_context_high->index_1h` score `0.0274` n `194` status `ready` deltaP `6.218` edge `0.0112` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.3202` n `194` status `ready` deltaP `2.6946` edge `0.0085` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.4186` n `194` status `ready` deltaP `-0.6327` edge `-0.0005` maxDD `-0.5823`
- `market_context_high->index_4h` score `-0.4635` n `190` status `ready` deltaP `4.4865` edge `0.0224` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.6826` n `190` status `ready` deltaP `1.9207` edge `0.0026` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.4323` n `194` status `ready` deltaP `-3.1761` edge `-0.0064` maxDD `-3.3428`
- `market_context_high->metal_4h` score `-2.1671` n `190` status `ready` deltaP `-6.5629` edge `-0.0086` maxDD `-11.3713`
- `market_context_high->crypto_alt_24h` score `-2.953` n `153` status `ready` deltaP `13.3476` edge `0.3734` maxDD `-53.6115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
