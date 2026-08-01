# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T06:52:33.671034+00:00`
- Price records: `672`
- Market context records: `8595`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5898`

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

- `news_risk_high->unknown_24h` score `4749.2416` n `64` status `ready` deltaP `35.4167` edge `395.5761` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.8524` n `64` status `ready` deltaP `20.6555` edge `0.4097` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.2152` n `64` status `ready` deltaP `18.7881` edge `0.0784` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.808` n `64` status `ready` deltaP `17.0004` edge `0.085` maxDD `-2.4803`
- `market_context_high->crypto_alt_4h` score `1.5027` n `62` status `ready` deltaP `11.0739` edge `0.1471` maxDD `-5.323`
- `news_risk_high->crypto_major_4h` score `1.0013` n `64` status `ready` deltaP `6.4405` edge `0.163` maxDD `-3.5385`
- `news_risk_high->crypto_alt_1h` score `0.3978` n `64` status `ready` deltaP `7.6628` edge `0.0526` maxDD `-1.8813`
- `news_risk_high->crypto_alt_4h` score `0.3858` n `64` status `ready` deltaP `10.6707` edge `0.1175` maxDD `-5.8012`
- `news_risk_high->crypto_major_1h` score `0.3602` n `64` status `ready` deltaP `7.064` edge `0.0503` maxDD `-2.0972`
- `news_risk_high->fx_4h` score `0.0984` n `64` status `ready` deltaP `12.2332` edge `0.0224` maxDD `-0.6604`
- `news_risk_high->fx_1h` score `0.0979` n `64` status `ready` deltaP `5.436` edge `0.0044` maxDD `-0.2475`
- `news_risk_high->metal_4h` score `0.0562` n `64` status `ready` deltaP `3.3918` edge `0.0322` maxDD `-0.8085`
- `news_risk_high->index_1h` score `0.0418` n `64` status `ready` deltaP `4.2197` edge `0.0089` maxDD `-0.5338`
- `market_context_high->fx_4h` score `-0.0699` n `62` status `ready` deltaP `9.0578` edge `0.0134` maxDD `-1.3685`
- `news_risk_high->metal_1h` score `-0.1335` n `64` status `ready` deltaP `3.256` edge `0.0075` maxDD `-0.5599`
- `market_context_high->fx_1h` score `-0.2669` n `62` status `ready` deltaP `2.3614` edge `0.0003` maxDD `-0.6874`
- `market_context_high->commodity_1h` score `-0.2959` n `62` status `ready` deltaP `4.4572` edge `-0.0051` maxDD `-2.0038`
- `market_context_high->crypto_alt_1h` score `-0.579` n `62` status `ready` deltaP `-3.3755` edge `0.011` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.7189` n `62` status `ready` deltaP `1.2459` edge `-0.0153` maxDD `-1.5667`
- `market_context_high->metal_1h` score `-0.9745` n `62` status `ready` deltaP `-2.994` edge `-0.0118` maxDD `-1.6224`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
