# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T18:07:28.028581+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14824`

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

- `news_risk_high->unknown_4h` score `13.5075` n `51` status `ready` deltaP `24.2587` edge `0.9685` maxDD `-0.0348`
- `risk_on_high->unknown_1h` score `4.0829` n `37` status `ready` deltaP `-8.0636` edge `0.6221` maxDD `-1.5916`
- `risk_on_and_context->unknown_1h` score `4.0829` n `37` status `ready` deltaP `-8.0636` edge `0.6221` maxDD `-1.5916`
- `news_risk_high->unknown_1h` score `3.2968` n `51` status `ready` deltaP `17.5325` edge `0.1883` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.0303` n `51` status `ready` deltaP `35.9487` edge `0.0263` maxDD `-0.0746`
- `news_risk_high->equity_4h` score `2.6698` n `51` status `ready` deltaP `23.2694` edge `0.1444` maxDD `-2.164`
- `risk_on_high->metal_4h` score `2.1939` n `33` status `ready` deltaP `29.3422` edge `-0.004` maxDD `-0.0367`
- `risk_on_and_context->metal_4h` score `2.1939` n `33` status `ready` deltaP `29.3422` edge `-0.004` maxDD `-0.0367`
- `risk_on_high->equity_4h` score `1.5636` n `33` status `ready` deltaP `-1.686` edge `0.2547` maxDD `-0.773`
- `risk_on_and_context->equity_4h` score `1.5636` n `33` status `ready` deltaP `-1.686` edge `0.2547` maxDD `-0.773`
- `news_risk_high->fx_1h` score `1.1392` n `51` status `ready` deltaP `15.7978` edge `0.0066` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `0.9839` n `137` status `ready` deltaP `5.9825` edge `0.087` maxDD `-1.5916`
- `market_context_high->crypto_alt_4h` score `0.9169` n `126` status `ready` deltaP `8.7809` edge `0.1643` maxDD `-7.0478`
- `risk_on_high->fx_4h` score `0.7562` n `33` status `ready` deltaP `17.4104` edge `0.0041` maxDD `-0.1905`
- `risk_on_and_context->fx_4h` score `0.7562` n `33` status `ready` deltaP `17.4104` edge `0.0041` maxDD `-0.1905`
- `news_risk_high->equity_1h` score `0.6982` n `51` status `ready` deltaP `15.9475` edge `0.0196` maxDD `-0.9128`
- `market_context_high->commodity_24h` score `0.5136` n `109` status `ready` deltaP `-2.6726` edge `0.1081` maxDD `-0.7984`
- `news_risk_high->index_4h` score `0.4681` n `51` status `ready` deltaP `8.9759` edge `0.0189` maxDD `-0.1788`
- `risk_on_high->index_4h` score `0.3552` n `33` status `ready` deltaP `7.7282` edge `0.042` maxDD `-0.1719`
- `risk_on_and_context->index_4h` score `0.3552` n `33` status `ready` deltaP `7.7282` edge `0.042` maxDD `-0.1719`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
