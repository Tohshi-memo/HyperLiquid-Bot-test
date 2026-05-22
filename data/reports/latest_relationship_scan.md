# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T20:51:49.125023+00:00`
- Price records: `672`
- Market context records: `1563`
- Flow alert records: `6410`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8813`

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

- `market_context_high->metal_24h` score `12.7504` n `182` status `ready` deltaP `25.0324` edge `0.9957` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.043` n `182` status `ready` deltaP `26.9974` edge `0.9419` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `9.5301` n `182` status `ready` deltaP `26.7399` edge `0.7291` maxDD `-8.0553`
- `market_context_high->index_24h` score `4.0296` n `182` status `ready` deltaP `20.7799` edge `0.3059` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.1526` n `182` status `ready` deltaP `15.6307` edge `0.3912` maxDD `-14.2815`
- `market_context_high->equity_4h` score `0.5184` n `199` status `ready` deltaP `6.1581` edge `0.1116` maxDD `-5.0894`
- `market_context_high->fx_24h` score `0.4378` n `182` status `ready` deltaP `14.0987` edge `0.0474` maxDD `-1.3925`
- `market_context_high->crypto_alt_4h` score `0.0765` n `199` status `ready` deltaP `13.2545` edge `0.2534` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-0.0923` n `199` status `ready` deltaP `9.1272` edge `0.1982` maxDD `-13.3376`
- `market_context_high->crypto_alt_1h` score `-0.2973` n `199` status `ready` deltaP `1.1171` edge `0.0568` maxDD `-4.1892`
- `market_context_high->fx_1h` score `-0.6499` n `199` status `ready` deltaP `-2.4433` edge `-0.0038` maxDD `-0.3914`
- `market_context_high->commodity_1h` score `-0.6892` n `199` status `ready` deltaP `0.1016` edge `0.0031` maxDD `-4.7041`
- `market_context_high->metal_1h` score `-0.7251` n `199` status `ready` deltaP `5.2975` edge `0.0053` maxDD `-6.3532`
- `market_context_high->equity_1h` score `-0.7313` n `199` status `ready` deltaP `-0.7334` edge `0.0248` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.738` n `199` status `ready` deltaP `0.0256` edge `0.0015` maxDD `-1.7205`
- `market_context_high->crypto_major_1h` score `-0.8638` n `199` status `ready` deltaP `-0.2941` edge `0.0269` maxDD `-6.1883`
- `market_context_high->index_4h` score `-1.3672` n `199` status `ready` deltaP `-3.8301` edge `0.0205` maxDD `-3.7119`
- `market_context_high->metal_4h` score `-1.3729` n `199` status `ready` deltaP `10.2111` edge `0.0867` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-1.3768` n `199` status `ready` deltaP `-10.3973` edge `-0.0143` maxDD `-1.4313`
- `market_context_high->commodity_4h` score `-5.0276` n `199` status `ready` deltaP `-13.3281` edge `-0.093` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
