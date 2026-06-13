# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-13T15:15:12.224571+00:00`
- Price records: `672`
- Market context records: `3802`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13344`

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

- `risk_on_high->crypto_major_24h` score `31.0018` n `32` status `ready` deltaP `32.8125` edge `2.369` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `31.0018` n `32` status `ready` deltaP `32.8125` edge `2.369` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `25.4785` n `32` status `ready` deltaP `41.1458` edge `1.8489` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `25.4785` n `32` status `ready` deltaP `41.1458` edge `1.8489` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.2203` n `32` status `ready` deltaP `31.9444` edge `1.7372` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.2203` n `32` status `ready` deltaP `31.9444` edge `1.7372` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.4376` n `32` status `ready` deltaP `31.25` edge `0.7448` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.4376` n `32` status `ready` deltaP `31.25` edge `0.7448` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `9.452` n `32` status `ready` deltaP `14.939` edge `0.8003` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `9.452` n `32` status `ready` deltaP `14.939` edge `0.8003` maxDD `-5.9781`
- `market_context_high->equity_24h` score `7.4013` n `152` status `ready` deltaP `20.7511` edge `0.7532` maxDD `-13.6477`
- `market_context_high->crypto_major_24h` score `5.6583` n `152` status `ready` deltaP `7.648` edge `0.8669` maxDD `-31.0425`
- `market_context_high->index_24h` score `5.3578` n `152` status `ready` deltaP `26.6447` edge `0.3828` maxDD `-7.1159`
- `market_context_high->metal_24h` score `4.3413` n `152` status `ready` deltaP `26.4072` edge `0.3289` maxDD `-9.1203`
- `market_context_high->crypto_major_4h` score `2.6254` n `182` status `ready` deltaP `13.222` edge `0.3207` maxDD `-10.5381`
- `risk_on_high->equity_4h` score `1.4473` n `32` status `ready` deltaP `7.5457` edge `0.2487` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.4473` n `32` status `ready` deltaP `7.5457` edge `0.2487` maxDD `-5.7426`
- `risk_on_high->commodity_4h` score `1.3637` n `32` status `ready` deltaP `16.5396` edge `0.0901` maxDD `-3.6044`
- `risk_on_and_context->commodity_4h` score `1.3637` n `32` status `ready` deltaP `16.5396` edge `0.0901` maxDD `-3.6044`
- `risk_on_high->metal_24h` score `1.3197` n `32` status `ready` deltaP `14.2361` edge `0.0412` maxDD `-0.7574`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
