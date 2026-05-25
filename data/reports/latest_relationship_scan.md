# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T12:37:15.193901+00:00`
- Price records: `672`
- Market context records: `1842`
- Flow alert records: `7203`
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

- `market_context_high->crypto_alt_4h` score `6.8236` n `196` status `ready` deltaP `22.6201` edge `0.5323` maxDD `-5.1574`
- `market_context_high->metal_24h` score `6.3357` n `178` status `ready` deltaP `24.9864` edge `0.604` maxDD `-12.7414`
- `market_context_high->crypto_major_4h` score `6.2471` n `196` status `ready` deltaP `25.7996` edge `0.4732` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `4.4329` n `196` status `ready` deltaP `17.6705` edge `0.454` maxDD `-9.8581`
- `market_context_high->index_24h` score `3.2686` n `178` status `ready` deltaP `16.653` edge `0.2842` maxDD `-4.1604`
- `market_context_high->unknown_24h` score `2.7075` n `178` status `ready` deltaP `14.56` edge `0.6606` maxDD `-35.8966`
- `market_context_high->equity_4h` score `2.67` n `196` status `ready` deltaP `15.6079` edge `0.2279` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.42` n `178` status `ready` deltaP `13.6314` edge `0.5173` maxDD `-33.1875`
- `market_context_high->index_4h` score `0.7275` n `196` status `ready` deltaP `11.6134` edge `0.0921` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.3936` n `199` status `ready` deltaP `5.4472` edge `0.0951` maxDD `-3.2225`
- `market_context_high->crypto_major_24h` score `0.2762` n `178` status `ready` deltaP `19.3801` edge `0.7524` maxDD `-62.3533`
- `market_context_high->crypto_alt_1h` score `0.2353` n `199` status `ready` deltaP `5.6074` edge `0.0936` maxDD `-4.9097`
- `market_context_high->equity_1h` score `-0.0363` n `199` status `ready` deltaP `4.6874` edge `0.0451` maxDD `-2.6836`
- `market_context_high->fx_24h` score `-0.0377` n `178` status `ready` deltaP `12.1294` edge `0.0209` maxDD `-1.3925`
- `market_context_high->unknown_1h` score `-0.4845` n `199` status `ready` deltaP `3.4371` edge `0.0319` maxDD `-3.6151`
- `market_context_high->metal_4h` score `-0.5606` n `196` status `ready` deltaP `12.8951` edge `0.1365` maxDD `-12.5349`
- `market_context_high->metal_1h` score `-0.5655` n `199` status `ready` deltaP `5.6826` edge `0.0232` maxDD `-6.3532`
- `market_context_high->index_1h` score `-0.5954` n `199` status `ready` deltaP `-0.006` edge `0.0136` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.7383` n `199` status `ready` deltaP `-4.5497` edge `-0.0011` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-1.0577` n `196` status `ready` deltaP `-5.8922` edge `-0.0075` maxDD `-1.1056`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
