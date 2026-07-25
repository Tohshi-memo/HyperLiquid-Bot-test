# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T15:52:27.446443+00:00`
- Price records: `672`
- Market context records: `7893`
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

- `market_context_high->equity_24h` score `14.4926` n `105` status `ready` deltaP `30.0008` edge `1.1419` maxDD `-6.0681`
- `market_context_high->equity_4h` score `5.1823` n `107` status `ready` deltaP `16.5057` edge `0.4111` maxDD `-5.1426`
- `market_context_high->metal_24h` score `5.1039` n `105` status `ready` deltaP `25.2463` edge `0.3256` maxDD `-0.4864`
- `market_context_high->commodity_24h` score `1.8248` n `105` status `ready` deltaP `21.8569` edge `0.1647` maxDD `-7.0012`
- `market_context_high->crypto_alt_4h` score `1.6588` n `107` status `ready` deltaP `13.8224` edge `0.1578` maxDD `-3.9374`
- `market_context_high->crypto_major_4h` score `1.5208` n `107` status `ready` deltaP `15.5607` edge `0.1948` maxDD `-6.7444`
- `market_context_high->fx_24h` score `1.3045` n `105` status `ready` deltaP `34.0959` edge `0.0487` maxDD `-3.0343`
- `market_context_high->equity_1h` score `1.289` n `111` status `ready` deltaP `11.2613` edge `0.1141` maxDD `-4.2072`
- `market_context_high->index_4h` score `1.1441` n `107` status `ready` deltaP `16.8111` edge `0.0615` maxDD `-0.9255`
- `market_context_high->crypto_major_1h` score `1.102` n `111` status `ready` deltaP `12.614` edge `0.0486` maxDD `-1.6021`
- `market_context_high->metal_4h` score `0.944` n `107` status `ready` deltaP `11.2804` edge `0.1032` maxDD `-0.979`
- `market_context_high->commodity_4h` score `0.6068` n `107` status `ready` deltaP `9.9037` edge `0.0439` maxDD `-1.0817`
- `market_context_high->index_1h` score `0.5996` n `111` status `ready` deltaP `11.1112` edge `0.0189` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.3258` n `111` status `ready` deltaP `4.5005` edge `0.0404` maxDD `-1.4603`
- `market_context_high->index_24h` score `0.2947` n `105` status `ready` deltaP `2.0417` edge `0.1246` maxDD `-1.4255`
- `market_context_high->metal_1h` score `0.089` n `111` status `ready` deltaP `4.3481` edge `0.0246` maxDD `-0.6936`
- `market_context_high->fx_1h` score `-0.2619` n `111` status `ready` deltaP `0.7507` edge `-0.0003` maxDD `-0.3963`
- `market_context_high->commodity_1h` score `-0.2663` n `111` status `ready` deltaP `3.003` edge `0.0027` maxDD `-1.5486`
- `market_context_high->fx_4h` score `-0.4673` n `107` status `ready` deltaP `2.4171` edge `0.0022` maxDD `-1.2583`
- `market_context_high->crypto_alt_24h` score `-1.8096` n `105` status `ready` deltaP `10.6838` edge `0.2263` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
