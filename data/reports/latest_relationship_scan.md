# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-13T05:07:30.065893+00:00`
- Price records: `672`
- Market context records: `3757`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13105`

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

- `risk_on_high->crypto_major_24h` score `29.0987` n `32` status `ready` deltaP `30.7292` edge `2.2243` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `29.0987` n `32` status `ready` deltaP `30.7292` edge `2.2243` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `23.137` n `32` status `ready` deltaP `35.9375` edge `1.6885` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `23.137` n `32` status `ready` deltaP `35.9375` edge `1.6885` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `21.7796` n `32` status `ready` deltaP `31.7708` edge `1.6183` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `21.7796` n `32` status `ready` deltaP `31.7708` edge `1.6183` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.4688` n `32` status `ready` deltaP `31.25` edge `0.7474` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.4688` n `32` status `ready` deltaP `31.25` edge `0.7474` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `10.2779` n `32` status `ready` deltaP `18.9024` edge `0.8427` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `10.2779` n `32` status `ready` deltaP `18.9024` edge `0.8427` maxDD `-5.9781`
- `market_context_high->equity_24h` score `5.4763` n `161` status `ready` deltaP `16.6828` edge `0.6199` maxDD `-13.6477`
- `market_context_high->index_24h` score `5.4396` n `161` status `ready` deltaP `26.9022` edge `0.3879` maxDD `-7.1159`
- `market_context_high->metal_24h` score `4.57` n `161` status `ready` deltaP `27.3001` edge `0.342` maxDD `-9.1203`
- `market_context_high->crypto_major_24h` score `4.2117` n `161` status `ready` deltaP `7.1461` edge `0.7497` maxDD `-31.0425`
- `market_context_high->crypto_major_4h` score `1.7213` n `165` status `ready` deltaP `8.9403` edge `0.2739` maxDD `-10.5381`
- `risk_on_high->metal_24h` score `1.3394` n `32` status `ready` deltaP `14.0625` edge `0.044` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `1.3394` n `32` status `ready` deltaP `14.0625` edge `0.044` maxDD `-0.7574`
- `risk_on_high->equity_4h` score `1.2227` n `32` status `ready` deltaP `7.5457` edge `0.2199` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.2227` n `32` status `ready` deltaP `7.5457` edge `0.2199` maxDD `-5.7426`
- `risk_on_high->crypto_alt_4h` score `1.1049` n `32` status `ready` deltaP `-1.9055` edge `0.2892` maxDD `-11.7537`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
