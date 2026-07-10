# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T00:07:28.557934+00:00`
- Price records: `672`
- Market context records: `6230`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11110`

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

- `news_risk_high->crypto_alt_24h` score `13.6358` n `32` status `ready` deltaP `42.2194` edge `0.8696` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.3285` n `32` status `ready` deltaP `54.2517` edge `0.1657` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1707` n `32` status `ready` deltaP `43.6738` edge `0.061` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `2.8322` n `32` status `ready` deltaP `15.625` edge `0.3369` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.3332` n `32` status `ready` deltaP `28.1437` edge `0.0207` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `2.1667` n `192` status `ready` deltaP `2.7102` edge `0.2633` maxDD `-3.7317`
- `news_risk_high->commodity_24h` score `1.6487` n `32` status `ready` deltaP `22.6403` edge `0.007` maxDD `-0.3101`
- `news_risk_high->crypto_major_1h` score `1.3976` n `32` status `ready` deltaP `14.4274` edge `0.1297` maxDD `-2.0691`
- `market_context_high->unknown_4h` score `1.3396` n `192` status `ready` deltaP `-0.4701` edge `0.368` maxDD `-11.925`
- `news_risk_high->crypto_alt_1h` score `0.7966` n `32` status `ready` deltaP `10.5726` edge `0.0778` maxDD `-1.6923`
- `market_context_high->metal_24h` score `-0.0525` n `192` status `ready` deltaP `19.8023` edge `0.1181` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.1988` n `32` status `ready` deltaP `8.801` edge `0.003` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.3003` n `192` status `ready` deltaP `1.0604` edge `-0.001` maxDD `-0.5659`
- `market_context_high->commodity_1h` score `-0.5811` n `192` status `ready` deltaP `-0.8982` edge `0.0022` maxDD `-0.5708`
- `market_context_high->metal_4h` score `-0.5898` n `192` status `ready` deltaP `4.1286` edge `0.0156` maxDD `-3.4996`
- `news_risk_high->metal_1h` score `-0.8041` n `32` status `ready` deltaP `-3.8922` edge `-0.0274` maxDD `-1.6464`
- `market_context_high->crypto_alt_1h` score `-0.8671` n `192` status `ready` deltaP `4.8434` edge `0.0318` maxDD `-9.3536`
- `market_context_high->metal_1h` score `-0.8964` n `192` status `ready` deltaP `1.3161` edge `-0.0036` maxDD `-2.0564`
- `market_context_high->crypto_major_1h` score `-0.902` n `192` status `ready` deltaP `4.5316` edge `0.0309` maxDD `-9.807`
- `market_context_high->equity_4h` score `-0.9146` n `192` status `ready` deltaP `1.9055` edge `0.0028` maxDD `-2.671`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
