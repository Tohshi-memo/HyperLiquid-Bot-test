# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-19T02:52:27.375010+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8749`

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

- `market_context_high->commodity_24h` score `1.5018` n `84` status `ready` deltaP `14.8799` edge `0.1111` maxDD `-1.8119`
- `market_context_high->crypto_major_4h` score `0.9819` n `84` status `ready` deltaP `9.5746` edge `0.4025` maxDD `-15.2359`
- `risk_on_high->equity_1h` score `0.7516` n `51` status `ready` deltaP `14.3615` edge `0.0271` maxDD `-2.1501`
- `risk_on_and_context->equity_1h` score `0.7516` n `51` status `ready` deltaP `14.3615` edge `0.0271` maxDD `-2.1501`
- `market_context_high->crypto_major_1h` score `0.4439` n `85` status `ready` deltaP `4.3959` edge `0.1165` maxDD `-3.7781`
- `risk_on_high->commodity_24h` score `0.3562` n `51` status `ready` deltaP `12.8491` edge `0.0238` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.3562` n `51` status `ready` deltaP `12.8491` edge `0.0238` maxDD `-1.7154`
- `risk_on_high->index_1h` score `0.3492` n `51` status `ready` deltaP `8.9472` edge `0.001` maxDD `-0.5238`
- `risk_on_and_context->index_1h` score `0.3492` n `51` status `ready` deltaP `8.9472` edge `0.001` maxDD `-0.5238`
- `market_context_high->crypto_major_24h` score `0.1695` n `84` status `ready` deltaP `3.3482` edge `0.6091` maxDD `-35.1086`
- `risk_on_high->fx_1h` score `0.1006` n `51` status `ready` deltaP `6.2621` edge `0.0013` maxDD `-0.1065`
- `risk_on_and_context->fx_1h` score `0.1006` n `51` status `ready` deltaP `6.2621` edge `0.0013` maxDD `-0.1065`
- `risk_on_high->crypto_major_4h` score `-0.4396` n `51` status `ready` deltaP `3.4821` edge `0.1685` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `-0.4396` n `51` status `ready` deltaP `3.4821` edge `0.1685` maxDD `-11.1788`
- `market_context_high->fx_1h` score `-0.4748` n `85` status `ready` deltaP `-1.1888` edge `-0.0004` maxDD `-0.537`
- `risk_on_high->fx_4h` score `-0.4803` n `51` status `ready` deltaP `-2.4555` edge `0.0032` maxDD `-0.1486`
- `risk_on_and_context->fx_4h` score `-0.4803` n `51` status `ready` deltaP `-2.4555` edge `0.0032` maxDD `-0.1486`
- `market_context_high->fx_4h` score `-0.5834` n `84` status `ready` deltaP `-2.3154` edge `0.0037` maxDD `-0.7115`
- `market_context_high->crypto_alt_1h` score `-0.7081` n `85` status `ready` deltaP `-2.279` edge `0.0744` maxDD `-7.3329`
- `market_context_high->metal_1h` score `-0.728` n `85` status `ready` deltaP `-3.7549` edge `0.0041` maxDD `-0.7924`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
