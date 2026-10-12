# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T10:07:29.465162+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8030`

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

- `market_context_high->unknown_4h` score `27.2834` n `113` status `ready` deltaP `-3.1878` edge `2.3595` maxDD `-1.8373`
- `market_context_high->crypto_major_24h` score `21.0144` n `46` status `ready` deltaP `29.461` edge `1.7142` maxDD `-8.0862`
- `market_context_high->crypto_alt_24h` score `19.614` n `46` status `ready` deltaP `17.8291` edge `1.7248` maxDD `-12.0663`
- `risk_on_high->crypto_alt_4h` score `3.7692` n `48` status `ready` deltaP `18.1911` edge `0.2376` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `3.7692` n `48` status `ready` deltaP `18.1911` edge `0.2376` maxDD `-1.9151`
- `risk_on_high->crypto_major_4h` score `3.4394` n `48` status `ready` deltaP `32.6728` edge `0.3084` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.4394` n `48` status `ready` deltaP `32.6728` edge `0.3084` maxDD `-4.1548`
- `market_context_high->equity_24h` score `2.6857` n `46` status `ready` deltaP `3.9931` edge `0.458` maxDD `-7.5571`
- `market_context_high->unknown_1h` score `2.2861` n `113` status `ready` deltaP `-4.1333` edge `0.2517` maxDD `-1.024`
- `market_context_high->index_24h` score `1.803` n `46` status `ready` deltaP `25.8152` edge `0.1151` maxDD `-0.4833`
- `market_context_high->crypto_major_4h` score `1.3677` n `113` status `ready` deltaP `11.9132` edge `0.2404` maxDD `-10.8012`
- `risk_on_high->crypto_alt_1h` score `0.816` n `48` status `ready` deltaP `5.6387` edge `0.0901` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `0.816` n `48` status `ready` deltaP `5.6387` edge `0.0901` maxDD `-2.4421`
- `market_context_high->crypto_alt_1h` score `0.8052` n `113` status `ready` deltaP `7.4824` edge `0.1123` maxDD `-4.9401`
- `market_context_high->metal_24h` score `0.7259` n `46` status `ready` deltaP `13.1416` edge `0.0529` maxDD `-2.0684`
- `market_context_high->crypto_alt_4h` score `0.5623` n `113` status `ready` deltaP `5.4514` edge `0.2461` maxDD `-13.1802`
- `risk_on_high->crypto_major_1h` score `0.3469` n `48` status `ready` deltaP `4.7655` edge `0.078` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `0.3469` n `48` status `ready` deltaP `4.7655` edge `0.078` maxDD `-3.2233`
- `market_context_high->crypto_major_1h` score `0.1094` n `113` status `ready` deltaP `1.9262` edge `0.0775` maxDD `-3.4384`
- `market_context_high->metal_1h` score `-0.1842` n `113` status `ready` deltaP `4.5546` edge `0.0021` maxDD `-0.4868`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
