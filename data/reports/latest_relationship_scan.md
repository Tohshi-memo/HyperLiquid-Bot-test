# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-13T08:52:33.778773+00:00`
- Price records: `672`
- Market context records: `3773`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13073`

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

- `risk_on_high->crypto_major_24h` score `29.7098` n `32` status `ready` deltaP `31.4236` edge `2.2706` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `29.7098` n `32` status `ready` deltaP `31.4236` edge `2.2706` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `24.0271` n `32` status `ready` deltaP `37.6736` edge `1.7511` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `24.0271` n `32` status `ready` deltaP `37.6736` edge `1.7511` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `22.4355` n `32` status `ready` deltaP `31.9444` edge `1.6718` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `22.4355` n `32` status `ready` deltaP `31.9444` edge `1.6718` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.5264` n `32` status `ready` deltaP `31.25` edge `0.7522` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.5264` n `32` status `ready` deltaP `31.25` edge `0.7522` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `10.2111` n `32` status `ready` deltaP `18.2927` edge `0.8412` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `10.2111` n `32` status `ready` deltaP `18.2927` edge `0.8412` maxDD `-5.9781`
- `market_context_high->equity_24h` score `6.0775` n `157` status `ready` deltaP `17.9284` edge `0.6617` maxDD `-13.6477`
- `market_context_high->index_24h` score `5.3563` n `157` status `ready` deltaP `26.7914` edge `0.3817` maxDD `-7.1159`
- `market_context_high->crypto_major_24h` score `4.4612` n `157` status `ready` deltaP `7.1601` edge `0.7704` maxDD `-31.0425`
- `market_context_high->metal_24h` score `4.4253` n `157` status `ready` deltaP `26.8412` edge `0.333` maxDD `-9.1203`
- `market_context_high->crypto_major_4h` score `1.8525` n `161` status `ready` deltaP `9.17` edge `0.2833` maxDD `-10.5381`
- `risk_on_high->equity_4h` score `1.4447` n `32` status `ready` deltaP `8.1555` edge `0.2443` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.4447` n `32` status `ready` deltaP `8.1555` edge `0.2443` maxDD `-5.7426`
- `risk_on_high->metal_24h` score `1.3298` n `32` status `ready` deltaP `14.0625` edge `0.0432` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `1.3298` n `32` status `ready` deltaP `14.0625` edge `0.0432` maxDD `-0.7574`
- `risk_on_high->crypto_alt_4h` score `1.1153` n `32` status `ready` deltaP `-2.2104` edge `0.2921` maxDD `-11.7537`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
