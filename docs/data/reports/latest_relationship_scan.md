# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T03:37:18.062396+00:00`
- Price records: `672`
- Market context records: `1908`
- Flow alert records: `7391`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4518`

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

- `market_context_high->crypto_alt_4h` score `7.736` n `199` status `ready` deltaP `24.1857` edge `0.5979` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `7.1565` n `199` status `ready` deltaP `28.7819` edge `0.5291` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `3.9117` n `199` status `ready` deltaP `17.5006` edge `0.4117` maxDD `-9.8581`
- `market_context_high->equity_4h` score `2.5539` n `199` status `ready` deltaP `15.1918` edge `0.221` maxDD `-5.0894`
- `market_context_high->metal_24h` score `1.8923` n `185` status `ready` deltaP `16.9041` edge `0.2876` maxDD `-12.7414`
- `market_context_high->unknown_24h` score `1.5494` n `185` status `ready` deltaP `13.0292` edge `0.5743` maxDD `-35.8966`
- `market_context_high->index_24h` score `1.1766` n `185` status `ready` deltaP `8.263` edge `0.1658` maxDD `-4.1604`
- `market_context_high->crypto_major_1h` score `0.7135` n `200` status `ready` deltaP `7.7515` edge `0.1064` maxDD `-3.2225`
- `market_context_high->index_4h` score `0.5164` n `199` status `ready` deltaP `10.5504` edge `0.0816` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `0.5152` n `200` status `ready` deltaP `7.1557` edge `0.1066` maxDD `-4.9097`
- `market_context_high->fx_24h` score `0.201` n `185` status `ready` deltaP `14.4539` edge `0.0253` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.04` n `200` status `ready` deltaP `5.4671` edge `0.0396` maxDD `-2.6836`
- `market_context_high->equity_24h` score `-0.2765` n `185` status `ready` deltaP `9.1347` edge `0.4059` maxDD `-33.1875`
- `market_context_high->metal_1h` score `-0.5424` n `200` status `ready` deltaP `6.2006` edge `0.0227` maxDD `-6.3532`
- `market_context_high->fx_1h` score `-0.6171` n `200` status `ready` deltaP `-2.5479` edge `0.0011` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.6742` n `200` status `ready` deltaP `-0.4371` edge `0.0099` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.6988` n `199` status `ready` deltaP `11.9331` edge `0.1314` maxDD `-12.5349`
- `market_context_high->crypto_major_24h` score `-0.7379` n `185` status `ready` deltaP `16.9632` edge `0.684` maxDD `-62.3533`
- `market_context_high->fx_4h` score `-0.832` n `199` status `ready` deltaP `-2.7523` edge `0.0005` maxDD `-1.1056`
- `market_context_high->unknown_1h` score `-0.9244` n `200` status `ready` deltaP `1.9581` edge `0.0051` maxDD `-3.6151`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
