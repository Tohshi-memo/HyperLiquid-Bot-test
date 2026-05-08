# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T19:52:19.677198+00:00`
- Price records: `672`
- Market context records: `789`
- Flow alert records: `2221`
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

- `market_context_high->crypto_major_24h` score `13.0575` n `149` status `ready` deltaP `30.8585` edge `0.9158` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.1861` n `149` status `ready` deltaP `7.1414` edge `0.4727` maxDD `-0.0508`
- `risk_on_high->equity_4h` score `3.7806` n `33` status `ready` deltaP `10.391` edge `0.2823` maxDD `-0.9217`
- `risk_on_and_context->equity_4h` score `3.7806` n `33` status `ready` deltaP `10.391` edge `0.2823` maxDD `-0.9217`
- `risk_on_high->crypto_major_4h` score `3.0278` n `33` status `ready` deltaP `21.032` edge `0.1493` maxDD `-0.9758`
- `risk_on_and_context->crypto_major_4h` score `3.0278` n `33` status `ready` deltaP `21.032` edge `0.1493` maxDD `-0.9758`
- `risk_on_high->index_4h` score `3.0237` n `33` status `ready` deltaP `19.047` edge `0.1338` maxDD `-0.038`
- `risk_on_and_context->index_4h` score `3.0237` n `33` status `ready` deltaP `19.047` edge `0.1338` maxDD `-0.038`
- `risk_on_high->crypto_alt_4h` score `2.9531` n `33` status `ready` deltaP `21.5493` edge `0.1229` maxDD `-0.6377`
- `risk_on_and_context->crypto_alt_4h` score `2.9531` n `33` status `ready` deltaP `21.5493` edge `0.1229` maxDD `-0.6377`
- `risk_on_high->metal_1h` score `1.0812` n `33` status `ready` deltaP `12.8108` edge `0.0277` maxDD `-0.5074`
- `risk_on_and_context->metal_1h` score `1.0812` n `33` status `ready` deltaP `12.8108` edge `0.0277` maxDD `-0.5074`
- `risk_on_high->commodity_4h` score `0.6196` n `33` status `ready` deltaP `3.6224` edge `0.1384` maxDD `-1.3162`
- `risk_on_and_context->commodity_4h` score `0.6196` n `33` status `ready` deltaP `3.6224` edge `0.1384` maxDD `-1.3162`
- `market_context_high->index_24h` score `0.3603` n `149` status `ready` deltaP `2.5702` edge `0.2124` maxDD `-5.9609`
- `risk_on_high->commodity_1h` score `0.2777` n `33` status `ready` deltaP `7.9188` edge `0.0204` maxDD `-0.6739`
- `risk_on_and_context->commodity_1h` score `0.2777` n `33` status `ready` deltaP `7.9188` edge `0.0204` maxDD `-0.6739`
- `risk_on_high->fx_1h` score `0.2559` n `33` status `ready` deltaP `8.1641` edge `0.0019` maxDD `-0.2147`
- `risk_on_and_context->fx_1h` score `0.2559` n `33` status `ready` deltaP `8.1641` edge `0.0019` maxDD `-0.2147`
- `risk_on_high->crypto_major_1h` score `-0.1081` n `33` status `ready` deltaP `4.5818` edge `-0.014` maxDD `-1.0995`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
