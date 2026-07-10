# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T08:22:29.766351+00:00`
- Price records: `672`
- Market context records: `6265`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11096`

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

- `news_risk_high->crypto_alt_24h` score `14.9041` n `32` status `ready` deltaP `42.8034` edge `0.9714` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `5.9502` n `32` status `ready` deltaP `50.6024` edge `0.1585` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1781` n `32` status `ready` deltaP `43.8262` edge `0.0606` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `3.8269` n `32` status `ready` deltaP `16.2274` edge `0.4604` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `2.4615` n `32` status `ready` deltaP `25.8552` edge `0.0533` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.3296` n `32` status `ready` deltaP `27.994` edge `0.0214` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `2.1459` n `196` status `ready` deltaP `2.7802` edge `0.2611` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.3712` n `32` status `ready` deltaP `14.128` edge `0.1283` maxDD `-2.0691`
- `market_context_high->unknown_4h` score `1.3663` n `192` status `ready` deltaP `-1.2322` edge `0.3753` maxDD `-11.925`
- `news_risk_high->crypto_alt_1h` score `0.7982` n `32` status `ready` deltaP `10.5726` edge `0.078` maxDD `-1.6923`
- `news_risk_high->index_24h` score `-0.1479` n `32` status `ready` deltaP `9.4342` edge `0.0053` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.1491` n `192` status `ready` deltaP `4.6494` edge `0.0483` maxDD `-2.671`
- `market_context_high->fx_1h` score `-0.2724` n `196` status `ready` deltaP `1.4634` edge `-0.0001` maxDD `-0.5659`
- `market_context_high->metal_24h` score `-0.3236` n `192` status `ready` deltaP `17.573` edge `0.0982` maxDD `-11.8809`
- `market_context_high->commodity_1h` score `-0.3926` n `196` status `ready` deltaP `-0.8707` edge `0.0015` maxDD `-0.682`
- `market_context_high->metal_4h` score `-0.4946` n `192` status `ready` deltaP `4.281` edge `0.0268` maxDD `-3.4996`
- `news_risk_high->metal_1h` score `-0.7021` n `32` status `ready` deltaP `-2.3952` edge `-0.0243` maxDD `-1.6464`
- `market_context_high->crypto_alt_1h` score `-0.8007` n `196` status `ready` deltaP `5.7894` edge `0.034` maxDD `-9.3536`
- `market_context_high->metal_1h` score `-0.8439` n `196` status `ready` deltaP `1.6864` edge `-0.0017` maxDD `-2.0564`
- `market_context_high->crypto_major_1h` score `-0.9206` n `196` status `ready` deltaP `4.1152` edge `0.0313` maxDD `-9.807`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
