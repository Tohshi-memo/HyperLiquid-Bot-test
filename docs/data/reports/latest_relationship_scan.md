# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T08:07:31.425589+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11478`

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

- `risk_on_high->unknown_4h` score `20.9437` n `133` status `ready` deltaP `8.5412` edge `1.7502` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `20.9437` n `133` status `ready` deltaP `8.5412` edge `1.7502` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `13.5279` n `179` status `ready` deltaP `11.5445` edge `1.1199` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `12.2588` n `133` status `ready` deltaP `-0.9039` edge `1.0853` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `12.2588` n `133` status `ready` deltaP `-0.9039` edge `1.0853` maxDD `-1.95`
- `market_context_high->unknown_1h` score `10.7076` n `189` status `ready` deltaP `0.8784` edge `0.9495` maxDD `-2.0446`
- `market_context_high->equity_24h` score `1.6188` n `160` status `ready` deltaP `16.8403` edge `0.4572` maxDD `-20.7654`
- `risk_on_high->equity_24h` score `1.0394` n `133` status `ready` deltaP `12.6345` edge `0.4169` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `1.0394` n `133` status `ready` deltaP `12.6345` edge `0.4169` maxDD `-19.828`
- `news_risk_high->commodity_4h` score `0.4825` n `65` status `ready` deltaP `7.1599` edge `0.0404` maxDD `-0.7681`
- `risk_on_high->metal_1h` score `0.1101` n `133` status `ready` deltaP `12.2631` edge `0.0036` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.1101` n `133` status `ready` deltaP `12.2631` edge `0.0036` maxDD `-1.699`
- `news_risk_high->index_1h` score `-0.0426` n `65` status `ready` deltaP `4.977` edge `-0.0033` maxDD `-0.8275`
- `news_risk_high->commodity_1h` score `-0.1502` n `65` status `ready` deltaP `4.6523` edge `0.0011` maxDD `-0.9036`
- `risk_on_high->index_1h` score `-0.1707` n `133` status `ready` deltaP `3.693` edge `-0.002` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.1707` n `133` status `ready` deltaP `3.693` edge `-0.002` maxDD `-0.5605`
- `news_risk_high->commodity_24h` score `-0.1726` n `65` status `ready` deltaP `3.4615` edge `-0.0182` maxDD `-0.2074`
- `risk_on_high->crypto_alt_1h` score `-0.2642` n `133` status `ready` deltaP `4.6013` edge `0.049` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.2642` n `133` status `ready` deltaP `4.6013` edge `0.049` maxDD `-5.4685`
- `market_context_high->metal_1h` score `-0.3171` n `189` status `ready` deltaP `6.5544` edge `0.0013` maxDD `-2.1858`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
