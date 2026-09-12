# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T14:14:53.385698+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12058`

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

- `market_context_high->unknown_24h` score `4933.6998` n `99` status `ready` deltaP `13.4312` edge `411.0573` maxDD `-0.082`
- `risk_on_high->unknown_24h` score `2178.7729` n `52` status `ready` deltaP `15.4514` edge `181.4614` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `2178.7729` n `52` status `ready` deltaP `15.4514` edge `181.4614` maxDD `0.0`
- `news_risk_high->unknown_1h` score `383.2755` n `82` status `ready` deltaP `-4.8014` edge `32.0138` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `24.6959` n `59` status `ready` deltaP `55.0259` edge `1.7812` maxDD `-5.8705`
- `risk_on_high->crypto_alt_24h` score `17.8836` n `52` status `ready` deltaP `39.3429` edge `1.251` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `17.8836` n `52` status `ready` deltaP `39.3429` edge `1.251` maxDD `-0.8386`
- `news_risk_high->crypto_alt_24h` score `17.7348` n `59` status `ready` deltaP `30.3142` edge `1.3246` maxDD `-2.2369`
- `market_context_high->crypto_alt_24h` score `15.5833` n `99` status `ready` deltaP `32.7967` edge `1.1627` maxDD `-3.9523`
- `news_risk_high->equity_24h` score `12.4577` n `59` status `ready` deltaP `34.9783` edge `0.8148` maxDD `-0.1212`
- `risk_on_high->equity_24h` score `8.9782` n `52` status `ready` deltaP `38.3681` edge `0.4924` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `8.9782` n `52` status `ready` deltaP `38.3681` edge `0.4924` maxDD `0.0`
- `market_context_high->equity_24h` score `8.7166` n `99` status `ready` deltaP `38.3681` edge `0.4706` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.7135` n `52` status `ready` deltaP `42.554` edge `0.4796` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.7135` n `52` status `ready` deltaP `42.554` edge `0.4796` maxDD `-1.9733`
- `news_risk_high->metal_24h` score `8.4807` n `59` status `ready` deltaP `54.5139` edge `0.3433` maxDD `0.0`
- `news_risk_high->index_24h` score `7.9383` n `59` status `ready` deltaP `51.8185` edge `0.3254` maxDD `-0.0797`
- `risk_on_high->index_24h` score `4.8584` n `52` status `ready` deltaP `49.4391` edge `0.0795` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `4.8584` n `52` status `ready` deltaP `49.4391` edge `0.0795` maxDD `-0.0051`
- `risk_on_high->equity_4h` score `4.1649` n `52` status `ready` deltaP `37.1248` edge `0.1089` maxDD `-0.079`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
