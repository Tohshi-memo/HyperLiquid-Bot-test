# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-09T19:29:29.751676+00:00`
- Price records: `672`
- Market context records: `3412`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13116`

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

- `risk_on_high->crypto_major_24h` score `55.8182` n `32` status `ready` deltaP `58.3333` edge `4.2669` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `55.8182` n `32` status `ready` deltaP `58.3333` edge `4.2669` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `55.4114` n `32` status `ready` deltaP `57.6389` edge `4.2485` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `55.4114` n `32` status `ready` deltaP `57.6389` edge `4.2485` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `45.8585` n `32` status `ready` deltaP `56.0764` edge `3.4477` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `45.8585` n `32` status `ready` deltaP `56.0764` edge `3.4477` maxDD `0.0`
- `risk_on_high->index_24h` score `23.8655` n `32` status `ready` deltaP `51.3889` edge `1.6462` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.8655` n `32` status `ready` deltaP `51.3889` edge `1.6462` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `21.6372` n `154` status `ready` deltaP `18.5561` edge `2.4753` maxDD `-56.6728`
- `market_context_high->crypto_major_24h` score `20.9407` n `154` status `ready` deltaP `24.4453` edge `2.3552` maxDD `-54.8486`
- `market_context_high->equity_24h` score `20.6397` n `154` status `ready` deltaP `33.3491` edge `2.1389` maxDD `-40.9667`
- `risk_on_high->crypto_major_4h` score `15.0744` n `32` status `ready` deltaP `27.439` edge `1.1855` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.0744` n `32` status `ready` deltaP `27.439` edge `1.1855` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `13.527` n `32` status `ready` deltaP `28.9931` edge `0.9601` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `13.527` n `32` status `ready` deltaP `28.9931` edge `0.9601` maxDD `-0.7574`
- `market_context_high->index_24h` score `12.6728` n `154` status `ready` deltaP `36.4538` edge `1.0347` maxDD `-15.0661`
- `risk_on_high->crypto_alt_4h` score `6.8086` n `32` status `ready` deltaP `7.5457` edge `0.7015` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `6.8086` n `32` status `ready` deltaP `7.5457` edge `0.7015` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `4.5562` n `32` status `ready` deltaP `17.6067` edge `0.5802` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `4.5562` n `32` status `ready` deltaP `17.6067` edge `0.5802` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
