# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T23:22:24.402020+00:00`
- Price records: `672`
- Market context records: `6653`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11766`

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

- `market_context_high->unknown_1h` score `2.4134` n `202` status `ready` deltaP `-5.112` edge `0.3253` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `1.0066` n `199` status `ready` deltaP `11.7013` edge `0.1927` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `0.1122` n `202` status `ready` deltaP `8.7612` edge `0.0503` maxDD `-4.2122`
- `market_context_high->unknown_24h` score `0.0828` n `199` status `ready` deltaP `-3.2498` edge `0.3899` maxDD `-11.9426`
- `market_context_high->crypto_alt_1h` score `-0.0217` n `202` status `ready` deltaP `6.3319` edge `0.0449` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.2271` n `202` status `ready` deltaP `3.1215` edge `0.0008` maxDD `-0.7249`
- `market_context_high->index_1h` score `-0.4813` n `202` status `ready` deltaP `0.7144` edge `0.0053` maxDD `-0.7417`
- `market_context_high->unknown_4h` score `-0.5789` n `202` status `ready` deltaP `-15.1156` edge `0.2931` maxDD `-10.5788`
- `market_context_high->commodity_1h` score `-0.6743` n `202` status `ready` deltaP `-1.371` edge `-0.009` maxDD `-2.1314`
- `market_context_high->index_4h` score `-0.7574` n `202` status `ready` deltaP `11.5009` edge `0.0142` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-0.8388` n `202` status `ready` deltaP `3.3156` edge `0.0107` maxDD `-3.8827`
- `market_context_high->crypto_major_4h` score `-0.9576` n `202` status `ready` deltaP `11.4269` edge `0.1325` maxDD `-16.8495`
- `market_context_high->metal_1h` score `-1.1541` n `202` status `ready` deltaP `-3.4876` edge `0.0012` maxDD `-1.5966`
- `market_context_high->crypto_alt_4h` score `-1.2709` n `202` status `ready` deltaP `8.7222` edge `0.1191` maxDD `-19.2145`
- `market_context_high->fx_4h` score `-1.4368` n `202` status `ready` deltaP `5.4908` edge `0.0004` maxDD `-3.3635`
- `market_context_high->commodity_4h` score `-1.4395` n `202` status `ready` deltaP `-1.3765` edge `-0.0259` maxDD `-5.6246`
- `market_context_high->metal_4h` score `-1.947` n `202` status `ready` deltaP `0.7697` edge `0.0313` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-4.357` n `202` status `ready` deltaP `8.9139` edge `0.0044` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-6.306` n `199` status `ready` deltaP `-11.7342` edge `-0.0092` maxDD `-10.7124`
- `market_context_high->metal_24h` score `-6.4973` n `199` status `ready` deltaP `-4.1053` edge `0.0146` maxDD `-26.9513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
