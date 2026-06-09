# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-09T15:37:37.120195+00:00`
- Price records: `672`
- Market context records: `3396`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13074`

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

- `risk_on_high->crypto_major_24h` score `55.5806` n `32` status `ready` deltaP `58.3333` edge `4.2471` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `55.5806` n `32` status `ready` deltaP `58.3333` edge `4.2471` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `54.2267` n `32` status `ready` deltaP `55.7292` edge `4.1625` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `54.2267` n `32` status `ready` deltaP `55.7292` edge `4.1625` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `45.4397` n `32` status `ready` deltaP `56.0764` edge `3.4128` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `45.4397` n `32` status `ready` deltaP `56.0764` edge `3.4128` maxDD `0.0`
- `risk_on_high->index_24h` score `23.2979` n `32` status `ready` deltaP `51.3889` edge `1.5989` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.2979` n `32` status `ready` deltaP `51.3889` edge `1.5989` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `21.1057` n `155` status `ready` deltaP `17.5639` edge `2.4402` maxDD `-56.8787`
- `market_context_high->crypto_major_24h` score `19.4836` n `155` status `ready` deltaP `24.0389` edge `2.3271` maxDD `-62.098`
- `market_context_high->equity_24h` score `19.1339` n `155` status `ready` deltaP `32.8506` edge `2.1033` maxDD `-46.8916`
- `risk_on_high->crypto_major_4h` score `15.1642` n `32` status `ready` deltaP `28.2012` edge `1.1879` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.1642` n `32` status `ready` deltaP `28.2012` edge `1.1879` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `13.641` n `32` status `ready` deltaP `28.9931` edge `0.9696` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `13.641` n `32` status `ready` deltaP `28.9931` edge `0.9696` maxDD `-0.7574`
- `market_context_high->index_24h` score `12.0412` n `155` status `ready` deltaP `35.905` edge `1.0072` maxDD `-15.7838`
- `risk_on_high->crypto_alt_4h` score `6.85` n `32` status `ready` deltaP `8.003` edge `0.7019` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `6.85` n `32` status `ready` deltaP `8.003` edge `0.7019` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.8283` n `32` status `ready` deltaP `15.4726` edge `0.5011` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.8283` n `32` status `ready` deltaP `15.4726` edge `0.5011` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
