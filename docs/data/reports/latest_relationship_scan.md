# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T08:07:32.304026+00:00`
- Price records: `672`
- Market context records: `3667`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12897`

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

- `risk_on_high->crypto_major_24h` score `34.3499` n `32` status `ready` deltaP `38.8889` edge `2.6075` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `34.3499` n `32` status `ready` deltaP `38.8889` edge `2.6075` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `29.2158` n `32` status `ready` deltaP `40.9722` edge `2.1615` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `29.2158` n `32` status `ready` deltaP `40.9722` edge `2.1615` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `26.1688` n `32` status `ready` deltaP `38.0208` edge `1.9424` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `26.1688` n `32` status `ready` deltaP `38.0208` edge `1.9424` maxDD `-0.8779`
- `risk_on_high->index_24h` score `16.3998` n `32` status `ready` deltaP `40.9722` edge `1.0935` maxDD `0.0`
- `risk_on_and_context->index_24h` score `16.3998` n `32` status `ready` deltaP `40.9722` edge `1.0935` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `11.5582` n `32` status `ready` deltaP `20.7317` edge `0.9372` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `11.5582` n `32` status `ready` deltaP `20.7317` edge `0.9372` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `7.9134` n `32` status `ready` deltaP `26.5625` edge `0.5085` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `7.9134` n `32` status `ready` deltaP `26.5625` edge `0.5085` maxDD `-0.7574`
- `market_context_high->index_24h` score `6.0037` n `157` status `ready` deltaP `26.3225` edge `0.4964` maxDD `-11.3924`
- `market_context_high->equity_24h` score `4.9278` n `157` status `ready` deltaP `18.0423` edge `0.8568` maxDD `-35.3144`
- `risk_on_high->crypto_alt_4h` score `2.7286` n `32` status `ready` deltaP `0.9909` edge `0.4052` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `2.7286` n `32` status `ready` deltaP `0.9909` edge `0.4052` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `2.6862` n `32` status `ready` deltaP `10.5945` edge `0.3872` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.6862` n `32` status `ready` deltaP `10.5945` edge `0.3872` maxDD `-5.7426`
- `market_context_high->metal_24h` score `1.3628` n `157` status `ready` deltaP `20.8698` edge `0.4308` maxDD `-21.6171`
- `risk_on_high->crypto_major_1h` score `1.3166` n `32` status `ready` deltaP `3.4244` edge `0.2529` maxDD `-5.8885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
