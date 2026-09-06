# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T20:07:26.798575+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10299`

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

- `risk_on_high->unknown_24h` score `270.1546` n `103` status `ready` deltaP `26.0097` edge `22.3446` maxDD `-0.0761`
- `risk_on_and_context->unknown_24h` score `270.1546` n `103` status `ready` deltaP `26.0097` edge `22.3446` maxDD `-0.0761`
- `risk_on_high->crypto_major_24h` score `20.0934` n `103` status `ready` deltaP `32.376` edge `1.5103` maxDD `-1.4687`
- `risk_on_and_context->crypto_major_24h` score `20.0934` n `103` status `ready` deltaP `32.376` edge `1.5103` maxDD `-1.4687`
- `risk_on_high->crypto_alt_24h` score `12.7974` n `103` status `ready` deltaP `26.5692` edge `0.9233` maxDD `-1.385`
- `risk_on_and_context->crypto_alt_24h` score `12.7974` n `103` status `ready` deltaP `26.5692` edge `0.9233` maxDD `-1.385`
- `market_context_high->crypto_alt_24h` score `7.8619` n `196` status `ready` deltaP `21.2195` edge `0.573` maxDD `-2.7445`
- `market_context_high->equity_24h` score `6.6443` n `196` status `ready` deltaP `22.7537` edge `0.4068` maxDD `-0.0508`
- `risk_on_high->equity_24h` score `5.8982` n `103` status `ready` deltaP `22.293` edge `0.3477` maxDD `-0.0508`
- `risk_on_and_context->equity_24h` score `5.8982` n `103` status `ready` deltaP `22.293` edge `0.3477` maxDD `-0.0508`
- `risk_on_high->crypto_alt_4h` score `3.3308` n `117` status `ready` deltaP `26.6065` edge `0.2696` maxDD `-11.5528`
- `risk_on_and_context->crypto_alt_4h` score `3.3308` n `117` status `ready` deltaP `26.6065` edge `0.2696` maxDD `-11.5528`
- `risk_on_high->index_24h` score `2.1147` n `103` status `ready` deltaP `19.4899` edge `0.0797` maxDD `-0.6727`
- `risk_on_and_context->index_24h` score `2.1147` n `103` status `ready` deltaP `19.4899` edge `0.0797` maxDD `-0.6727`
- `market_context_high->index_24h` score `1.8914` n `196` status `ready` deltaP `19.6038` edge `0.0917` maxDD `-1.1821`
- `risk_on_high->crypto_major_4h` score `1.6868` n `117` status `ready` deltaP `20.5207` edge `0.2052` maxDD `-13.1152`
- `risk_on_and_context->crypto_major_4h` score `1.6868` n `117` status `ready` deltaP `20.5207` edge `0.2052` maxDD `-13.1152`
- `risk_on_high->metal_24h` score `0.776` n `103` status `ready` deltaP `14.7013` edge `0.0985` maxDD `-3.0953`
- `risk_on_and_context->metal_24h` score `0.776` n `103` status `ready` deltaP `14.7013` edge `0.0985` maxDD `-3.0953`
- `risk_on_high->crypto_alt_1h` score `0.6056` n `129` status `ready` deltaP `3.8516` edge `0.0764` maxDD `-2.4624`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
