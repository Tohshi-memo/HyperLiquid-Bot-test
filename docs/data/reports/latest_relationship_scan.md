# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T00:52:27.483477+00:00`
- Price records: `672`
- Market context records: `5405`
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

- `market_context_high->crypto_major_24h` score `4.703` n `194` status `ready` deltaP `20.9765` edge `0.7061` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `3.6305` n `205` status `ready` deltaP `15.8536` edge `0.4261` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `2.9141` n `205` status `ready` deltaP `11.4634` edge `0.3305` maxDD `-9.46`
- `market_context_high->equity_4h` score `2.3309` n `205` status `ready` deltaP `11.2805` edge `0.2829` maxDD `-7.4425`
- `market_context_high->equity_1h` score `0.4608` n `205` status `ready` deltaP `7.9093` edge `0.0822` maxDD `-5.0555`
- `market_context_high->crypto_major_1h` score `0.1916` n `205` status `ready` deltaP `5.2227` edge `0.1057` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `0.1331` n `205` status `ready` deltaP `2.9772` edge `0.0874` maxDD `-5.0257`
- `market_context_high->index_1h` score `0.0736` n `205` status `ready` deltaP `5.8756` edge `0.0163` maxDD `-0.9472`
- `market_context_high->equity_24h` score `0.04` n `194` status `ready` deltaP `8.0327` edge `0.5335` maxDD `-40.0306`
- `market_context_high->fx_24h` score `-0.1484` n `194` status `ready` deltaP `7.1646` edge `0.0294` maxDD `-0.8294`
- `market_context_high->fx_1h` score `-0.4555` n `205` status `ready` deltaP `-1.2531` edge `-0.0011` maxDD `-0.5823`
- `market_context_high->metal_1h` score `-0.5011` n `205` status `ready` deltaP `1.9293` edge `0.0129` maxDD `-2.0682`
- `market_context_high->index_4h` score `-0.9677` n `205` status `ready` deltaP `6.4024` edge `0.0376` maxDD `-2.874`
- `market_context_high->fx_4h` score `-1.1951` n `205` status `ready` deltaP `0.2439` edge `0.0017` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.4579` n `205` status `ready` deltaP `-3.021` edge `-0.0069` maxDD `-3.5563`
- `market_context_high->index_24h` score `-1.6283` n `194` status `ready` deltaP `12.8275` edge `0.0774` maxDD `-12.5551`
- `market_context_high->metal_4h` score `-2.47` n `205` status `ready` deltaP `-5.7622` edge `-0.0258` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.3276` n `205` status `ready` deltaP `-7.5914` edge `-0.0462` maxDD `-14.1062`
- `market_context_high->crypto_alt_24h` score `-5.3641` n `194` status `ready` deltaP `12.2405` edge `0.3411` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-6.9798` n `194` status `ready` deltaP `-4.4226` edge `-0.1276` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
