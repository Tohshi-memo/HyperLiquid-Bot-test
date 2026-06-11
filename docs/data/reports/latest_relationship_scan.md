# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-11T23:07:28.982575+00:00`
- Price records: `672`
- Market context records: `3629`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13163`

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

- `risk_on_high->crypto_major_24h` score `40.3975` n `32` status `ready` deltaP `45.1389` edge `3.0698` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `40.3975` n `32` status `ready` deltaP `45.1389` edge `3.0698` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `37.277` n `32` status `ready` deltaP `47.2222` edge `2.7916` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `37.277` n `32` status `ready` deltaP `47.2222` edge `2.7916` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `32.8344` n `32` status `ready` deltaP `44.2708` edge `2.4562` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `32.8344` n `32` status `ready` deltaP `44.2708` edge `2.4562` maxDD `-0.8779`
- `risk_on_high->index_24h` score `21.401` n `32` status `ready` deltaP `47.2222` edge `1.4686` maxDD `0.0`
- `risk_on_and_context->index_24h` score `21.401` n `32` status `ready` deltaP `47.2222` edge `1.4686` maxDD `0.0`
- `risk_on_high->metal_24h` score `13.8254` n `32` status `ready` deltaP `32.8125` edge `0.9595` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `13.8254` n `32` status `ready` deltaP `32.8125` edge `0.9595` maxDD `-0.7574`
- `risk_on_high->crypto_major_4h` score `12.3256` n `32` status `ready` deltaP `22.1037` edge `0.992` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `12.3256` n `32` status `ready` deltaP `22.1037` edge `0.992` maxDD `-5.9781`
- `market_context_high->equity_24h` score `11.547` n `158` status `ready` deltaP `23.8045` edge `1.4448` maxDD `-40.9667`
- `market_context_high->index_24h` score `10.0511` n `158` status `ready` deltaP `32.0323` edge `0.8457` maxDD `-15.0661`
- `market_context_high->crypto_major_24h` score `5.0749` n `158` status `ready` deltaP `10.9221` edge `1.1232` maxDD `-54.8486`
- `market_context_high->metal_24h` score `4.5109` n `158` status `ready` deltaP `26.7207` edge `0.8542` maxDD `-25.9879`
- `risk_on_high->crypto_alt_4h` score `3.8828` n `32` status `ready` deltaP `2.6677` edge `0.4902` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `3.8828` n `32` status `ready` deltaP `2.6677` edge `0.4902` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `2.747` n `32` status `ready` deltaP `11.5091` edge `0.3889` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.747` n `32` status `ready` deltaP `11.5091` edge `0.3889` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
