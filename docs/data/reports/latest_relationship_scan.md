# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T03:37:28.249615+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11837`

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

- `market_context_high->crypto_major_24h` score `4.0567` n `73` status `ready` deltaP `13.2974` edge `0.3702` maxDD `-4.9964`
- `market_context_high->metal_24h` score `0.6502` n `73` status `ready` deltaP `4.8384` edge `0.0759` maxDD `-1.3176`
- `market_context_high->commodity_24h` score `0.6431` n `73` status `ready` deltaP `12.6469` edge `0.1526` maxDD `-4.666`
- `market_context_high->commodity_4h` score `0.4539` n `105` status `ready` deltaP `10.9132` edge `0.0501` maxDD `-2.4692`
- `market_context_high->unknown_1h` score `0.1272` n `105` status `ready` deltaP `7.3054` edge `-0.0122` maxDD `-0.7386`
- `market_context_high->index_1h` score `0.0964` n `105` status `ready` deltaP `7.6718` edge `0.0032` maxDD `-0.3584`
- `market_context_high->metal_4h` score `-0.0701` n `105` status `ready` deltaP `8.4378` edge `0.0018` maxDD `-2.0294`
- `market_context_high->equity_1h` score `-0.0951` n `105` status `ready` deltaP `3.5344` edge `0.0245` maxDD `-1.8201`
- `market_context_high->crypto_major_4h` score `-0.1482` n `105` status `ready` deltaP `4.7039` edge `0.0607` maxDD `-3.885`
- `market_context_high->fx_4h` score `-0.1607` n `105` status `ready` deltaP `5.3136` edge `0.0019` maxDD `-0.3904`
- `market_context_high->metal_1h` score `-0.5968` n `105` status `ready` deltaP `-0.9795` edge `-0.0032` maxDD `-1.3425`
- `market_context_high->index_24h` score `-0.6424` n `73` status `ready` deltaP `8.1218` edge `-0.0551` maxDD `-1.5393`
- `market_context_high->fx_1h` score `-0.6727` n `105` status `ready` deltaP `-3.0881` edge `0.0007` maxDD `-0.2273`
- `market_context_high->commodity_1h` score `-0.7078` n `105` status `ready` deltaP `-4.5851` edge `0.0011` maxDD `-1.5684`
- `market_context_high->index_4h` score `-0.8135` n `105` status `ready` deltaP `-5.167` edge `-0.0023` maxDD `-0.7375`
- `market_context_high->crypto_major_1h` score `-0.9633` n `105` status `ready` deltaP `-3.7824` edge `-0.0027` maxDD `-3.6463`
- `market_context_high->unknown_24h` score `-0.9739` n `73` status `ready` deltaP `3.8152` edge `-0.0847` maxDD `-1.2479`
- `market_context_high->crypto_alt_1h` score `-1.2418` n `105` status `ready` deltaP `-2.8842` edge `0.0046` maxDD `-3.1082`
- `market_context_high->crypto_alt_4h` score `-1.4942` n `105` status `ready` deltaP `2.9908` edge `0.0364` maxDD `-10.4985`
- `market_context_high->equity_4h` score `-1.5077` n `105` status `ready` deltaP `-7.8354` edge `-0.0224` maxDD `-4.8257`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
