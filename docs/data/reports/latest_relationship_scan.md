# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T23:52:28.067867+00:00`
- Price records: `672`
- Market context records: `6229`
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

- `news_risk_high->crypto_alt_24h` score `13.5782` n `32` status `ready` deltaP `42.2194` edge `0.8648` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.3445` n `32` status `ready` deltaP `54.4218` edge `0.1659` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1695` n `32` status `ready` deltaP `43.6738` edge `0.0609` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `2.7901` n `32` status `ready` deltaP `15.625` edge `0.3315` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.3332` n `32` status `ready` deltaP `28.1437` edge `0.0207` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `2.0815` n `192` status `ready` deltaP `2.5605` edge `0.2572` maxDD `-3.7317`
- `news_risk_high->commodity_24h` score `1.6123` n `32` status `ready` deltaP `22.4702` edge `0.0051` maxDD `-0.3101`
- `news_risk_high->crypto_major_1h` score `1.3984` n `32` status `ready` deltaP `14.4274` edge `0.1298` maxDD `-2.0691`
- `market_context_high->unknown_4h` score `1.2206` n `192` status `ready` deltaP `-0.6225` edge `0.3591` maxDD `-11.925`
- `news_risk_high->crypto_alt_1h` score `0.7857` n `32` status `ready` deltaP `10.4229` edge `0.0774` maxDD `-1.6923`
- `market_context_high->metal_24h` score `-0.0525` n `192` status `ready` deltaP `19.8023` edge `0.1181` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.2019` n `32` status `ready` deltaP `8.801` edge `0.0026` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.3003` n `192` status `ready` deltaP `1.0604` edge `-0.001` maxDD `-0.5659`
- `market_context_high->commodity_1h` score `-0.5679` n `192` status `ready` deltaP `-0.7485` edge `0.0023` maxDD `-0.5708`
- `market_context_high->metal_4h` score `-0.5953` n `192` status `ready` deltaP `4.1286` edge `0.0149` maxDD `-3.4996`
- `news_risk_high->metal_1h` score `-0.8127` n `32` status `ready` deltaP `-4.0419` edge `-0.0275` maxDD `-1.6464`
- `market_context_high->crypto_alt_1h` score `-0.878` n `192` status `ready` deltaP `4.6937` edge `0.0314` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.9012` n `192` status `ready` deltaP `4.5316` edge `0.031` maxDD `-9.807`
- `market_context_high->metal_1h` score `-0.9095` n `192` status `ready` deltaP `1.1664` edge `-0.0037` maxDD `-2.0564`
- `market_context_high->equity_4h` score `-0.9364` n `192` status `ready` deltaP `1.753` edge `0.002` maxDD `-2.671`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
