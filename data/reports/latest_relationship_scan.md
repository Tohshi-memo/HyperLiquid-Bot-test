# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T16:52:34.170943+00:00`
- Price records: `672`
- Market context records: `7898`
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

- `market_context_high->equity_24h` score `14.9094` n `101` status `ready` deltaP `29.7803` edge `1.1781` maxDD `-6.0681`
- `market_context_high->metal_24h` score `5.7946` n `101` status `ready` deltaP `28.5001` edge `0.3428` maxDD `-0.3268`
- `market_context_high->equity_4h` score `5.5546` n `104` status `ready` deltaP `19.2543` edge `0.4238` maxDD `-5.1426`
- `market_context_high->commodity_24h` score `1.8806` n `101` status `ready` deltaP `21.5501` edge `0.1714` maxDD `-7.0012`
- `market_context_high->crypto_alt_4h` score `1.6077` n `104` status `ready` deltaP `12.8987` edge `0.1597` maxDD `-3.9374`
- `market_context_high->index_4h` score `1.5154` n `104` status `ready` deltaP `18.4457` edge `0.0643` maxDD `-0.8791`
- `market_context_high->equity_1h` score `1.4328` n `110` status `ready` deltaP `12.5935` edge `0.1172` maxDD `-4.2072`
- `market_context_high->crypto_major_4h` score `1.4184` n `104` status `ready` deltaP `14.7162` edge `0.1919` maxDD `-6.7444`
- `market_context_high->crypto_major_1h` score `1.3853` n `110` status `ready` deltaP `15.3157` edge `0.0542` maxDD `-1.6021`
- `market_context_high->metal_4h` score `1.3725` n `104` status `ready` deltaP `13.4615` edge `0.1077` maxDD `-0.979`
- `market_context_high->fx_24h` score `1.3269` n `101` status `ready` deltaP `34.5417` edge `0.0486` maxDD `-3.0343`
- `market_context_high->index_24h` score `0.7032` n `101` status `ready` deltaP `3.7043` edge `0.1301` maxDD `-1.3621`
- `market_context_high->crypto_alt_1h` score `0.5767` n `110` status `ready` deltaP `7.1121` edge `0.0439` maxDD `-1.4603`
- `market_context_high->index_1h` score `0.5719` n `110` status `ready` deltaP `10.7508` edge `0.019` maxDD `-0.7743`
- `market_context_high->commodity_4h` score `0.385` n `104` status `ready` deltaP `8.548` edge `0.0353` maxDD `-1.1495`
- `market_context_high->metal_1h` score `0.2318` n `110` status `ready` deltaP `4.8231` edge `0.025` maxDD `-0.6936`
- `market_context_high->fx_1h` score `-0.2667` n `110` status `ready` deltaP `0.4341` edge `0.0001` maxDD `-0.3086`
- `market_context_high->fx_4h` score `-0.3577` n `104` status `ready` deltaP `3.6462` edge `0.0046` maxDD `-0.9813`
- `market_context_high->commodity_1h` score `-0.3612` n `110` status `ready` deltaP `3.5189` edge `0.0033` maxDD `-1.5486`
- `market_context_high->crypto_alt_24h` score `-1.9896` n `101` status `ready` deltaP `8.8269` edge `0.2156` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
