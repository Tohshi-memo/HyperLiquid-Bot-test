# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T08:22:15.244095+00:00`
- Price records: `672`
- Market context records: `1405`
- Flow alert records: `5959`
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

- `market_context_high->crypto_major_24h` score `12.234` n `156` status `ready` deltaP `27.4038` edge `0.95` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `11.4865` n `156` status `ready` deltaP `28.8061` edge `0.9668` maxDD `-15.1306`
- `market_context_high->metal_24h` score `11.181` n `156` status `ready` deltaP `10.5101` edge `1.0284` maxDD `-6.3373`
- `market_context_high->index_24h` score `3.8022` n `156` status `ready` deltaP `19.4978` edge `0.2955` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.2466` n `156` status `ready` deltaP `12.6603` edge `0.3355` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.0058` n `200` status `ready` deltaP `6.2866` edge `0.1249` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.0638` n `156` status `ready` deltaP `9.7088` edge `0.0455` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.0828` n `204` status `ready` deltaP `4.2005` edge `0.0116` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.165` n `204` status `ready` deltaP `2.5948` edge `0.0248` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.2094` n `204` status `ready` deltaP `4.5761` edge `-0.0014` maxDD `-0.3914`
- `market_context_high->metal_1h` score `-0.7224` n `204` status `ready` deltaP `4.7816` edge `-0.007` maxDD `-5.0663`
- `market_context_high->crypto_alt_1h` score `-0.7502` n `204` status `ready` deltaP `0.411` edge `0.0218` maxDD `-3.6309`
- `market_context_high->commodity_1h` score `-0.7877` n `204` status `ready` deltaP `-1.2387` edge `0.0041` maxDD `-2.252`
- `market_context_high->index_4h` score `-0.8109` n `200` status `ready` deltaP `-0.9268` edge `0.0475` maxDD `-3.7119`
- `market_context_high->crypto_major_4h` score `-1.5231` n `200` status `ready` deltaP `4.4939` edge `0.114` maxDD `-13.3376`
- `market_context_high->fx_4h` score `-1.5688` n `200` status `ready` deltaP `-3.7012` edge `-0.009` maxDD `-1.4313`
- `market_context_high->crypto_major_1h` score `-1.5724` n `204` status `ready` deltaP `-2.1222` edge `-0.0062` maxDD `-6.1883`
- `market_context_high->crypto_alt_4h` score `-1.5992` n `200` status `ready` deltaP `5.6829` edge `0.1608` maxDD `-19.5565`
- `market_context_high->metal_4h` score `-2.5144` n `200` status `ready` deltaP `5.128` edge `-0.0004` maxDD `-11.4653`
- `market_context_high->commodity_4h` score `-4.0272` n `200` status `ready` deltaP `-10.2805` edge `-0.0124` maxDD `-8.04`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
