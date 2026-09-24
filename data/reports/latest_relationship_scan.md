# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T23:22:28.837877+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `10145`

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

- `market_context_high->unknown_1h` score `84.3151` n `47` status `ready` deltaP `9.9663` edge `6.9669` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `46.6289` n `47` status `ready` deltaP `30.4226` edge `3.7222` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `30.8152` n `47` status `ready` deltaP `24.782` edge `2.4407` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.5574` n `47` status `ready` deltaP `33.5476` edge `1.9417` maxDD `-2.1786`
- `market_context_high->index_24h` score `8.0795` n `47` status `ready` deltaP `37.1934` edge `0.4383` maxDD `-0.3705`
- `news_risk_high->unknown_1h` score `7.9299` n `114` status `ready` deltaP `-3.3223` edge `0.7074` maxDD `-0.9543`
- `market_context_high->metal_24h` score `4.3043` n `47` status `ready` deltaP `36.2737` edge `0.1407` maxDD `-0.2401`
- `news_risk_high->commodity_24h` score `3.3934` n `72` status `ready` deltaP `31.7708` edge `0.1058` maxDD `-1.7857`
- `news_risk_high->crypto_alt_1h` score `3.0075` n `114` status `ready` deltaP `15.4297` edge `0.1987` maxDD `-1.7416`
- `market_context_high->index_4h` score `2.8939` n `47` status `ready` deltaP `33.2641` edge `0.0348` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.3673` n `47` status `ready` deltaP `16.992` edge `0.1258` maxDD `-1.3444`
- `news_risk_high->crypto_major_1h` score `2.0564` n `114` status `ready` deltaP `15.343` edge `0.125` maxDD `-2.4737`
- `news_risk_high->metal_1h` score `1.4509` n `114` status `ready` deltaP `18.7835` edge `0.0242` maxDD `-0.6142`
- `news_risk_high->crypto_major_4h` score `1.2402` n `102` status `ready` deltaP `12.9902` edge `0.2299` maxDD `-13.719`
- `news_risk_high->crypto_alt_4h` score `1.1691` n `102` status `ready` deltaP `6.8478` edge `0.2969` maxDD `-15.9436`
- `news_risk_high->fx_4h` score `1.1104` n `102` status `ready` deltaP `18.2747` edge `0.0343` maxDD `-0.421`
- `market_context_high->index_1h` score `0.9715` n `47` status `ready` deltaP `14.7598` edge `0.0104` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.9223` n `47` status `ready` deltaP `11.4664` edge `0.0407` maxDD `-1.5564`
- `news_risk_high->metal_24h` score `0.3496` n `72` status `ready` deltaP `20.1389` edge `0.0554` maxDD `-7.2536`
- `news_risk_high->fx_24h` score `0.3189` n `72` status `ready` deltaP `17.5347` edge `0.0871` maxDD `-1.7159`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
