# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T21:07:17.623939+00:00`
- Price records: `672`
- Market context records: `1564`
- Flow alert records: `6413`
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

- `market_context_high->metal_24h` score `12.7931` n `182` status `ready` deltaP `25.206` edge `0.9981` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.073` n `182` status `ready` deltaP `26.9974` edge `0.9444` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `9.5673` n `182` status `ready` deltaP `26.7399` edge `0.7322` maxDD `-8.0553`
- `market_context_high->index_24h` score `4.026` n `182` status `ready` deltaP `20.7799` edge `0.3056` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.2109` n `182` status `ready` deltaP `15.8043` edge `0.3949` maxDD `-14.2815`
- `market_context_high->equity_4h` score `0.551` n `199` status `ready` deltaP `6.3105` edge `0.1133` maxDD `-5.0894`
- `market_context_high->fx_24h` score `0.4203` n `182` status `ready` deltaP `13.9251` edge `0.0471` maxDD `-1.3925`
- `market_context_high->crypto_alt_4h` score `0.1038` n `199` status `ready` deltaP `13.2545` edge `0.2569` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-0.0618` n `199` status `ready` deltaP `9.2796` edge `0.2011` maxDD `-13.3376`
- `market_context_high->crypto_alt_1h` score `-0.295` n `199` status `ready` deltaP `1.1171` edge `0.0571` maxDD `-4.1892`
- `market_context_high->fx_1h` score `-0.6413` n `199` status `ready` deltaP `-2.2936` edge `-0.0037` maxDD `-0.3914`
- `market_context_high->commodity_1h` score `-0.6923` n `199` status `ready` deltaP `0.1016` edge `0.0027` maxDD `-4.7041`
- `market_context_high->equity_1h` score `-0.7169` n `199` status `ready` deltaP `-0.5837` edge `0.025` maxDD `-2.8014`
- `market_context_high->metal_1h` score `-0.7251` n `199` status `ready` deltaP `5.2975` edge `0.0053` maxDD `-6.3532`
- `market_context_high->index_1h` score `-0.7368` n `199` status `ready` deltaP `0.0256` edge `0.0016` maxDD `-1.7205`
- `market_context_high->crypto_major_1h` score `-0.8506` n `199` status `ready` deltaP `-0.1444` edge `0.0276` maxDD `-6.1883`
- `market_context_high->index_4h` score `-1.3478` n `199` status `ready` deltaP `-3.6777` edge `0.0211` maxDD `-3.7119`
- `market_context_high->metal_4h` score `-1.3535` n `199` status `ready` deltaP `10.3636` edge `0.0873` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-1.3775` n `199` status `ready` deltaP `-10.3973` edge `-0.0144` maxDD `-1.4313`
- `market_context_high->commodity_4h` score `-5.0322` n `199` status `ready` deltaP `-13.3281` edge `-0.0936` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
