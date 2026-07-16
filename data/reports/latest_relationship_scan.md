# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T04:07:29.888547+00:00`
- Price records: `672`
- Market context records: `6882`
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

- `market_context_high->unknown_24h` score `0.7002` n `182` status `ready` deltaP `-4.5041` edge `0.5003` maxDD `-12.7737`
- `market_context_high->fx_1h` score `-0.2401` n `224` status `ready` deltaP `2.3872` edge `0.0018` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.5686` n `224` status `ready` deltaP `2.0611` edge `0.0153` maxDD `-3.7803`
- `market_context_high->crypto_major_1h` score `-0.5874` n `224` status `ready` deltaP `3.8468` edge `0.0158` maxDD `-4.2314`
- `market_context_high->commodity_1h` score `-0.6128` n `224` status `ready` deltaP `-0.8982` edge `-0.0041` maxDD `-2.1443`
- `market_context_high->index_1h` score `-0.7985` n `224` status `ready` deltaP `-1.3286` edge `-0.0024` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.9032` n `224` status `ready` deltaP `-4.7423` edge `-0.0074` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-0.9181` n `224` status `ready` deltaP `12.3258` edge `0.0065` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.3328` n `224` status `ready` deltaP `-2.1886` edge `-0.0073` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.5762` n `224` status `ready` deltaP `-2.8122` edge `-0.0225` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `-1.597` n `182` status `ready` deltaP `2.2406` edge `0.0388` maxDD `-5.2791`
- `market_context_high->equity_1h` score `-1.8276` n `224` status `ready` deltaP `1.3366` edge `-0.0252` maxDD `-13.1084`
- `market_context_high->index_4h` score `-1.9914` n `224` status `ready` deltaP `3.7892` edge `-0.0226` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-2.381` n `224` status `ready` deltaP `0.49` edge `-0.0102` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-3.0758` n `224` status `ready` deltaP `-1.3066` edge `-0.0529` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.1033` n `224` status `ready` deltaP `-0.0762` edge `-0.039` maxDD `-20.6678`
- `market_context_high->unknown_4h` score `-3.1845` n `224` status `ready` deltaP `-9.6472` edge `0.0355` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.3427` n `182` status `ready` deltaP `-7.5542` edge `-0.0079` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.3434` n `224` status `ready` deltaP `1.3393` edge `-0.1559` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-8.7442` n `182` status `ready` deltaP `-16.1683` edge `-0.1547` maxDD `-28.352`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
