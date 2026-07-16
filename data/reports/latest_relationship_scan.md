# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T02:52:23.845254+00:00`
- Price records: `672`
- Market context records: `6877`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11796`

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

- `market_context_high->unknown_24h` score `1.0403` n `177` status `ready` deltaP `-3.4368` edge `0.5315` maxDD `-12.3511`
- `market_context_high->fx_1h` score `-0.2479` n `224` status `ready` deltaP `2.2375` edge `0.0018` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.6009` n `224` status `ready` deltaP `1.7617` edge `0.0146` maxDD `-3.7803`
- `market_context_high->crypto_major_1h` score `-0.6077` n `224` status `ready` deltaP `3.6971` edge `0.0151` maxDD `-4.2314`
- `market_context_high->commodity_1h` score `-0.6143` n `224` status `ready` deltaP `-0.8982` edge `-0.0043` maxDD `-2.1443`
- `market_context_high->index_1h` score `-0.8141` n `224` status `ready` deltaP `-1.628` edge `-0.0024` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.8838` n `224` status `ready` deltaP `-4.4429` edge `-0.0069` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-0.96` n `224` status `ready` deltaP `11.5636` edge `0.0062` maxDD `-2.1765`
- `market_context_high->commodity_24h` score `-1.2465` n `177` status `ready` deltaP `4.0566` edge `0.0559` maxDD `-5.2791`
- `market_context_high->commodity_4h` score `-1.3462` n `224` status `ready` deltaP `-2.3411` edge `-0.008` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.6242` n `224` status `ready` deltaP `-3.1116` edge `-0.0245` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.8572` n `224` status `ready` deltaP `1.0372` edge `-0.027` maxDD `-13.1084`
- `market_context_high->index_4h` score `-1.9804` n `224` status `ready` deltaP `3.9417` edge `-0.0222` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-2.3802` n `224` status `ready` deltaP `0.49` edge `-0.0101` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-3.0758` n `224` status `ready` deltaP `-1.3066` edge `-0.0529` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.097` n `224` status `ready` deltaP `-0.0762` edge `-0.0382` maxDD `-20.6678`
- `market_context_high->unknown_4h` score `-3.1965` n `224` status `ready` deltaP `-9.6472` edge `0.0345` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.5275` n `177` status `ready` deltaP `-9.3392` edge `-0.0114` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.3339` n `224` status `ready` deltaP `1.4917` edge `-0.1557` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-8.8623` n `177` status `ready` deltaP `-17.7168` edge `-0.1642` maxDD `-28.3109`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
