# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T05:52:27.394282+00:00`
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

- `news_risk_high->unknown_4h` score `16.8159` n `45` status `ready` deltaP `28.3537` edge `1.2123` maxDD `0.0`
- `risk_on_high->unknown_1h` score `5.175` n `32` status `ready` deltaP `-8.5516` edge `0.7666` maxDD `-1.6898`
- `risk_on_and_context->unknown_1h` score `5.175` n `32` status `ready` deltaP `-8.5516` edge `0.7666` maxDD `-1.6898`
- `news_risk_high->equity_4h` score `4.7532` n `45` status `ready` deltaP `34.8374` edge `0.1977` maxDD `-0.7078`
- `news_risk_high->unknown_1h` score `3.8318` n `51` status `ready` deltaP `20.6763` edge `0.2119` maxDD `-0.7674`
- `news_risk_high->fx_4h` score `3.0836` n `45` status `ready` deltaP `36.6904` edge `0.0258` maxDD `-0.0746`
- `news_risk_high->index_4h` score `1.3616` n `45` status `ready` deltaP `19.1057` edge `0.0247` maxDD `-0.0884`
- `news_risk_high->fx_1h` score `1.2086` n `51` status `ready` deltaP `16.696` edge `0.0064` maxDD `-0.0257`
- `news_risk_high->metal_4h` score `1.0846` n `45` status `ready` deltaP `18.0861` edge `-0.0042` maxDD `-0.0795`
- `market_context_high->unknown_1h` score `0.9917` n `135` status `ready` deltaP `4.9901` edge `0.0955` maxDD `-1.6898`
- `news_risk_high->equity_1h` score `0.8469` n `51` status `ready` deltaP `18.3427` edge `0.0228` maxDD `-0.9204`
- `market_context_high->unknown_4h` score `0.8365` n `129` status `ready` deltaP `22.1521` edge `-0.0608` maxDD `-0.3736`
- `risk_on_high->fx_1h` score `0.5308` n `32` status `ready` deltaP `8.6078` edge `0.0042` maxDD `-0.055`
- `risk_on_and_context->fx_1h` score `0.5308` n `32` status `ready` deltaP `8.6078` edge `0.0042` maxDD `-0.055`
- `news_risk_high->index_1h` score `0.2154` n `51` status `ready` deltaP `8.9732` edge `0.0031` maxDD `-0.1583`
- `news_risk_high->commodity_1h` score `0.1739` n `51` status `ready` deltaP `8.3891` edge `-0.0106` maxDD `-0.4666`
- `market_context_high->fx_4h` score `0.1699` n `129` status `ready` deltaP `8.37` edge `0.0086` maxDD `-0.3527`
- `risk_on_high->equity_1h` score `-0.0323` n `32` status `ready` deltaP `-2.2455` edge `0.0473` maxDD `-0.9176`
- `risk_on_and_context->equity_1h` score `-0.0323` n `32` status `ready` deltaP `-2.2455` edge `0.0473` maxDD `-0.9176`
- `risk_on_high->index_1h` score `-0.0669` n `32` status `ready` deltaP `0.1497` edge `0.0083` maxDD `-0.0965`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
