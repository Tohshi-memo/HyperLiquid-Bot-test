# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-09T09:07:27.391013+00:00`
- Price records: `672`
- Market context records: `3368`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13080`

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

- `risk_on_high->crypto_major_24h` score `56.7057` n `32` status `ready` deltaP `59.7222` edge `4.3316` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `56.7057` n `32` status `ready` deltaP `59.7222` edge `4.3316` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `53.5709` n `32` status `ready` deltaP `54.6875` edge `4.1148` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `53.5709` n `32` status `ready` deltaP `54.6875` edge `4.1148` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `45.9525` n `32` status `ready` deltaP `56.7708` edge `3.4509` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `45.9525` n `32` status `ready` deltaP `56.7708` edge `3.4509` maxDD `0.0`
- `risk_on_high->index_24h` score `23.1602` n `32` status `ready` deltaP `50.8681` edge `1.5909` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.1602` n `32` status `ready` deltaP `50.8681` edge `1.5909` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `15.3858` n `32` status `ready` deltaP `27.8963` edge `1.2084` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.3858` n `32` status `ready` deltaP `27.8963` edge `1.2084` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `14.9527` n `32` status `ready` deltaP `32.6389` edge `1.0546` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `14.9527` n `32` status `ready` deltaP `32.6389` edge `1.0546` maxDD `-0.7574`
- `market_context_high->crypto_alt_24h` score `13.6979` n `157` status `ready` deltaP `18.3221` edge `2.492` maxDD `-61.6407`
- `market_context_high->index_24h` score `11.8963` n `157` status `ready` deltaP `35.5815` edge `1.0096` maxDD `-16.1026`
- `market_context_high->equity_24h` score `10.6404` n `157` status `ready` deltaP `30.6562` edge `2.0014` maxDD `-53.663`
- `risk_on_high->crypto_alt_4h` score `7.315` n `32` status `ready` deltaP `8.4604` edge `0.7376` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.315` n `32` status `ready` deltaP `8.4604` edge `0.7376` maxDD `-11.7537`
- `market_context_high->crypto_major_24h` score `4.4393` n `157` status `ready` deltaP `21.4459` edge `2.1213` maxDD `-124.9436`
- `risk_on_high->equity_4h` score `3.5463` n `32` status `ready` deltaP `14.1006` edge `0.4741` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.5463` n `32` status `ready` deltaP `14.1006` edge `0.4741` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
