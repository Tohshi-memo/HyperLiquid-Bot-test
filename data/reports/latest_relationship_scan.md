# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T22:37:37.389040+00:00`
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

- `market_context_high->unknown_1h` score `84.5251` n `47` status `ready` deltaP `10.116` edge `6.9834` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `46.2557` n `47` status `ready` deltaP `30.4226` edge `3.6911` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `30.6232` n `47` status `ready` deltaP `24.782` edge `2.4247` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.4113` n `47` status `ready` deltaP `33.0267` edge `1.933` maxDD `-2.1786`
- `market_context_high->index_24h` score `8.027` n `47` status `ready` deltaP `36.6726` edge `0.4374` maxDD `-0.3705`
- `news_risk_high->unknown_1h` score `6.9081` n `114` status `ready` deltaP `-4.0498` edge `0.6271` maxDD `-0.9543`
- `market_context_high->metal_24h` score `4.2326` n `47` status `ready` deltaP `35.7528` edge `0.1382` maxDD `-0.2401`
- `news_risk_high->crypto_alt_1h` score `3.0988` n `114` status `ready` deltaP `15.4297` edge `0.2044` maxDD `-1.5895`
- `news_risk_high->commodity_24h` score `3.0528` n `75` status `ready` deltaP `28.4583` edge `0.0995` maxDD `-1.7857`
- `market_context_high->index_4h` score `2.8805` n `47` status `ready` deltaP `33.1117` edge `0.0347` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.3139` n `47` status `ready` deltaP `16.5347` edge `0.1244` maxDD `-1.3444`
- `news_risk_high->crypto_major_1h` score `2.1613` n `114` status `ready` deltaP `15.343` edge `0.128` maxDD `-2.0144`
- `news_risk_high->crypto_major_4h` score `2.0077` n `102` status `ready` deltaP `15.4741` edge `0.2773` maxDD `-13.719`
- `news_risk_high->crypto_alt_4h` score `1.9652` n `102` status `ready` deltaP `8.5037` edge `0.3522` maxDD `-15.9436`
- `news_risk_high->metal_1h` score `1.4558` n `114` status `ready` deltaP `18.7835` edge `0.0246` maxDD `-0.6142`
- `news_risk_high->fx_4h` score `1.3535` n `102` status `ready` deltaP `20.7586` edge `0.038` maxDD `-0.421`
- `market_context_high->index_1h` score `0.9739` n `47` status `ready` deltaP `14.7598` edge `0.0106` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.9354` n `47` status `ready` deltaP `11.6161` edge `0.0408` maxDD `-1.5564`
- `news_risk_high->metal_24h` score `0.5176` n `75` status `ready` deltaP `21.2847` edge `0.0693` maxDD `-7.2536`
- `news_risk_high->fx_24h` score `0.4764` n `75` status `ready` deltaP `19.4236` edge `0.0947` maxDD `-1.7159`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
