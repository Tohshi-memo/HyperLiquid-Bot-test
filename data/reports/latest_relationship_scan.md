# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T20:37:27.132168+00:00`
- Price records: `672`
- Market context records: `6852`
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

- `market_context_high->unknown_24h` score `1.1027` n `176` status `ready` deltaP `-1.5467` edge `0.5269` maxDD `-12.3511`
- `market_context_high->fx_1h` score `-0.2445` n `223` status `ready` deltaP `2.3187` edge `0.0017` maxDD `-0.5468`
- `market_context_high->commodity_24h` score `-0.4312` n `176` status `ready` deltaP `6.9287` edge `0.1047` maxDD `-5.2791`
- `market_context_high->crypto_alt_1h` score `-0.5809` n `223` status `ready` deltaP `1.8622` edge `0.0156` maxDD `-3.7803`
- `market_context_high->crypto_major_1h` score `-0.6046` n `223` status `ready` deltaP `3.8056` edge `0.0144` maxDD `-4.2122`
- `market_context_high->commodity_1h` score `-0.6899` n `223` status `ready` deltaP `-2.171` edge `-0.0055` maxDD `-2.1443`
- `market_context_high->index_1h` score `-0.8896` n `223` status `ready` deltaP `-2.9148` edge `-0.0035` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.9565` n `223` status `ready` deltaP `-5.602` edge `-0.0085` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-1.0024` n `216` status `ready` deltaP `10.7498` edge `0.0062` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.4682` n `216` status `ready` deltaP `-3.9521` edge `-0.0129` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.631` n `223` status `ready` deltaP `-2.7618` edge `-0.0274` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.9955` n `223` status `ready` deltaP `-0.527` edge `-0.0343` maxDD `-13.1084`
- `market_context_high->index_4h` score `-2.0838` n `216` status `ready` deltaP `2.5237` edge `-0.026` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-2.4894` n `216` status `ready` deltaP `-1.0106` edge `-0.0141` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-3.0329` n `216` status `ready` deltaP `-0.542` edge `-0.0525` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.1638` n `216` status `ready` deltaP `-0.5646` edge `-0.0435` maxDD `-20.6678`
- `market_context_high->unknown_4h` score `-3.201` n `216` status `ready` deltaP `-9.3439` edge `0.0321` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.4984` n `176` status `ready` deltaP `-9.7853` edge `-0.006` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.6728` n `216` status `ready` deltaP `-0.4347` edge `-0.1863` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-9.0913` n `176` status `ready` deltaP `-18.8447` edge `-0.1914` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
