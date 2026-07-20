# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-20T11:37:30.103869+00:00`
- Price records: `672`
- Market context records: `7350`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14631`

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

- `risk_on_high->crypto_major_4h` score `7.1487` n `32` status `ready` deltaP `39.253` edge `0.3533` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `7.1487` n `32` status `ready` deltaP `39.253` edge `0.3533` maxDD `-0.8742`
- `risk_on_high->crypto_alt_4h` score `5.8559` n `32` status `ready` deltaP `32.3933` edge `0.2964` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `5.8559` n `32` status `ready` deltaP `32.3933` edge `0.2964` maxDD `-0.9492`
- `risk_on_high->unknown_4h` score `5.4004` n `32` status `ready` deltaP `18.9024` edge `0.367` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `5.4004` n `32` status `ready` deltaP `18.9024` edge `0.367` maxDD `-0.4384`
- `risk_on_high->crypto_major_1h` score `1.2667` n `32` status `ready` deltaP `20.2283` edge `0.052` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.2667` n `32` status `ready` deltaP `20.2283` edge `0.052` maxDD `-0.957`
- `risk_on_high->commodity_1h` score `0.2523` n `32` status `ready` deltaP `4.1479` edge `0.0213` maxDD `-0.2339`
- `risk_on_and_context->commodity_1h` score `0.2523` n `32` status `ready` deltaP `4.1479` edge `0.0213` maxDD `-0.2339`
- `risk_on_high->equity_1h` score `0.2038` n `32` status `ready` deltaP `4.3544` edge `0.0348` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.2038` n `32` status `ready` deltaP `4.3544` edge `0.0348` maxDD `-1.3497`
- `risk_on_high->crypto_alt_1h` score `0.1663` n `32` status `ready` deltaP `1.0479` edge `0.0514` maxDD `-0.9651`
- `risk_on_and_context->crypto_alt_1h` score `0.1663` n `32` status `ready` deltaP `1.0479` edge `0.0514` maxDD `-0.9651`
- `risk_on_high->metal_4h` score `-0.1068` n `32` status `ready` deltaP `-0.4573` edge `0.0765` maxDD `-0.5882`
- `risk_on_and_context->metal_4h` score `-0.1068` n `32` status `ready` deltaP `-0.4573` edge `0.0765` maxDD `-0.5882`
- `market_context_high->fx_1h` score `-0.1886` n `129` status `ready` deltaP `3.7887` edge `-0.0005` maxDD `-0.5821`
- `market_context_high->unknown_4h` score `-0.5326` n `129` status `ready` deltaP `6.8384` edge `0.122` maxDD `-6.2031`
- `market_context_high->commodity_1h` score `-0.712` n `129` status `ready` deltaP `-3.2649` edge `-0.0123` maxDD `-1.5775`
- `market_context_high->index_1h` score `-0.7992` n `129` status `ready` deltaP `-5.1609` edge `-0.0072` maxDD `-1.868`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
