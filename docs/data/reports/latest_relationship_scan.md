# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-18T10:22:26.249433+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9258`

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

- `market_context_high->commodity_24h` score `2.5309` n `124` status `ready` deltaP `19.8241` edge `0.1639` maxDD `-1.8119`
- `market_context_high->crypto_major_4h` score `2.1048` n `143` status `ready` deltaP `17.6627` edge `0.3981` maxDD `-15.2359`
- `risk_on_high->commodity_24h` score `2.0549` n `83` status `ready` deltaP `19.8921` edge `0.1184` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `2.0549` n `83` status `ready` deltaP `19.8921` edge `0.1184` maxDD `-1.7154`
- `market_context_high->crypto_major_1h` score `0.6374` n `143` status `ready` deltaP `4.847` edge `0.1097` maxDD `-3.7781`
- `risk_on_high->crypto_major_4h` score `0.2208` n `91` status `ready` deltaP `14.0663` edge `0.1826` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `0.2208` n `91` status `ready` deltaP `14.0663` edge `0.1826` maxDD `-11.1788`
- `market_context_high->crypto_alt_1h` score `0.0794` n `143` status `ready` deltaP `6.2414` edge `0.115` maxDD `-7.3329`
- `risk_on_high->index_1h` score `-0.0545` n `91` status `ready` deltaP `4.2553` edge `0.0055` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.0545` n `91` status `ready` deltaP `4.2553` edge `0.0055` maxDD `-0.7394`
- `risk_on_high->fx_1h` score `-0.2484` n `91` status `ready` deltaP `1.3481` edge `-0.0028` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.2484` n `91` status `ready` deltaP `1.3481` edge `-0.0028` maxDD `-0.376`
- `market_context_high->metal_1h` score `-0.3437` n `143` status `ready` deltaP `5.1422` edge `0.0086` maxDD `-0.9556`
- `market_context_high->index_1h` score `-0.3828` n `143` status `ready` deltaP `5.8538` edge `0.0039` maxDD `-1.3195`
- `risk_on_high->equity_1h` score `-0.4824` n `91` status `ready` deltaP `9.1081` edge `0.0287` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.4824` n `91` status `ready` deltaP `9.1081` edge `0.0287` maxDD `-5.3696`
- `market_context_high->metal_4h` score `-0.509` n `143` status `ready` deltaP `6.9579` edge `0.0449` maxDD `-1.6961`
- `risk_on_high->metal_1h` score `-0.5413` n `91` status `ready` deltaP `-0.0527` edge `0.0041` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.5413` n `91` status `ready` deltaP `-0.0527` edge `0.0041` maxDD `-0.8513`
- `market_context_high->fx_1h` score `-0.7003` n `143` status `ready` deltaP `-0.65` edge `-0.0019` maxDD `-0.503`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
