# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T17:07:34.743863+00:00`
- Price records: `672`
- Market context records: `6303`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11116`

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

- `news_risk_high->crypto_alt_24h` score `15.2166` n `32` status `ready` deltaP `43.2292` edge `0.9946` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `5.9845` n `32` status `ready` deltaP `50.5208` edge `0.1619` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1973` n `32` status `ready` deltaP `43.8262` edge `0.0622` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `4.1516` n `32` status `ready` deltaP `16.6667` edge `0.4991` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `3.1497` n `32` status `ready` deltaP `28.4722` edge `0.0932` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.4003` n `32` status `ready` deltaP `28.8922` edge `0.0213` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.4297` n `32` status `ready` deltaP `14.128` edge `0.1358` maxDD `-2.0691`
- `market_context_high->unknown_1h` score `0.9854` n `208` status `ready` deltaP `-1.9605` edge `0.196` maxDD `-3.7317`
- `news_risk_high->crypto_alt_1h` score `0.9034` n `32` status `ready` deltaP `11.4708` edge `0.0855` maxDD `-1.6923`
- `market_context_high->metal_4h` score `-0.0202` n `196` status `ready` deltaP `8.6455` edge `0.037` maxDD `-2.7056`
- `market_context_high->metal_24h` score `-0.1204` n `169` status `ready` deltaP `21.0306` edge `0.1012` maxDD `-11.8809`
- `market_context_high->metal_1h` score `-0.4114` n `208` status `ready` deltaP `3.5871` edge `0.0011` maxDD `-1.8877`
- `news_risk_high->index_24h` score `-0.4117` n `32` status `ready` deltaP `5.3819` edge `-0.0015` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.5988` n `196` status `ready` deltaP `5.3198` edge `0.0443` maxDD `-7.8562`
- `market_context_high->commodity_1h` score `-0.6046` n `208` status `ready` deltaP `-1.0796` edge `-0.002` maxDD `-2.1314`
- `market_context_high->fx_1h` score `-0.7119` n `208` status `ready` deltaP `-0.9155` edge `-0.002` maxDD `-0.7646`
- `news_risk_high->metal_1h` score `-0.7442` n `32` status `ready` deltaP `-3.1437` edge `-0.0247` maxDD `-1.6464`
- `market_context_high->index_1h` score `-0.8238` n `208` status `ready` deltaP `-3.1207` edge `0.0021` maxDD `-0.9531`
- `market_context_high->unknown_4h` score `-0.8443` n `196` status `ready` deltaP `-7.5939` edge `0.2335` maxDD `-11.925`
- `market_context_high->crypto_alt_1h` score `-0.9286` n `208` status `ready` deltaP `5.4612` edge `0.0198` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
