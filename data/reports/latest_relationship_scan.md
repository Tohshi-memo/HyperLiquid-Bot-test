# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T19:07:27.391580+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10804`

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

- `risk_on_high->unknown_4h` score `19.5898` n `133` status `ready` deltaP `7.3216` edge `1.6455` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `19.5898` n `133` status `ready` deltaP `7.3216` edge `1.6455` maxDD `-2.2797`
- `risk_on_high->unknown_1h` score `11.5317` n `133` status `ready` deltaP `-1.8021` edge `1.0307` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `11.5317` n `133` status `ready` deltaP `-1.8021` edge `1.0307` maxDD `-1.95`
- `market_context_high->unknown_4h` score `10.2622` n `212` status `ready` deltaP `9.1233` edge `0.8639` maxDD `-2.563`
- `market_context_high->unknown_1h` score `8.7412` n `217` status `ready` deltaP `-0.8562` edge `0.7972` maxDD `-2.0446`
- `news_risk_high->crypto_alt_24h` score `3.6323` n `46` status `ready` deltaP `18.8029` edge `0.2043` maxDD `-0.8236`
- `news_risk_high->crypto_major_4h` score `2.1889` n `46` status `ready` deltaP `9.4247` edge `0.1679` maxDD `-1.5324`
- `news_risk_high->commodity_24h` score `2.1079` n `46` status `ready` deltaP `12.9076` edge `0.1068` maxDD `-0.042`
- `news_risk_high->equity_1h` score `1.6698` n `46` status `ready` deltaP `16.1286` edge `0.0707` maxDD `-0.7924`
- `news_risk_high->metal_4h` score `1.5815` n `46` status `ready` deltaP `16.5562` edge `0.0477` maxDD `-0.7692`
- `news_risk_high->commodity_4h` score `1.5484` n `46` status `ready` deltaP `11.0286` edge `0.0756` maxDD `-0.2737`
- `news_risk_high->index_1h` score `1.1601` n `46` status `ready` deltaP `14.8464` edge `0.0111` maxDD `-0.0724`
- `news_risk_high->metal_1h` score `0.7316` n `46` status `ready` deltaP `9.3726` edge `0.0178` maxDD `-0.2118`
- `news_risk_high->fx_4h` score `0.3189` n `46` status `ready` deltaP `10.7105` edge `0.0004` maxDD `-0.9514`
- `news_risk_high->crypto_alt_1h` score `0.1723` n `46` status `ready` deltaP `3.9053` edge `0.0186` maxDD `-1.0885`
- `news_risk_high->commodity_1h` score `0.1682` n `46` status `ready` deltaP `8.3312` edge `0.0031` maxDD `-0.9036`
- `risk_on_high->metal_1h` score `0.1` n `133` status `ready` deltaP `12.4128` edge `0.0013` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.1` n `133` status `ready` deltaP `12.4128` edge `0.0013` maxDD `-1.699`
- `news_risk_high->crypto_major_1h` score `0.0679` n `46` status `ready` deltaP `-0.371` edge `0.0404` maxDD `-1.0047`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
