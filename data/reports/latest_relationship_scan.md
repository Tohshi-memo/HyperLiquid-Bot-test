# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T17:07:30.743126+00:00`
- Price records: `672`
- Market context records: `5267`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9604`

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

- `market_context_high->unknown_24h` score `26.0764` n `148` status `ready` deltaP `29.8986` edge `1.9827` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `10.0131` n `148` status `ready` deltaP `27.9654` edge `1.0084` maxDD `-22.166`
- `market_context_high->crypto_alt_4h` score `4.2865` n `163` status `ready` deltaP `15.6142` edge `0.4172` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.8018` n `163` status `ready` deltaP `14.3947` edge `0.4501` maxDD `-14.0065`
- `market_context_high->equity_24h` score `3.5162` n `148` status `ready` deltaP `19.5899` edge `0.7253` maxDD `-40.0306`
- `market_context_high->unknown_4h` score `1.4118` n `163` status `ready` deltaP `15.7003` edge `0.1152` maxDD `-5.5109`
- `market_context_high->equity_4h` score `0.7329` n `163` status `ready` deltaP `8.7807` edge `0.1664` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.5261` n `148` status `ready` deltaP `12.7769` edge `0.0482` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.4386` n `175` status `ready` deltaP `4.3952` edge `0.1034` maxDD `-5.0257`
- `market_context_high->index_24h` score `0.2268` n `148` status `ready` deltaP `21.0257` edge `0.0524` maxDD `-7.413`
- `market_context_high->crypto_major_1h` score `0.2159` n `175` status `ready` deltaP `5.3755` edge `0.1067` maxDD `-6.9639`
- `market_context_high->equity_1h` score `0.0707` n `175` status `ready` deltaP `6.4072` edge `0.0597` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.0165` n `175` status `ready` deltaP `5.5637` edge `0.0119` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.2266` n `175` status `ready` deltaP `4.0958` edge `0.013` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.2947` n `175` status `ready` deltaP `1.0197` edge `0.0002` maxDD `-0.5823`
- `market_context_high->crypto_alt_24h` score `-0.3528` n `148` status `ready` deltaP `15.0478` edge `0.5108` maxDD `-40.5078`
- `market_context_high->index_4h` score `-0.6426` n `163` status `ready` deltaP `5.2334` edge `0.0233` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.7299` n `163` status `ready` deltaP `1.1325` edge `0.0018` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.3894` n `175` status `ready` deltaP `-3.1702` edge `-0.0069` maxDD `-3.0196`
- `market_context_high->metal_4h` score `-1.5734` n `163` status `ready` deltaP `-2.021` edge `0.0121` maxDD `-9.3609`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
