# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T15:37:23.844867+00:00`
- Price records: `672`
- Market context records: `1436`
- Flow alert records: `6047`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8796`

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

- `market_context_high->crypto_alt_24h` score `12.1865` n `154` status `ready` deltaP `28.7811` edge `1.0253` maxDD `-15.1306`
- `market_context_high->metal_24h` score `12.0704` n `154` status `ready` deltaP `13.377` edge `1.0834` maxDD `-6.3373`
- `market_context_high->crypto_major_24h` score `11.6516` n `154` status `ready` deltaP `27.3539` edge `0.9018` maxDD `-8.0553`
- `market_context_high->index_24h` score `4.0605` n `154` status `ready` deltaP `19.3813` edge `0.3178` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.3207` n `154` status `ready` deltaP `12.5271` edge `0.4259` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.2068` n `209` status `ready` deltaP `6.234` edge `0.142` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.1507` n `154` status `ready` deltaP `9.8801` edge `0.0516` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.1553` n `221` status `ready` deltaP `1.9914` edge `0.0338` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.2188` n `221` status `ready` deltaP `2.8762` edge `0.0091` maxDD `-1.7205`
- `market_context_high->commodity_1h` score `-0.6092` n `221` status `ready` deltaP `-0.3726` edge `0.0132` maxDD `-2.252`
- `market_context_high->crypto_alt_1h` score `-0.6877` n `221` status `ready` deltaP `1.7639` edge `0.0333` maxDD `-4.1892`
- `market_context_high->index_4h` score `-0.7026` n `209` status `ready` deltaP `-0.5025` edge `0.0537` maxDD `-3.7119`
- `market_context_high->fx_1h` score `-0.7235` n `221` status `ready` deltaP `0.8454` edge `-0.0027` maxDD `-0.3914`
- `market_context_high->metal_1h` score `-0.8886` n `221` status `ready` deltaP `4.1794` edge `-0.0082` maxDD `-6.3532`
- `market_context_high->crypto_alt_4h` score `-1.0812` n `209` status `ready` deltaP `8.6482` edge `0.1842` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-1.2806` n `209` status `ready` deltaP `4.9306` edge `0.1313` maxDD `-13.3376`
- `market_context_high->fx_4h` score `-1.6212` n `209` status `ready` deltaP `-4.2661` edge `-0.0096` maxDD `-1.4313`
- `market_context_high->crypto_major_1h` score `-1.6482` n `221` status `ready` deltaP `-0.9544` edge `0.0047` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.7336` n `209` status `ready` deltaP `5.2398` edge `0.012` maxDD `-12.5349`
- `market_context_high->commodity_4h` score `-4.0711` n `209` status `ready` deltaP `-10.0034` edge `-0.0179` maxDD `-8.04`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
