# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T06:37:34.414872+00:00`
- Price records: `672`
- Market context records: `6162`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11132`

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

- `news_risk_high->crypto_alt_24h` score `12.6105` n `32` status `ready` deltaP `42.8879` edge `0.7797` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `7.4848` n `32` status `ready` deltaP `65.6897` edge `0.1858` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1787` n `32` status `ready` deltaP `43.5038` edge `0.0628` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.4147` n `32` status `ready` deltaP `29.0419` edge `0.0215` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.6974` n `195` status `ready` deltaP `1.104` edge `0.2349` maxDD `-3.7317`
- `news_risk_high->crypto_major_24h` score `1.3643` n `32` status `ready` deltaP `16.3147` edge `0.1441` maxDD `-4.2368`
- `news_risk_high->crypto_major_1h` score `1.2051` n `32` status `ready` deltaP `12.9304` edge `0.115` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.6097` n `32` status `ready` deltaP `8.1774` edge `0.0698` maxDD `-1.6923`
- `market_context_high->unknown_4h` score `0.2113` n `195` status `ready` deltaP `-0.9091` edge `0.2769` maxDD `-11.925`
- `market_context_high->metal_24h` score `0.0584` n `195` status `ready` deltaP `20.1503` edge `0.13` maxDD `-11.8809`
- `news_risk_high->index_24h` score `0.0051` n `32` status `ready` deltaP `10.2155` edge `0.0197` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.0099` n `195` status `ready` deltaP `2.8788` edge `0.0717` maxDD `-2.671`
- `market_context_high->fx_1h` score `-0.2606` n `195` status `ready` deltaP `1.7342` edge `-0.0004` maxDD `-0.5659`
- `market_context_high->metal_4h` score `-0.5792` n `195` status `ready` deltaP `4.1842` edge `0.0166` maxDD `-3.4996`
- `market_context_high->commodity_1h` score `-0.7176` n `195` status `ready` deltaP `-1.6897` edge `-0.0039` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.7652` n `32` status `ready` deltaP `-2.994` edge `-0.0284` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.8116` n `195` status `ready` deltaP `2.3906` edge `-0.0037` maxDD `-2.0564`
- `news_risk_high->commodity_24h` score `-0.8658` n `32` status `ready` deltaP `11.7888` edge `-0.1302` maxDD `-0.3101`
- `market_context_high->equity_1h` score `-0.9232` n `195` status `ready` deltaP `-2.0559` edge `0.0069` maxDD `-4.2573`
- `market_context_high->crypto_alt_1h` score `-0.9662` n `195` status `ready` deltaP `3.1614` edge `0.0303` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
