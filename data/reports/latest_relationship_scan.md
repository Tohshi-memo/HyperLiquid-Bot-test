# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T09:07:23.754160+00:00`
- Price records: `672`
- Market context records: `8605`
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

- `news_risk_high->unknown_24h` score `4748.3772` n `64` status `ready` deltaP `34.7222` edge `395.5087` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `19.0954` n `32` status `ready` deltaP `49.6528` edge `1.3` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `5.7893` n `64` status `ready` deltaP `20.0457` edge `0.4085` maxDD `-3.4427`
- `market_context_high->crypto_major_24h` score `5.4201` n `32` status `ready` deltaP `18.75` edge `0.7935` maxDD `-14.5555`
- `market_context_high->fx_24h` score `3.6486` n `32` status `ready` deltaP `37.1528` edge `0.0902` maxDD `-0.3737`
- `news_risk_high->index_4h` score `2.2652` n `64` status `ready` deltaP `19.3979` edge `0.0785` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.7253` n `64` status `ready` deltaP `16.1022` edge `0.0841` maxDD `-2.4803`
- `market_context_high->crypto_alt_4h` score `1.5766` n `62` status `ready` deltaP `11.6837` edge `0.1492` maxDD `-5.323`
- `market_context_high->metal_24h` score `1.3516` n `32` status `ready` deltaP `11.8056` edge `0.0979` maxDD `-1.7845`
- `news_risk_high->crypto_major_4h` score `1.0959` n `64` status `ready` deltaP `7.6601` edge `0.167` maxDD `-3.5385`
- `market_context_high->index_24h` score `1.0027` n `32` status `ready` deltaP `23.0903` edge `0.0549` maxDD `-3.0893`
- `news_risk_high->crypto_alt_4h` score `0.4338` n `64` status `ready` deltaP `11.2805` edge `0.1196` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.397` n `64` status `ready` deltaP `7.6628` edge `0.0525` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3493` n `64` status `ready` deltaP `6.9143` edge `0.0499` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.1134` n `64` status `ready` deltaP `5.7354` edge `0.0044` maxDD `-0.2475`
- `news_risk_high->fx_4h` score `0.0716` n `64` status `ready` deltaP `11.9284` edge `0.0222` maxDD `-0.6604`
- `news_risk_high->metal_4h` score `0.038` n `64` status `ready` deltaP `3.0869` edge `0.0319` maxDD `-0.8085`
- `news_risk_high->index_1h` score `0.0255` n `64` status `ready` deltaP `3.9203` edge `0.0088` maxDD `-0.5338`
- `market_context_high->fx_4h` score `-0.0966` n `62` status `ready` deltaP `8.753` edge `0.0132` maxDD `-1.3685`
- `news_risk_high->metal_1h` score `-0.1467` n `64` status `ready` deltaP `3.1063` edge `0.0074` maxDD `-0.5599`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
