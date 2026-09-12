# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T23:52:31.574605+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12499`

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

- `market_context_high->unknown_24h` score `16103.4155` n `60` status `ready` deltaP `12.1181` edge `1341.8757` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `382.3516` n `82` status `ready` deltaP `-5.6996` edge `31.9428` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `18.2385` n `82` status `ready` deltaP `33.1004` edge `1.348` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.0442` n `82` status `ready` deltaP `39.8459` edge `1.3851` maxDD `-9.098`
- `market_context_high->crypto_alt_24h` score `10.6809` n `60` status `ready` deltaP `23.5069` edge `0.8161` maxDD `-3.9523`
- `market_context_high->equity_24h` score `10.2195` n `60` status `ready` deltaP `45.1389` edge `0.5507` maxDD `0.0`
- `news_risk_high->index_24h` score `6.022` n `82` status `ready` deltaP `41.2644` edge `0.2444` maxDD `-0.0797`
- `news_risk_high->equity_24h` score `5.9744` n `82` status `ready` deltaP `14.6511` edge `0.5782` maxDD `-6.5742`
- `news_risk_high->metal_24h` score `5.1102` n `82` status `ready` deltaP `29.2599` edge `0.2762` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `4.2356` n `60` status `ready` deltaP `42.5347` edge `0.0694` maxDD `0.0`
- `market_context_high->index_24h` score `3.7768` n `60` status `ready` deltaP `40.4514` edge `0.0843` maxDD `-0.1391`
- `market_context_high->metal_24h` score `0.3317` n `60` status `ready` deltaP `9.0973` edge `0.1069` maxDD `-3.0021`
- `risk_on_high->metal_1h` score `0.1152` n `53` status `ready` deltaP `6.2733` edge `0.0008` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `0.1152` n `53` status `ready` deltaP `6.2733` edge `0.0008` maxDD `-0.3081`
- `news_risk_high->index_4h` score `0.1008` n `82` status `ready` deltaP `7.1646` edge `0.028` maxDD `-0.6935`
- `risk_on_high->index_1h` score `-0.0094` n `53` status `ready` deltaP `5.7056` edge `0.0004` maxDD `-0.1711`
- `risk_on_and_context->index_1h` score `-0.0094` n `53` status `ready` deltaP `5.7056` edge `0.0004` maxDD `-0.1711`
- `risk_on_high->crypto_alt_4h` score `-0.0245` n `51` status `ready` deltaP `6.274` edge `0.1225` maxDD `-6.7304`
- `risk_on_and_context->crypto_alt_4h` score `-0.0245` n `51` status `ready` deltaP `6.274` edge `0.1225` maxDD `-6.7304`
- `risk_on_high->fx_1h` score `-0.0851` n `53` status `ready` deltaP `1.7512` edge `0.003` maxDD `-0.0464`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
