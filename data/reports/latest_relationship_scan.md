# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T20:37:36.974025+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6994`

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

- `market_context_high->unknown_24h` score `1590.0807` n `134` status `ready` deltaP `-6.0894` edge `132.5903` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `108.0353` n `76` status `ready` deltaP `-0.4649` edge `9.0186` maxDD `-0.3382`
- `market_context_high->unknown_4h` score `36.3394` n `134` status `ready` deltaP `0.4163` edge `3.0388` maxDD `-0.3966`
- `market_context_high->equity_24h` score `5.8133` n `134` status `ready` deltaP `16.6589` edge `0.6491` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `5.1703` n `64` status `ready` deltaP `18.6357` edge `0.3727` maxDD `-3.6198`
- `market_context_high->index_24h` score `3.6298` n `134` status `ready` deltaP `35.2638` edge `0.0857` maxDD `-0.1315`
- `news_risk_high->commodity_4h` score `0.6522` n `64` status `ready` deltaP `6.4787` edge `0.048` maxDD `-0.9471`
- `news_risk_high->crypto_alt_1h` score `0.6073` n `76` status `ready` deltaP `5.8068` edge `0.0948` maxDD `-3.9659`
- `market_context_high->metal_4h` score `0.4038` n `134` status `ready` deltaP `16.1358` edge `0.0338` maxDD `-1.8344`
- `market_context_high->metal_1h` score `0.3891` n `134` status `ready` deltaP `10.9036` edge `0.0151` maxDD `-0.3659`
- `market_context_high->commodity_4h` score `0.3337` n `134` status `ready` deltaP `14.5477` edge `0.0527` maxDD `-1.0837`
- `market_context_high->equity_1h` score `0.3109` n `134` status `ready` deltaP `5.3803` edge `0.0776` maxDD `-2.3383`
- `market_context_high->equity_4h` score `0.2083` n `134` status `ready` deltaP `3.3059` edge `0.1631` maxDD `-6.008`
- `market_context_high->crypto_major_1h` score `0.0576` n `134` status `ready` deltaP `7.4649` edge `0.0578` maxDD `-5.2213`
- `market_context_high->fx_1h` score `-0.094` n `134` status `ready` deltaP `3.7291` edge `-0.0011` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.2445` n `134` status `ready` deltaP `2.393` edge `0.0151` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.4895` n `134` status `ready` deltaP `-0.0159` edge `-0.0028` maxDD `-0.4545`
- `news_risk_high->commodity_1h` score `-0.6526` n `76` status `ready` deltaP `-4.9322` edge `0.0066` maxDD `-1.2575`
- `market_context_high->index_1h` score `-0.7923` n `134` status `ready` deltaP `-1.6467` edge `0.0008` maxDD `-1.1344`
- `news_risk_high->index_1h` score `-0.8231` n `76` status `ready` deltaP `-2.9625` edge `-0.0058` maxDD `-1.3981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
