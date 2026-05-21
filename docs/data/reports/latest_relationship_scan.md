# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T01:07:15.382902+00:00`
- Price records: `672`
- Market context records: `1375`
- Flow alert records: `5870`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8804`

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

- `market_context_high->crypto_major_24h` score `13.246` n `147` status `ready` deltaP `30.8284` edge `1.0115` maxDD `-8.0553`
- `market_context_high->metal_24h` score `12.0938` n `147` status `ready` deltaP `13.4744` edge `1.0847` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `10.8999` n `147` status `ready` deltaP `28.6884` edge `0.9187` maxDD `-15.1306`
- `market_context_high->index_24h` score `4.1516` n `147` status `ready` deltaP `21.8998` edge `0.3086` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.6821` n `147` status `ready` deltaP `14.9837` edge `0.3563` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.5798` n `172` status `ready` deltaP `8.9762` edge `0.1548` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.1022` n `147` status `ready` deltaP `9.0738` edge `0.0442` maxDD `-1.3605`
- `market_context_high->index_1h` score `-0.1028` n `184` status `ready` deltaP `3.6514` edge `0.0136` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.1071` n `172` status `ready` deltaP `10.9614` edge `0.0611` maxDD `-6.4478`
- `market_context_high->equity_1h` score `-0.1232` n `184` status `ready` deltaP `2.5482` edge `0.0286` maxDD `-2.8014`
- `market_context_high->index_4h` score `-0.3605` n `172` status `ready` deltaP `0.5212` edge `0.0592` maxDD `-3.7119`
- `market_context_high->metal_1h` score `-0.4179` n `184` status `ready` deltaP `6.2842` edge `0.0034` maxDD `-3.5762`
- `market_context_high->fx_1h` score `-0.4209` n `184` status `ready` deltaP `2.1576` edge `-0.0029` maxDD `-0.3914`
- `market_context_high->commodity_1h` score `-0.689` n `184` status `ready` deltaP `-0.2603` edge `0.0058` maxDD `-2.252`
- `market_context_high->crypto_alt_1h` score `-0.6958` n `184` status `ready` deltaP `0.4003` edge `0.0264` maxDD `-3.6309`
- `market_context_high->crypto_major_1h` score `-1.4248` n `184` status `ready` deltaP `-1.7573` edge `-0.0005` maxDD `-6.1883`
- `market_context_high->crypto_alt_4h` score `-1.5558` n `172` status `ready` deltaP `7.2462` edge `0.154` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-1.7234` n `172` status `ready` deltaP `3.46` edge `0.1042` maxDD `-13.3376`
- `market_context_high->fx_4h` score `-1.9989` n `172` status `ready` deltaP `-8.253` edge `-0.0145` maxDD `-1.4313`
- `market_context_high->unknown_4h` score `-3.1968` n `172` status `ready` deltaP `2.2759` edge `-0.1979` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
