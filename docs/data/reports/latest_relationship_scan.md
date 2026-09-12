# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T23:07:30.984309+00:00`
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

- `market_context_high->unknown_24h` score `14796.1734` n `63` status `ready` deltaP `12.2768` edge `1232.9378` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `382.3744` n `82` status `ready` deltaP `-5.5499` edge `31.9437` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `18.2301` n `82` status `ready` deltaP `33.1004` edge `1.3473` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `17.995` n `82` status `ready` deltaP `39.8459` edge `1.381` maxDD `-9.098`
- `market_context_high->crypto_alt_24h` score `11.5301` n `63` status `ready` deltaP `24.7768` edge `0.8784` maxDD `-3.9523`
- `market_context_high->equity_24h` score `10.0518` n `63` status `ready` deltaP `44.6181` edge `0.5402` maxDD `0.0`
- `news_risk_high->index_24h` score `6.022` n `82` status `ready` deltaP `41.2644` edge `0.2444` maxDD `-0.0797`
- `news_risk_high->equity_24h` score `5.9027` n `82` status `ready` deltaP `14.1303` edge `0.5757` maxDD `-6.5742`
- `news_risk_high->metal_24h` score `5.144` n `82` status `ready` deltaP `29.6071` edge `0.2767` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `3.9285` n `63` status `ready` deltaP `40.6002` edge `0.0609` maxDD `-0.0019`
- `market_context_high->index_24h` score `3.4246` n `63` status `ready` deltaP `36.4832` edge `0.0814` maxDD `-0.1391`
- `risk_on_high->metal_1h` score `0.1033` n `53` status `ready` deltaP `6.1236` edge `0.0008` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `0.1033` n `53` status `ready` deltaP `6.1236` edge `0.0008` maxDD `-0.3081`
- `news_risk_high->index_4h` score `0.0834` n `82` status `ready` deltaP `6.8597` edge `0.0278` maxDD `-0.6935`
- `market_context_high->metal_24h` score `0.0664` n `63` status `ready` deltaP `6.7461` edge `0.1044` maxDD `-3.269`
- `risk_on_high->index_1h` score `-0.0094` n `53` status `ready` deltaP `5.7056` edge `0.0004` maxDD `-0.1711`
- `risk_on_and_context->index_1h` score `-0.0094` n `53` status `ready` deltaP `5.7056` edge `0.0004` maxDD `-0.1711`
- `risk_on_high->crypto_alt_4h` score `-0.0775` n `48` status `ready` deltaP `5.3862` edge `0.1165` maxDD `-6.6544`
- `risk_on_and_context->crypto_alt_4h` score `-0.0775` n `48` status `ready` deltaP `5.3862` edge `0.1165` maxDD `-6.6544`
- `risk_on_high->fx_1h` score `-0.0928` n `53` status `ready` deltaP `1.6015` edge `0.003` maxDD `-0.0464`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
