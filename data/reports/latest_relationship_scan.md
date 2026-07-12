# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T05:37:26.395048+00:00`
- Price records: `672`
- Market context records: `6467`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5907`

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

- `news_risk_high->crypto_alt_24h` score `12.1341` n `32` status `ready` deltaP `32.1181` edge `0.8118` maxDD `-0.5131`
- `market_context_high->unknown_24h` score `6.8536` n `153` status `ready` deltaP `15.8497` edge `0.7955` maxDD `-15.0689`
- `news_risk_high->fx_24h` score `6.3328` n `32` status `ready` deltaP `52.4306` edge `0.1782` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.0962` n `32` status `ready` deltaP `42.6067` edge `0.0619` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `3.822` n `32` status `ready` deltaP `14.4097` edge `0.4719` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `3.4269` n `32` status `ready` deltaP `30.9028` edge `0.1001` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `1.843` n `38` status `ready` deltaP `23.0618` edge `0.0179` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.5375` n `172` status `ready` deltaP `-5.7861` edge `0.2568` maxDD `-3.2083`
- `news_risk_high->crypto_major_1h` score `0.5489` n `38` status `ready` deltaP `4.751` edge `0.0924` maxDD `-2.6299`
- `market_context_high->commodity_24h` score `0.4167` n `153` status `ready` deltaP `7.3121` edge `0.1728` maxDD `-5.2791`
- `market_context_high->index_4h` score `0.3552` n `172` status `ready` deltaP `10.4297` edge `0.0277` maxDD `-0.4108`
- `market_context_high->unknown_4h` score `0.2619` n `172` status `ready` deltaP `-15.2404` edge `0.364` maxDD `-10.5788`
- `market_context_high->crypto_alt_4h` score `0.1` n `172` status `ready` deltaP `7.6361` edge `0.1128` maxDD `-6.7632`
- `news_risk_high->crypto_alt_1h` score `0.0578` n `38` status `ready` deltaP `1.434` edge `0.0488` maxDD `-2.0756`
- `market_context_high->metal_4h` score `0.0445` n `172` status `ready` deltaP `10.3694` edge `0.0434` maxDD `-2.7056`
- `news_risk_high->index_24h` score `-0.4618` n `32` status `ready` deltaP `4.6875` edge `-0.0033` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.5513` n `172` status `ready` deltaP `0.8982` edge `0.0011` maxDD `-1.8877`
- `market_context_high->equity_4h` score `-0.5794` n `172` status `ready` deltaP `6.6151` edge `0.0515` maxDD `-8.2573`
- `market_context_high->commodity_1h` score `-0.5923` n `172` status `ready` deltaP `-0.4839` edge `-0.0044` maxDD `-2.1314`
- `news_risk_high->unknown_1h` score `-0.6511` n `38` status `ready` deltaP `3.8528` edge `-0.0428` maxDD `-0.9718`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
