# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T16:22:15.609965+00:00`
- Price records: `672`
- Market context records: `1858`
- Flow alert records: `7250`
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

- `market_context_high->crypto_alt_4h` score `6.5083` n `199` status `ready` deltaP `21.2893` edge `0.5149` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `5.9826` n `199` status `ready` deltaP `24.8184` edge `0.4577` maxDD `-4.9684`
- `market_context_high->metal_24h` score `5.2322` n `178` status `ready` deltaP `22.3822` edge `0.5294` maxDD `-12.7414`
- `market_context_high->unknown_4h` score `4.1474` n `199` status `ready` deltaP `16.8909` edge `0.4354` maxDD `-9.8581`
- `market_context_high->index_24h` score `2.5851` n `178` status `ready` deltaP `14.0489` edge `0.2446` maxDD `-4.1604`
- `market_context_high->unknown_24h` score `2.2952` n `178` status `ready` deltaP `13.1711` edge `0.6355` maxDD `-35.8966`
- `market_context_high->equity_4h` score `2.1276` n `199` status `ready` deltaP `13.9723` edge `0.1936` maxDD `-5.0894`
- `market_context_high->equity_24h` score `0.4569` n `178` status `ready` deltaP `11.0272` edge `0.4544` maxDD `-33.1875`
- `market_context_high->index_4h` score `0.3981` n `199` status `ready` deltaP `9.9407` edge `0.0758` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.2545` n `199` status `ready` deltaP `4.9981` edge `0.0865` maxDD `-3.2225`
- `market_context_high->crypto_major_24h` score `0.1927` n `178` status `ready` deltaP `19.2065` edge `0.7466` maxDD `-62.3533`
- `market_context_high->fx_24h` score `0.1485` n `178` status `ready` deltaP `13.6919` edge `0.026` maxDD `-1.3925`
- `market_context_high->crypto_alt_1h` score `0.0243` n `199` status `ready` deltaP `4.5595` edge `0.083` maxDD `-4.9097`
- `market_context_high->equity_1h` score `-0.2307` n `199` status `ready` deltaP `4.0886` edge `0.0329` maxDD `-2.6836`
- `market_context_high->unknown_1h` score `-0.5516` n `199` status `ready` deltaP `2.988` edge `0.0293` maxDD `-3.6151`
- `market_context_high->metal_1h` score `-0.5811` n `199` status `ready` deltaP `5.8323` edge `0.0202` maxDD `-6.3532`
- `market_context_high->metal_4h` score `-0.66` n `199` status `ready` deltaP `12.238` edge `0.1326` maxDD `-12.5349`
- `market_context_high->fx_1h` score `-0.6745` n `199` status `ready` deltaP `-3.5018` edge `0.0001` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.7392` n `199` status `ready` deltaP `-1.0539` edge `0.0086` maxDD `-1.7205`
- `market_context_high->fx_4h` score `-0.9891` n `199` status `ready` deltaP `-5.0389` edge `-0.0044` maxDD `-1.1056`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
