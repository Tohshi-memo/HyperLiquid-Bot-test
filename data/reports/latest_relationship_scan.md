# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T23:52:27.189185+00:00`
- Price records: `672`
- Market context records: `6865`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11810`

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

- `market_context_high->unknown_24h` score `1.1979` n `176` status `ready` deltaP `-1.8001` edge `0.5408` maxDD `-12.3511`
- `market_context_high->fx_1h` score `-0.2487` n `224` status `ready` deltaP `2.2375` edge `0.0017` maxDD `-0.5468`
- `market_context_high->commodity_1h` score `-0.6291` n `224` status `ready` deltaP `-1.1976` edge `-0.0042` maxDD `-2.1443`
- `market_context_high->crypto_alt_1h` score `-0.6512` n `224` status `ready` deltaP `1.3126` edge `0.0134` maxDD `-3.7803`
- `market_context_high->crypto_major_1h` score `-0.6856` n `224` status `ready` deltaP `3.0983` edge `0.0126` maxDD `-4.2314`
- `market_context_high->index_1h` score `-0.8678` n `224` status `ready` deltaP `-2.5262` edge `-0.0033` maxDD `-2.2895`
- `market_context_high->commodity_24h` score `-0.8864` n `176` status `ready` deltaP `4.7789` edge `0.0811` maxDD `-5.2791`
- `market_context_high->metal_1h` score `-0.957` n `224` status `ready` deltaP `-5.6405` edge `-0.0083` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-0.9835` n `223` status `ready` deltaP `11.1282` edge `0.0061` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.3298` n `223` status `ready` deltaP `-2.1759` edge `-0.007` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.6793` n `224` status `ready` deltaP `-3.5607` edge `-0.0261` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.9312` n `224` status `ready` deltaP `0.139` edge `-0.0305` maxDD `-13.1084`
- `market_context_high->index_4h` score `-2.0433` n `223` status `ready` deltaP `3.0612` edge `-0.0244` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-2.4585` n `223` status `ready` deltaP `-0.6259` edge `-0.0127` maxDD `-5.5324`
- `market_context_high->unknown_4h` score `-3.145` n `223` status `ready` deltaP `-9.2737` edge `0.0363` maxDD `-10.2579`
- `market_context_high->crypto_major_4h` score `-3.1532` n `223` status `ready` deltaP `-1.8961` edge `-0.0589` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.203` n `223` status `ready` deltaP `-0.9747` edge `-0.0458` maxDD `-20.6678`
- `market_context_high->fx_24h` score `-4.5541` n `176` status `ready` deltaP `-9.8816` edge `-0.01` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.5322` n `223` status `ready` deltaP `0.1235` edge `-0.172` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-8.996` n `176` status `ready` deltaP `-18.9332` edge `-0.1786` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
