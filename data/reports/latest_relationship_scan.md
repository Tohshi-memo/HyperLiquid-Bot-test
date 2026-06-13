# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-13T04:52:32.247413+00:00`
- Price records: `672`
- Market context records: `3756`
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

- `risk_on_high->crypto_major_24h` score `29.002` n `32` status `ready` deltaP `30.5556` edge `2.2174` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `29.002` n `32` status `ready` deltaP `30.5556` edge `2.2174` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `23.0559` n `32` status `ready` deltaP `35.7639` edge `1.6829` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `23.0559` n `32` status `ready` deltaP `35.7639` edge `1.6829` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `21.6625` n `32` status `ready` deltaP `31.5972` edge `1.6097` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `21.6625` n `32` status `ready` deltaP `31.5972` edge `1.6097` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.4508` n `32` status `ready` deltaP `31.25` edge `0.7459` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.4508` n `32` status `ready` deltaP `31.25` edge `0.7459` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `10.2009` n `32` status `ready` deltaP `18.75` edge `0.8373` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `10.2009` n `32` status `ready` deltaP `18.75` edge `0.8373` maxDD `-5.9781`
- `market_context_high->index_24h` score `5.4216` n `161` status `ready` deltaP `26.9022` edge `0.3864` maxDD `-7.1159`
- `market_context_high->equity_24h` score `5.3952` n `161` status `ready` deltaP `16.5092` edge `0.6143` maxDD `-13.6477`
- `market_context_high->metal_24h` score `4.564` n `161` status `ready` deltaP `27.3001` edge `0.3415` maxDD `-9.1203`
- `market_context_high->crypto_major_24h` score `4.115` n `161` status `ready` deltaP `6.9725` edge `0.7428` maxDD `-31.0425`
- `market_context_high->crypto_major_4h` score `1.6443` n `165` status `ready` deltaP `8.7879` edge `0.2685` maxDD `-10.5381`
- `risk_on_high->metal_24h` score `1.3334` n `32` status `ready` deltaP `14.0625` edge `0.0435` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `1.3334` n `32` status `ready` deltaP `14.0625` edge `0.0435` maxDD `-0.7574`
- `risk_on_high->equity_4h` score `1.2054` n `32` status `ready` deltaP `7.3933` edge `0.2187` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.2054` n `32` status `ready` deltaP `7.3933` edge `0.2187` maxDD `-5.7426`
- `risk_on_high->crypto_alt_4h` score `1.0207` n `32` status `ready` deltaP `-2.0579` edge `0.2832` maxDD `-11.7537`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
