# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T23:37:29.071504+00:00`
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

- `market_context_high->unknown_24h` score `15503.7149` n `61` status `ready` deltaP `12.1727` edge `1291.9002` maxDD `-0.0752`
- `news_risk_high->unknown_1h` score `379.2145` n `82` status `ready` deltaP `-5.6996` edge `31.6814` maxDD `-1.7087`
- `news_risk_high->crypto_alt_24h` score `18.2337` n `82` status `ready` deltaP `33.1004` edge `1.3476` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.0286` n `82` status `ready` deltaP `39.8459` edge `1.3838` maxDD `-9.098`
- `market_context_high->crypto_alt_24h` score `10.9763` n `61` status `ready` deltaP `23.9441` edge `0.8378` maxDD `-3.9523`
- `market_context_high->equity_24h` score `9.9457` n `61` status `ready` deltaP `44.7917` edge `0.5302` maxDD `0.0`
- `news_risk_high->equity_24h` score `6.4442` n `82` status `ready` deltaP `14.3039` edge `0.6146` maxDD `-6.1686`
- `news_risk_high->index_24h` score `6.022` n `82` status `ready` deltaP `41.2644` edge `0.2444` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `5.1265` n `82` status `ready` deltaP `29.4335` edge `0.2764` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `4.1869` n `61` status `ready` deltaP `42.3611` edge `0.0665` maxDD `0.0`
- `market_context_high->index_24h` score `3.658` n `61` status `ready` deltaP `39.0853` edge `0.0835` maxDD `-0.1391`
- `market_context_high->metal_24h` score `0.244` n `61` status `ready` deltaP `8.3419` edge `0.106` maxDD `-3.0934`
- `risk_on_high->metal_1h` score `0.1033` n `53` status `ready` deltaP `6.1236` edge `0.0008` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `0.1033` n `53` status `ready` deltaP `6.1236` edge `0.0008` maxDD `-0.3081`
- `news_risk_high->index_4h` score `0.0921` n `82` status `ready` deltaP `7.0122` edge `0.0279` maxDD `-0.6935`
- `risk_on_high->index_1h` score `-0.0094` n `53` status `ready` deltaP `5.7056` edge `0.0004` maxDD `-0.1711`
- `risk_on_and_context->index_1h` score `-0.0094` n `53` status `ready` deltaP `5.7056` edge `0.0004` maxDD `-0.1711`
- `risk_on_high->fx_1h` score `-0.0928` n `53` status `ready` deltaP `1.6015` edge `0.003` maxDD `-0.0464`
- `risk_on_and_context->fx_1h` score `-0.0928` n `53` status `ready` deltaP `1.6015` edge `0.003` maxDD `-0.0464`
- `risk_on_high->crypto_alt_4h` score `-0.108` n `50` status `ready` deltaP `5.372` edge `0.1178` maxDD `-6.7304`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
