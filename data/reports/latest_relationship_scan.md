# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T16:07:18.140612+00:00`
- Price records: `672`
- Market context records: `1857`
- Flow alert records: `7246`
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

- `market_context_high->crypto_alt_4h` score `6.5011` n `199` status `ready` deltaP `21.2893` edge `0.5143` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `5.9452` n `199` status `ready` deltaP `24.666` edge `0.4556` maxDD `-4.9684`
- `market_context_high->metal_24h` score `5.3133` n `178` status `ready` deltaP `22.5558` edge `0.535` maxDD `-12.7414`
- `market_context_high->unknown_4h` score `4.1618` n `199` status `ready` deltaP `16.8909` edge `0.4366` maxDD `-9.8581`
- `market_context_high->index_24h` score `2.6253` n `178` status `ready` deltaP `14.2225` edge `0.2468` maxDD `-4.1604`
- `market_context_high->unknown_24h` score `2.3535` n `178` status `ready` deltaP `13.3447` edge `0.6392` maxDD `-35.8966`
- `market_context_high->equity_4h` score `2.1106` n `199` status `ready` deltaP `13.8198` edge `0.1932` maxDD `-5.0894`
- `market_context_high->equity_24h` score `0.4959` n `178` status `ready` deltaP `11.2008` edge `0.4565` maxDD `-33.1875`
- `market_context_high->index_4h` score `0.3981` n `199` status `ready` deltaP `9.9407` edge `0.0758` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.2353` n `199` status `ready` deltaP `4.8484` edge `0.0859` maxDD `-3.2225`
- `market_context_high->crypto_major_24h` score `0.1807` n `178` status `ready` deltaP `19.2065` edge `0.7456` maxDD `-62.3533`
- `market_context_high->fx_24h` score `0.1334` n `178` status `ready` deltaP `13.5183` edge `0.0259` maxDD `-1.3925`
- `market_context_high->crypto_alt_1h` score `0.0231` n `199` status `ready` deltaP `4.5595` edge `0.0829` maxDD `-4.9097`
- `market_context_high->equity_1h` score `-0.2319` n `199` status `ready` deltaP `4.0886` edge `0.0328` maxDD `-2.6836`
- `market_context_high->unknown_1h` score `-0.5216` n `199` status `ready` deltaP `3.1377` edge `0.0308` maxDD `-3.6151`
- `market_context_high->metal_1h` score `-0.5928` n `199` status `ready` deltaP `5.6826` edge `0.0197` maxDD `-6.3532`
- `market_context_high->metal_4h` score `-0.6576` n `199` status `ready` deltaP `12.238` edge `0.1328` maxDD `-12.5349`
- `market_context_high->fx_1h` score `-0.683` n `199` status `ready` deltaP `-3.6515` edge `0.0` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.726` n `199` status `ready` deltaP `-0.9042` edge `0.0087` maxDD `-1.7205`
- `market_context_high->fx_4h` score `-0.9891` n `199` status `ready` deltaP `-5.0389` edge `-0.0044` maxDD `-1.1056`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
