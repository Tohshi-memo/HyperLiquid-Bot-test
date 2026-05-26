# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T10:37:19.717610+00:00`
- Price records: `672`
- Market context records: `1938`
- Flow alert records: `7476`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7541`

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

- `market_context_high->crypto_alt_4h` score `6.9981` n `216` status `ready` deltaP `22.1319` edge `0.5501` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.3895` n `216` status `ready` deltaP `26.005` edge `0.4837` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `3.033` n `216` status `ready` deltaP `15.4867` edge `0.3519` maxDD `-9.8581`
- `market_context_high->equity_4h` score `2.0125` n `216` status `ready` deltaP `13.584` edge `0.1866` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `0.6371` n `197` status `ready` deltaP `14.4194` edge `0.489` maxDD `-35.8966`
- `market_context_high->crypto_major_1h` score `0.6273` n `228` status `ready` deltaP `7.724` edge `0.0994` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.4857` n `228` status `ready` deltaP `7.2224` edge `0.1037` maxDD `-4.9097`
- `market_context_high->metal_24h` score `0.2041` n `197` status `ready` deltaP `11.8664` edge `0.1805` maxDD `-12.7414`
- `market_context_high->index_24h` score `0.1485` n `197` status `ready` deltaP `4.3218` edge `0.1064` maxDD `-4.1604`
- `market_context_high->index_4h` score `0.0758` n `216` status `ready` deltaP `7.8478` edge `0.0629` maxDD `-3.7119`
- `market_context_high->equity_1h` score `-0.1615` n `228` status `ready` deltaP `5.0426` edge `0.0323` maxDD `-2.6836`
- `market_context_high->fx_24h` score `-0.2938` n `197` status `ready` deltaP `9.7831` edge `0.0152` maxDD `-1.3925`
- `market_context_high->fx_1h` score `-0.6116` n `228` status `ready` deltaP `-2.3532` edge `0.0005` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.6405` n `228` status `ready` deltaP `0.4202` edge `0.007` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.7508` n `228` status `ready` deltaP `3.648` edge `0.013` maxDD `-6.3532`
- `market_context_high->fx_4h` score `-0.9318` n `216` status `ready` deltaP `-4.432` edge `-0.0011` maxDD `-1.1056`
- `market_context_high->equity_24h` score `-1.0249` n `197` status `ready` deltaP `8.0751` edge `0.3506` maxDD `-33.1875`
- `market_context_high->unknown_1h` score `-1.3728` n `228` status `ready` deltaP `0.9429` edge `-0.0255` maxDD `-3.6151`
- `market_context_high->metal_4h` score `-1.4773` n `216` status `ready` deltaP `7.2267` edge `0.0979` maxDD `-12.5349`
- `market_context_high->commodity_1h` score `-1.9921` n `228` status `ready` deltaP `1.1556` edge `-0.0073` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
