# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-11T22:52:28.150087+00:00`
- Price records: `672`
- Market context records: `3628`
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

- `risk_on_high->crypto_major_24h` score `40.6046` n `32` status `ready` deltaP `45.3125` edge `3.0859` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `40.6046` n `32` status `ready` deltaP `45.3125` edge `3.0859` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `37.5261` n `32` status `ready` deltaP `47.3958` edge `2.8112` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `37.5261` n `32` status `ready` deltaP `47.3958` edge `2.8112` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `33.0571` n `32` status `ready` deltaP `44.4444` edge `2.4736` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `33.0571` n `32` status `ready` deltaP `44.4444` edge `2.4736` maxDD `-0.8779`
- `risk_on_high->index_24h` score `21.5613` n `32` status `ready` deltaP `47.3958` edge `1.4808` maxDD `0.0`
- `risk_on_and_context->index_24h` score `21.5613` n `32` status `ready` deltaP `47.3958` edge `1.4808` maxDD `0.0`
- `risk_on_high->metal_24h` score `14.0265` n `32` status `ready` deltaP `32.9861` edge `0.9751` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `14.0265` n `32` status `ready` deltaP `32.9861` edge `0.9751` maxDD `-0.7574`
- `risk_on_high->crypto_major_4h` score `12.357` n `32` status `ready` deltaP `22.2561` edge `0.9936` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `12.357` n `32` status `ready` deltaP `22.2561` edge `0.9936` maxDD `-5.9781`
- `market_context_high->equity_24h` score `11.796` n `158` status `ready` deltaP `23.9781` edge `1.4644` maxDD `-40.9667`
- `market_context_high->index_24h` score `10.2114` n `158` status `ready` deltaP `32.2059` edge `0.8579` maxDD `-15.0661`
- `market_context_high->crypto_major_24h` score `5.282` n `158` status `ready` deltaP `11.0957` edge `1.1393` maxDD `-54.8486`
- `market_context_high->metal_24h` score `4.6416` n `158` status `ready` deltaP `26.8943` edge `0.8698` maxDD `-25.9879`
- `risk_on_high->crypto_alt_4h` score `3.9238` n `32` status `ready` deltaP `2.8201` edge `0.4926` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `3.9238` n `32` status `ready` deltaP `2.8201` edge `0.4926` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `2.7775` n `32` status `ready` deltaP `11.6616` edge `0.3918` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.7775` n `32` status `ready` deltaP `11.6616` edge `0.3918` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
