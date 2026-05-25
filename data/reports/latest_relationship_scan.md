# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T12:52:19.292546+00:00`
- Price records: `672`
- Market context records: `1843`
- Flow alert records: `7206`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4489`

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

- `market_context_high->crypto_alt_4h` score `6.7934` n `196` status `ready` deltaP `22.4676` edge `0.5308` maxDD `-5.1574`
- `market_context_high->metal_24h` score `6.2966` n `178` status `ready` deltaP `24.8128` edge `0.6019` maxDD `-12.7414`
- `market_context_high->crypto_major_4h` score `6.2097` n `196` status `ready` deltaP `25.6471` edge `0.4711` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `4.4547` n `196` status `ready` deltaP `17.8229` edge `0.4548` maxDD `-9.8581`
- `market_context_high->index_24h` score `3.2343` n `178` status `ready` deltaP `16.4794` edge `0.2825` maxDD `-4.1604`
- `market_context_high->unknown_24h` score `2.7063` n `178` status `ready` deltaP `14.56` edge `0.6605` maxDD `-35.8966`
- `market_context_high->equity_4h` score `2.629` n `196` status `ready` deltaP `15.4554` edge `0.2255` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.3533` n `178` status `ready` deltaP `13.4577` edge `0.5129` maxDD `-33.1875`
- `market_context_high->index_4h` score `0.7069` n `196` status `ready` deltaP `11.461` edge `0.0914` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.3924` n `199` status `ready` deltaP `5.4472` edge `0.095` maxDD `-3.2225`
- `market_context_high->crypto_major_24h` score `0.2678` n `178` status `ready` deltaP `19.3801` edge `0.7517` maxDD `-62.3533`
- `market_context_high->crypto_alt_1h` score `0.2186` n `199` status `ready` deltaP `5.4577` edge `0.0932` maxDD `-4.9097`
- `market_context_high->equity_1h` score `-0.0124` n `199` status `ready` deltaP `4.8371` edge `0.0461` maxDD `-2.6836`
- `market_context_high->fx_24h` score `-0.0341` n `178` status `ready` deltaP `12.1294` edge `0.0212` maxDD `-1.3925`
- `market_context_high->unknown_1h` score `-0.4665` n `199` status `ready` deltaP `3.5868` edge `0.0324` maxDD `-3.6151`
- `market_context_high->metal_1h` score `-0.5507` n `199` status `ready` deltaP `5.8323` edge `0.0241` maxDD `-6.3532`
- `market_context_high->metal_4h` score `-0.5594` n `196` status `ready` deltaP `12.8951` edge `0.1366` maxDD `-12.5349`
- `market_context_high->index_1h` score `-0.5858` n `199` status `ready` deltaP `-0.006` edge `0.0144` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.7461` n `199` status `ready` deltaP `-4.6994` edge `-0.0011` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-1.0561` n `196` status `ready` deltaP `-5.8922` edge `-0.0073` maxDD `-1.1056`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
