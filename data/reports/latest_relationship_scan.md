# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T21:52:26.705784+00:00`
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

- `news_risk_high->unknown_4h` score `13.1273` n `51` status `ready` deltaP `23.4965` edge `0.9419` maxDD `-0.0348`
- `risk_on_high->unknown_1h` score `3.913` n `37` status `ready` deltaP `-9.2612` edge `0.6083` maxDD `-1.5916`
- `risk_on_and_context->unknown_1h` score `3.913` n `37` status `ready` deltaP `-9.2612` edge `0.6083` maxDD `-1.5916`
- `news_risk_high->unknown_1h` score `3.0354` n `51` status `ready` deltaP `16.3349` edge `0.1745` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.0253` n `51` status `ready` deltaP `35.7963` edge `0.0269` maxDD `-0.0746`
- `risk_on_high->equity_4h` score `2.8095` n `37` status `ready` deltaP `2.7934` edge `0.2585` maxDD `-0.773`
- `risk_on_and_context->equity_4h` score `2.8095` n `37` status `ready` deltaP `2.7934` edge `0.2585` maxDD `-0.773`
- `news_risk_high->equity_4h` score `2.5476` n `51` status `ready` deltaP `22.5072` edge `0.1393` maxDD `-2.164`
- `risk_on_high->metal_4h` score `2.2411` n `37` status `ready` deltaP `29.738` edge `-0.0027` maxDD `-0.0367`
- `risk_on_and_context->metal_4h` score `2.2411` n `37` status `ready` deltaP `29.738` edge `-0.0027` maxDD `-0.0367`
- `market_context_high->unknown_1h` score `1.4602` n `148` status `ready` deltaP `8.3063` edge `0.1112` maxDD `-1.5916`
- `market_context_high->unknown_4h` score `1.2949` n `136` status `ready` deltaP `21.0455` edge `-0.0187` maxDD `-0.0956`
- `news_risk_high->fx_1h` score `1.2302` n `51` status `ready` deltaP `16.8457` edge `0.0072` maxDD `-0.0257`
- `market_context_high->crypto_alt_4h` score `1.1432` n `136` status `ready` deltaP `10.8142` edge `0.1696` maxDD `-7.0478`
- `risk_on_high->index_4h` score `0.9398` n `37` status `ready` deltaP `12.3146` edge `0.0442` maxDD `-0.1719`
- `risk_on_and_context->index_4h` score `0.9398` n `37` status `ready` deltaP `12.3146` edge `0.0442` maxDD `-0.1719`
- `market_context_high->commodity_24h` score `0.7489` n `105` status `ready` deltaP `-0.9772` edge `0.1164` maxDD `-0.7984`
- `news_risk_high->equity_1h` score `0.6724` n `51` status `ready` deltaP `15.6481` edge `0.0183` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.4597` n `51` status `ready` deltaP `8.9759` edge `0.0182` maxDD `-0.1788`
- `news_risk_high->commodity_1h` score `0.2266` n `51` status `ready` deltaP `8.9879` edge `-0.0102` maxDD `-0.4666`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
