# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T23:07:29.774011+00:00`
- Price records: `672`
- Market context records: `6862`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11809`

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

- `market_context_high->unknown_24h` score `1.2093` n `176` status `ready` deltaP `-1.6268` edge `0.5411` maxDD `-12.3511`
- `market_context_high->fx_1h` score `-0.2457` n `224` status `ready` deltaP `2.3109` edge `0.0016` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.6447` n `224` status `ready` deltaP `1.394` edge `0.0134` maxDD `-3.7803`
- `market_context_high->commodity_1h` score `-0.657` n `224` status `ready` deltaP `-1.5695` edge `-0.0053` maxDD `-2.1443`
- `market_context_high->crypto_major_1h` score `-0.6959` n `224` status `ready` deltaP `3.0303` edge `0.0122` maxDD `-4.2314`
- `market_context_high->commodity_24h` score `-0.7752` n `176` status `ready` deltaP `5.2988` edge `0.0869` maxDD `-5.2791`
- `market_context_high->index_1h` score `-0.8469` n `224` status `ready` deltaP `-2.1534` edge `-0.0031` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.9408` n `224` status `ready` deltaP `-5.4199` edge `-0.0077` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-0.9914` n `223` status `ready` deltaP `10.976` edge `0.0061` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.3519` n `223` status `ready` deltaP `-2.4803` edge `-0.0078` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.6196` n `224` status `ready` deltaP `-3.1897` edge `-0.0236` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.9272` n `224` status `ready` deltaP `0.2162` edge `-0.0305` maxDD `-13.1084`
- `market_context_high->index_4h` score `-2.0433` n `223` status `ready` deltaP `3.0612` edge `-0.0244` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-2.449` n `223` status `ready` deltaP `-0.4737` edge `-0.0125` maxDD `-5.5324`
- `market_context_high->unknown_4h` score `-3.1062` n `223` status `ready` deltaP `-8.9693` edge `0.0375` maxDD `-10.2579`
- `market_context_high->crypto_major_4h` score `-3.1548` n `223` status `ready` deltaP `-1.8961` edge `-0.0591` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.2015` n `223` status `ready` deltaP `-0.9747` edge `-0.0456` maxDD `-20.6678`
- `market_context_high->fx_24h` score `-4.5433` n `176` status `ready` deltaP `-9.8816` edge `-0.0091` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.5613` n `223` status `ready` deltaP `-0.1809` edge `-0.1737` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-9.0132` n `176` status `ready` deltaP `-18.9332` edge `-0.1808` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
