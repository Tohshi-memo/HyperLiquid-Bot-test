# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T08:37:15.631382+00:00`
- Price records: `672`
- Market context records: `1407`
- Flow alert records: `5962`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8785`

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

- `market_context_high->crypto_major_24h` score `12.168` n `156` status `ready` deltaP `27.4038` edge `0.9445` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `11.4877` n `156` status `ready` deltaP `28.8061` edge `0.9669` maxDD `-15.1306`
- `market_context_high->metal_24h` score `11.1726` n `156` status `ready` deltaP `10.5101` edge `1.0277` maxDD `-6.3373`
- `market_context_high->index_24h` score `3.7914` n `156` status `ready` deltaP `19.4978` edge `0.2946` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.249` n `156` status `ready` deltaP `12.6603` edge `0.3357` maxDD `-14.2815`
- `market_context_high->equity_4h` score `0.9839` n `201` status `ready` deltaP `6.2386` edge `0.1234` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.0638` n `156` status `ready` deltaP `9.7088` edge `0.0455` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.1056` n `204` status `ready` deltaP `4.0508` edge `0.0107` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.1914` n `204` status `ready` deltaP `2.4451` edge `0.0236` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.2214` n `204` status `ready` deltaP `4.4264` edge `-0.0014` maxDD `-0.3914`
- `market_context_high->metal_1h` score `-0.7403` n `204` status `ready` deltaP `4.6319` edge `-0.0083` maxDD `-5.0663`
- `market_context_high->crypto_alt_1h` score `-0.7538` n `204` status `ready` deltaP `0.411` edge `0.0215` maxDD `-3.6309`
- `market_context_high->commodity_1h` score `-0.7625` n `204` status `ready` deltaP `-1.089` edge `0.0052` maxDD `-2.252`
- `market_context_high->index_4h` score `-0.8494` n `201` status `ready` deltaP `-1.2726` edge `0.0466` maxDD `-3.7119`
- `market_context_high->crypto_major_4h` score `-1.4956` n `201` status `ready` deltaP `4.7029` edge `0.1149` maxDD `-13.3376`
- `market_context_high->fx_4h` score `-1.5345` n `201` status `ready` deltaP `-3.2573` edge `-0.0091` maxDD `-1.4313`
- `market_context_high->crypto_alt_4h` score `-1.5713` n `201` status `ready` deltaP `5.867` edge `0.1619` maxDD `-19.5565`
- `market_context_high->crypto_major_1h` score `-1.5952` n `204` status `ready` deltaP `-2.2719` edge `-0.0071` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-2.6176` n `201` status `ready` deltaP `4.8469` edge `-0.0018` maxDD `-11.5581`
- `market_context_high->commodity_4h` score `-3.9932` n `201` status `ready` deltaP `-9.9745` edge `-0.0116` maxDD `-8.04`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
