# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-10T09:52:36.086008+00:00`
- Price records: `672`
- Market context records: `3472`
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

- `risk_on_high->crypto_major_24h` score `56.2425` n `32` status `ready` deltaP `58.5069` edge `4.3011` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `56.2425` n `32` status `ready` deltaP `58.5069` edge `4.3011` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `54.8048` n `32` status `ready` deltaP `59.8958` edge `4.1829` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `54.8048` n `32` status `ready` deltaP `59.8958` edge `4.1829` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `44.9957` n `32` status `ready` deltaP `56.0764` edge `3.3758` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `44.9957` n `32` status `ready` deltaP `56.0764` edge `3.3758` maxDD `0.0`
- `risk_on_high->index_24h` score `24.2375` n `32` status `ready` deltaP `51.3889` edge `1.6772` maxDD `0.0`
- `risk_on_and_context->index_24h` score `24.2375` n `32` status `ready` deltaP `51.3889` edge `1.6772` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `21.0469` n `155` status `ready` deltaP `24.2125` edge `2.3656` maxDD `-54.8486`
- `market_context_high->crypto_alt_24h` score `20.8979` n `155` status `ready` deltaP `20.4402` edge `2.4053` maxDD `-56.6728`
- `market_context_high->equity_24h` score `19.4082` n `155` status `ready` deltaP `32.8506` edge `2.0396` maxDD `-40.9667`
- `risk_on_high->crypto_major_4h` score `15.8849` n `32` status `ready` deltaP `30.6402` edge `1.2317` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.8849` n `32` status `ready` deltaP `30.6402` edge `1.2317` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `14.529` n `32` status `ready` deltaP `28.9931` edge `1.0436` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `14.529` n `32` status `ready` deltaP `28.9931` edge `1.0436` maxDD `-0.7574`
- `market_context_high->index_24h` score `12.8641` n `155` status `ready` deltaP `35.905` edge `1.0543` maxDD `-15.0661`
- `risk_on_high->crypto_alt_4h` score `7.8581` n `32` status `ready` deltaP `10.8994` edge `0.7666` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.8581` n `32` status `ready` deltaP `10.8994` edge `0.7666` maxDD `-11.7537`
- `market_context_high->metal_24h` score `5.0173` n `155` status `ready` deltaP `23.4689` edge `0.9408` maxDD `-25.9879`
- `risk_on_high->equity_4h` score `4.6184` n `32` status `ready` deltaP `19.2835` edge `0.577` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
