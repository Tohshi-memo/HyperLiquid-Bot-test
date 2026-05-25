# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T22:34:00.136409+00:00`
- Price records: `672`
- Market context records: `1885`
- Flow alert records: `7328`
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

- `market_context_high->crypto_alt_4h` score `7.1127` n `199` status `ready` deltaP `22.8137` edge `0.5551` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.7927` n `199` status `ready` deltaP `27.7148` edge `0.5059` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `4.3409` n `199` status `ready` deltaP `18.1104` edge `0.4434` maxDD `-9.8581`
- `market_context_high->metal_24h` score `3.201` n `183` status `ready` deltaP `18.5024` edge `0.386` maxDD `-12.7414`
- `market_context_high->equity_4h` score `2.3622` n `199` status `ready` deltaP `14.4296` edge `0.2101` maxDD `-5.0894`
- `market_context_high->index_24h` score `1.8715` n `183` status `ready` deltaP `11.3844` edge `0.2029` maxDD `-4.1604`
- `market_context_high->unknown_24h` score `1.6704` n `183` status `ready` deltaP `12.8756` edge `0.5854` maxDD `-35.8966`
- `market_context_high->crypto_major_1h` score `0.5494` n `199` status `ready` deltaP `6.6448` edge `0.1001` maxDD `-3.2225`
- `market_context_high->index_4h` score `0.4399` n `199` status `ready` deltaP `9.7882` edge `0.0803` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `0.2929` n `199` status `ready` deltaP `5.9068` edge `0.0964` maxDD `-4.9097`
- `market_context_high->fx_24h` score `0.2118` n `183` status `ready` deltaP `14.4837` edge `0.026` maxDD `-1.3925`
- `market_context_high->equity_24h` score `0.0981` n `183` status `ready` deltaP `10.2772` edge `0.4295` maxDD `-33.1875`
- `market_context_high->equity_1h` score `-0.1443` n `199` status `ready` deltaP `4.5377` edge `0.0371` maxDD `-2.6836`
- `market_context_high->crypto_major_24h` score `-0.2361` n `183` status `ready` deltaP `18.4056` edge `0.7162` maxDD `-62.3533`
- `market_context_high->metal_1h` score `-0.4938` n `199` status `ready` deltaP `6.8802` edge `0.0244` maxDD `-6.3532`
- `market_context_high->unknown_1h` score `-0.5204` n `199` status `ready` deltaP `3.1377` edge `0.0309` maxDD `-3.6151`
- `market_context_high->metal_4h` score `-0.5602` n `199` status `ready` deltaP `12.3905` edge `0.1399` maxDD `-12.5349`
- `market_context_high->index_1h` score `-0.6709` n `199` status `ready` deltaP `-0.4551` edge `0.0103` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.7095` n `199` status `ready` deltaP `-4.1006` edge `-0.0004` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-0.9852` n `199` status `ready` deltaP `-5.0389` edge `-0.0039` maxDD `-1.1056`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
