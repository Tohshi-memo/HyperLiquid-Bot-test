# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-11T17:52:38.272610+00:00`
- Price records: `672`
- Market context records: `3607`
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

- `risk_on_high->crypto_major_24h` score `45.2395` n `32` status `ready` deltaP `48.7847` edge `3.449` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `45.2395` n `32` status `ready` deltaP `48.7847` edge `3.449` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `41.9486` n `32` status `ready` deltaP `50.8681` edge `3.1566` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `41.9486` n `32` status `ready` deltaP `50.8681` edge `3.1566` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `38.2837` n `32` status `ready` deltaP `47.9167` edge `2.886` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `38.2837` n `32` status `ready` deltaP `47.9167` edge `2.886` maxDD `-0.8779`
- `risk_on_high->index_24h` score `24.4862` n `32` status `ready` deltaP `50.8681` edge `1.7014` maxDD `0.0`
- `risk_on_and_context->index_24h` score `24.4862` n `32` status `ready` deltaP `50.8681` edge `1.7014` maxDD `0.0`
- `risk_on_high->metal_24h` score `17.4723` n `32` status `ready` deltaP `36.4583` edge `1.2391` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `17.4723` n `32` status `ready` deltaP `36.4583` edge `1.2391` maxDD `-0.7574`
- `market_context_high->equity_24h` score `16.2186` n `158` status `ready` deltaP `27.4504` edge `1.8098` maxDD `-40.9667`
- `risk_on_high->crypto_major_4h` score `13.3095` n `32` status `ready` deltaP `24.8476` edge `1.0557` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `13.3095` n `32` status `ready` deltaP `24.8476` edge `1.0557` maxDD `-5.9781`
- `market_context_high->index_24h` score `13.1363` n `158` status `ready` deltaP `35.6782` edge `1.0785` maxDD `-15.0661`
- `market_context_high->crypto_major_24h` score `9.9169` n `158` status `ready` deltaP `14.5679` edge `1.5024` maxDD `-54.8486`
- `market_context_high->metal_24h` score `6.8814` n `158` status `ready` deltaP `30.3665` edge `1.1338` maxDD `-25.9879`
- `risk_on_high->crypto_alt_4h` score `5.0431` n `32` status `ready` deltaP `5.4116` edge `0.5686` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `5.0431` n `32` status `ready` deltaP `5.4116` edge `0.5686` maxDD `-11.7537`
- `market_context_high->crypto_alt_24h` score `4.4104` n `158` status `ready` deltaP `8.6366` edge `1.1142` maxDD `-56.6728`
- `risk_on_high->equity_4h` score `3.6116` n `32` status `ready` deltaP `14.7104` edge `0.4784` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
