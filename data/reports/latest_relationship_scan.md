# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T07:52:29.758585+00:00`
- Price records: `672`
- Market context records: `6477`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5869`

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

- `news_risk_high->crypto_alt_24h` score `12.5051` n `32` status `ready` deltaP `33.6806` edge `0.8323` maxDD `-0.5131`
- `market_context_high->unknown_24h` score `7.0371` n `154` status `ready` deltaP `16.7929` edge `0.8045` maxDD `-15.0689`
- `news_risk_high->fx_24h` score `6.4306` n `32` status `ready` deltaP `53.4722` edge `0.1794` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.1739` n `32` status `ready` deltaP `15.9722` edge `0.5066` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `3.9388` n `35` status `ready` deltaP `41.3153` edge `0.0574` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.1723` n `32` status `ready` deltaP `29.3403` edge `0.0893` maxDD `-0.3101`
- `market_context_high->unknown_1h` score `2.0439` n `175` status `ready` deltaP `-4.3002` edge `0.2891` maxDD `-3.2083`
- `news_risk_high->fx_1h` score `1.8071` n `38` status `ready` deltaP `22.6127` edge `0.0179` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `0.5691` n `38` status `ready` deltaP `4.9007` edge `0.094` maxDD `-2.6299`
- `market_context_high->index_4h` score `0.4599` n `172` status `ready` deltaP `11.6492` edge `0.0283` maxDD `-0.4108`
- `market_context_high->unknown_4h` score `0.2907` n `172` status `ready` deltaP `-15.2404` edge `0.3664` maxDD `-10.5788`
- `market_context_high->commodity_24h` score `0.2065` n `154` status `ready` deltaP `6.0043` edge `0.164` maxDD `-5.2791`
- `market_context_high->crypto_alt_4h` score `0.2064` n `172` status `ready` deltaP `8.2459` edge `0.1176` maxDD `-6.7632`
- `market_context_high->metal_4h` score `0.1335` n `172` status `ready` deltaP `11.4364` edge `0.0437` maxDD `-2.7056`
- `news_risk_high->crypto_alt_1h` score `0.0804` n `38` status `ready` deltaP `1.5837` edge `0.0507` maxDD `-2.0756`
- `news_risk_high->index_24h` score `-0.4587` n `32` status `ready` deltaP `4.6875` edge `-0.0029` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.4847` n `172` status `ready` deltaP `7.9871` edge `0.0545` maxDD `-8.2573`
- `news_risk_high->unknown_1h` score `-0.4928` n `38` status `ready` deltaP `4.4516` edge `-0.0336` maxDD `-0.9718`
- `market_context_high->metal_1h` score `-0.5045` n `175` status `ready` deltaP `1.7827` edge `0.0012` maxDD `-1.8877`
- `market_context_high->commodity_1h` score `-0.5557` n `175` status `ready` deltaP `0.0539` edge `-0.0033` maxDD `-2.1314`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
