# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T15:07:26.374952+00:00`
- Price records: `672`
- Market context records: `4945`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9456`

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

- `market_context_high->unknown_1h` score `18.7645` n `97` status `ready` deltaP `9.9096` edge `1.5394` maxDD `-1.674`
- `market_context_high->unknown_4h` score `12.1918` n `94` status `ready` deltaP `28.2596` edge `0.879` maxDD `-1.7801`
- `market_context_high->crypto_major_4h` score `7.2305` n `94` status `ready` deltaP `20.829` edge `0.5861` maxDD `-7.1265`
- `market_context_high->crypto_alt_4h` score `7.0027` n `94` status `ready` deltaP `21.4323` edge `0.5759` maxDD `-7.8181`
- `market_context_high->unknown_24h` score `5.8369` n `90` status `ready` deltaP `26.9792` edge `0.3408` maxDD `-1.4072`
- `market_context_high->equity_4h` score `1.7591` n `94` status `ready` deltaP `14.5854` edge `0.1875` maxDD `-6.3852`
- `market_context_high->metal_4h` score `1.6475` n `94` status `ready` deltaP `12.633` edge `0.1193` maxDD `-1.9651`
- `market_context_high->index_4h` score `0.9737` n `94` status `ready` deltaP `12.4676` edge `0.0442` maxDD `-0.6938`
- `market_context_high->crypto_major_1h` score `0.838` n `97` status `ready` deltaP `8.6811` edge `0.1534` maxDD `-5.6406`
- `market_context_high->equity_1h` score `0.8281` n `97` status `ready` deltaP `7.5823` edge `0.0758` maxDD `-2.5875`
- `market_context_high->crypto_alt_1h` score `0.6511` n `97` status `ready` deltaP `9.5114` edge `0.1223` maxDD `-5.5126`
- `market_context_high->metal_1h` score `0.0757` n `97` status `ready` deltaP `4.2749` edge `0.0358` maxDD `-1.3057`
- `market_context_high->commodity_1h` score `-0.4096` n `97` status `ready` deltaP `0.9985` edge `0.0068` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.4203` n `97` status `ready` deltaP `1.3797` edge `0.0124` maxDD `-0.7054`
- `market_context_high->commodity_4h` score `-0.9677` n `94` status `ready` deltaP `6.4089` edge `-0.0047` maxDD `-4.4933`
- `market_context_high->fx_4h` score `-1.1207` n `94` status `ready` deltaP `-6.3797` edge `-0.0041` maxDD `-1.0967`
- `market_context_high->fx_24h` score `-1.4413` n `90` status `ready` deltaP `-0.9722` edge `-0.0126` maxDD `-2.749`
- `market_context_high->fx_1h` score `-1.5792` n `97` status `ready` deltaP `-9.7259` edge `-0.0055` maxDD `-0.5675`
- `market_context_high->commodity_24h` score `-4.1568` n `90` status `ready` deltaP `19.0625` edge `0.0374` maxDD `-27.5371`
- `market_context_high->metal_24h` score `-6.9488` n `90` status `ready` deltaP `-9.1319` edge `0.0273` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
