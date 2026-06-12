# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T07:37:30.243815+00:00`
- Price records: `672`
- Market context records: `3665`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13157`

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

- `risk_on_high->crypto_major_24h` score `34.5648` n `32` status `ready` deltaP `39.2361` edge `2.6231` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `34.5648` n `32` status `ready` deltaP `39.2361` edge `2.6231` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `29.6156` n `32` status `ready` deltaP `41.3194` edge `2.1925` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `29.6156` n `32` status `ready` deltaP `41.3194` edge `2.1925` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `26.409` n `32` status `ready` deltaP `38.3681` edge `1.9601` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `26.409` n `32` status `ready` deltaP `38.3681` edge `1.9601` maxDD `-0.8779`
- `risk_on_high->index_24h` score `16.6568` n `32` status `ready` deltaP `41.3194` edge `1.1126` maxDD `0.0`
- `risk_on_and_context->index_24h` score `16.6568` n `32` status `ready` deltaP `41.3194` edge `1.1126` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `11.5414` n `32` status `ready` deltaP `20.7317` edge `0.9358` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `11.5414` n `32` status `ready` deltaP `20.7317` edge `0.9358` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `8.204` n `32` status `ready` deltaP `26.9097` edge `0.5304` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `8.204` n `32` status `ready` deltaP `26.9097` edge `0.5304` maxDD `-0.7574`
- `market_context_high->index_24h` score `6.2607` n `157` status `ready` deltaP `26.6697` edge `0.5155` maxDD `-11.3924`
- `market_context_high->equity_24h` score `5.3276` n `157` status `ready` deltaP `18.3895` edge `0.8878` maxDD `-35.3144`
- `risk_on_high->crypto_alt_4h` score `2.7226` n `32` status `ready` deltaP `0.9909` edge `0.4047` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `2.7226` n `32` status `ready` deltaP `0.9909` edge `0.4047` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `2.6438` n `32` status `ready` deltaP `10.2896` edge `0.3838` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.6438` n `32` status `ready` deltaP `10.2896` edge `0.3838` maxDD `-5.7426`
- `market_context_high->metal_24h` score `1.5517` n `157` status `ready` deltaP `21.217` edge `0.4527` maxDD `-21.6171`
- `risk_on_high->crypto_major_1h` score `1.3532` n `32` status `ready` deltaP `3.7238` edge `0.2556` maxDD `-5.8885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
