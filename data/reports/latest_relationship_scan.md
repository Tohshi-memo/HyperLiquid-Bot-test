# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T21:52:31.372603+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11564`

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

- `risk_on_high->crypto_alt_4h` score `9.2754` n `42` status `ready` deltaP `34.9521` edge `0.5581` maxDD `-0.4529`
- `risk_on_and_context->crypto_alt_4h` score `9.2754` n `42` status `ready` deltaP `34.9521` edge `0.5581` maxDD `-0.4529`
- `news_risk_high->crypto_alt_24h` score `9.2747` n `49` status `ready` deltaP `24.38` edge `1.3641` maxDD `-22.3391`
- `risk_on_high->crypto_major_4h` score `7.0954` n `42` status `ready` deltaP `37.1225` edge `0.3714` maxDD `-1.208`
- `risk_on_and_context->crypto_major_4h` score `7.0954` n `42` status `ready` deltaP `37.1225` edge `0.3714` maxDD `-1.208`
- `news_risk_high->unknown_4h` score `6.8415` n `58` status `ready` deltaP `3.1696` edge `0.608` maxDD `-1.7205`
- `market_context_high->metal_24h` score `4.6838` n `104` status `ready` deltaP `34.415` edge `0.2628` maxDD `-3.1535`
- `risk_on_high->metal_4h` score `3.0827` n `42` status `ready` deltaP `34.1681` edge `0.0377` maxDD `-0.0208`
- `risk_on_and_context->metal_4h` score `3.0827` n `42` status `ready` deltaP `34.1681` edge `0.0377` maxDD `-0.0208`
- `news_risk_high->unknown_1h` score `3.0614` n `58` status `ready` deltaP `-0.733` edge `0.2957` maxDD `-0.8558`
- `risk_on_high->equity_4h` score `1.8285` n `42` status `ready` deltaP `14.6269` edge `0.0798` maxDD `-0.3281`
- `risk_on_and_context->equity_4h` score `1.8285` n `42` status `ready` deltaP `14.6269` edge `0.0798` maxDD `-0.3281`
- `market_context_high->unknown_4h` score `1.7561` n `144` status `ready` deltaP `17.5135` edge `0.0766` maxDD `-1.0945`
- `risk_on_high->metal_1h` score `1.5339` n `54` status `ready` deltaP `21.0801` edge `0.0087` maxDD `-0.0463`
- `risk_on_and_context->metal_1h` score `1.5339` n `54` status `ready` deltaP `21.0801` edge `0.0087` maxDD `-0.0463`
- `market_context_high->unknown_1h` score `1.5114` n `156` status `ready` deltaP `8.153` edge `0.1197` maxDD `-1.5148`
- `news_risk_high->fx_4h` score `1.3157` n `58` status `ready` deltaP `31.0082` edge `0.0169` maxDD `-0.3953`
- `risk_on_high->index_4h` score `1.0845` n `42` status `ready` deltaP `17.1603` edge `0.0069` maxDD `-0.1405`
- `risk_on_and_context->index_4h` score `1.0845` n `42` status `ready` deltaP `17.1603` edge `0.0069` maxDD `-0.1405`
- `risk_on_high->unknown_1h` score `0.9622` n `54` status `ready` deltaP `0.0333` edge `0.1239` maxDD `-1.5148`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
