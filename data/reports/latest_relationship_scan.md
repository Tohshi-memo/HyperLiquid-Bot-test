# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T18:07:33.085939+00:00`
- Price records: `672`
- Market context records: `8537`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5914`

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

- `news_risk_high->unknown_24h` score `6279.7517` n `52` status `ready` deltaP `42.8285` edge `523.0692` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.7436` n `64` status `ready` deltaP `20.9604` edge `0.3986` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.0131` n `64` status `ready` deltaP `16.5015` edge `0.0768` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.663` n `64` status `ready` deltaP `15.6531` edge `0.0819` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `1.0092` n `64` status `ready` deltaP `6.593` edge `0.163` maxDD `-3.5385`
- `market_context_high->crypto_alt_4h` score `0.8224` n `53` status `ready` deltaP `8.5855` edge `0.1439` maxDD `-5.323`
- `news_risk_high->crypto_alt_4h` score `0.7735` n `64` status `ready` deltaP `14.4817` edge `0.1418` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.4578` n `64` status `ready` deltaP `8.2616` edge `0.0563` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3275` n `64` status `ready` deltaP `6.6149` edge `0.0491` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.08` n `64` status `ready` deltaP `5.1366` edge `0.0041` maxDD `-0.2475`
- `news_risk_high->metal_4h` score `0.0085` n `64` status `ready` deltaP `2.3247` edge `0.0332` maxDD `-0.8085`
- `news_risk_high->index_1h` score `0.0075` n `64` status `ready` deltaP `3.6209` edge `0.0085` maxDD `-0.5338`
- `news_risk_high->fx_4h` score `-0.0222` n `64` status `ready` deltaP `10.8613` edge `0.0215` maxDD `-0.6604`
- `news_risk_high->metal_1h` score `-0.1311` n `64` status `ready` deltaP `3.256` edge `0.0077` maxDD `-0.5599`
- `market_context_high->fx_1h` score `-0.2848` n `62` status `ready` deltaP `2.062` edge `0.0` maxDD `-0.6874`
- `market_context_high->commodity_1h` score `-0.3278` n `62` status `ready` deltaP `3.559` edge `-0.0032` maxDD `-2.0038`
- `market_context_high->crypto_alt_1h` score `-0.519` n `62` status `ready` deltaP `-2.7767` edge `0.0147` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.7716` n `62` status `ready` deltaP `0.6471` edge `-0.0157` maxDD `-1.5667`
- `market_context_high->metal_1h` score `-0.9721` n `62` status `ready` deltaP `-2.994` edge `-0.0116` maxDD `-1.6224`
- `market_context_high->fx_4h` score `-1.0716` n `53` status `ready` deltaP `-1.0786` edge `-0.0025` maxDD `-1.3685`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
