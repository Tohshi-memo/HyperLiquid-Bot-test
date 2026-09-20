# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T19:07:32.213054+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9806`

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

- `news_risk_high->crypto_major_24h` score `23.6732` n `98` status `ready` deltaP `11.0545` edge `2.5849` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `20.3734` n `98` status `ready` deltaP `15.2671` edge `2.0841` maxDD `-32.7147`
- `market_context_high->unknown_4h` score `12.7187` n `40` status `ready` deltaP `-1.0976` edge `1.0822` maxDD `-0.5326`
- `news_risk_high->crypto_alt_4h` score `5.1952` n `101` status `ready` deltaP `22.1202` edge `0.4064` maxDD `-7.675`
- `market_context_high->commodity_4h` score `4.2339` n `40` status `ready` deltaP `37.0427` edge `0.1192` maxDD `-0.0659`
- `news_risk_high->crypto_major_4h` score `4.0595` n `101` status `ready` deltaP `21.2056` edge `0.3227` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.9117` n `101` status `ready` deltaP `16.6805` edge `0.178` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.1767` n `101` status `ready` deltaP `18.4769` edge `0.1105` maxDD `-2.8494`
- `market_context_high->fx_4h` score `2.0588` n `40` status `ready` deltaP `27.0122` edge `0.013` maxDD `-0.0543`
- `news_risk_high->commodity_24h` score `1.0479` n `98` status `ready` deltaP `22.775` edge `0.1131` maxDD `-3.4467`
- `market_context_high->fx_1h` score `1.0298` n `52` status `ready` deltaP `14.4404` edge `0.007` maxDD `-0.063`
- `market_context_high->commodity_1h` score `0.6642` n `52` status `ready` deltaP `11.8148` edge `0.0339` maxDD `-0.2012`
- `news_risk_high->metal_1h` score `0.6425` n `101` status `ready` deltaP `14.7477` edge `0.0154` maxDD `-0.8144`
- `news_risk_high->metal_4h` score `0.63` n `101` status `ready` deltaP `17.2512` edge `0.0429` maxDD `-2.0994`
- `news_risk_high->equity_24h` score `0.5482` n `98` status `ready` deltaP `16.3974` edge `0.0773` maxDD `-4.941`
- `news_risk_high->equity_1h` score `0.2424` n `101` status `ready` deltaP `5.5137` edge `0.024` maxDD `-0.9112`
- `market_context_high->metal_1h` score `0.2298` n `52` status `ready` deltaP `7.0935` edge `0.0067` maxDD `-0.4538`
- `news_risk_high->metal_24h` score `0.1456` n `98` status `ready` deltaP `14.9837` edge `0.0032` maxDD `-2.4203`
- `news_risk_high->fx_4h` score `0.1347` n `101` status `ready` deltaP `7.8785` edge `0.0223` maxDD `-0.421`
- `news_risk_high->fx_1h` score `-0.3298` n `101` status `ready` deltaP `1.6452` edge `0.0059` maxDD `-0.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
