# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-11T17:37:43.795220+00:00`
- Price records: `672`
- Market context records: `3606`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13138`

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

- `risk_on_high->crypto_major_24h` score `45.4466` n `32` status `ready` deltaP `48.9583` edge `3.4651` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `45.4466` n `32` status `ready` deltaP `48.9583` edge `3.4651` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `42.1161` n `32` status `ready` deltaP `51.0417` edge `3.1694` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `42.1161` n `32` status `ready` deltaP `51.0417` edge `3.1694` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `38.5231` n `32` status `ready` deltaP `48.0903` edge `2.9048` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `38.5231` n `32` status `ready` deltaP `48.0903` edge `2.9048` maxDD `-0.8779`
- `risk_on_high->index_24h` score `24.5913` n `32` status `ready` deltaP `51.0417` edge `1.709` maxDD `0.0`
- `risk_on_and_context->index_24h` score `24.5913` n `32` status `ready` deltaP `51.0417` edge `1.709` maxDD `0.0`
- `risk_on_high->metal_24h` score `17.6037` n `32` status `ready` deltaP `36.6319` edge `1.2489` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `17.6037` n `32` status `ready` deltaP `36.6319` edge `1.2489` maxDD `-0.7574`
- `market_context_high->equity_24h` score `16.3861` n `158` status `ready` deltaP `27.624` edge `1.8226` maxDD `-40.9667`
- `risk_on_high->crypto_major_4h` score `13.3601` n `32` status `ready` deltaP `25.0` edge `1.0589` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `13.3601` n `32` status `ready` deltaP `25.0` edge `1.0589` maxDD `-5.9781`
- `market_context_high->index_24h` score `13.2414` n `158` status `ready` deltaP `35.8518` edge `1.0861` maxDD `-15.0661`
- `market_context_high->crypto_major_24h` score `10.124` n `158` status `ready` deltaP `14.7415` edge `1.5185` maxDD `-54.8486`
- `market_context_high->metal_24h` score `6.9668` n `158` status `ready` deltaP `30.5401` edge `1.1436` maxDD `-25.9879`
- `risk_on_high->crypto_alt_4h` score `5.1141` n `32` status `ready` deltaP `5.564` edge `0.5735` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `5.1141` n `32` status `ready` deltaP `5.564` edge `0.5735` maxDD `-11.7537`
- `market_context_high->crypto_alt_24h` score `4.6499` n `158` status `ready` deltaP `8.8102` edge `1.133` maxDD `-56.6728`
- `risk_on_high->equity_4h` score `3.6398` n `32` status `ready` deltaP `14.8628` edge `0.481` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
