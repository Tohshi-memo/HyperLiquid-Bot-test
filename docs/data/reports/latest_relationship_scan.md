# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T17:37:17.432105+00:00`
- Price records: `672`
- Market context records: `1863`
- Flow alert records: `7265`
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

- `market_context_high->crypto_alt_4h` score `6.4915` n `199` status `ready` deltaP `21.2893` edge `0.5135` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.0826` n `199` status `ready` deltaP `25.1233` edge `0.464` maxDD `-4.9684`
- `market_context_high->metal_24h` score `4.8015` n `178` status `ready` deltaP `21.5142` edge `0.4993` maxDD `-12.7414`
- `market_context_high->unknown_4h` score `4.103` n `199` status `ready` deltaP `16.8909` edge `0.4317` maxDD `-9.8581`
- `market_context_high->index_24h` score `2.4088` n `178` status `ready` deltaP `13.1808` edge `0.2357` maxDD `-4.1604`
- `market_context_high->equity_4h` score `2.1372` n `199` status `ready` deltaP `13.9723` edge `0.1944` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `2.044` n `178` status `ready` deltaP `12.4766` edge `0.6192` maxDD `-35.8966`
- `market_context_high->index_4h` score `0.3957` n `199` status `ready` deltaP `9.9407` edge `0.0756` maxDD `-3.7119`
- `market_context_high->equity_24h` score `0.3631` n `178` status `ready` deltaP `10.68` edge `0.4489` maxDD `-33.1875`
- `market_context_high->crypto_major_1h` score `0.2976` n `199` status `ready` deltaP `5.2975` edge `0.0881` maxDD `-3.2225`
- `market_context_high->crypto_major_24h` score `0.2227` n `178` status `ready` deltaP `19.2065` edge `0.7491` maxDD `-62.3533`
- `market_context_high->fx_24h` score `0.1636` n `178` status `ready` deltaP `13.8655` edge `0.0261` maxDD `-1.3925`
- `market_context_high->crypto_alt_1h` score `-0.0105` n `199` status `ready` deltaP `4.4098` edge `0.0811` maxDD `-4.9097`
- `market_context_high->equity_1h` score `-0.2534` n `199` status `ready` deltaP `3.9389` edge `0.032` maxDD `-2.6836`
- `market_context_high->unknown_1h` score `-0.5768` n `199` status `ready` deltaP `2.988` edge `0.0272` maxDD `-3.6151`
- `market_context_high->metal_1h` score `-0.5936` n `199` status `ready` deltaP `5.6826` edge `0.0196` maxDD `-6.3532`
- `market_context_high->fx_1h` score `-0.6581` n `199` status `ready` deltaP `-3.2024` edge `0.0002` maxDD `-0.3914`
- `market_context_high->metal_4h` score `-0.6804` n `199` status `ready` deltaP `12.238` edge `0.1309` maxDD `-12.5349`
- `market_context_high->index_1h` score `-0.7763` n `199` status `ready` deltaP `-1.3533` edge `0.0075` maxDD `-1.7205`
- `market_context_high->fx_4h` score `-0.9891` n `199` status `ready` deltaP `-5.0389` edge `-0.0044` maxDD `-1.1056`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
