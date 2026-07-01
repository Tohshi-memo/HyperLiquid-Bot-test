# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T14:37:36.688512+00:00`
- Price records: `672`
- Market context records: `5361`
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

- `market_context_high->unknown_24h` score `11.7993` n `169` status `ready` deltaP `17.0386` edge `0.8827` maxDD `-0.3748`
- `market_context_high->crypto_major_24h` score `5.0647` n `169` status `ready` deltaP `22.0332` edge `0.7292` maxDD `-29.6555`
- `market_context_high->equity_24h` score `3.8019` n `169` status `ready` deltaP `16.2907` edge `0.7711` maxDD `-40.0306`
- `market_context_high->crypto_major_4h` score `2.1623` n `194` status `ready` deltaP `12.7263` edge `0.3246` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `1.7672` n `194` status `ready` deltaP `9.2925` edge `0.2494` maxDD `-9.46`
- `market_context_high->equity_4h` score `1.5596` n `194` status `ready` deltaP `9.635` edge `0.2296` maxDD `-7.4425`
- `market_context_high->index_24h` score `0.6065` n `169` status `ready` deltaP `18.976` edge `0.1044` maxDD `-9.0959`
- `market_context_high->fx_24h` score `0.1743` n `169` status `ready` deltaP `10.1044` edge `0.0367` maxDD `-0.8294`
- `market_context_high->equity_1h` score `0.1647` n `205` status `ready` deltaP `6.2626` edge `0.0685` maxDD `-5.0555`
- `market_context_high->crypto_major_1h` score `0.1209` n `205` status `ready` deltaP `4.6239` edge `0.1038` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `0.078` n `205` status `ready` deltaP `2.2287` edge `0.0878` maxDD `-5.0257`
- `market_context_high->index_1h` score `-0.0978` n `205` status `ready` deltaP `4.3786` edge `0.012` maxDD `-0.9472`
- `market_context_high->fx_1h` score `-0.4664` n `205` status `ready` deltaP `-1.4028` edge `-0.0015` maxDD `-0.5823`
- `market_context_high->index_4h` score `-0.5481` n `194` status `ready` deltaP `5.9388` edge `0.0277` maxDD `-2.704`
- `market_context_high->metal_1h` score `-0.5825` n `205` status `ready` deltaP `1.0311` edge `0.0121` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.6486` n `194` status `ready` deltaP `2.4406` edge `0.0035` maxDD `-1.567`
- `market_context_high->unknown_4h` score `-1.2835` n `194` status `ready` deltaP `7.6031` edge `-0.0392` maxDD `-6.1421`
- `market_context_high->commodity_1h` score `-1.5705` n `205` status `ready` deltaP `-4.2186` edge `-0.0083` maxDD `-3.5563`
- `market_context_high->metal_4h` score `-2.8446` n `194` status `ready` deltaP `-8.9012` edge `-0.0529` maxDD `-12.8631`
- `market_context_high->crypto_alt_24h` score `-3.7618` n `169` status `ready` deltaP `12.1404` edge `0.3065` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
