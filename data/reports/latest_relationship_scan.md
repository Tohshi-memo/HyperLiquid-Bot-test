# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-13T11:22:31.120849+00:00`
- Price records: `672`
- Market context records: `3784`
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

- `risk_on_high->crypto_major_24h` score `30.4093` n `32` status `ready` deltaP `32.2917` edge `2.3231` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `30.4093` n `32` status `ready` deltaP `32.2917` edge `2.3231` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `24.742` n `32` status `ready` deltaP `39.4097` edge `1.7991` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `24.742` n `32` status `ready` deltaP `39.4097` edge `1.7991` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `22.9539` n `32` status `ready` deltaP `31.9444` edge `1.715` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `22.9539` n `32` status `ready` deltaP `31.9444` edge `1.715` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.548` n `32` status `ready` deltaP `31.25` edge `0.754` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.548` n `32` status `ready` deltaP `31.25` edge `0.754` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `10.0491` n `32` status `ready` deltaP `17.378` edge `0.8338` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `10.0491` n `32` status `ready` deltaP `17.378` edge `0.8338` maxDD `-5.9781`
- `market_context_high->equity_24h` score `6.7924` n `157` status `ready` deltaP `19.6645` edge `0.7097` maxDD `-13.6477`
- `market_context_high->index_24h` score `5.3779` n `157` status `ready` deltaP `26.7914` edge `0.3835` maxDD `-7.1159`
- `market_context_high->crypto_major_24h` score `5.1607` n `157` status `ready` deltaP `8.0282` edge `0.8229` maxDD `-31.0425`
- `market_context_high->metal_24h` score `4.5291` n `157` status `ready` deltaP `27.0148` edge `0.3405` maxDD `-9.1203`
- `market_context_high->crypto_major_4h` score `2.051` n `171` status `ready` deltaP `10.6163` edge `0.2902` maxDD `-10.5381`
- `risk_on_high->equity_4h` score `1.4852` n `32` status `ready` deltaP `8.003` edge `0.2505` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.4852` n `32` status `ready` deltaP `8.003` edge `0.2505` maxDD `-5.7426`
- `risk_on_high->metal_24h` score `1.4337` n `32` status `ready` deltaP `14.2361` edge `0.0507` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `1.4337` n `32` status `ready` deltaP `14.2361` edge `0.0507` maxDD `-0.7574`
- `market_context_high->equity_4h` score `1.2216` n `171` status `ready` deltaP `10.2143` edge `0.2041` maxDD `-8.2982`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
