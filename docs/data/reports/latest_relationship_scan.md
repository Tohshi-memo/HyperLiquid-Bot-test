# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-09T10:07:12.040680+00:00`
- Price records: `672`
- Market context records: `854`
- Flow alert records: `2399`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1332`

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

- `market_context_high->crypto_major_24h` score `11.9278` n `163` status `ready` deltaP `27.3719` edge `0.8449` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `5.4071` n `163` status `ready` deltaP `7.199` edge `0.4074` maxDD `-0.0508`
- `risk_on_high->equity_4h` score `3.42` n `33` status `ready` deltaP `9.1233` edge `0.2607` maxDD `-0.9217`
- `risk_on_and_context->equity_4h` score `3.42` n `33` status `ready` deltaP `9.1233` edge `0.2607` maxDD `-0.9217`
- `risk_on_high->crypto_major_4h` score `2.5562` n `33` status `ready` deltaP `19.2027` edge `0.1222` maxDD `-0.9758`
- `risk_on_and_context->crypto_major_4h` score `2.5562` n `33` status `ready` deltaP `19.2027` edge `0.1222` maxDD `-0.9758`
- `risk_on_high->crypto_alt_4h` score `2.4609` n `33` status `ready` deltaP `20.4823` edge `0.089` maxDD `-0.6377`
- `risk_on_and_context->crypto_alt_4h` score `2.4609` n `33` status `ready` deltaP `20.4823` edge `0.089` maxDD `-0.6377`
- `risk_on_high->index_4h` score `2.4413` n `33` status `ready` deltaP `13.507` edge `0.1222` maxDD `-0.038`
- `risk_on_and_context->index_4h` score `2.4413` n `33` status `ready` deltaP `13.507` edge `0.1222` maxDD `-0.038`
- `risk_on_high->metal_1h` score `1.165` n `33` status `ready` deltaP `13.709` edge `0.0287` maxDD `-0.5074`
- `risk_on_and_context->metal_1h` score `1.165` n `33` status `ready` deltaP `13.709` edge `0.0287` maxDD `-0.5074`
- `risk_on_high->commodity_4h` score `0.7796` n `33` status `ready` deltaP `4.6008` edge `0.1524` maxDD `-1.3162`
- `risk_on_and_context->commodity_4h` score `0.7796` n `33` status `ready` deltaP `4.6008` edge `0.1524` maxDD `-1.3162`
- `risk_on_high->commodity_1h` score `0.346` n `33` status `ready` deltaP `8.8868` edge `0.0227` maxDD `-0.6739`
- `risk_on_and_context->commodity_1h` score `0.346` n `33` status `ready` deltaP `8.8868` edge `0.0227` maxDD `-0.6739`
- `risk_on_high->fx_1h` score `0.2345` n `33` status `ready` deltaP `7.7981` edge `0.0016` maxDD `-0.2147`
- `risk_on_and_context->fx_1h` score `0.2345` n `33` status `ready` deltaP `7.7981` edge `0.0016` maxDD `-0.2147`
- `risk_on_high->crypto_major_1h` score `-0.1113` n `33` status `ready` deltaP `5.0309` edge `-0.0174` maxDD `-1.0995`
- `risk_on_and_context->crypto_major_1h` score `-0.1113` n `33` status `ready` deltaP `5.0309` edge `-0.0174` maxDD `-1.0995`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
