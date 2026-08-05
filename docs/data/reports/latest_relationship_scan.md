# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T18:52:45.007056+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11684`

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

- `market_context_high->unknown_24h` score `13.0417` n `90` status `ready` deltaP `4.9653` edge `1.058` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `3.9005` n `101` status `ready` deltaP `0.0286` edge `0.4244` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.4696` n `101` status `ready` deltaP `15.9593` edge `0.1007` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.9367` n `90` status `ready` deltaP `2.0139` edge `0.2235` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.9106` n `90` status `ready` deltaP `24.7223` edge `0.0725` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4379` n `108` status `ready` deltaP `7.8288` edge `0.0259` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0466` n `108` status `ready` deltaP `6.2098` edge `-0.0025` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.0391` n `101` status `ready` deltaP `10.9333` edge `0.0081` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5131` n `108` status `ready` deltaP `-1.5358` edge `-0.0061` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.7612` n `101` status `ready` deltaP `2.848` edge `0.0069` maxDD `-3.211`
- `market_context_high->index_1h` score `-0.8003` n `108` status `ready` deltaP `-4.5298` edge `-0.019` maxDD `-1.6054`
- `market_context_high->crypto_alt_24h` score `-1.4519` n `90` status `ready` deltaP `0.7291` edge `-0.0467` maxDD `-4.5445`
- `market_context_high->crypto_alt_1h` score `-1.4803` n `108` status `ready` deltaP `-4.8459` edge `-0.02` maxDD `-3.0178`
- `market_context_high->crypto_alt_4h` score `-1.7695` n `101` status `ready` deltaP `-1.9455` edge `-0.0749` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.7937` n `108` status `ready` deltaP `1.2309` edge `-0.0846` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.1185` n `101` status `ready` deltaP `-12.3083` edge `-0.0641` maxDD `-4.7021`
- `market_context_high->index_24h` score `-2.4493` n `90` status `ready` deltaP `-10.7292` edge `-0.023` maxDD `-7.8922`
- `market_context_high->crypto_major_1h` score `-3.3578` n `108` status `ready` deltaP `-11.3828` edge `-0.0666` maxDD `-7.6533`
- `market_context_high->unknown_1h` score `-3.5772` n `108` status `ready` deltaP `2.2344` edge `-0.2683` maxDD `-1.2421`
- `market_context_high->commodity_24h` score `-6.0374` n `90` status `ready` deltaP `10.8334` edge `-0.0248` maxDD `-51.0493`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
