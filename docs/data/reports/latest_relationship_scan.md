# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T13:22:27.401083+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13758`

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

- `market_context_high->index_1h` score `0.4353` n `122` status `ready` deltaP `11.7675` edge `0.0066` maxDD `-0.5685`
- `market_context_high->equity_1h` score `0.3417` n `122` status `ready` deltaP `8.6949` edge `0.052` maxDD `-3.1861`
- `market_context_high->fx_4h` score `0.2221` n `110` status `ready` deltaP `10.3104` edge `0.01` maxDD `-0.3539`
- `market_context_high->fx_1h` score `-0.0572` n `122` status `ready` deltaP `3.5781` edge `0.0047` maxDD `-0.2043`
- `market_context_high->equity_4h` score `-0.0899` n `110` status `ready` deltaP `4.6425` edge `0.1245` maxDD `-8.3685`
- `market_context_high->index_4h` score `-0.2704` n `110` status `ready` deltaP `6.2001` edge `0.0164` maxDD `-1.7252`
- `market_context_high->metal_4h` score `-0.3907` n `110` status `ready` deltaP `4.3487` edge `-0.0215` maxDD `-1.273`
- `market_context_high->metal_1h` score `-0.4441` n `122` status `ready` deltaP `1.1117` edge `-0.0048` maxDD `-0.503`
- `market_context_high->commodity_24h` score `-0.4643` n `105` status `ready` deltaP `4.4147` edge `0.1152` maxDD `-4.666`
- `market_context_high->unknown_1h` score `-0.5321` n `122` status `ready` deltaP `9.9416` edge `-0.0879` maxDD `-0.4843`
- `market_context_high->commodity_4h` score `-0.6524` n `110` status `ready` deltaP `-1.2916` edge `0.01` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.6678` n `122` status `ready` deltaP `-4.4125` edge `0.0004` maxDD `-1.1941`
- `market_context_high->crypto_alt_1h` score `-0.8823` n `122` status `ready` deltaP `-0.265` edge `0.0084` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-1.4385` n `122` status `ready` deltaP `-3.3793` edge `-0.0594` maxDD `-4.1996`
- `market_context_high->crypto_alt_4h` score `-2.9175` n `110` status `ready` deltaP `-0.4102` edge `-0.1134` maxDD `-5.4926`
- `market_context_high->fx_24h` score `-3.0313` n `105` status `ready` deltaP `-12.6488` edge `-0.0073` maxDD `-2.2121`
- `market_context_high->index_24h` score `-4.1743` n `105` status `ready` deltaP `-5.4217` edge `-0.0488` maxDD `-18.6848`
- `market_context_high->crypto_major_4h` score `-4.275` n `110` status `ready` deltaP `-0.9977` edge `-0.2475` maxDD `-3.1677`
- `market_context_high->metal_24h` score `-4.4715` n `105` status `ready` deltaP `-16.7212` edge `-0.131` maxDD `-11.4635`
- `market_context_high->unknown_24h` score `-4.963` n `105` status `ready` deltaP `8.4673` edge `-0.4194` maxDD `-1.0505`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
