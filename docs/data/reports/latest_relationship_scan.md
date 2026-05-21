# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T08:52:21.090166+00:00`
- Price records: `672`
- Market context records: `1408`
- Flow alert records: `5965`
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

- `market_context_high->crypto_major_24h` score `12.1044` n `156` status `ready` deltaP `27.4038` edge `0.9392` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `11.4877` n `156` status `ready` deltaP `28.8061` edge `0.9669` maxDD `-15.1306`
- `market_context_high->metal_24h` score `11.1702` n `156` status `ready` deltaP `10.5101` edge `1.0275` maxDD `-6.3373`
- `market_context_high->index_24h` score `3.7878` n `156` status `ready` deltaP `19.4978` edge `0.2943` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.2574` n `156` status `ready` deltaP `12.6603` edge `0.3364` maxDD `-14.2815`
- `market_context_high->equity_4h` score `0.9274` n `202` status `ready` deltaP `5.847` edge `0.1213` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.065` n `156` status `ready` deltaP `9.7088` edge `0.0456` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.1248` n `204` status `ready` deltaP `3.9011` edge `0.0101` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.2166` n `204` status `ready` deltaP `2.2954` edge `0.0225` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.2346` n `204` status `ready` deltaP `4.2767` edge `-0.0015` maxDD `-0.3914`
- `market_context_high->commodity_1h` score `-0.7421` n `204` status `ready` deltaP `-0.9393` edge `0.0059` maxDD `-2.252`
- `market_context_high->crypto_alt_1h` score `-0.7538` n `204` status `ready` deltaP `0.411` edge `0.0215` maxDD `-3.6309`
- `market_context_high->metal_1h` score `-0.7567` n `204` status `ready` deltaP `4.4822` edge `-0.0094` maxDD `-5.0663`
- `market_context_high->index_4h` score `-0.8912` n `202` status `ready` deltaP `-1.6149` edge `0.0454` maxDD `-3.7119`
- `market_context_high->crypto_major_4h` score `-1.4791` n `202` status `ready` deltaP `4.9097` edge `0.1149` maxDD `-13.3376`
- `market_context_high->crypto_alt_4h` score `-1.5555` n `202` status `ready` deltaP `6.0492` edge `0.162` maxDD `-19.5565`
- `market_context_high->fx_4h` score `-1.5556` n `202` status `ready` deltaP `-3.5061` edge `-0.0092` maxDD `-1.4313`
- `market_context_high->crypto_major_1h` score `-1.6096` n `204` status `ready` deltaP `-2.4216` edge `-0.0073` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-2.7335` n `202` status `ready` deltaP `4.5686` edge `-0.0033` maxDD `-11.7291`
- `market_context_high->commodity_4h` score `-3.9951` n `202` status `ready` deltaP `-10.0141` edge `-0.0115` maxDD `-8.04`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
