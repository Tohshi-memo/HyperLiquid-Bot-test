# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T08:22:35.953012+00:00`
- Price records: `672`
- Market context records: `5126`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5560`

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

- `market_context_high->unknown_24h` score `28.337` n `64` status `ready` deltaP `28.6458` edge `2.2047` maxDD `-1.4072`
- `market_context_high->unknown_1h` score `8.745` n `126` status `ready` deltaP `9.2696` edge `0.7311` maxDD `-2.7986`
- `market_context_high->unknown_4h` score `7.1418` n `117` status `ready` deltaP `19.6008` edge `0.5667` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `5.0114` n `117` status `ready` deltaP `13.7599` edge `0.4858` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.4851` n `117` status `ready` deltaP `11.5007` edge `0.443` maxDD `-14.0065`
- `market_context_high->commodity_24h` score `1.1458` n `64` status `ready` deltaP `19.2708` edge `0.1391` maxDD `-5.9869`
- `market_context_high->crypto_alt_1h` score `0.8481` n `126` status `ready` deltaP `5.9144` edge `0.1274` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.7626` n `126` status `ready` deltaP `8.2644` edge `0.133` maxDD `-6.9639`
- `market_context_high->equity_1h` score `0.7403` n `126` status `ready` deltaP `8.0411` edge `0.0674` maxDD `-2.745`
- `market_context_high->equity_4h` score `0.5216` n `117` status `ready` deltaP `7.3849` edge `0.1581` maxDD `-7.4425`
- `market_context_high->metal_1h` score `0.1728` n `126` status `ready` deltaP `7.3662` edge `0.0245` maxDD `-1.4501`
- `market_context_high->index_1h` score `0.0248` n `126` status `ready` deltaP `5.5556` edge `0.0154` maxDD `-1.0296`
- `market_context_high->index_4h` score `-0.4` n `117` status `ready` deltaP `4.3581` edge `0.0314` maxDD `-2.9391`
- `market_context_high->commodity_1h` score `-0.6009` n `126` status `ready` deltaP `0.2091` edge `-0.0015` maxDD `-2.155`
- `market_context_high->fx_1h` score `-0.6238` n `126` status `ready` deltaP `-2.1267` edge `-0.0017` maxDD `-0.7944`
- `market_context_high->metal_4h` score `-0.6884` n `117` status `ready` deltaP `0.4169` edge `0.05` maxDD `-4.6157`
- `market_context_high->metal_24h` score `-0.8393` n `64` status `ready` deltaP `0.3472` edge `0.1605` maxDD `-15.9669`
- `market_context_high->fx_4h` score `-1.006` n `117` status `ready` deltaP `-3.2964` edge `0.0003` maxDD `-1.9169`
- `market_context_high->fx_24h` score `-1.3841` n `64` status `ready` deltaP `-1.7361` edge `-0.0089` maxDD `-1.2564`
- `market_context_high->commodity_4h` score `-2.5259` n `117` status `ready` deltaP `-1.5375` edge `-0.0289` maxDD `-7.3737`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
