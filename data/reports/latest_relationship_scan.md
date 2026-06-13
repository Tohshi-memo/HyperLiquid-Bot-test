# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-13T12:07:36.639759+00:00`
- Price records: `672`
- Market context records: `3788`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13040`

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

- `risk_on_high->crypto_major_24h` score `30.5749` n `32` status `ready` deltaP `32.2917` edge `2.3369` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `30.5749` n `32` status `ready` deltaP `32.2917` edge `2.3369` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `24.96` n `32` status `ready` deltaP `39.9306` edge `1.8138` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `24.96` n `32` status `ready` deltaP `39.9306` edge `1.8138` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.0775` n `32` status `ready` deltaP `31.9444` edge `1.7253` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.0775` n `32` status `ready` deltaP `31.9444` edge `1.7253` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.5564` n `32` status `ready` deltaP `31.25` edge `0.7547` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.5564` n `32` status `ready` deltaP `31.25` edge `0.7547` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `9.9849` n `32` status `ready` deltaP `16.9207` edge `0.8315` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `9.9849` n `32` status `ready` deltaP `16.9207` edge `0.8315` maxDD `-5.9781`
- `market_context_high->equity_24h` score `7.0105` n `157` status `ready` deltaP `20.1854` edge `0.7244` maxDD `-13.6477`
- `market_context_high->index_24h` score `5.3863` n `157` status `ready` deltaP `26.7914` edge `0.3842` maxDD `-7.1159`
- `market_context_high->crypto_major_24h` score `5.3263` n `157` status `ready` deltaP `8.0282` edge `0.8367` maxDD `-31.0425`
- `market_context_high->metal_24h` score `4.5387` n `157` status `ready` deltaP `27.0148` edge `0.3413` maxDD `-9.1203`
- `market_context_high->crypto_major_4h` score `2.0224` n `174` status `ready` deltaP `10.8144` edge `0.2865` maxDD `-10.5381`
- `risk_on_high->equity_4h` score `1.5238` n `32` status `ready` deltaP `8.4604` edge `0.2524` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.5238` n `32` status `ready` deltaP `8.4604` edge `0.2524` maxDD `-5.7426`
- `risk_on_high->metal_24h` score `1.4433` n `32` status `ready` deltaP `14.2361` edge `0.0515` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `1.4433` n `32` status `ready` deltaP `14.2361` edge `0.0515` maxDD `-0.7574`
- `market_context_high->equity_4h` score `1.1154` n `174` status `ready` deltaP `9.5021` edge `0.2` maxDD `-8.2982`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
