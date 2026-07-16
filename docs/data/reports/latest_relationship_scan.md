# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T04:37:24.164554+00:00`
- Price records: `672`
- Market context records: `6885`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11798`

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

- `market_context_high->unknown_24h` score `0.5355` n `184` status `ready` deltaP `-5.0655` edge `0.4874` maxDD `-13.1312`
- `market_context_high->fx_1h` score `-0.2394` n `224` status `ready` deltaP `2.3872` edge `0.0019` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.5254` n `224` status `ready` deltaP `2.3605` edge `0.0169` maxDD `-3.7803`
- `market_context_high->crypto_major_1h` score `-0.5478` n `224` status `ready` deltaP `4.1462` edge `0.0171` maxDD `-4.2314`
- `market_context_high->commodity_1h` score `-0.6205` n `224` status `ready` deltaP `-1.0479` edge `-0.0041` maxDD `-2.1443`
- `market_context_high->index_1h` score `-0.79` n `224` status `ready` deltaP `-1.1789` edge `-0.0023` maxDD `-2.2895`
- `market_context_high->fx_4h` score `-0.9007` n `224` status `ready` deltaP `12.6307` edge `0.0067` maxDD `-2.1765`
- `market_context_high->metal_1h` score `-0.9134` n `224` status `ready` deltaP `-4.892` edge `-0.0077` maxDD `-2.1427`
- `market_context_high->commodity_4h` score `-1.3146` n `224` status `ready` deltaP `-1.8838` edge `-0.007` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.5714` n `224` status `ready` deltaP `-2.8122` edge `-0.0221` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `-1.7273` n `184` status `ready` deltaP `1.5419` edge `0.0326` maxDD `-5.2791`
- `market_context_high->equity_1h` score `-1.8027` n `224` status `ready` deltaP `1.636` edge `-0.024` maxDD `-13.1084`
- `market_context_high->index_4h` score `-1.9938` n `224` status `ready` deltaP `3.7892` edge `-0.0229` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-2.381` n `224` status `ready` deltaP `0.49` edge `-0.0102` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-3.0758` n `224` status `ready` deltaP `-1.3066` edge `-0.0529` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.0899` n `224` status `ready` deltaP `0.0762` edge `-0.0383` maxDD `-20.6678`
- `market_context_high->unknown_4h` score `-3.1869` n `224` status `ready` deltaP `-9.6472` edge `0.0353` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.2697` n `184` status `ready` deltaP `-6.8674` edge `-0.0064` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.3496` n `224` status `ready` deltaP `1.3393` edge `-0.1567` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-8.6773` n `184` status `ready` deltaP `-15.4218` edge `-0.1511` maxDD `-28.352`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
