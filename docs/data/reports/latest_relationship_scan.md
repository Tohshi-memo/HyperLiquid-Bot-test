# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-09T00:07:15.946143+00:00`
- Price records: `672`
- Market context records: `810`
- Flow alert records: `2275`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1170`

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

- `market_context_high->crypto_major_24h` score `12.4949` n `149` status `ready` deltaP `29.9905` edge `0.8747` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `5.3785` n `149` status `ready` deltaP `7.1414` edge `0.4054` maxDD `-0.0508`
- `risk_on_high->equity_4h` score `3.5244` n `33` status `ready` deltaP `10.0379` edge `0.2633` maxDD `-0.9217`
- `risk_on_and_context->equity_4h` score `3.5244` n `33` status `ready` deltaP `10.0379` edge `0.2633` maxDD `-0.9217`
- `risk_on_high->index_4h` score `2.8107` n `33` status `ready` deltaP `17.1656` edge `0.1286` maxDD `-0.038`
- `risk_on_and_context->index_4h` score `2.8107` n `33` status `ready` deltaP `17.1656` edge `0.1286` maxDD `-0.038`
- `risk_on_high->crypto_major_4h` score `2.7502` n `33` status `ready` deltaP `19.8125` edge `0.1343` maxDD `-0.9758`
- `risk_on_and_context->crypto_major_4h` score `2.7502` n `33` status `ready` deltaP `19.8125` edge `0.1343` maxDD `-0.9758`
- `risk_on_high->crypto_alt_4h` score `2.6179` n `33` status `ready` deltaP `20.3298` edge `0.1031` maxDD `-0.6377`
- `risk_on_and_context->crypto_alt_4h` score `2.6179` n `33` status `ready` deltaP `20.3298` edge `0.1031` maxDD `-0.6377`
- `risk_on_high->metal_1h` score `1.1399` n `33` status `ready` deltaP `13.2599` edge `0.0296` maxDD `-0.5074`
- `risk_on_and_context->metal_1h` score `1.1399` n `33` status `ready` deltaP `13.2599` edge `0.0296` maxDD `-0.5074`
- `risk_on_high->commodity_4h` score `0.8642` n `33` status `ready` deltaP `5.9728` edge `0.1541` maxDD `-1.3162`
- `risk_on_and_context->commodity_4h` score `0.8642` n `33` status `ready` deltaP `5.9728` edge `0.1541` maxDD `-1.3162`
- `risk_on_high->commodity_1h` score `0.3616` n `33` status `ready` deltaP `9.0365` edge `0.0237` maxDD `-0.6739`
- `risk_on_and_context->commodity_1h` score `0.3616` n `33` status `ready` deltaP `9.0365` edge `0.0237` maxDD `-0.6739`
- `risk_on_high->fx_1h` score `0.2867` n `33` status `ready` deltaP `8.6963` edge `0.0023` maxDD `-0.2147`
- `risk_on_and_context->fx_1h` score `0.2867` n `33` status `ready` deltaP `8.6963` edge `0.0023` maxDD `-0.2147`
- `risk_on_high->crypto_major_1h` score `-0.1378` n `33` status `ready` deltaP `4.4321` edge `-0.0168` maxDD `-1.0995`
- `risk_on_and_context->crypto_major_1h` score `-0.1378` n `33` status `ready` deltaP `4.4321` edge `-0.0168` maxDD `-1.0995`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
