# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T23:22:39.082383+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8743`

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

- `market_context_high->unknown_4h` score `49.3018` n `148` status `ready` deltaP `5.0882` edge `4.0898` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.9435` n `135` status `ready` deltaP `27.1875` edge `0.0495` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.3936` n `148` status `ready` deltaP `9.8276` edge `0.0031` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.065` n `148` status `ready` deltaP `8.4542` edge `0.0089` maxDD `-0.4545`
- `market_context_high->commodity_4h` score `-0.0649` n `148` status `ready` deltaP `9.2205` edge `0.055` maxDD `-1.0837`
- `market_context_high->metal_1h` score `-0.1558` n `148` status `ready` deltaP `7.2746` edge `0.0062` maxDD `-1.3073`
- `market_context_high->fx_24h` score `-0.4277` n `135` status `ready` deltaP `11.9097` edge `0.023` maxDD `-1.2451`
- `market_context_high->crypto_major_1h` score `-0.4328` n `148` status `ready` deltaP `6.7527` edge `0.0278` maxDD `-6.9306`
- `market_context_high->commodity_1h` score `-0.5291` n `148` status `ready` deltaP `0.6757` edge `0.0098` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.6755` n `148` status `ready` deltaP `-2.1767` edge `-0.0038` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.8212` n `148` status `ready` deltaP `8.1905` edge `-0.0058` maxDD `-4.6603`
- `market_context_high->equity_24h` score `-1.3578` n `135` status `ready` deltaP `8.0671` edge `0.1295` maxDD `-15.7143`
- `market_context_high->metal_24h` score `-1.4363` n `135` status `ready` deltaP `12.1065` edge `0.0774` maxDD `-8.2244`
- `market_context_high->equity_1h` score `-1.4531` n `148` status `ready` deltaP `1.6426` edge `-0.006` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.7304` n `148` status `ready` deltaP `2.1605` edge `0.0001` maxDD `-12.2409`
- `market_context_high->index_4h` score `-3.0224` n `148` status `ready` deltaP `-8.3224` edge `-0.0342` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.7299` n `135` status `ready` deltaP `0.544` edge `0.0039` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.8058` n `148` status `ready` deltaP `3.2713` edge `-0.0778` maxDD `-27.2215`
- `market_context_high->unknown_1h` score `-4.617` n `148` status `ready` deltaP `0.1012` edge `-0.3365` maxDD `-1.5807`
- `market_context_high->equity_4h` score `-5.7045` n `148` status `ready` deltaP `-3.16` edge `-0.1869` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
