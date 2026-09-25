# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T08:07:25.818831+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11230`

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

- `market_context_high->unknown_1h` score `84.7617` n `47` status `ready` deltaP `8.4693` edge `7.0141` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `49.9969` n `47` status `ready` deltaP `30.9434` edge `3.9994` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `32.32` n `47` status `ready` deltaP `24.782` edge `2.5661` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.9155` n `47` status `ready` deltaP `34.5892` edge `1.9646` maxDD `-2.1786`
- `news_risk_high->unknown_1h` score `8.5578` n `114` status `ready` deltaP `3.9527` edge `0.7007` maxDD `-0.4452`
- `market_context_high->index_24h` score `8.0632` n `47` status `ready` deltaP `37.0198` edge `0.4381` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.7617` n `47` status `ready` deltaP `40.2667` edge `0.1522` maxDD `-0.2401`
- `news_risk_high->commodity_24h` score `3.6079` n `50` status `ready` deltaP `29.9375` edge `0.1359` maxDD `-1.7857`
- `market_context_high->index_4h` score `2.8305` n `47` status `ready` deltaP `32.5019` edge `0.0346` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.4083` n `47` status `ready` deltaP `16.2298` edge `0.1343` maxDD `-1.3444`
- `market_context_high->crypto_alt_4h` score `1.1642` n `47` status `ready` deltaP `9.688` edge `0.0992` maxDD `-3.3417`
- `market_context_high->equity_1h` score `0.9918` n `47` status `ready` deltaP `11.9155` edge `0.0435` maxDD `-1.5564`
- `market_context_high->index_1h` score `0.9595` n `47` status `ready` deltaP `14.6101` edge `0.0104` maxDD `-0.2275`
- `news_risk_high->crypto_alt_1h` score `0.9114` n `114` status `ready` deltaP `8.8823` edge `0.1078` maxDD `-4.2849`
- `market_context_high->fx_1h` score `0.4446` n `47` status `ready` deltaP `9.8101` edge `0.0073` maxDD `-0.1854`
- `market_context_high->metal_1h` score `0.064` n `47` status `ready` deltaP `4.026` edge `0.013` maxDD `-0.1976`
- `news_risk_high->metal_1h` score `0.0226` n `114` status `ready` deltaP `8.5986` edge `0.0075` maxDD `-0.7016`
- `market_context_high->crypto_major_1h` score `-0.0199` n `47` status `ready` deltaP `3.2552` edge `0.0584` maxDD `-4.5405`
- `news_risk_high->crypto_major_1h` score `-0.0692` n `114` status `ready` deltaP `3.7031` edge `0.0451` maxDD `-3.3776`
- `news_risk_high->index_1h` score `-0.138` n `114` status `ready` deltaP `3.0387` edge `0.0059` maxDD `-0.5083`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
