# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T08:07:27.519107+00:00`
- Price records: `672`
- Market context records: `6478`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5869`

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

- `news_risk_high->crypto_alt_24h` score `12.5346` n `32` status `ready` deltaP `33.8542` edge `0.8336` maxDD `-0.5131`
- `market_context_high->unknown_24h` score `6.939` n `155` status `ready` deltaP `16.5266` edge `0.7981` maxDD `-15.0689`
- `news_risk_high->fx_24h` score `6.4318` n `32` status `ready` deltaP `53.4722` edge `0.1795` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.2072` n `32` status `ready` deltaP `16.1458` edge `0.5097` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `3.9474` n `36` status `ready` deltaP `41.6328` edge `0.056` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.1428` n `32` status `ready` deltaP `29.1667` edge `0.088` maxDD `-0.3101`
- `market_context_high->unknown_1h` score `1.988` n `176` status `ready` deltaP `-4.4298` edge `0.2853` maxDD `-3.2083`
- `news_risk_high->fx_1h` score `1.8191` n `38` status `ready` deltaP `22.7624` edge `0.0179` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `0.5582` n `38` status `ready` deltaP `4.751` edge `0.0936` maxDD `-2.6299`
- `market_context_high->index_4h` score `0.4599` n `172` status `ready` deltaP `11.6492` edge `0.0283` maxDD `-0.4108`
- `market_context_high->unknown_4h` score `0.275` n `172` status `ready` deltaP `-15.3928` edge `0.3661` maxDD `-10.5788`
- `market_context_high->crypto_alt_4h` score `0.2294` n `172` status `ready` deltaP `8.3983` edge `0.1185` maxDD `-6.7632`
- `market_context_high->commodity_24h` score `0.2235` n `155` status `ready` deltaP `6.082` edge `0.1649` maxDD `-5.2791`
- `market_context_high->metal_4h` score `0.1457` n `172` status `ready` deltaP `11.5889` edge `0.0437` maxDD `-2.7056`
- `news_risk_high->crypto_alt_1h` score `0.0688` n `38` status `ready` deltaP `1.434` edge `0.0502` maxDD `-2.0756`
- `news_risk_high->index_24h` score `-0.4579` n `32` status `ready` deltaP `4.6875` edge `-0.0028` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.4744` n `172` status `ready` deltaP `8.1395` edge `0.0548` maxDD `-8.2573`
- `news_risk_high->unknown_1h` score `-0.4773` n `38` status `ready` deltaP `4.6013` edge `-0.0333` maxDD `-0.9718`
- `market_context_high->metal_1h` score `-0.5193` n `176` status `ready` deltaP `1.497` edge `0.0012` maxDD `-1.8877`
- `market_context_high->crypto_major_1h` score `-0.5831` n `176` status `ready` deltaP `6.5154` edge `0.0084` maxDD `-6.7936`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
