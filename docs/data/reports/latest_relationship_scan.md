# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-19T02:37:26.854423+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8749`

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

- `market_context_high->commodity_24h` score `1.5461` n `85` status `ready` deltaP `15.0282` edge `0.1138` maxDD `-1.8119`
- `market_context_high->crypto_major_4h` score `1.0227` n `85` status `ready` deltaP `10.1488` edge `0.4039` maxDD `-15.2359`
- `risk_on_high->equity_1h` score `0.6669` n `52` status `ready` deltaP `13.4558` edge `0.027` maxDD `-2.2239`
- `risk_on_and_context->equity_1h` score `0.6669` n `52` status `ready` deltaP `13.4558` edge `0.027` maxDD `-2.2239`
- `risk_on_high->commodity_24h` score `0.474` n `52` status `ready` deltaP `13.2408` edge `0.031` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.474` n `52` status `ready` deltaP `13.2408` edge `0.031` maxDD `-1.7154`
- `market_context_high->crypto_major_1h` score `0.4011` n `86` status `ready` deltaP `3.9027` edge `0.1143` maxDD `-3.7781`
- `risk_on_high->index_1h` score `0.2745` n `52` status `ready` deltaP `8.0793` edge `0.0008` maxDD `-0.5428`
- `risk_on_and_context->index_1h` score `0.2745` n `52` status `ready` deltaP `8.0793` edge `0.0008` maxDD `-0.5428`
- `risk_on_high->fx_1h` score `0.0059` n `52` status `ready` deltaP `5.1686` edge `0.0007` maxDD `-0.1065`
- `risk_on_and_context->fx_1h` score `0.0059` n `52` status `ready` deltaP `5.1686` edge `0.0007` maxDD `-0.1065`
- `market_context_high->crypto_major_24h` score `-0.0487` n `85` status `ready` deltaP `3.1576` edge `0.5824` maxDD `-35.1086`
- `risk_on_high->crypto_major_4h` score `-0.3379` n `52` status `ready` deltaP `4.5379` edge `0.1745` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `-0.3379` n `52` status `ready` deltaP `4.5379` edge `0.1745` maxDD `-11.1788`
- `risk_on_high->fx_4h` score `-0.4081` n `52` status `ready` deltaP `-1.5526` edge `0.0032` maxDD `-0.1486`
- `risk_on_and_context->fx_4h` score `-0.4081` n `52` status `ready` deltaP `-1.5526` edge `0.0032` maxDD `-0.1486`
- `market_context_high->fx_1h` score `-0.507` n `86` status `ready` deltaP `-1.7634` edge `-0.0007` maxDD `-0.537`
- `market_context_high->fx_4h` score `-0.5586` n `85` status `ready` deltaP `-1.824` edge `0.0036` maxDD `-0.7115`
- `market_context_high->crypto_alt_1h` score `-0.6732` n `86` status `ready` deltaP `-1.6224` edge `0.0745` maxDD `-7.3329`
- `market_context_high->index_1h` score `-0.7948` n `86` status `ready` deltaP `1.505` edge `-0.0039` maxDD `-1.1229`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
