# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-10T13:52:33.257065+00:00`
- Price records: `672`
- Market context records: `3488`
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

- `risk_on_high->crypto_major_24h` score `55.2441` n `32` status `ready` deltaP `58.5069` edge `4.2179` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `55.2441` n `32` status `ready` deltaP `58.5069` edge `4.2179` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `52.7845` n `32` status `ready` deltaP `59.7222` edge `4.0157` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `52.7845` n `32` status `ready` deltaP `59.7222` edge `4.0157` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `44.9441` n `32` status `ready` deltaP `56.0764` edge `3.3715` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `44.9441` n `32` status `ready` deltaP `56.0764` edge `3.3715` maxDD `0.0`
- `risk_on_high->index_24h` score `24.5243` n `32` status `ready` deltaP `51.3889` edge `1.7011` maxDD `0.0`
- `risk_on_and_context->index_24h` score `24.5243` n `32` status `ready` deltaP `51.3889` edge `1.7011` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `20.0485` n `155` status `ready` deltaP `24.2125` edge `2.2824` maxDD `-54.8486`
- `market_context_high->equity_24h` score `19.3566` n `155` status `ready` deltaP `32.8506` edge `2.0353` maxDD `-40.9667`
- `market_context_high->crypto_alt_24h` score `18.8776` n `155` status `ready` deltaP `20.2666` edge `2.2381` maxDD `-56.6728`
- `risk_on_high->metal_24h` score `15.6317` n `32` status `ready` deltaP `29.8611` edge `1.1297` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `15.6317` n `32` status `ready` deltaP `29.8611` edge `1.1297` maxDD `-0.7574`
- `risk_on_high->crypto_major_4h` score `15.3975` n `32` status `ready` deltaP `29.5732` edge `1.1982` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.3975` n `32` status `ready` deltaP `29.5732` edge `1.1982` maxDD `-5.9781`
- `market_context_high->index_24h` score `13.1509` n `155` status `ready` deltaP `35.905` edge `1.0782` maxDD `-15.0661`
- `risk_on_high->crypto_alt_4h` score `7.7087` n `32` status `ready` deltaP `10.4421` edge `0.7572` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.7087` n `32` status `ready` deltaP `10.4421` edge `0.7572` maxDD `-11.7537`
- `market_context_high->metal_24h` score `5.734` n `155` status `ready` deltaP `24.3369` edge `1.0269` maxDD `-25.9879`
- `risk_on_high->equity_4h` score `4.2706` n `32` status `ready` deltaP `18.3689` edge `0.5385` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
