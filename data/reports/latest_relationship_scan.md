# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-17T01:22:24.978782+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11831`

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

- `market_context_high->unknown_24h` score `37.8011` n `76` status `ready` deltaP `-38.8432` edge `5.3736` maxDD `-7.8016`
- `market_context_high->commodity_24h` score `4.4253` n `76` status `ready` deltaP `34.1648` edge `0.1759` maxDD `-0.4576`
- `market_context_high->commodity_4h` score `0.9126` n `106` status `ready` deltaP `10.9497` edge `0.0502` maxDD `-0.7718`
- `market_context_high->index_24h` score `0.6925` n `76` status `ready` deltaP `15.9905` edge `-0.0311` maxDD `-0.0904`
- `market_context_high->crypto_major_24h` score `-0.073` n `76` status `ready` deltaP `-0.9686` edge `0.1881` maxDD `-9.9468`
- `market_context_high->metal_4h` score `-0.1278` n `106` status `ready` deltaP `16.915` edge `0.0173` maxDD `-4.5909`
- `market_context_high->metal_1h` score `-0.3719` n `111` status `ready` deltaP `5.4122` edge `0.0045` maxDD `-1.7257`
- `market_context_high->fx_1h` score `-0.4357` n `111` status `ready` deltaP `-2.5517` edge `-0.0018` maxDD `-0.2968`
- `market_context_high->commodity_1h` score `-0.5322` n `111` status `ready` deltaP `-1.3459` edge `0.0092` maxDD `-0.8998`
- `market_context_high->fx_4h` score `-0.5458` n `106` status `ready` deltaP `-0.6471` edge `-0.0052` maxDD `-0.504`
- `market_context_high->index_1h` score `-0.7166` n `111` status `ready` deltaP `-5.6872` edge `-0.0018` maxDD `-0.5064`
- `market_context_high->crypto_major_4h` score `-1.4093` n `106` status `ready` deltaP `1.5532` edge `-0.007` maxDD `-4.6638`
- `market_context_high->index_4h` score `-1.9368` n `106` status `ready` deltaP `-11.2517` edge `-0.0055` maxDD `-0.8045`
- `market_context_high->crypto_major_1h` score `-1.9595` n `111` status `ready` deltaP `-6.0056` edge `-0.0222` maxDD `-4.0845`
- `market_context_high->crypto_alt_1h` score `-1.9842` n `111` status `ready` deltaP `-6.1553` edge `-0.0191` maxDD `-4.7507`
- `market_context_high->equity_1h` score `-2.1363` n `111` status `ready` deltaP `-8.0824` edge `-0.0374` maxDD `-3.606`
- `market_context_high->equity_24h` score `-2.4112` n `76` status `ready` deltaP `9.6308` edge `-0.1091` maxDD `-9.1496`
- `market_context_high->fx_24h` score `-2.8218` n `76` status `ready` deltaP `-25.3381` edge `-0.0321` maxDD `-1.8596`
- `market_context_high->metal_24h` score `-2.8225` n `76` status `ready` deltaP `-17.5896` edge `0.0066` maxDD `-7.0954`
- `market_context_high->equity_4h` score `-5.7354` n `106` status `ready` deltaP `-20.3233` edge `-0.153` maxDD `-8.8237`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
