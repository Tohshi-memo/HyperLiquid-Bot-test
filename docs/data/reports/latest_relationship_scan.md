# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T20:37:17.352134+00:00`
- Price records: `672`
- Market context records: `1877`
- Flow alert records: `7303`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4510`

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

- `market_context_high->crypto_alt_4h` score `6.7981` n `199` status `ready` deltaP `21.7467` edge `0.536` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.5805` n `199` status `ready` deltaP `26.9526` edge `0.4933` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `4.3265` n `199` status `ready` deltaP `18.1104` edge `0.4422` maxDD `-9.8581`
- `market_context_high->metal_24h` score `3.8036` n `179` status `ready` deltaP `19.5249` edge `0.4294` maxDD `-12.7414`
- `market_context_high->equity_4h` score `2.355` n `199` status `ready` deltaP `14.4296` edge `0.2095` maxDD `-5.0894`
- `market_context_high->index_24h` score `2.1921` n `179` status `ready` deltaP `12.4069` edge `0.2228` maxDD `-4.1604`
- `market_context_high->unknown_24h` score `1.933` n `179` status `ready` deltaP `12.5582` edge `0.6094` maxDD `-35.8966`
- `market_context_high->index_4h` score `0.4665` n `199` status `ready` deltaP `9.9407` edge `0.0815` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.4343` n `199` status `ready` deltaP `6.046` edge `0.0945` maxDD `-3.2225`
- `market_context_high->equity_24h` score `0.3775` n `179` status `ready` deltaP `10.7397` edge `0.4497` maxDD `-33.1875`
- `market_context_high->fx_24h` score `0.2588` n `179` status `ready` deltaP `14.9509` edge `0.0268` maxDD `-1.3925`
- `market_context_high->crypto_major_24h` score `0.2149` n `179` status `ready` deltaP `18.944` edge `0.7502` maxDD `-62.3533`
- `market_context_high->crypto_alt_1h` score `0.1298` n `199` status `ready` deltaP `5.1583` edge `0.0878` maxDD `-4.9097`
- `market_context_high->equity_1h` score `-0.2546` n `199` status `ready` deltaP `3.6395` edge `0.0339` maxDD `-2.6836`
- `market_context_high->unknown_1h` score `-0.5312` n `199` status `ready` deltaP `3.1377` edge `0.03` maxDD `-3.6151`
- `market_context_high->metal_1h` score `-0.5507` n `199` status `ready` deltaP `6.1317` edge `0.0221` maxDD `-6.3532`
- `market_context_high->metal_4h` score `-0.5578` n `199` status `ready` deltaP `12.3905` edge `0.1401` maxDD `-12.5349`
- `market_context_high->fx_1h` score `-0.6846` n `199` status `ready` deltaP `-3.6515` edge `-0.0002` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.7548` n `199` status `ready` deltaP `-1.2036` edge `0.0083` maxDD `-1.7205`
- `market_context_high->fx_4h` score `-0.9915` n `199` status `ready` deltaP `-5.0389` edge `-0.0047` maxDD `-1.1056`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
