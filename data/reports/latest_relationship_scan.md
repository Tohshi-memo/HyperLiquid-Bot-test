# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T15:07:18.155021+00:00`
- Price records: `672`
- Market context records: `1641`
- Flow alert records: `6633`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8834`

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

- `market_context_high->metal_24h` score `9.6549` n `175` status `ready` deltaP `26.9809` edge `0.8673` maxDD `-12.7414`
- `market_context_high->index_24h` score `3.429` n `175` status `ready` deltaP `19.0275` edge `0.2967` maxDD `-5.3574`
- `market_context_high->crypto_alt_4h` score `3.1453` n `185` status `ready` deltaP `19.6692` edge `0.3974` maxDD `-16.3135`
- `market_context_high->crypto_major_4h` score `1.6533` n `185` status `ready` deltaP `15.4288` edge `0.3058` maxDD `-13.3376`
- `market_context_high->equity_4h` score `1.5263` n `185` status `ready` deltaP `11.5866` edge `0.1594` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.1305` n `175` status `ready` deltaP `18.1282` edge `0.4632` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.0124` n `195` status `ready` deltaP `3.3525` edge `0.0816` maxDD `-4.1892`
- `market_context_high->crypto_major_24h` score `-0.0342` n `175` status `ready` deltaP `23.8099` edge `0.697` maxDD `-62.3533`
- `market_context_high->fx_24h` score `-0.4344` n `175` status `ready` deltaP `6.7363` edge `0.0238` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.4733` n `195` status `ready` deltaP `1.1262` edge `0.0339` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.4886` n `195` status `ready` deltaP `0.5528` edge `-0.0031` maxDD `-0.3914`
- `market_context_high->index_4h` score `-0.5047` n `185` status `ready` deltaP `-0.0009` edge `0.0442` maxDD `-3.7119`
- `market_context_high->index_1h` score `-0.6288` n `195` status `ready` deltaP `0.3555` edge `0.0084` maxDD `-1.7205`
- `market_context_high->crypto_major_1h` score `-0.6429` n `195` status `ready` deltaP `0.2342` edge `0.0434` maxDD `-5.5244`
- `market_context_high->crypto_alt_24h` score `-0.6803` n `175` status `ready` deltaP `24.2733` edge `0.9624` maxDD `-88.8062`
- `market_context_high->commodity_1h` score `-0.8454` n `195` status `ready` deltaP `1.6229` edge `-0.0069` maxDD `-6.6507`
- `market_context_high->metal_1h` score `-1.326` n `195` status `ready` deltaP `2.862` edge `0.004` maxDD `-6.3532`
- `market_context_high->fx_4h` score `-1.3866` n `185` status `ready` deltaP `-10.7063` edge `-0.0135` maxDD `-1.4313`
- `market_context_high->metal_4h` score `-1.4945` n `185` status `ready` deltaP `7.3266` edge `0.0958` maxDD `-12.5349`
- `market_context_high->unknown_4h` score `-3.5312` n `185` status `ready` deltaP `8.8584` edge `-0.1262` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
