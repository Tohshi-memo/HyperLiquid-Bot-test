# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T02:22:33.809009+00:00`
- Price records: `672`
- Market context records: `5309`
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

- `market_context_high->unknown_24h` score `19.9754` n `153` status `ready` deltaP `23.8664` edge `1.5145` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `7.4732` n `153` status `ready` deltaP `25.7353` edge `0.8662` maxDD `-26.5332`
- `market_context_high->equity_24h` score `5.2453` n `153` status `ready` deltaP `19.6181` edge `0.8692` maxDD `-40.0306`
- `market_context_high->crypto_alt_4h` score `3.3231` n `194` status `ready` deltaP `12.6461` edge `0.3567` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.2337` n `194` status `ready` deltaP `13.4885` edge `0.4088` maxDD `-14.0065`
- `market_context_high->equity_4h` score `1.8942` n `194` status `ready` deltaP `10.3972` edge `0.2524` maxDD `-7.4425`
- `market_context_high->equity_1h` score `0.5542` n `194` status `ready` deltaP `8.9111` edge `0.0833` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.5361` n `153` status `ready` deltaP `13.3068` edge `0.0455` maxDD `-0.8294`
- `market_context_high->index_24h` score `0.3462` n `153` status `ready` deltaP `20.9967` edge `0.0679` maxDD `-7.413`
- `market_context_high->crypto_alt_1h` score `0.222` n `194` status `ready` deltaP `3.1437` edge `0.0937` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.0886` n `194` status `ready` deltaP `5.0898` edge `0.098` maxDD `-6.9639`
- `market_context_high->index_1h` score `0.0406` n `194` status `ready` deltaP `6.3677` edge `0.0113` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.3171` n `194` status `ready` deltaP `2.6946` edge `0.0089` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.4116` n `194` status `ready` deltaP `-0.483` edge `-0.0006` maxDD `-0.5823`
- `market_context_high->index_4h` score `-0.5568` n `194` status `ready` deltaP `3.7826` edge `0.0193` maxDD `-2.9391`
- `market_context_high->unknown_4h` score `-0.5724` n `194` status `ready` deltaP `10.9568` edge `-0.0025` maxDD `-6.126`
- `market_context_high->fx_4h` score `-0.6296` n `194` status `ready` deltaP `2.7454` edge `0.0039` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.4359` n `194` status `ready` deltaP `-3.1761` edge `-0.0067` maxDD `-3.3428`
- `market_context_high->metal_4h` score `-2.4297` n `194` status `ready` deltaP `-7.0719` edge `-0.0119` maxDD `-12.8631`
- `market_context_high->crypto_alt_24h` score `-3.01` n `153` status `ready` deltaP `13.3476` edge `0.3661` maxDD `-53.6115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
