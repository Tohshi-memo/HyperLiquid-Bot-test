# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T06:22:26.136133+00:00`
- Price records: `672`
- Market context records: `3046`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6969`

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

- `market_context_high->crypto_alt_24h` score `25.0602` n `99` status `ready` deltaP `13.0681` edge `2.3929` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `13.5359` n `99` status `ready` deltaP `24.6686` edge `1.01` maxDD `-1.7175`
- `market_context_high->commodity_24h` score `13.2516` n `99` status `ready` deltaP `43.7658` edge `0.8366` maxDD `-1.2589`
- `market_context_high->equity_24h` score `9.4468` n `99` status `ready` deltaP `24.2425` edge `1.3247` maxDD `-18.3486`
- `market_context_high->index_24h` score `9.0393` n `99` status `ready` deltaP `23.6585` edge `0.7211` maxDD `-4.7103`
- `market_context_high->commodity_4h` score `2.6541` n `129` status `ready` deltaP `17.8637` edge `0.1668` maxDD `-2.8438`
- `market_context_high->commodity_1h` score `-0.1248` n `133` status `ready` deltaP `1.434` edge `0.0223` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.4778` n `133` status `ready` deltaP `3.9789` edge `0.0185` maxDD `-4.5023`
- `market_context_high->unknown_4h` score `-0.479` n `129` status `ready` deltaP `1.6981` edge `0.0541` maxDD `-3.7602`
- `market_context_high->fx_1h` score `-0.535` n `133` status `ready` deltaP `-4.7409` edge `0.0` maxDD `-0.2921`
- `market_context_high->crypto_alt_1h` score `-0.5577` n `133` status `ready` deltaP `6.3842` edge `0.0989` maxDD `-14.7034`
- `market_context_high->equity_1h` score `-0.6812` n `133` status `ready` deltaP `3.2405` edge `0.0324` maxDD `-8.3065`
- `market_context_high->crypto_major_1h` score `-0.9082` n `133` status `ready` deltaP `4.7172` edge `0.0784` maxDD `-15.1032`
- `market_context_high->unknown_1h` score `-0.9529` n `133` status `ready` deltaP `4.6013` edge `-0.037` maxDD `-3.1801`
- `market_context_high->index_4h` score `-0.9613` n `129` status `ready` deltaP `12.5602` edge `0.0623` maxDD `-16.8761`
- `market_context_high->fx_4h` score `-1.1292` n `129` status `ready` deltaP `-8.6358` edge `-0.0037` maxDD `-1.0127`
- `market_context_high->metal_1h` score `-1.1762` n `133` status `ready` deltaP `-1.7537` edge `-0.0023` maxDD `-7.278`
- `market_context_high->fx_24h` score `-1.2905` n `99` status `ready` deltaP `-0.7575` edge `-0.0153` maxDD `-0.6418`
- `market_context_high->equity_4h` score `-2.9259` n `129` status `ready` deltaP `9.8423` edge `0.052` maxDD `-34.4188`
- `market_context_high->crypto_alt_4h` score `-3.2249` n `129` status `ready` deltaP `17.8696` edge `0.2719` maxDD `-58.6918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
