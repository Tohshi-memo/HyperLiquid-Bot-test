# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T18:22:24.628360+00:00`
- Price records: `672`
- Market context records: `6417`
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

- `news_risk_high->crypto_alt_24h` score `12.804` n `32` status `ready` deltaP `32.8125` edge `0.863` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.6684` n `32` status `ready` deltaP `56.25` edge `0.1807` maxDD `0.0`
- `market_context_high->unknown_24h` score `5.684` n `146` status `ready` deltaP `15.1946` edge `0.7024` maxDD `-15.0689`
- `news_risk_high->fx_4h` score `4.2289` n `32` status `ready` deltaP `44.1311` edge `0.0628` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `4.1566` n `32` status `ready` deltaP `35.7639` edge `0.1285` maxDD `-0.3101`
- `news_risk_high->crypto_major_24h` score `3.8033` n `32` status `ready` deltaP `14.4097` edge `0.4695` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.4721` n `32` status `ready` deltaP `29.7904` edge `0.0213` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.5084` n `32` status `ready` deltaP `14.4274` edge `0.1439` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.8637` n `32` status `ready` deltaP `10.2732` edge `0.0884` maxDD `-1.6923`
- `market_context_high->unknown_1h` score `0.7178` n `204` status `ready` deltaP `-5.9352` edge `0.2002` maxDD `-3.7317`
- `market_context_high->metal_4h` score `0.3755` n `202` status `ready` deltaP `11.042` edge `0.0415` maxDD `-2.7056`
- `market_context_high->index_4h` score `0.1773` n `202` status `ready` deltaP `8.941` edge `0.0228` maxDD `-0.4108`
- `news_risk_high->unknown_1h` score `-0.2716` n `32` status `ready` deltaP `6.381` edge `-0.0307` maxDD `-0.7581`
- `market_context_high->metal_24h` score `-0.2883` n `146` status `ready` deltaP `18.5978` edge `0.0959` maxDD `-11.8809`
- `market_context_high->equity_4h` score `-0.5225` n `202` status `ready` deltaP `8.0702` edge `0.0491` maxDD `-8.2573`
- `market_context_high->metal_1h` score `-0.5285` n `204` status `ready` deltaP `1.1712` edge `0.0022` maxDD `-1.8877`
- `news_risk_high->metal_1h` score `-0.5963` n `32` status `ready` deltaP `-0.2994` edge `-0.0247` maxDD `-1.6464`
- `market_context_high->fx_1h` score `-0.7106` n `204` status `ready` deltaP `-0.6018` edge `-0.0019` maxDD `-0.9308`
- `market_context_high->commodity_24h` score `-0.7364` n `146` status `ready` deltaP `-2.7207` edge `0.1157` maxDD `-5.6914`
- `market_context_high->index_1h` score `-0.7385` n `204` status `ready` deltaP `-3.7983` edge `0.0026` maxDD `-0.7564`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
