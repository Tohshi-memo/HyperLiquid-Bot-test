# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-13T21:26:31.187108+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11712`

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

- `market_context_high->unknown_24h` score `89.4008` n `151` status `ready` deltaP `-27.1179` edge `7.9221` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.7217` n `32` status `ready` deltaP `-41.6667` edge `4.6761` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.7217` n `32` status `ready` deltaP `-41.6667` edge `4.6761` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `9.5638` n `36` status `ready` deltaP `10.0694` edge `0.7678` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `6.6011` n `36` status `ready` deltaP `35.5183` edge `0.3133` maxDD `0.0`
- `risk_on_high->commodity_24h` score `4.625` n `32` status `ready` deltaP `32.1181` edge `0.1713` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.625` n `32` status `ready` deltaP `32.1181` edge `0.1713` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.9348` n `32` status `ready` deltaP `20.6555` edge `0.1251` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.9348` n `32` status `ready` deltaP `20.6555` edge `0.1251` maxDD `-0.1258`
- `market_context_high->commodity_24h` score `2.6154` n `151` status `ready` deltaP `21.5221` edge `0.1548` maxDD `-2.4263`
- `news_risk_high->index_24h` score `2.3806` n `36` status `ready` deltaP `14.7569` edge `0.1` maxDD `0.0`
- `risk_on_high->fx_24h` score `1.6423` n `32` status `ready` deltaP `18.75` edge `0.0303` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.6423` n `32` status `ready` deltaP `18.75` edge `0.0303` maxDD `-0.1418`
- `news_risk_high->index_4h` score `1.6081` n `36` status `ready` deltaP `19.004` edge `0.0205` maxDD `-0.0546`
- `market_context_high->commodity_4h` score `1.583` n `151` status `ready` deltaP `17.3649` edge `0.08` maxDD `-2.1077`
- `news_risk_high->equity_1h` score `1.4625` n `36` status `ready` deltaP `6.9362` edge `0.1075` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.3294` n `32` status `ready` deltaP `14.1093` edge `0.04` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.3294` n `32` status `ready` deltaP `14.1093` edge `0.04` maxDD `-0.1957`
- `risk_on_high->crypto_major_24h` score `1.3166` n `32` status `ready` deltaP `12.6736` edge `0.1999` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.3166` n `32` status `ready` deltaP `12.6736` edge `0.1999` maxDD `-6.2481`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
