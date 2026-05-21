# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T22:37:19.328889+00:00`
- Price records: `672`
- Market context records: `1467`
- Flow alert records: `6134`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8809`

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

- `market_context_high->crypto_alt_24h` score `13.1139` n `168` status `ready` deltaP `28.9435` edge `1.1015` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `12.0568` n `168` status `ready` deltaP `27.6786` edge `0.9334` maxDD `-8.0553`
- `market_context_high->metal_24h` score `11.19` n `168` status `ready` deltaP `15.3026` edge `0.9972` maxDD `-6.3373`
- `market_context_high->equity_24h` score `4.296` n `168` status `ready` deltaP `13.3929` edge `0.5014` maxDD `-14.2815`
- `market_context_high->index_24h` score `4.2327` n `168` status `ready` deltaP `20.1389` edge `0.3271` maxDD `-5.3574`
- `market_context_high->equity_4h` score `1.5782` n `221` status `ready` deltaP `7.3819` edge `0.1653` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.2714` n `168` status `ready` deltaP `12.0784` edge `0.047` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.1226` n `221` status `ready` deltaP `3.3287` edge `0.0141` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.1304` n `221` status `ready` deltaP `1.9881` edge `0.0359` maxDD `-2.8014`
- `market_context_high->crypto_alt_4h` score `-0.1604` n `221` status `ready` deltaP `11.6233` edge `0.2411` maxDD `-19.5565`
- `market_context_high->index_4h` score `-0.3862` n `221` status `ready` deltaP `1.5479` edge `0.0664` maxDD `-3.7119`
- `market_context_high->fx_1h` score `-0.4854` n `221` status `ready` deltaP `0.5392` edge `-0.0026` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.5299` n `221` status `ready` deltaP `1.9204` edge `0.0454` maxDD `-4.1892`
- `market_context_high->fx_4h` score `-1.0459` n `221` status `ready` deltaP `-4.1607` edge `-0.0093` maxDD `-1.4313`
- `market_context_high->crypto_major_4h` score `-1.0464` n `221` status `ready` deltaP `5.5934` edge `0.1464` maxDD `-13.3376`
- `market_context_high->commodity_1h` score `-1.2099` n `221` status `ready` deltaP `-1.2741` edge `-0.0002` maxDD `-4.7041`
- `market_context_high->metal_1h` score `-1.2118` n `221` status `ready` deltaP `4.785` edge `0.0007` maxDD `-6.3532`
- `market_context_high->crypto_major_1h` score `-1.5601` n `221` status `ready` deltaP `-0.4985` edge `0.009` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.7733` n `221` status `ready` deltaP `8.0565` edge `0.0677` maxDD `-12.5349`
- `market_context_high->commodity_4h` score `-4.0539` n `221` status `ready` deltaP `-11.6861` edge `-0.0702` maxDD `-17.3969`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
