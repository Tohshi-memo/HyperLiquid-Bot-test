# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T10:52:26.108587+00:00`
- Price records: `672`
- Market context records: `6911`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11684`

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

- `market_context_high->unknown_24h` score `-0.0495` n `195` status `ready` deltaP `-5.6944` edge `0.4325` maxDD `-14.4045`
- `market_context_high->fx_1h` score `-0.1615` n `224` status `ready` deltaP `3.7345` edge `0.0029` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.4031` n `224` status `ready` deltaP `2.8096` edge `0.0241` maxDD `-3.7803`
- `market_context_high->crypto_major_1h` score `-0.4711` n `224` status `ready` deltaP `4.4456` edge `0.0215` maxDD `-4.2314`
- `market_context_high->commodity_1h` score `-0.6206` n `224` status `ready` deltaP `-0.8982` edge `-0.0051` maxDD `-2.1443`
- `market_context_high->fx_4h` score `-0.722` n `224` status `ready` deltaP `15.527` edge `0.0103` maxDD `-2.1765`
- `market_context_high->index_1h` score `-0.7643` n `224` status `ready` deltaP `-0.7298` edge `-0.002` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.8191` n `224` status `ready` deltaP `-3.5447` edge `-0.0046` maxDD `-2.1427`
- `market_context_high->commodity_4h` score `-1.3081` n `224` status `ready` deltaP `-1.5789` edge `-0.0082` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.5426` n `224` status `ready` deltaP `-2.6625` edge `-0.0207` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.7076` n `224` status `ready` deltaP `2.6839` edge `-0.0188` maxDD `-13.1084`
- `market_context_high->index_4h` score `-1.8745` n `224` status `ready` deltaP `5.6185` edge `-0.0198` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-2.1535` n `224` status `ready` deltaP `2.929` edge `0.0027` maxDD `-5.5324`
- `market_context_high->commodity_24h` score `-2.6315` n `195` status `ready` deltaP `-1.7056` edge `-0.0211` maxDD `-5.2791`
- `market_context_high->crypto_alt_4h` score `-2.7028` n `224` status `ready` deltaP `2.2104` edge `-0.0029` maxDD `-20.6678`
- `market_context_high->crypto_major_4h` score `-2.8041` n `224` status `ready` deltaP `-0.0871` edge `-0.0262` maxDD `-16.9508`
- `market_context_high->unknown_4h` score `-2.9719` n `224` status `ready` deltaP `-7.6655` edge `0.04` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.1053` n `195` status `ready` deltaP `-4.9016` edge `-0.0058` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.0643` n `224` status `ready` deltaP `3.0161` edge `-0.1313` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-8.2577` n `195` status `ready` deltaP `-12.5796` edge `-0.1156` maxDD `-28.4043`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
