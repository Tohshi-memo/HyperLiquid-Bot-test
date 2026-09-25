# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T00:37:25.805620+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `10157`

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

- `market_context_high->unknown_1h` score `83.8856` n `47` status `ready` deltaP `9.5172` edge `6.9341` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `47.2073` n `47` status `ready` deltaP `30.4226` edge `3.7704` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `31.102` n `47` status `ready` deltaP `24.782` edge `2.4646` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.7961` n `47` status `ready` deltaP `34.4156` edge `1.9558` maxDD `-2.1786`
- `news_risk_high->unknown_1h` score `10.0125` n `114` status `ready` deltaP `-1.1398` edge `0.8664` maxDD `-0.9543`
- `market_context_high->index_24h` score `8.1693` n `47` status `ready` deltaP `38.0614` edge `0.44` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.4157` n `47` status `ready` deltaP `37.1417` edge `0.1442` maxDD `-0.2401`
- `news_risk_high->commodity_24h` score `3.3757` n `67` status `ready` deltaP `31.4599` edge `0.1064` maxDD `-1.7857`
- `market_context_high->index_4h` score `2.9353` n `47` status `ready` deltaP `33.7215` edge `0.0352` maxDD `-0.2323`
- `news_risk_high->crypto_alt_1h` score `2.9067` n `114` status `ready` deltaP `15.4297` edge `0.1903` maxDD `-1.7416`
- `market_context_high->equity_4h` score `2.4203` n `47` status `ready` deltaP `17.1445` edge `0.1292` maxDD `-1.3444`
- `news_risk_high->crypto_major_1h` score `1.9988` n `114` status `ready` deltaP `15.343` edge `0.1202` maxDD `-2.4737`
- `news_risk_high->metal_1h` score `1.1618` n `114` status `ready` deltaP `15.8735` edge `0.0195` maxDD `-0.6142`
- `market_context_high->index_1h` score `0.9439` n `47` status `ready` deltaP `14.4604` edge `0.0101` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.8743` n `47` status `ready` deltaP `11.0173` edge `0.0397` maxDD `-1.5564`
- `news_risk_high->fx_4h` score `0.7579` n `102` status `ready` deltaP `14.963` edge `0.027` maxDD `-0.421`
- `market_context_high->crypto_alt_4h` score `0.2691` n `47` status `ready` deltaP `6.9441` edge `0.0429` maxDD `-3.3417`
- `market_context_high->fx_1h` score `0.2158` n `47` status `ready` deltaP `7.2652` edge `0.0052` maxDD `-0.1854`
- `news_risk_high->metal_24h` score `0.0862` n `67` status `ready` deltaP `17.8975` edge `0.0327` maxDD `-7.2536`
- `news_risk_high->crypto_major_4h` score `0.0647` n `102` status `ready` deltaP `10.5063` edge `0.1485` maxDD `-13.719`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
