# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T16:07:26.032109+00:00`
- Price records: `672`
- Market context records: `7894`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14713`

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

- `market_context_high->equity_24h` score `14.6068` n `104` status `ready` deltaP `29.9727` edge `1.1516` maxDD `-6.0681`
- `market_context_high->equity_4h` score `5.2832` n `106` status `ready` deltaP `17.1669` edge `0.4151` maxDD `-5.1426`
- `market_context_high->metal_24h` score `5.2752` n `104` status `ready` deltaP `26.0613` edge `0.3299` maxDD `-0.4568`
- `market_context_high->commodity_24h` score `1.8439` n `104` status `ready` deltaP `21.8104` edge `0.1666` maxDD `-7.0012`
- `market_context_high->crypto_alt_4h` score `1.6159` n `106` status `ready` deltaP `13.4961` edge `0.1564` maxDD `-3.9374`
- `market_context_high->crypto_major_4h` score `1.4728` n `106` status `ready` deltaP `15.2609` edge `0.1928` maxDD `-6.7444`
- `market_context_high->equity_1h` score `1.3505` n `110` status `ready` deltaP `11.8346` edge `0.1154` maxDD `-4.2072`
- `market_context_high->fx_24h` score `1.3312` n `104` status `ready` deltaP `34.6088` edge `0.0487` maxDD `-3.0343`
- `market_context_high->index_4h` score `1.2508` n `106` status `ready` deltaP `17.3196` edge `0.0624` maxDD `-0.8904`
- `market_context_high->crypto_major_1h` score `1.1419` n `110` status `ready` deltaP `13.0376` edge `0.0491` maxDD `-1.6021`
- `market_context_high->metal_4h` score `1.0445` n `106` status `ready` deltaP `11.7013` edge `0.1046` maxDD `-0.979`
- `market_context_high->commodity_4h` score `0.5891` n `106` status `ready` deltaP `9.7566` edge `0.0434` maxDD `-1.0817`
- `market_context_high->index_1h` score `0.5719` n `110` status `ready` deltaP `10.7508` edge `0.019` maxDD `-0.7743`
- `market_context_high->index_24h` score `0.4` n `104` status `ready` deltaP `2.463` edge `0.1261` maxDD `-1.4019`
- `market_context_high->crypto_alt_1h` score `0.3585` n `110` status `ready` deltaP `4.834` edge `0.0409` maxDD `-1.4603`
- `market_context_high->metal_1h` score `0.1806` n `110` status `ready` deltaP `4.8231` edge `0.0249` maxDD `-0.6936`
- `market_context_high->fx_1h` score `-0.2376` n `110` status `ready` deltaP `1.193` edge `-0.0002` maxDD `-0.3901`
- `market_context_high->commodity_1h` score `-0.2797` n `110` status `ready` deltaP `2.76` edge `0.0026` maxDD `-1.5486`
- `market_context_high->fx_4h` score `-0.4308` n `106` status `ready` deltaP `2.8403` edge `0.0029` maxDD `-1.1648`
- `market_context_high->crypto_alt_24h` score `-1.8539` n `104` status `ready` deltaP `10.2076` edge `0.2238` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
