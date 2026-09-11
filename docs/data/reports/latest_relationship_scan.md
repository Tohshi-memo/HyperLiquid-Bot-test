# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-11T21:52:30.226473+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11321`

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

- `news_risk_high->unknown_1h` score `479.9195` n `73` status `ready` deltaP `-5.2416` edge `40.0704` maxDD `-1.7068`
- `risk_on_high->crypto_alt_24h` score `24.2548` n `91` status `ready` deltaP `42.4222` edge `1.7614` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `24.2548` n `91` status `ready` deltaP `42.4222` edge `1.7614` maxDD `-0.8386`
- `news_risk_high->crypto_major_24h` score `22.4602` n `32` status `ready` deltaP `48.7847` edge `1.6365` maxDD `-5.8705`
- `market_context_high->crypto_alt_24h` score `21.3452` n `151` status `ready` deltaP `37.3207` edge `1.6127` maxDD `-3.9523`
- `news_risk_high->crypto_alt_24h` score `13.9582` n `32` status `ready` deltaP `26.0417` edge `1.0342` maxDD `-2.2369`
- `news_risk_high->equity_24h` score `9.6266` n `32` status `ready` deltaP `30.7292` edge `0.6072` maxDD `-0.1212`
- `risk_on_high->equity_24h` score `9.4539` n `91` status `ready` deltaP `36.9792` edge `0.5413` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.4539` n `91` status `ready` deltaP `36.9792` edge `0.5413` maxDD `0.0`
- `market_context_high->equity_24h` score `9.1647` n `151` status `ready` deltaP `36.9792` edge `0.5172` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.5729` n `91` status `ready` deltaP `42.2507` edge `0.4699` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.5729` n `91` status `ready` deltaP `42.2507` edge `0.4699` maxDD `-1.9733`
- `news_risk_high->metal_24h` score `7.8345` n `32` status `ready` deltaP `51.0417` edge `0.3126` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `7.6379` n `91` status `ready` deltaP `25.021` edge `1.2192` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.6379` n `91` status `ready` deltaP `25.021` edge `1.2192` maxDD `-24.5429`
- `news_risk_high->index_24h` score `7.5473` n `32` status `ready` deltaP `48.6111` edge `0.3142` maxDD `-0.0797`
- `risk_on_high->crypto_major_4h` score `6.6264` n `91` status `ready` deltaP `31.1344` edge `0.4305` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `6.6264` n `91` status `ready` deltaP `31.1344` edge `0.4305` maxDD `-3.8693`
- `risk_on_high->index_24h` score `5.3884` n `91` status `ready` deltaP `51.5644` edge `0.1095` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `5.3884` n `91` status `ready` deltaP `51.5644` edge `0.1095` maxDD `-0.0051`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
