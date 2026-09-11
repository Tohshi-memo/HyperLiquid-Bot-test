# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-11T01:37:30.615702+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11352`

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

- `news_risk_high->unknown_1h` score `1225.8846` n `43` status `ready` deltaP `-5.6016` edge `102.2298` maxDD `-1.1656`
- `news_risk_high->unknown_4h` score `402.0145` n `31` status `ready` deltaP `-25.5458` edge `33.7359` maxDD `-2.1509`
- `risk_on_high->crypto_alt_24h` score `20.4656` n `91` status `ready` deltaP `36.1722` edge `1.4873` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `20.4656` n `91` status `ready` deltaP `36.1722` edge `1.4873` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `16.1081` n `199` status `ready` deltaP `28.6014` edge `1.2344` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `9.0275` n `91` status `ready` deltaP `42.0983` edge `0.5088` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `9.0275` n `91` status `ready` deltaP `42.0983` edge `0.5088` maxDD `-1.9733`
- `market_context_high->equity_24h` score `8.1262` n `199` status `ready` deltaP `28.9931` edge `0.4839` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `7.7899` n `91` status `ready` deltaP `32.6588` edge `0.5173` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `7.7899` n `91` status `ready` deltaP `32.6588` edge `0.5173` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `7.2432` n `91` status `ready` deltaP `25.021` edge `1.1686` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.2432` n `91` status `ready` deltaP `25.021` edge `1.1686` maxDD `-24.5429`
- `risk_on_high->equity_24h` score `6.613` n `91` status `ready` deltaP `28.9931` edge `0.3578` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `6.613` n `91` status `ready` deltaP `28.9931` edge `0.3578` maxDD `0.0`
- `risk_on_high->index_24h` score `4.7507` n `91` status `ready` deltaP `44.7936` edge `0.1015` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `4.7507` n `91` status `ready` deltaP `44.7936` edge `0.1015` maxDD `-0.0051`
- `market_context_high->index_24h` score `3.861` n `199` status `ready` deltaP `39.0451` edge `0.1008` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `3.5442` n `91` status `ready` deltaP `33.0407` edge `0.0844` maxDD `-0.079`
- `risk_on_and_context->equity_4h` score `3.5442` n `91` status `ready` deltaP `33.0407` edge `0.0844` maxDD `-0.079`
- `market_context_high->equity_4h` score `2.3741` n `199` status `ready` deltaP `26.0663` edge `0.1096` maxDD `-2.843`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
