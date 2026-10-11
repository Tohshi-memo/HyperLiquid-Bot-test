# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T22:52:25.266652+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9132`

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

- `market_context_high->unknown_24h` score `1394.1333` n `40` status `ready` deltaP `-22.5694` edge `116.3646` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `45.3365` n `100` status `ready` deltaP `-4.7561` edge `3.8678` maxDD `-2.3109`
- `market_context_high->equity_24h` score `8.8068` n `40` status `ready` deltaP `27.6736` edge `0.5923` maxDD `-1.0977`
- `market_context_high->index_24h` score `6.418` n `40` status `ready` deltaP `52.4306` edge `0.1853` maxDD `0.0`
- `market_context_high->unknown_1h` score `3.6709` n `112` status `ready` deltaP `-2.8603` edge `0.3586` maxDD `-1.0231`
- `market_context_high->fx_24h` score `3.02` n `40` status `ready` deltaP `34.3403` edge `0.0357` maxDD `-0.0374`
- `risk_on_high->commodity_1h` score `1.922` n `33` status `ready` deltaP `23.8478` edge `0.0149` maxDD `-0.0975`
- `risk_on_and_context->commodity_1h` score `1.922` n `33` status `ready` deltaP `23.8478` edge `0.0149` maxDD `-0.0975`
- `market_context_high->crypto_major_24h` score `1.3816` n `40` status `ready` deltaP `-21.1111` edge `0.5707` maxDD `-17.8526`
- `risk_on_high->crypto_alt_1h` score `1.1953` n `33` status `ready` deltaP `11.8763` edge `0.1296` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `1.1953` n `33` status `ready` deltaP `11.8763` edge `0.1296` maxDD `-2.4421`
- `market_context_high->commodity_4h` score `0.6647` n `100` status `ready` deltaP `13.5488` edge `0.0184` maxDD `-1.6002`
- `risk_on_high->metal_1h` score `0.5966` n `33` status `ready` deltaP `11.6903` edge `0.0177` maxDD `-0.1987`
- `risk_on_and_context->metal_1h` score `0.5966` n `33` status `ready` deltaP `11.6903` edge `0.0177` maxDD `-0.1987`
- `market_context_high->fx_4h` score `0.387` n `100` status `ready` deltaP `9.4268` edge `0.0061` maxDD `-0.2692`
- `risk_on_high->crypto_major_1h` score `0.3823` n `33` status `ready` deltaP `4.5455` edge `0.084` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `0.3823` n `33` status `ready` deltaP `4.5455` edge `0.084` maxDD `-3.2233`
- `market_context_high->commodity_1h` score `0.3424` n `112` status `ready` deltaP `7.5599` edge `0.0065` maxDD `-0.6025`
- `market_context_high->crypto_alt_1h` score `0.1414` n `112` status `ready` deltaP `5.031` edge `0.088` maxDD `-4.9401`
- `market_context_high->metal_4h` score `-0.0195` n `100` status `ready` deltaP `7.628` edge `0.0198` maxDD `-1.1153`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
