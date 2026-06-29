# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T08:07:27.609424+00:00`
- Price records: `672`
- Market context records: `5125`
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

- `market_context_high->unknown_24h` score `27.5789` n `65` status `ready` deltaP `28.6645` edge `2.1414` maxDD `-1.4072`
- `market_context_high->unknown_1h` score `8.6083` n `126` status `ready` deltaP `8.6256` edge `0.724` maxDD `-2.7986`
- `market_context_high->unknown_4h` score `7.0914` n `117` status `ready` deltaP `19.6008` edge `0.5625` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `5.0894` n `117` status `ready` deltaP `13.7599` edge `0.4923` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.5211` n `117` status `ready` deltaP `11.5007` edge `0.446` maxDD `-14.0065`
- `market_context_high->commodity_24h` score `0.9052` n `65` status `ready` deltaP `18.3333` edge `0.1279` maxDD `-6.726`
- `market_context_high->crypto_alt_1h` score `0.8601` n `126` status `ready` deltaP `5.9144` edge `0.1284` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.7566` n `126` status `ready` deltaP `8.2644` edge `0.1325` maxDD `-6.9639`
- `market_context_high->equity_1h` score `0.7367` n `126` status `ready` deltaP `8.0411` edge `0.0671` maxDD `-2.745`
- `market_context_high->equity_4h` score `0.5` n `117` status `ready` deltaP `7.3849` edge `0.1563` maxDD `-7.4425`
- `market_context_high->metal_1h` score `0.1813` n `126` status `ready` deltaP `7.3662` edge `0.0256` maxDD `-1.4501`
- `market_context_high->index_1h` score `0.0248` n `126` status `ready` deltaP `5.5556` edge `0.0154` maxDD `-1.0296`
- `market_context_high->index_4h` score `-0.4055` n `117` status `ready` deltaP `4.3581` edge `0.0307` maxDD `-2.9391`
- `market_context_high->commodity_1h` score `-0.6072` n `126` status `ready` deltaP `0.2091` edge `-0.0023` maxDD `-2.155`
- `market_context_high->fx_1h` score `-0.623` n `126` status `ready` deltaP `-2.1267` edge `-0.0016` maxDD `-0.7944`
- `market_context_high->metal_4h` score `-0.6782` n `117` status `ready` deltaP `0.4169` edge `0.0513` maxDD `-4.6157`
- `market_context_high->fx_4h` score `-1.0036` n `117` status `ready` deltaP `-3.2964` edge `0.0006` maxDD `-1.9169`
- `market_context_high->metal_24h` score `-1.177` n `65` status `ready` deltaP `-0.2297` edge `0.1429` maxDD `-17.381`
- `market_context_high->fx_24h` score `-1.4472` n `65` status `ready` deltaP `-2.3077` edge `-0.0094` maxDD `-1.3321`
- `market_context_high->commodity_4h` score `-2.5699` n `117` status `ready` deltaP `-1.5375` edge `-0.0304` maxDD `-7.5471`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
