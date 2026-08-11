# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-11T02:22:28.791070+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11744`

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

- `market_context_high->unknown_24h` score `24.0181` n `145` status `ready` deltaP `-14.5772` edge `2.3441` maxDD `-9.6329`
- `market_context_high->fx_24h` score `1.1037` n `145` status `ready` deltaP `20.4064` edge `0.0367` maxDD `-1.4613`
- `market_context_high->commodity_4h` score `0.9425` n `168` status `ready` deltaP `12.4201` edge `0.0672` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.7126` n `180` status `ready` deltaP `9.7173` edge `0.0289` maxDD `-0.7439`
- `market_context_high->fx_1h` score `-0.1426` n `180` status `ready` deltaP `4.1218` edge `-0.0006` maxDD `-0.613`
- `market_context_high->fx_4h` score `-0.1729` n `168` status `ready` deltaP `4.9216` edge `0.005` maxDD `-0.4647`
- `market_context_high->index_1h` score `-0.8623` n `180` status `ready` deltaP `-7.0758` edge `-0.0046` maxDD `-1.0359`
- `market_context_high->metal_1h` score `-1.2864` n `180` status `ready` deltaP `-5.2195` edge `-0.0088` maxDD `-2.0884`
- `market_context_high->equity_1h` score `-1.4731` n `180` status `ready` deltaP `-6.4604` edge `-0.0181` maxDD `-6.8818`
- `market_context_high->metal_24h` score `-1.6542` n `145` status `ready` deltaP `2.5482` edge `-0.0224` maxDD `-2.9283`
- `market_context_high->index_4h` score `-1.9746` n `168` status `ready` deltaP `-8.1446` edge `-0.0198` maxDD `-1.5693`
- `market_context_high->index_24h` score `-2.1329` n `145` status `ready` deltaP `-9.1078` edge `-0.0032` maxDD `-6.7627`
- `market_context_high->commodity_24h` score `-2.3972` n `145` status `ready` deltaP `7.7763` edge `0.0797` maxDD `-25.7771`
- `market_context_high->crypto_alt_1h` score `-2.6354` n `180` status `ready` deltaP `-9.1084` edge `-0.0403` maxDD `-6.4874`
- `market_context_high->metal_4h` score `-3.2586` n `168` status `ready` deltaP `-8.5439` edge `-0.0382` maxDD `-6.1111`
- `market_context_high->crypto_major_1h` score `-3.6678` n `180` status `ready` deltaP `-9.4245` edge `-0.0524` maxDD `-11.9002`
- `market_context_high->equity_4h` score `-4.6183` n `168` status `ready` deltaP `-17.6829` edge `-0.1633` maxDD `-15.8728`
- `market_context_high->crypto_major_24h` score `-6.6376` n `145` status `ready` deltaP `-12.7258` edge `-0.189` maxDD `-33.5037`
- `market_context_high->crypto_alt_4h` score `-6.8286` n `168` status `ready` deltaP `-13.117` edge `-0.1468` maxDD `-20.1177`
- `market_context_high->crypto_alt_24h` score `-9.633` n `145` status `ready` deltaP `-13.339` edge `-0.234` maxDD `-27.3857`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
