# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T01:07:28.216939+00:00`
- Price records: `672`
- Market context records: `5406`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11510`

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

- `market_context_high->crypto_major_24h` score `4.6303` n `194` status `ready` deltaP `20.8029` edge `0.7012` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `3.6811` n `205` status `ready` deltaP `16.0061` edge `0.4293` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `2.9515` n `205` status `ready` deltaP `11.6159` edge `0.3326` maxDD `-9.46`
- `market_context_high->equity_4h` score `2.3539` n `205` status `ready` deltaP `11.433` edge `0.2838` maxDD `-7.4425`
- `market_context_high->equity_1h` score `0.4584` n `205` status `ready` deltaP `7.9093` edge `0.082` maxDD `-5.0555`
- `market_context_high->crypto_major_1h` score `0.212` n `205` status `ready` deltaP `5.3724` edge `0.1064` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `0.1343` n `205` status `ready` deltaP `2.9772` edge `0.0875` maxDD `-5.0257`
- `market_context_high->index_1h` score `0.0736` n `205` status `ready` deltaP `5.8756` edge `0.0163` maxDD `-0.9472`
- `market_context_high->equity_24h` score `0.016` n `194` status `ready` deltaP `8.0327` edge `0.5315` maxDD `-40.0306`
- `market_context_high->fx_24h` score `-0.1322` n `194` status `ready` deltaP `7.3382` edge `0.0296` maxDD `-0.8294`
- `market_context_high->fx_1h` score `-0.4555` n `205` status `ready` deltaP `-1.2531` edge `-0.0011` maxDD `-0.5823`
- `market_context_high->metal_1h` score `-0.5227` n `205` status `ready` deltaP `1.7796` edge `0.0121` maxDD `-2.0682`
- `market_context_high->index_4h` score `-0.9519` n `205` status `ready` deltaP `6.5548` edge `0.0379` maxDD `-2.874`
- `market_context_high->fx_4h` score `-1.1963` n `205` status `ready` deltaP `0.2439` edge `0.0016` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.4591` n `205` status `ready` deltaP `-3.021` edge `-0.007` maxDD `-3.5563`
- `market_context_high->index_24h` score `-1.6223` n `194` status `ready` deltaP `12.8275` edge `0.0779` maxDD `-12.5551`
- `market_context_high->metal_4h` score `-2.4731` n `205` status `ready` deltaP `-5.7622` edge `-0.0262` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.3276` n `205` status `ready` deltaP `-7.5914` edge `-0.0462` maxDD `-14.1062`
- `market_context_high->crypto_alt_24h` score `-5.4464` n `194` status `ready` deltaP `12.0668` edge `0.3354` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-6.9853` n `194` status `ready` deltaP `-4.4226` edge `-0.1283` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
