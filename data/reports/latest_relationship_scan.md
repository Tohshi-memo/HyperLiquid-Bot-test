# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-18T15:52:31.420902+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9222`

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

- `market_context_high->commodity_24h` score `2.1252` n `127` status `ready` deltaP `19.3729` edge `0.1331` maxDD `-1.8119`
- `risk_on_high->commodity_24h` score `1.9591` n `90` status `ready` deltaP `21.1401` edge `0.1021` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `1.9591` n `90` status `ready` deltaP `21.1401` edge `0.1021` maxDD `-1.7154`
- `market_context_high->crypto_major_4h` score `0.9215` n `128` status `ready` deltaP `15.1487` edge `0.3576` maxDD `-15.2359`
- `risk_on_high->crypto_major_4h` score `0.6802` n `91` status `ready` deltaP `15.8956` edge `0.2293` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `0.6802` n `91` status `ready` deltaP `15.8956` edge `0.2293` maxDD `-11.1788`
- `market_context_high->crypto_major_1h` score `0.525` n `128` status `ready` deltaP `4.9869` edge `0.0994` maxDD `-3.7781`
- `risk_on_high->index_1h` score `0.1125` n `91` status `ready` deltaP `6.2073` edge `0.0064` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.1125` n `91` status `ready` deltaP `6.2073` edge `0.0064` maxDD `-0.7394`
- `risk_on_high->fx_1h` score `-0.2562` n `91` status `ready` deltaP `1.1979` edge `-0.0028` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.2562` n `91` status `ready` deltaP `1.1979` edge `-0.0028` maxDD `-0.376`
- `risk_on_high->equity_1h` score `-0.277` n `91` status `ready` deltaP `10.9099` edge `0.0338` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.277` n `91` status `ready` deltaP `10.9099` edge `0.0338` maxDD `-5.3696`
- `market_context_high->crypto_alt_1h` score `-0.3515` n `128` status `ready` deltaP `2.7788` edge `0.0864` maxDD `-7.3329`
- `market_context_high->index_1h` score `-0.3698` n `128` status `ready` deltaP `3.6318` edge `0.0032` maxDD `-1.3195`
- `risk_on_high->metal_1h` score `-0.4681` n `91` status `ready` deltaP `1.2946` edge `0.0045` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4681` n `91` status `ready` deltaP `1.2946` edge `0.0045` maxDD `-0.8513`
- `market_context_high->fx_1h` score `-0.5276` n `128` status `ready` deltaP `-2.013` edge `-0.0021` maxDD `-0.503`
- `risk_on_high->crypto_major_1h` score `-0.6146` n `91` status `ready` deltaP `-0.2501` edge `0.0148` maxDD `-4.6876`
- `risk_on_and_context->crypto_major_1h` score `-0.6146` n `91` status `ready` deltaP `-0.2501` edge `0.0148` maxDD `-4.6876`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
