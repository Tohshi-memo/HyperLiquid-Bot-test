# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T16:52:15.361933+00:00`
- Price records: `672`
- Market context records: `1648`
- Flow alert records: `6655`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8834`

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

- `market_context_high->metal_24h` score `9.2312` n `169` status `ready` deltaP `27.5496` edge `0.8282` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `4.011` n `185` status `ready` deltaP `21.6109` edge `0.4566` maxDD `-16.3135`
- `market_context_high->index_24h` score `3.6301` n `169` status `ready` deltaP `19.5461` edge `0.31` maxDD `-5.3574`
- `market_context_high->crypto_major_4h` score `2.2934` n `185` status `ready` deltaP `17.3705` edge `0.3462` maxDD `-13.3376`
- `market_context_high->equity_4h` score `1.6895` n `185` status `ready` deltaP `11.5866` edge `0.173` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.4677` n `169` status `ready` deltaP `18.5633` edge `0.4884` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.342` n `194` status `ready` deltaP `5.3198` edge `0.0954` maxDD `-4.1892`
- `market_context_high->crypto_major_24h` score `0.202` n `169` status `ready` deltaP `24.3627` edge `0.713` maxDD `-62.3533`
- `market_context_high->crypto_alt_24h` score `0.0116` n `169` status `ready` deltaP `25.0169` edge `1.0151` maxDD `-88.8062`
- `market_context_high->equity_1h` score `-0.2714` n `194` status `ready` deltaP `1.6437` edge `0.0351` maxDD `-2.8014`
- `market_context_high->index_4h` score `-0.4563` n `185` status `ready` deltaP `-0.0009` edge `0.0504` maxDD `-3.7119`
- `market_context_high->fx_1h` score `-0.4742` n `194` status `ready` deltaP `0.8303` edge `-0.0031` maxDD `-0.3914`
- `market_context_high->fx_24h` score `-0.5182` n `169` status `ready` deltaP `6.214` edge `0.0203` maxDD `-1.3925`
- `market_context_high->crypto_major_1h` score `-0.523` n `194` status `ready` deltaP `1.4461` edge `0.0507` maxDD `-5.5244`
- `market_context_high->index_1h` score `-0.5334` n `194` status `ready` deltaP `-1.6822` edge `0.006` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.871` n `194` status `ready` deltaP `2.6267` edge `0.0044` maxDD `-6.3532`
- `market_context_high->commodity_1h` score `-0.8775` n `194` status `ready` deltaP `1.1637` edge `-0.0071` maxDD `-6.7191`
- `market_context_high->metal_4h` score `-1.4693` n `185` status `ready` deltaP `7.3266` edge `0.0979` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-2.0997` n `185` status `ready` deltaP `-10.318` edge `-0.0133` maxDD `-1.4313`
- `market_context_high->unknown_4h` score `-2.8922` n `185` status `ready` deltaP `10.8001` edge `-0.0859` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
