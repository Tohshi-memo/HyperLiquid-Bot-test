# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T04:07:19.664850+00:00`
- Price records: `672`
- Market context records: `1910`
- Flow alert records: `7397`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4518`

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

- `market_context_high->crypto_alt_4h` score `7.8264` n `199` status `ready` deltaP `24.4906` edge `0.6034` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `7.2337` n `199` status `ready` deltaP `29.0867` edge `0.5335` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `3.9129` n `199` status `ready` deltaP `17.5006` edge `0.4118` maxDD `-9.8581`
- `market_context_high->equity_4h` score `2.6035` n `199` status `ready` deltaP `15.4967` edge `0.2231` maxDD `-5.0894`
- `market_context_high->metal_24h` score `1.6416` n `187` status `ready` deltaP `16.0196` edge `0.2726` maxDD `-12.7414`
- `market_context_high->unknown_24h` score `1.3731` n `187` status `ready` deltaP `13.1796` edge `0.5586` maxDD `-35.8966`
- `market_context_high->index_24h` score `1.0162` n `187` status `ready` deltaP `7.7281` edge `0.156` maxDD `-4.1604`
- `market_context_high->crypto_major_1h` score `0.7368` n `202` status `ready` deltaP `8.0127` edge `0.1066` maxDD `-3.2225`
- `market_context_high->index_4h` score `0.537` n `199` status `ready` deltaP `10.7029` edge `0.0823` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `0.5145` n `202` status `ready` deltaP `7.2064` edge `0.1062` maxDD `-4.9097`
- `market_context_high->fx_24h` score `0.1163` n `187` status `ready` deltaP `13.5751` edge `0.0241` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.0426` n `202` status `ready` deltaP `5.5241` edge `0.039` maxDD `-2.6836`
- `market_context_high->metal_1h` score `-0.5348` n `202` status `ready` deltaP `6.3319` edge `0.0228` maxDD `-6.3532`
- `market_context_high->equity_24h` score `-0.548` n `187` status `ready` deltaP `8.1866` edge `0.3896` maxDD `-33.1875`
- `market_context_high->fx_1h` score `-0.6265` n `202` status `ready` deltaP `-2.7287` edge `0.0011` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.6717` n `202` status `ready` deltaP `-0.3009` edge `0.0092` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.6904` n `199` status `ready` deltaP `11.9331` edge `0.1321` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-0.8138` n `199` status `ready` deltaP `-2.4474` edge `0.0008` maxDD `-1.1056`
- `market_context_high->unknown_1h` score `-0.9544` n `202` status `ready` deltaP `2.0484` edge `0.002` maxDD `-3.6151`
- `market_context_high->crypto_major_24h` score `-1.0765` n `187` status `ready` deltaP `16.0614` edge `0.6618` maxDD `-62.3533`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
