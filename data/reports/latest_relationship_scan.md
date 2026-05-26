# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T04:37:20.838084+00:00`
- Price records: `672`
- Market context records: `1912`
- Flow alert records: `7403`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4518`

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

- `market_context_high->crypto_alt_4h` score `7.8832` n `199` status `ready` deltaP `24.7954` edge `0.6061` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `7.2893` n `199` status `ready` deltaP `29.3916` edge `0.5361` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `3.9311` n `199` status `ready` deltaP `17.6531` edge `0.4123` maxDD `-9.8581`
- `market_context_high->equity_4h` score `2.6483` n `199` status `ready` deltaP `15.8015` edge `0.2248` maxDD `-5.0894`
- `market_context_high->metal_24h` score `1.3767` n `189` status `ready` deltaP `15.1538` edge `0.2563` maxDD `-12.7414`
- `market_context_high->unknown_24h` score `1.1892` n `189` status `ready` deltaP `13.3267` edge `0.5423` maxDD `-35.8966`
- `market_context_high->index_24h` score `0.828` n `189` status `ready` deltaP `6.8453` edge `0.1462` maxDD `-4.1604`
- `market_context_high->crypto_major_1h` score `0.7571` n `204` status `ready` deltaP `8.2658` edge `0.1066` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.5723` n `204` status `ready` deltaP `7.5995` edge `0.1084` maxDD `-4.9097`
- `market_context_high->index_4h` score `0.5564` n `199` status `ready` deltaP `10.8553` edge `0.0829` maxDD `-3.7119`
- `market_context_high->fx_24h` score `0.0343` n `189` status `ready` deltaP `12.715` edge `0.023` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.047` n `204` status `ready` deltaP `5.5742` edge `0.0383` maxDD `-2.6836`
- `market_context_high->metal_1h` score `-0.5701` n `204` status `ready` deltaP `5.9234` edge `0.021` maxDD `-6.3532`
- `market_context_high->fx_1h` score `-0.6185` n `204` status `ready` deltaP `-2.5596` edge `0.001` maxDD `-0.3914`
- `market_context_high->metal_4h` score `-0.648` n `199` status `ready` deltaP `12.238` edge `0.1336` maxDD `-12.5349`
- `market_context_high->index_1h` score `-0.6532` n `204` status `ready` deltaP `-0.0235` edge `0.0089` maxDD `-1.7205`
- `market_context_high->equity_24h` score `-0.7931` n `189` status `ready` deltaP `7.4322` edge `0.3742` maxDD `-33.1875`
- `market_context_high->fx_4h` score `-0.7956` n `199` status `ready` deltaP `-2.1425` edge `0.0011` maxDD `-1.1056`
- `market_context_high->unknown_1h` score `-1.0211` n `204` status `ready` deltaP `1.7994` edge `-0.0019` maxDD `-3.6151`
- `market_context_high->crypto_major_24h` score `-1.4207` n `189` status `ready` deltaP `15.1786` edge `0.639` maxDD `-62.3533`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
