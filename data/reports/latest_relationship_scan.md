# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T12:37:29.125483+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7269`

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

- `market_context_high->unknown_24h` score `2280.9829` n `113` status `ready` deltaP `-7.2317` edge `190.1731` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `93.8874` n `98` status `ready` deltaP `-5.6427` edge `7.8902` maxDD `-0.9571`
- `market_context_high->unknown_4h` score `60.3961` n `113` status `ready` deltaP `1.2748` edge `5.0378` maxDD `-0.3966`
- `news_risk_high->crypto_alt_24h` score `17.2875` n `44` status `ready` deltaP `45.8017` edge `1.1404` maxDD `-0.0763`
- `market_context_high->equity_24h` score `10.6003` n `113` status `ready` deltaP `26.4704` edge `0.9826` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `4.8328` n `98` status `ready` deltaP `17.8758` edge `0.4222` maxDD `-7.4246`
- `market_context_high->index_24h` score `4.6373` n `113` status `ready` deltaP `42.1583` edge `0.1237` maxDD `-0.1315`
- `market_context_high->metal_4h` score `0.9962` n `113` status `ready` deltaP `19.9074` edge `0.0384` maxDD `-0.8054`
- `news_risk_high->crypto_alt_1h` score `0.8541` n `98` status `ready` deltaP `7.6469` edge `0.1031` maxDD `-3.9659`
- `market_context_high->metal_1h` score `0.5679` n `113` status `ready` deltaP `12.8583` edge `0.0161` maxDD `-0.3209`
- `market_context_high->equity_4h` score `0.5244` n `113` status `ready` deltaP `4.99` edge `0.1733` maxDD `-4.48`
- `market_context_high->crypto_major_1h` score `0.2339` n `113` status `ready` deltaP `7.8083` edge `0.0702` maxDD `-5.2213`
- `market_context_high->equity_1h` score `0.2292` n `113` status `ready` deltaP `4.5811` edge `0.0864` maxDD `-2.3383`
- `market_context_high->fx_1h` score `0.0421` n `113` status `ready` deltaP `4.9905` edge `-0.0009` maxDD `-0.1575`
- `market_context_high->metal_24h` score `0.0392` n `113` status `ready` deltaP `12.1082` edge `0.189` maxDD `-10.5088`
- `market_context_high->commodity_4h` score `-0.0508` n `113` status `ready` deltaP `9.7453` edge `0.0504` maxDD `-1.0837`
- `market_context_high->fx_4h` score `-0.2608` n `113` status `ready` deltaP `3.6181` edge `-0.0013` maxDD `-0.2312`
- `market_context_high->crypto_major_4h` score `-0.424` n `113` status `ready` deltaP `14.5127` edge `0.1229` maxDD `-14.5879`
- `market_context_high->index_1h` score `-0.517` n `113` status `ready` deltaP `1.75` edge `0.0011` maxDD `-1.1344`
- `market_context_high->commodity_1h` score `-0.5763` n `113` status `ready` deltaP `-1.4242` edge `0.0129` maxDD `-0.4475`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
