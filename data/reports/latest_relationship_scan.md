# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T16:36:09.801825+00:00`
- Price records: `672`
- Market context records: `1859`
- Flow alert records: `7253`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4500`

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

- `market_context_high->crypto_alt_4h` score `6.5143` n `199` status `ready` deltaP `21.2893` edge `0.5154` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.0188` n `199` status `ready` deltaP `24.9709` edge `0.4597` maxDD `-4.9684`
- `market_context_high->metal_24h` score `5.1499` n `178` status `ready` deltaP `22.2086` edge `0.5237` maxDD `-12.7414`
- `market_context_high->unknown_4h` score `4.1558` n `199` status `ready` deltaP `16.8909` edge `0.4361` maxDD `-9.8581`
- `market_context_high->index_24h` score `2.5472` n `178` status `ready` deltaP `13.8753` edge `0.2426` maxDD `-4.1604`
- `market_context_high->unknown_24h` score `2.2748` n `178` status `ready` deltaP `13.1711` edge `0.6338` maxDD `-35.8966`
- `market_context_high->equity_4h` score `2.1446` n `199` status `ready` deltaP `14.1247` edge `0.194` maxDD `-5.0894`
- `market_context_high->equity_24h` score `0.4202` n `178` status `ready` deltaP `10.8536` edge `0.4525` maxDD `-33.1875`
- `market_context_high->index_4h` score `0.4005` n `199` status `ready` deltaP `9.9407` edge `0.076` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.2784` n `199` status `ready` deltaP `5.1478` edge `0.0875` maxDD `-3.2225`
- `market_context_high->crypto_major_24h` score `0.1963` n `178` status `ready` deltaP `19.2065` edge `0.7469` maxDD `-62.3533`
- `market_context_high->fx_24h` score `0.1636` n `178` status `ready` deltaP `13.8655` edge `0.0261` maxDD `-1.3925`
- `market_context_high->crypto_alt_1h` score `0.0279` n `199` status `ready` deltaP `4.5595` edge `0.0833` maxDD `-4.9097`
- `market_context_high->equity_1h` score `-0.2151` n `199` status `ready` deltaP `4.2383` edge `0.0332` maxDD `-2.6836`
- `market_context_high->unknown_1h` score `-0.53` n `199` status `ready` deltaP `3.1377` edge `0.0301` maxDD `-3.6151`
- `market_context_high->metal_1h` score `-0.578` n `199` status `ready` deltaP `5.8323` edge `0.0206` maxDD `-6.3532`
- `market_context_high->metal_4h` score `-0.6588` n `199` status `ready` deltaP `12.238` edge `0.1327` maxDD `-12.5349`
- `market_context_high->fx_1h` score `-0.6659` n `199` status `ready` deltaP `-3.3521` edge `0.0002` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.738` n `199` status `ready` deltaP `-1.0539` edge `0.0087` maxDD `-1.7205`
- `market_context_high->fx_4h` score `-0.9891` n `199` status `ready` deltaP `-5.0389` edge `-0.0044` maxDD `-1.1056`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
