# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T20:52:21.947178+00:00`
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

- `news_risk_high->unknown_4h` score `13.3897` n `51` status `ready` deltaP `24.1063` edge `0.9597` maxDD `-0.0348`
- `risk_on_high->unknown_1h` score `4.0003` n `37` status `ready` deltaP `-8.6624` edge `0.6155` maxDD `-1.5916`
- `risk_on_and_context->unknown_1h` score `4.0003` n `37` status `ready` deltaP `-8.6624` edge `0.6155` maxDD `-1.5916`
- `news_risk_high->unknown_1h` score `3.1697` n `51` status `ready` deltaP `16.9337` edge `0.1817` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.0217` n `51` status `ready` deltaP `35.7963` edge `0.0266` maxDD `-0.0746`
- `risk_on_high->equity_4h` score `2.8179` n `37` status `ready` deltaP `2.7934` edge `0.2592` maxDD `-0.773`
- `risk_on_and_context->equity_4h` score `2.8179` n `37` status `ready` deltaP `2.7934` edge `0.2592` maxDD `-0.773`
- `news_risk_high->equity_4h` score `2.556` n `51` status `ready` deltaP `22.5072` edge `0.14` maxDD `-2.164`
- `risk_on_high->metal_4h` score `2.2267` n `37` status `ready` deltaP `29.738` edge `-0.0039` maxDD `-0.0367`
- `risk_on_and_context->metal_4h` score `2.2267` n `37` status `ready` deltaP `29.738` edge `-0.0039` maxDD `-0.0367`
- `news_risk_high->fx_1h` score `1.229` n `51` status `ready` deltaP `16.8457` edge `0.0071` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.1351` n `146` status `ready` deltaP `7.1835` edge `0.0916` maxDD `-1.5916`
- `market_context_high->crypto_alt_4h` score `0.9873` n `134` status `ready` deltaP `10.0655` edge `0.1616` maxDD `-7.0478`
- `risk_on_high->index_4h` score `0.9422` n `37` status `ready` deltaP `12.3146` edge `0.0444` maxDD `-0.1719`
- `risk_on_and_context->index_4h` score `0.9422` n `37` status `ready` deltaP `12.3146` edge `0.0444` maxDD `-0.1719`
- `news_risk_high->equity_1h` score `0.7067` n `51` status `ready` deltaP `16.2469` edge `0.0187` maxDD `-0.9128`
- `market_context_high->commodity_24h` score `0.7063` n `107` status `ready` deltaP `-1.2088` edge `0.1144` maxDD `-0.7984`
- `news_risk_high->index_4h` score `0.4621` n `51` status `ready` deltaP `8.9759` edge `0.0184` maxDD `-0.1788`
- `market_context_high->unknown_4h` score `0.456` n `134` status `ready` deltaP `20.097` edge `-0.0788` maxDD `-0.3741`
- `news_risk_high->commodity_1h` score `0.229` n `51` status `ready` deltaP `8.9879` edge `-0.01` maxDD `-0.4666`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
