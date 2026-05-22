# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T04:52:14.787759+00:00`
- Price records: `672`
- Market context records: `1494`
- Flow alert records: `6212`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8811`

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

- `market_context_high->metal_24h` score `12.257` n `172` status `ready` deltaP `20.0905` edge `1.0042` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.5572` n `172` status `ready` deltaP `28.985` edge `0.9715` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.46` n `172` status `ready` deltaP `27.3538` edge `0.8025` maxDD `-8.0553`
- `market_context_high->index_24h` score `3.917` n `172` status `ready` deltaP `20.3327` edge `0.2995` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.3129` n `172` status `ready` deltaP `13.6144` edge `0.418` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.3229` n `200` status `ready` deltaP `7.1159` edge `0.1458` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.9497` n `172` status `ready` deltaP `19.4323` edge `0.0545` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.1332` n `200` status `ready` deltaP `1.8772` edge `0.0364` maxDD `-2.8014`
- `market_context_high->crypto_alt_4h` score `-0.1831` n `200` status `ready` deltaP `10.6646` edge `0.2456` maxDD `-19.5565`
- `market_context_high->index_1h` score `-0.2218` n `200` status `ready` deltaP `2.6737` edge `0.0102` maxDD `-1.7205`
- `market_context_high->crypto_alt_1h` score `-0.4693` n `200` status `ready` deltaP `1.8084` edge `0.0512` maxDD `-4.1892`
- `market_context_high->fx_1h` score `-0.5189` n `200` status `ready` deltaP `-0.0449` edge `-0.003` maxDD `-0.3914`
- `market_context_high->crypto_major_4h` score `-0.6559` n `200` status `ready` deltaP `6.4695` edge `0.1731` maxDD `-13.3376`
- `market_context_high->metal_1h` score `-0.7675` n `200` status `ready` deltaP `5.4581` edge `-0.0012` maxDD `-6.3532`
- `market_context_high->index_4h` score `-0.9002` n `200` status `ready` deltaP `-1.6829` edge `0.0451` maxDD `-3.7119`
- `market_context_high->fx_4h` score `-0.9691` n `200` status `ready` deltaP `-3.3537` edge `-0.009` maxDD `-1.4313`
- `market_context_high->commodity_1h` score `-1.0656` n `200` status `ready` deltaP `0.2006` edge `0.002` maxDD `-4.7041`
- `market_context_high->metal_4h` score `-1.2282` n `200` status `ready` deltaP `11.1951` edge `0.0922` maxDD `-12.5349`
- `market_context_high->crypto_major_1h` score `-1.4997` n `200` status `ready` deltaP `-0.7934` edge `0.016` maxDD `-6.1883`
- `market_context_high->commodity_4h` score `-4.3146` n `200` status `ready` deltaP `-14.1037` edge `-0.0875` maxDD `-17.3969`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
