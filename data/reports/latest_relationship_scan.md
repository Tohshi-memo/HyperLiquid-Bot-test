# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T17:07:30.230336+00:00`
- Price records: `672`
- Market context records: `7899`
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

- `market_context_high->equity_24h` score `15.0103` n `100` status `ready` deltaP `29.7361` edge `1.1868` maxDD `-6.0681`
- `market_context_high->metal_24h` score `5.9689` n `100` status `ready` deltaP `29.3813` edge `0.347` maxDD `-0.3038`
- `market_context_high->equity_4h` score `5.6252` n `104` status `ready` deltaP `20.063` edge `0.4243` maxDD `-5.1426`
- `market_context_high->commodity_24h` score `1.8959` n `100` status `ready` deltaP `21.4861` edge `0.1731` maxDD `-7.0012`
- `market_context_high->index_4h` score `1.6337` n `104` status `ready` deltaP `19.2543` edge `0.0646` maxDD `-0.8791`
- `market_context_high->crypto_alt_4h` score `1.6221` n `104` status `ready` deltaP `12.8987` edge `0.1609` maxDD `-3.9374`
- `market_context_high->metal_4h` score `1.4896` n `104` status `ready` deltaP `14.2707` edge `0.1079` maxDD `-0.979`
- `market_context_high->equity_1h` score `1.4814` n `109` status `ready` deltaP `13.0355` edge `0.1183` maxDD `-4.2072`
- `market_context_high->crypto_major_4h` score `1.4472` n `104` status `ready` deltaP `14.7162` edge `0.1943` maxDD `-6.7444`
- `market_context_high->crypto_major_1h` score `1.3535` n `109` status `ready` deltaP `15.0071` edge `0.0536` maxDD `-1.6021`
- `market_context_high->fx_24h` score `1.3117` n `100` status `ready` deltaP `34.25` edge `0.0486` maxDD `-3.0343`
- `market_context_high->index_24h` score `0.8053` n `100` status `ready` deltaP `4.1597` edge `0.1314` maxDD `-1.3621`
- `market_context_high->index_1h` score `0.6063` n `109` status `ready` deltaP `11.1511` edge `0.0192` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.5399` n `109` status `ready` deltaP `6.7118` edge `0.0435` maxDD `-1.4603`
- `market_context_high->metal_1h` score `0.2741` n `109` status `ready` deltaP `5.3068` edge `0.0253` maxDD `-0.6936`
- `market_context_high->commodity_4h` score `0.2081` n `104` status `ready` deltaP `7.7393` edge `0.0304` maxDD `-1.5058`
- `market_context_high->fx_1h` score `-0.2464` n `109` status `ready` deltaP `0.726` edge `0.0003` maxDD `-0.2715`
- `market_context_high->fx_4h` score `-0.3117` n `104` status `ready` deltaP `4.4548` edge `0.0051` maxDD `-0.9813`
- `market_context_high->commodity_1h` score `-0.3817` n `109` status `ready` deltaP `3.2771` edge `0.0032` maxDD `-1.5486`
- `market_context_high->crypto_alt_24h` score `-2.0492` n `100` status `ready` deltaP `8.312` edge `0.2114` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
