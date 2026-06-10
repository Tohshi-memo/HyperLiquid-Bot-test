# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-10T15:54:03.392090+00:00`
- Price records: `672`
- Market context records: `3497`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13142`

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

- `risk_on_high->crypto_major_24h` score `54.5671` n `32` status `ready` deltaP `58.1597` edge `4.1638` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `54.5671` n `32` status `ready` deltaP `58.1597` edge `4.1638` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `51.5598` n `32` status `ready` deltaP `58.3333` edge `3.9229` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `51.5598` n `32` status `ready` deltaP `58.3333` edge `3.9229` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `44.7039` n `32` status `ready` deltaP `55.7292` edge `3.3538` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `44.7039` n `32` status `ready` deltaP `55.7292` edge `3.3538` maxDD `0.0`
- `risk_on_high->index_24h` score `24.5099` n `32` status `ready` deltaP `51.3889` edge `1.6999` maxDD `0.0`
- `risk_on_and_context->index_24h` score `24.5099` n `32` status `ready` deltaP `51.3889` edge `1.6999` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `19.3715` n `155` status `ready` deltaP `23.8653` edge `2.2283` maxDD `-54.8486`
- `market_context_high->equity_24h` score `19.1165` n `155` status `ready` deltaP `32.5034` edge `2.0176` maxDD `-40.9667`
- `market_context_high->crypto_alt_24h` score `17.6529` n `155` status `ready` deltaP `18.8777` edge `2.1453` maxDD `-56.6728`
- `risk_on_high->metal_24h` score `16.0342` n `32` status `ready` deltaP `30.9028` edge `1.1563` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `16.0342` n `32` status `ready` deltaP `30.9028` edge `1.1563` maxDD `-0.7574`
- `risk_on_high->crypto_major_4h` score `14.9424` n `32` status `ready` deltaP `28.3537` edge `1.1684` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `14.9424` n `32` status `ready` deltaP `28.3537` edge `1.1684` maxDD `-5.9781`
- `market_context_high->index_24h` score `13.1365` n `155` status `ready` deltaP `35.905` edge `1.077` maxDD `-15.0661`
- `risk_on_high->crypto_alt_4h` score `7.2512` n `32` status `ready` deltaP `9.2226` edge `0.7272` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.2512` n `32` status `ready` deltaP `9.2226` edge `0.7272` maxDD `-11.7537`
- `market_context_high->metal_24h` score `5.9957` n `155` status `ready` deltaP `25.3786` edge `1.0535` maxDD `-25.9879`
- `risk_on_high->equity_4h` score `3.9989` n `32` status `ready` deltaP `17.1494` edge `0.5118` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
