# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-19T02:22:36.306597+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8747`

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

- `market_context_high->commodity_24h` score `1.5933` n `86` status `ready` deltaP `15.1688` edge `0.1168` maxDD `-1.8119`
- `market_context_high->crypto_major_4h` score `1.0479` n `86` status `ready` deltaP `10.7097` edge `0.4034` maxDD `-15.2359`
- `risk_on_high->commodity_24h` score `0.5948` n `53` status `ready` deltaP `13.6111` edge `0.0386` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.5948` n `53` status `ready` deltaP `13.6111` edge `0.0386` maxDD `-1.7154`
- `risk_on_high->equity_1h` score `0.3897` n `53` status `ready` deltaP `12.59` edge `0.0174` maxDD `-2.8417`
- `risk_on_and_context->equity_1h` score `0.3897` n `53` status `ready` deltaP `12.59` edge `0.0174` maxDD `-2.8417`
- `market_context_high->crypto_major_1h` score `0.3599` n `87` status `ready` deltaP `3.4242` edge `0.1122` maxDD `-3.7781`
- `risk_on_high->index_1h` score `0.2043` n `53` status `ready` deltaP `7.2497` edge `0.0007` maxDD `-0.5608`
- `risk_on_and_context->index_1h` score `0.2043` n `53` status `ready` deltaP `7.2497` edge `0.0007` maxDD `-0.5608`
- `risk_on_high->fx_1h` score `-0.0843` n `53` status `ready` deltaP `4.1164` edge `0.0002` maxDD `-0.1065`
- `risk_on_and_context->fx_1h` score `-0.0843` n `53` status `ready` deltaP `4.1164` edge `0.0002` maxDD `-0.1065`
- `risk_on_high->crypto_major_4h` score `-0.2655` n `53` status `ready` deltaP `5.5539` edge `0.177` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `-0.2655` n `53` status `ready` deltaP `5.5539` edge `0.177` maxDD `-11.1788`
- `market_context_high->crypto_major_24h` score `-0.2703` n `86` status `ready` deltaP `2.9757` edge `0.5552` maxDD `-35.1086`
- `risk_on_high->fx_4h` score `-0.4814` n `53` status `ready` deltaP `-2.4234` edge `0.0029` maxDD `-0.1486`
- `risk_on_and_context->fx_4h` score `-0.4814` n `53` status `ready` deltaP `-2.4234` edge `0.0029` maxDD `-0.1486`
- `market_context_high->fx_1h` score `-0.5385` n `87` status `ready` deltaP `-2.3247` edge `-0.001` maxDD `-0.537`
- `market_context_high->fx_4h` score `-0.5879` n `86` status `ready` deltaP `-2.3576` edge `0.0034` maxDD `-0.7115`
- `market_context_high->crypto_alt_1h` score `-0.6336` n `87` status `ready` deltaP `-0.9808` edge `0.0753` maxDD `-7.3329`
- `market_context_high->index_1h` score `-0.826` n `87` status `ready` deltaP `1.1339` edge `-0.0038` maxDD `-1.1408`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
