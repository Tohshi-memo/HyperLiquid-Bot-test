# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T20:07:32.940186+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14856`

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

- `news_risk_high->unknown_4h` score `13.4425` n `51` status `ready` deltaP `24.1063` edge `0.9641` maxDD `-0.0348`
- `risk_on_high->unknown_1h` score `4.0213` n `37` status `ready` deltaP `-8.6624` edge `0.6182` maxDD `-1.5916`
- `risk_on_and_context->unknown_1h` score `4.0213` n `37` status `ready` deltaP `-8.6624` edge `0.6182` maxDD `-1.5916`
- `news_risk_high->unknown_1h` score `3.2021` n `51` status `ready` deltaP `16.9337` edge `0.1844` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.0193` n `51` status `ready` deltaP `35.7963` edge `0.0264` maxDD `-0.0746`
- `risk_on_high->equity_4h` score `2.8555` n `37` status `ready` deltaP `3.0983` edge `0.2603` maxDD `-0.773`
- `risk_on_and_context->equity_4h` score `2.8555` n `37` status `ready` deltaP `3.0983` edge `0.2603` maxDD `-0.773`
- `news_risk_high->equity_4h` score `2.5936` n `51` status `ready` deltaP `22.8121` edge `0.1411` maxDD `-2.164`
- `risk_on_high->metal_4h` score `2.2377` n `37` status `ready` deltaP `29.8904` edge `-0.004` maxDD `-0.0367`
- `risk_on_and_context->metal_4h` score `2.2377` n `37` status `ready` deltaP `29.8904` edge `-0.004` maxDD `-0.0367`
- `news_risk_high->fx_1h` score `1.2146` n `51` status `ready` deltaP `16.696` edge `0.0069` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `0.9979` n `144` status `ready` deltaP `6.803` edge `0.0827` maxDD `-1.5916`
- `market_context_high->crypto_alt_4h` score `0.9459` n `133` status `ready` deltaP `9.6082` edge `0.1612` maxDD `-7.0478`
- `risk_on_high->index_4h` score `0.9434` n `37` status `ready` deltaP `12.3146` edge `0.0445` maxDD `-0.1719`
- `risk_on_and_context->index_4h` score `0.9434` n `37` status `ready` deltaP `12.3146` edge `0.0445` maxDD `-0.1719`
- `news_risk_high->equity_1h` score `0.6826` n `51` status `ready` deltaP `15.7978` edge `0.0186` maxDD `-0.9128`
- `market_context_high->commodity_24h` score `0.6611` n `108` status `ready` deltaP `-1.5047` edge `0.1126` maxDD `-0.7984`
- `news_risk_high->index_4h` score `0.4633` n `51` status `ready` deltaP `8.9759` edge `0.0185` maxDD `-0.1788`
- `market_context_high->unknown_4h` score `0.3301` n `133` status `ready` deltaP `20.0521` edge `-0.089` maxDD `-0.3741`
- `news_risk_high->commodity_1h` score `0.2302` n `51` status `ready` deltaP `8.9879` edge `-0.0099` maxDD `-0.4666`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
