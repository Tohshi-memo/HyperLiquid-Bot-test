# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T14:37:31.200558+00:00`
- Price records: `672`
- Market context records: `7887`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14709`

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

- `market_context_high->equity_24h` score `14.1387` n `108` status `ready` deltaP `29.7163` edge `1.1143` maxDD `-6.0681`
- `market_context_high->equity_4h` score `4.9511` n `108` status `ready` deltaP `15.5414` edge `0.4066` maxDD `-5.1426`
- `market_context_high->metal_24h` score `4.5825` n `108` status `ready` deltaP `22.8918` edge `0.3127` maxDD `-0.675`
- `market_context_high->commodity_24h` score `1.6982` n `108` status `ready` deltaP `21.6253` edge `0.1557` maxDD `-7.0012`
- `market_context_high->crypto_alt_4h` score `1.6796` n `108` status `ready` deltaP `14.1425` edge `0.1574` maxDD `-3.9374`
- `market_context_high->crypto_major_4h` score `1.5563` n `108` status `ready` deltaP `15.8549` edge `0.1958` maxDD `-6.7444`
- `market_context_high->crypto_major_1h` score `1.241` n `114` status `ready` deltaP `13.586` edge `0.0537` maxDD `-1.6021`
- `market_context_high->fx_24h` score `1.2259` n `108` status `ready` deltaP `32.6145` edge `0.0485` maxDD `-3.0343`
- `market_context_high->index_4h` score `0.8873` n `108` status `ready` deltaP `15.6941` edge `0.0607` maxDD `-0.9777`
- `market_context_high->equity_1h` score `0.8798` n `114` status `ready` deltaP `12.3834` edge `0.112` maxDD `-4.2072`
- `market_context_high->commodity_4h` score `0.8015` n `108` status `ready` deltaP `11.2864` edge `0.0509` maxDD `-1.0817`
- `market_context_high->metal_4h` score `0.6341` n `108` status `ready` deltaP `9.6271` edge `0.1009` maxDD `-0.979`
- `market_context_high->index_1h` score `0.5475` n `114` status `ready` deltaP `10.55` edge `0.0183` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.4688` n `114` status `ready` deltaP `5.5836` edge `0.0451` maxDD `-1.4603`
- `market_context_high->index_24h` score `0.005` n `108` status `ready` deltaP `0.9981` edge `0.1208` maxDD `-1.496`
- `market_context_high->metal_1h` score `-0.1315` n `114` status `ready` deltaP `3.5718` edge `0.0239` maxDD `-0.6936`
- `market_context_high->commodity_1h` score `-0.2133` n `114` status `ready` deltaP `3.9908` edge `0.0029` maxDD `-1.5486`
- `market_context_high->fx_1h` score `-0.4134` n `114` status `ready` deltaP `0.648` edge `-0.0003` maxDD `-0.4112`
- `market_context_high->fx_4h` score `-0.6142` n `108` status `ready` deltaP `2.0017` edge `0.001` maxDD `-1.4467`
- `market_context_high->crypto_alt_24h` score `-1.687` n `108` status `ready` deltaP `11.8865` edge `0.234` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
