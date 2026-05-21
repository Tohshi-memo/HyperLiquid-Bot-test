# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T02:07:17.402825+00:00`
- Price records: `672`
- Market context records: `1379`
- Flow alert records: `5883`
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

- `market_context_high->crypto_major_24h` score `13.4753` n `151` status `ready` deltaP `30.26` edge `1.0344` maxDD `-8.0553`
- `market_context_high->metal_24h` score `12.0411` n `151` status `ready` deltaP `13.3565` edge `1.0811` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.3494` n `151` status `ready` deltaP `28.7424` edge `0.9558` maxDD `-15.1306`
- `market_context_high->index_24h` score `4.2506` n `151` status `ready` deltaP `21.4577` edge `0.3198` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.7816` n `151` status `ready` deltaP `14.5776` edge `0.3673` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.5857` n `176` status `ready` deltaP `8.8553` edge `0.1561` maxDD `-3.6396`
- `market_context_high->metal_4h` score `0.0288` n `176` status `ready` deltaP `11.6547` edge `0.0678` maxDD `-6.4478`
- `market_context_high->index_1h` score `-0.0357` n `188` status `ready` deltaP `4.1152` edge `0.0161` maxDD `-1.7205`
- `market_context_high->fx_24h` score `-0.0435` n `151` status `ready` deltaP `8.8173` edge `0.0425` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.0546` n `188` status `ready` deltaP `2.8506` edge `0.0323` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.3363` n `188` status `ready` deltaP `3.1405` edge `-0.0024` maxDD `-0.3914`
- `market_context_high->index_4h` score `-0.3577` n `176` status `ready` deltaP `0.6513` edge `0.0587` maxDD `-3.7119`
- `market_context_high->metal_1h` score `-0.5249` n `188` status `ready` deltaP `6.6792` edge `0.0106` maxDD `-3.5762`
- `market_context_high->crypto_alt_1h` score `-0.6448` n `188` status `ready` deltaP `0.6784` edge `0.0288` maxDD `-3.6309`
- `market_context_high->commodity_1h` score `-0.7773` n `188` status `ready` deltaP `-0.8982` edge `0.0027` maxDD `-2.252`
- `market_context_high->crypto_major_1h` score `-1.3889` n `188` status `ready` deltaP `-1.6977` edge `0.0021` maxDD `-6.1883`
- `market_context_high->crypto_alt_4h` score `-1.4078` n `176` status `ready` deltaP `7.7605` edge `0.1629` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-1.4965` n `176` status `ready` deltaP `4.0465` edge `0.1192` maxDD `-13.3376`
- `market_context_high->fx_4h` score `-1.9318` n `176` status `ready` deltaP `-7.5943` edge `-0.0133` maxDD `-1.4313`
- `market_context_high->unknown_4h` score `-3.2669` n `176` status `ready` deltaP `3.4784` edge `-0.2149` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
