# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T22:22:27.299717+00:00`
- Price records: `672`
- Market context records: `5394`
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

- `market_context_high->crypto_major_24h` score `5.3603` n `194` status `ready` deltaP `22.7126` edge `0.7493` maxDD `-29.6555`
- `market_context_high->unknown_24h` score `4.7543` n `194` status `ready` deltaP `17.0569` edge `0.2955` maxDD `-0.3748`
- `market_context_high->crypto_major_4h` score `3.5505` n `205` status `ready` deltaP `15.2439` edge `0.4235` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `3.0182` n `205` status `ready` deltaP `12.2256` edge `0.3341` maxDD `-9.46`
- `market_context_high->equity_4h` score `2.3391` n `205` status `ready` deltaP `11.1281` edge `0.2846` maxDD `-7.4425`
- `market_context_high->equity_1h` score `0.4153` n `205` status `ready` deltaP `7.4602` edge `0.0814` maxDD `-5.0555`
- `market_context_high->equity_24h` score `0.1804` n `194` status `ready` deltaP `8.0327` edge `0.5452` maxDD `-40.0306`
- `market_context_high->index_1h` score `0.046` n `205` status `ready` deltaP `5.5762` edge `0.016` maxDD `-0.9472`
- `market_context_high->crypto_major_1h` score `0.0178` n `205` status `ready` deltaP `4.4742` edge `0.0962` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `-0.0275` n `205` status `ready` deltaP `2.079` edge `0.08` maxDD `-5.0257`
- `market_context_high->fx_24h` score `-0.1719` n `194` status `ready` deltaP `6.991` edge `0.0286` maxDD `-0.8294`
- `market_context_high->metal_1h` score `-0.4603` n `205` status `ready` deltaP `2.2287` edge `0.0143` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.4828` n `205` status `ready` deltaP `-1.7022` edge `-0.0016` maxDD `-0.5823`
- `market_context_high->unknown_4h` score `-0.6691` n `205` status `ready` deltaP `7.378` edge `0.0135` maxDD `-6.1421`
- `market_context_high->index_4h` score `-1.0333` n `205` status `ready` deltaP `5.7926` edge `0.0362` maxDD `-2.874`
- `market_context_high->fx_4h` score `-1.1975` n `205` status `ready` deltaP `0.2439` edge `0.0015` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.519` n `205` status `ready` deltaP `-3.7695` edge `-0.007` maxDD `-3.5563`
- `market_context_high->index_24h` score `-1.7087` n `194` status `ready` deltaP `12.8275` edge `0.0707` maxDD `-12.5551`
- `market_context_high->metal_4h` score `-2.4378` n `205` status `ready` deltaP `-5.4573` edge `-0.0237` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.3192` n `205` status `ready` deltaP `-7.5914` edge `-0.0455` maxDD `-14.1062`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
