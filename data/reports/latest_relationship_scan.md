# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T22:07:20.302312+00:00`
- Price records: `672`
- Market context records: `1465`
- Flow alert records: `6128`
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

- `market_context_high->crypto_alt_24h` score `12.8986` n `166` status `ready` deltaP `28.922` edge `1.0837` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `11.9945` n `166` status `ready` deltaP `27.6355` edge `0.9285` maxDD `-8.0553`
- `market_context_high->metal_24h` score `11.347` n `166` status `ready` deltaP `15.4346` edge `1.0094` maxDD `-6.3373`
- `market_context_high->index_24h` score `4.1719` n `166` status `ready` deltaP `20.0385` edge `0.3227` maxDD `-5.3574`
- `market_context_high->equity_24h` score `4.0804` n `166` status `ready` deltaP `13.2781` edge `0.4842` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.559` n `221` status `ready` deltaP `7.3819` edge `0.1637` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.2829` n `166` status `ready` deltaP `12.1172` edge `0.0477` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.0962` n `221` status `ready` deltaP `3.6281` edge `0.0143` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.1268` n `221` status `ready` deltaP `1.9881` edge `0.0362` maxDD `-2.8014`
- `market_context_high->crypto_alt_4h` score `-0.2124` n `221` status `ready` deltaP `11.3184` edge `0.2388` maxDD `-19.5565`
- `market_context_high->index_4h` score `-0.4032` n `221` status `ready` deltaP `1.3954` edge `0.066` maxDD `-3.7119`
- `market_context_high->fx_1h` score `-0.4691` n `221` status `ready` deltaP `0.8386` edge `-0.0025` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.5515` n `221` status `ready` deltaP `1.7707` edge `0.0446` maxDD `-4.1892`
- `market_context_high->fx_4h` score `-1.0459` n `221` status `ready` deltaP `-4.1607` edge `-0.0093` maxDD `-1.4313`
- `market_context_high->crypto_major_4h` score `-1.1092` n `221` status `ready` deltaP `5.2885` edge `0.1432` maxDD `-13.3376`
- `market_context_high->metal_1h` score `-1.1686` n `221` status `ready` deltaP `5.0844` edge `0.0023` maxDD `-6.3532`
- `market_context_high->commodity_1h` score `-1.2459` n `221` status `ready` deltaP `-1.5735` edge `-0.0012` maxDD `-4.7041`
- `market_context_high->crypto_major_1h` score `-1.5805` n `221` status `ready` deltaP `-0.6482` edge `0.0083` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.7721` n `221` status `ready` deltaP `8.0565` edge `0.0678` maxDD `-12.5349`
- `market_context_high->commodity_4h` score `-4.05` n `221` status `ready` deltaP `-11.6861` edge `-0.0697` maxDD `-17.3969`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
