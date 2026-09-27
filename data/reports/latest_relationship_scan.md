# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T22:37:26.720536+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7674`

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

- `news_risk_high->unknown_24h` score `720.2712` n `136` status `ready` deltaP `1.2153` edge `60.0145` maxDD `0.0`
- `news_risk_high->index_24h` score `1.4077` n `136` status `ready` deltaP `18.0352` edge `0.0666` maxDD `-2.2287`
- `news_risk_high->crypto_alt_24h` score `1.3518` n `136` status `ready` deltaP `14.6446` edge `0.4102` maxDD `-29.2814`
- `news_risk_high->metal_24h` score `0.8745` n `136` status `ready` deltaP `19.9449` edge `0.1254` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `0.0027` n `139` status `ready` deltaP `15.8931` edge `0.0552` maxDD `-9.2079`
- `news_risk_high->index_1h` score `-0.0528` n `139` status `ready` deltaP `3.063` edge `0.0042` maxDD `-0.3214`
- `news_risk_high->crypto_alt_1h` score `-0.0845` n `139` status `ready` deltaP `4.323` edge `0.0552` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `-0.2269` n `139` status `ready` deltaP `3.063` edge `0.0268` maxDD `-1.957`
- `news_risk_high->metal_1h` score `-0.7281` n `139` status `ready` deltaP `-0.3059` edge `0.0043` maxDD `-0.7016`
- `news_risk_high->equity_24h` score `-0.9416` n `136` status `ready` deltaP `12.0711` edge `0.0967` maxDD `-11.1179`
- `news_risk_high->fx_4h` score `-1.0349` n `139` status `ready` deltaP `13.0308` edge `0.0018` maxDD `-3.0414`
- `news_risk_high->fx_1h` score `-1.0706` n `139` status `ready` deltaP `-7.1717` edge `-0.0014` maxDD `-1.0436`
- `news_risk_high->crypto_major_1h` score `-1.1226` n `139` status `ready` deltaP `-3.7447` edge `0.0093` maxDD `-7.2607`
- `news_risk_high->index_4h` score `-1.1672` n `139` status `ready` deltaP `-2.9457` edge `0.0077` maxDD `-1.493`
- `news_risk_high->crypto_alt_4h` score `-1.8105` n `139` status `ready` deltaP `1.3336` edge `0.1062` maxDD `-15.9436`
- `news_risk_high->metal_4h` score `-1.8678` n `139` status `ready` deltaP `-13.7293` edge `0.0015` maxDD `-3.6214`
- `news_risk_high->commodity_1h` score `-1.901` n `139` status `ready` deltaP `-9.9201` edge `-0.0101` maxDD `-3.3986`
- `news_risk_high->crypto_major_24h` score `-2.6852` n `136` status `ready` deltaP `8.7725` edge `0.1612` maxDD `-26.1424`
- `news_risk_high->crypto_major_4h` score `-3.5063` n `139` status `ready` deltaP `-12.5603` edge `-0.0943` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-3.6538` n `139` status `ready` deltaP `-9.7978` edge `0.0027` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
