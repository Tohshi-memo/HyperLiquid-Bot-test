# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T09:37:24.202722+00:00`
- Price records: `672`
- Market context records: `8183`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5904`

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

- `news_risk_high->unknown_24h` score `8669.2971` n `43` status `ready` deltaP `36.9792` edge `722.1949` maxDD `0.0`
- `market_context_high->equity_24h` score `19.6237` n `48` status `ready` deltaP `43.0555` edge `1.4393` maxDD `-4.9489`
- `market_context_high->equity_4h` score `10.5489` n `49` status `ready` deltaP `43.0221` edge `0.5985` maxDD `-0.1655`
- `market_context_high->metal_24h` score `8.5563` n `48` status `ready` deltaP `43.9236` edge `0.4202` maxDD `0.0`
- `news_risk_high->equity_4h` score `8.1464` n `48` status `ready` deltaP `30.437` edge `0.5053` maxDD `-1.3479`
- `market_context_high->index_4h` score `4.2496` n `49` status `ready` deltaP `38.2374` edge `0.1035` maxDD `-0.0092`
- `market_context_high->crypto_alt_24h` score `4.1292` n `48` status `ready` deltaP `9.8958` edge `0.7375` maxDD `-13.2606`
- `news_risk_high->equity_1h` score `3.3065` n `52` status `ready` deltaP `24.6776` edge `0.1419` maxDD `-1.1366`
- `news_risk_high->crypto_major_4h` score `3.1704` n `48` status `ready` deltaP `16.6159` edge `0.3578` maxDD `-2.3018`
- `market_context_high->metal_4h` score `3.0167` n `49` status `ready` deltaP `30.1674` edge `0.073` maxDD `-0.4846`
- `market_context_high->equity_1h` score `2.9707` n `49` status `ready` deltaP `15.1014` edge `0.1672` maxDD `-0.6254`
- `news_risk_high->index_4h` score `2.7863` n `48` status `ready` deltaP `23.5265` edge `0.0944` maxDD `-0.191`
- `market_context_high->index_24h` score `2.1553` n `48` status `ready` deltaP `19.7917` edge `0.2108` maxDD `-1.3142`
- `news_risk_high->crypto_major_1h` score `2.027` n `52` status `ready` deltaP `13.6573` edge `0.1176` maxDD `-1.1783`
- `news_risk_high->crypto_alt_1h` score `1.7178` n `52` status `ready` deltaP `13.3579` edge `0.0975` maxDD `-1.1388`
- `news_risk_high->metal_4h` score `1.6264` n `48` status `ready` deltaP `15.2439` edge `0.0807` maxDD `-0.7433`
- `news_risk_high->crypto_alt_4h` score `1.4386` n `48` status `ready` deltaP `17.0732` edge `0.2098` maxDD `-5.8012`
- `market_context_high->fx_24h` score `1.1893` n `48` status `ready` deltaP `23.6111` edge `0.0599` maxDD `-0.5196`
- `market_context_high->index_1h` score `1.1381` n `49` status `ready` deltaP `20.1363` edge `0.0255` maxDD `-0.1069`
- `market_context_high->crypto_alt_4h` score `0.6127` n `49` status `ready` deltaP `1.512` edge `0.1688` maxDD `-3.0268`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
