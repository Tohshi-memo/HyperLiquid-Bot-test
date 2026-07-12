# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T06:22:33.486135+00:00`
- Price records: `672`
- Market context records: `6470`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5859`

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

- `news_risk_high->crypto_alt_24h` score `12.2681` n `32` status `ready` deltaP `32.6389` edge `0.8195` maxDD `-0.5131`
- `market_context_high->unknown_24h` score `6.9697` n `153` status `ready` deltaP `16.3706` edge `0.8017` maxDD `-15.0689`
- `news_risk_high->fx_24h` score `6.3793` n `32` status `ready` deltaP `52.9514` edge `0.1786` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1218` n `32` status `ready` deltaP `42.9116` edge `0.062` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `3.9497` n `32` status `ready` deltaP `14.9306` edge `0.4848` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `3.342` n `32` status `ready` deltaP `30.3819` edge `0.0965` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `1.8311` n `38` status `ready` deltaP `22.9121` edge `0.0179` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.5842` n `172` status `ready` deltaP `-5.4867` edge `0.2587` maxDD `-3.2083`
- `news_risk_high->crypto_major_1h` score `0.5894` n `38` status `ready` deltaP `5.2001` edge `0.0946` maxDD `-2.6299`
- `market_context_high->index_4h` score `0.3941` n `172` status `ready` deltaP `10.887` edge `0.0279` maxDD `-0.4108`
- `market_context_high->commodity_24h` score `0.3318` n `153` status `ready` deltaP `6.7912` edge `0.1692` maxDD `-5.2791`
- `market_context_high->unknown_4h` score `0.2921` n `172` status `ready` deltaP `-15.0879` edge `0.3655` maxDD `-10.5788`
- `market_context_high->crypto_alt_4h` score `0.1096` n `172` status `ready` deltaP `7.6361` edge `0.1136` maxDD `-6.7632`
- `news_risk_high->crypto_alt_1h` score `0.0882` n `38` status `ready` deltaP `1.7334` edge `0.0507` maxDD `-2.0756`
- `market_context_high->metal_4h` score `0.0701` n `172` status `ready` deltaP `10.6743` edge `0.0435` maxDD `-2.7056`
- `news_risk_high->index_24h` score `-0.4634` n `32` status `ready` deltaP `4.6875` edge `-0.0035` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.5271` n `172` status `ready` deltaP `1.3473` edge `0.0012` maxDD `-1.8877`
- `market_context_high->equity_4h` score `-0.5494` n `172` status `ready` deltaP `7.0724` edge `0.0523` maxDD `-8.2573`
- `market_context_high->commodity_1h` score `-0.5829` n `172` status `ready` deltaP `-0.3342` edge `-0.0042` maxDD `-2.1314`
- `news_risk_high->unknown_1h` score `-0.6044` n `38` status `ready` deltaP `4.1522` edge `-0.0409` maxDD `-0.9718`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
