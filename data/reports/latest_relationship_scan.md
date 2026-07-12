# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T23:22:32.246681+00:00`
- Price records: `672`
- Market context records: `6550`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9854`

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

- `market_context_high->unknown_24h` score `6.4123` n `144` status `ready` deltaP `11.8934` edge `0.7851` maxDD `-15.0689`
- `news_risk_high->fx_4h` score `3.6586` n `32` status `ready` deltaP `39.1768` edge `0.0483` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.4006` n `32` status `ready` deltaP `29.491` edge `0.0215` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.8792` n `203` status `ready` deltaP `-5.6842` edge `0.2846` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `1.3141` n `144` status `ready` deltaP `12.784` edge `0.2111` maxDD `-5.2791`
- `news_risk_high->crypto_major_1h` score `0.5755` n `32` status `ready` deltaP `4.753` edge `0.0958` maxDD `-2.6299`
- `market_context_high->index_4h` score `0.3768` n `195` status `ready` deltaP `11.4282` edge `0.0255` maxDD `-0.6232`
- `market_context_high->crypto_alt_4h` score `-0.0025` n `195` status `ready` deltaP `8.5726` edge `0.1017` maxDD `-7.0579`
- `news_risk_high->crypto_alt_1h` score `-0.03` n `32` status `ready` deltaP `0.0` edge `0.0471` maxDD `-2.0756`
- `market_context_high->equity_4h` score `-0.3566` n `195` status `ready` deltaP `10.1939` edge `0.0562` maxDD `-8.2573`
- `market_context_high->crypto_major_4h` score `-0.5581` n `195` status `ready` deltaP `11.0256` edge `0.084` maxDD `-12.6576`
- `market_context_high->index_1h` score `-0.5762` n `203` status `ready` deltaP `-0.7824` edge `0.0033` maxDD `-0.7564`
- `news_risk_high->unknown_1h` score `-0.6391` n `32` status `ready` deltaP `4.753` edge `-0.0478` maxDD `-0.9718`
- `market_context_high->crypto_major_1h` score `-0.647` n `203` status `ready` deltaP `5.6459` edge `0.006` maxDD `-6.7936`
- `market_context_high->fx_1h` score `-0.6836` n `203` status `ready` deltaP `-0.6814` edge `-0.0017` maxDD `-0.7249`
- `news_risk_high->commodity_4h` score `-0.8958` n `32` status `ready` deltaP `-7.4695` edge `-0.0115` maxDD `-1.6178`
- `market_context_high->commodity_1h` score `-0.9013` n `203` status `ready` deltaP `-0.2846` edge `-0.0049` maxDD `-2.1314`
- `market_context_high->crypto_alt_1h` score `-1.0071` n `203` status `ready` deltaP `5.665` edge `0.0096` maxDD `-5.8368`
- `news_risk_high->index_1h` score `-1.0634` n `32` status `ready` deltaP `-8.9259` edge `-0.0205` maxDD `-1.1725`
- `market_context_high->unknown_4h` score `-1.0659` n `195` status `ready` deltaP `-17.679` edge `0.2696` maxDD `-10.5788`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
