# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-11T18:52:37.047838+00:00`
- Price records: `672`
- Market context records: `3611`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13162`

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

- `risk_on_high->crypto_major_24h` score `44.3392` n `32` status `ready` deltaP `48.0903` edge `3.3786` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `44.3392` n `32` status `ready` deltaP `48.0903` edge `3.3786` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `41.2055` n `32` status `ready` deltaP `50.1736` edge `3.0993` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `41.2055` n `32` status `ready` deltaP `50.1736` edge `3.0993` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `37.2837` n `32` status `ready` deltaP `47.2222` edge `2.8073` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `37.2837` n `32` status `ready` deltaP `47.2222` edge `2.8073` maxDD `-0.8779`
- `risk_on_high->index_24h` score `24.0203` n `32` status `ready` deltaP `50.1736` edge `1.6672` maxDD `0.0`
- `risk_on_and_context->index_24h` score `24.0203` n `32` status `ready` deltaP `50.1736` edge `1.6672` maxDD `0.0`
- `risk_on_high->metal_24h` score `16.9439` n `32` status `ready` deltaP `35.7639` edge `1.1997` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `16.9439` n `32` status `ready` deltaP `35.7639` edge `1.1997` maxDD `-0.7574`
- `market_context_high->equity_24h` score `15.4755` n `158` status `ready` deltaP `26.7559` edge `1.7525` maxDD `-40.9667`
- `risk_on_high->crypto_major_4h` score `13.0627` n `32` status `ready` deltaP `24.2378` edge `1.0392` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `13.0627` n `32` status `ready` deltaP `24.2378` edge `1.0392` maxDD `-5.9781`
- `market_context_high->index_24h` score `12.6704` n `158` status `ready` deltaP `34.9837` edge `1.0443` maxDD `-15.0661`
- `market_context_high->crypto_major_24h` score `9.0166` n `158` status `ready` deltaP `13.8735` edge `1.432` maxDD `-54.8486`
- `market_context_high->metal_24h` score `6.5379` n `158` status `ready` deltaP `29.6721` edge `1.0944` maxDD `-25.9879`
- `risk_on_high->crypto_alt_4h` score `4.7459` n `32` status `ready` deltaP `4.8018` edge `0.5479` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `4.7459` n `32` status `ready` deltaP `4.8018` edge `0.5479` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.4761` n `32` status `ready` deltaP `14.1006` edge `0.4651` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.4761` n `32` status `ready` deltaP `14.1006` edge `0.4651` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
