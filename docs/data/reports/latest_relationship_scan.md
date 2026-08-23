# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T05:58:54.986716+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14882`

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

- `news_risk_high->unknown_4h` score `16.8483` n `45` status `ready` deltaP `28.3537` edge `1.215` maxDD `0.0`
- `risk_on_high->unknown_1h` score `5.2084` n `32` status `ready` deltaP `-8.5516` edge `0.7696` maxDD `-1.5876`
- `risk_on_and_context->unknown_1h` score `5.2084` n `32` status `ready` deltaP `-8.5516` edge `0.7696` maxDD `-1.5876`
- `news_risk_high->equity_4h` score `4.738` n `45` status `ready` deltaP `34.8374` edge `0.1969` maxDD `-0.7456`
- `news_risk_high->unknown_1h` score `3.8294` n `51` status `ready` deltaP `20.6763` edge `0.2117` maxDD `-0.7674`
- `news_risk_high->fx_4h` score `3.0824` n `45` status `ready` deltaP `36.6904` edge `0.0257` maxDD `-0.0746`
- `news_risk_high->index_4h` score `1.3616` n `45` status `ready` deltaP `19.1057` edge `0.0247` maxDD `-0.0884`
- `news_risk_high->fx_1h` score `1.2086` n `51` status `ready` deltaP `16.696` edge `0.0064` maxDD `-0.0257`
- `news_risk_high->metal_4h` score `1.086` n `45` status `ready` deltaP `18.0861` edge `-0.0041` maxDD `-0.0781`
- `market_context_high->unknown_1h` score `1.0131` n `135` status `ready` deltaP `4.9901` edge `0.096` maxDD `-1.5876`
- `news_risk_high->equity_1h` score `0.8469` n `51` status `ready` deltaP `18.3427` edge `0.0228` maxDD `-0.9204`
- `market_context_high->unknown_4h` score `0.8341` n `129` status `ready` deltaP `22.1521` edge `-0.061` maxDD `-0.3736`
- `risk_on_high->fx_1h` score `0.5287` n `32` status `ready` deltaP `8.6078` edge `0.0041` maxDD `-0.0605`
- `risk_on_and_context->fx_1h` score `0.5287` n `32` status `ready` deltaP `8.6078` edge `0.0041` maxDD `-0.0605`
- `news_risk_high->index_1h` score `0.2154` n `51` status `ready` deltaP `8.9732` edge `0.0031` maxDD `-0.1583`
- `news_risk_high->commodity_1h` score `0.1739` n `51` status `ready` deltaP `8.3891` edge `-0.0106` maxDD `-0.4666`
- `market_context_high->fx_4h` score `0.1711` n `129` status `ready` deltaP `8.37` edge `0.0087` maxDD `-0.3527`
- `risk_on_high->equity_1h` score `-0.0453` n `32` status `ready` deltaP `-2.2455` edge `0.0461` maxDD `-0.9554`
- `risk_on_and_context->equity_1h` score `-0.0453` n `32` status `ready` deltaP `-2.2455` edge `0.0461` maxDD `-0.9554`
- `risk_on_high->index_1h` score `-0.0678` n `32` status `ready` deltaP `0.1497` edge `0.0082` maxDD `-0.098`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
