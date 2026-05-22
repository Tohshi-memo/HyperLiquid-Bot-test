# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T03:07:15.187273+00:00`
- Price records: `672`
- Market context records: `1487`
- Flow alert records: `6190`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8810`

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

- `market_context_high->crypto_alt_24h` score `12.0948` n `172` status `ready` deltaP `28.985` edge `1.0163` maxDD `-15.1306`
- `market_context_high->metal_24h` score `11.4411` n `172` status `ready` deltaP `17.2359` edge `0.9844` maxDD `-6.3373`
- `market_context_high->crypto_major_24h` score `11.0492` n `172` status `ready` deltaP `27.3538` edge `0.8516` maxDD `-8.0553`
- `market_context_high->index_24h` score `4.0598` n `172` status `ready` deltaP `20.3327` edge `0.3114` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.7857` n `172` status `ready` deltaP `13.6144` edge `0.4574` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.5211` n `207` status `ready` deltaP `7.4025` edge `0.1604` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.7132` n `172` status `ready` deltaP `16.9856` edge `0.0511` maxDD `-1.3925`
- `market_context_high->crypto_alt_4h` score `0.0769` n `207` status `ready` deltaP `11.8144` edge `0.2596` maxDD `-19.5565`
- `market_context_high->equity_1h` score `0.0081` n `207` status `ready` deltaP `3.0439` edge `0.0404` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.1272` n `207` status `ready` deltaP `3.3911` edge `0.0133` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.5417` n `207` status `ready` deltaP `-0.439` edge `-0.0033` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.5958` n `207` status `ready` deltaP `0.9626` edge `0.0463` maxDD `-4.1892`
- `market_context_high->crypto_major_4h` score `-0.7036` n `207` status `ready` deltaP `6.6528` edge `0.1679` maxDD `-13.3376`
- `market_context_high->index_4h` score `-0.711` n `207` status `ready` deltaP `-0.5331` edge `0.0532` maxDD `-3.7119`
- `market_context_high->metal_1h` score `-0.7216` n `207` status `ready` deltaP `6.0112` edge `0.001` maxDD `-6.3532`
- `market_context_high->fx_4h` score `-1.0024` n `207` status `ready` deltaP `-3.9774` edge `-0.0091` maxDD `-1.4313`
- `market_context_high->commodity_1h` score `-1.0883` n `207` status `ready` deltaP `-0.0239` edge `0.0016` maxDD `-4.7041`
- `market_context_high->metal_4h` score `-1.5672` n `207` status `ready` deltaP `9.2679` edge `0.0768` maxDD `-12.5349`
- `market_context_high->crypto_major_1h` score `-1.6571` n `207` status `ready` deltaP `-1.7863` edge `0.0095` maxDD `-6.1883`
- `market_context_high->commodity_4h` score `-4.1477` n `207` status `ready` deltaP `-12.905` edge `-0.0741` maxDD `-17.3969`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
