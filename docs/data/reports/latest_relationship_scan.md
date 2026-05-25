# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T20:03:49.137423+00:00`
- Price records: `672`
- Market context records: `1874`
- Flow alert records: `7296`
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

- `market_context_high->crypto_alt_4h` score `6.7571` n `199` status `ready` deltaP `21.5942` edge `0.5336` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.525` n `199` status `ready` deltaP `26.6477` edge `0.4907` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `4.3133` n `199` status `ready` deltaP `18.1104` edge `0.4411` maxDD `-9.8581`
- `market_context_high->metal_24h` score `3.9234` n `178` status `ready` deltaP `19.778` edge `0.4377` maxDD `-12.7414`
- `market_context_high->equity_4h` score `2.3454` n `199` status `ready` deltaP `14.4296` edge `0.2087` maxDD `-5.0894`
- `market_context_high->index_24h` score `2.2675` n `178` status `ready` deltaP `12.66` edge `0.2274` maxDD `-4.1604`
- `market_context_high->unknown_24h` score `1.9912` n `178` status `ready` deltaP `12.4766` edge `0.6148` maxDD `-35.8966`
- `market_context_high->index_4h` score `0.4677` n `199` status `ready` deltaP `9.9407` edge `0.0816` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.4439` n `199` status `ready` deltaP `6.046` edge `0.0953` maxDD `-3.2225`
- `market_context_high->equity_24h` score `0.4291` n `178` status `ready` deltaP `10.68` edge `0.4544` maxDD `-33.1875`
- `market_context_high->crypto_major_24h` score `0.3283` n `178` status `ready` deltaP `19.2065` edge `0.7579` maxDD `-62.3533`
- `market_context_high->fx_24h` score `0.2728` n `178` status `ready` deltaP `15.0808` edge `0.0271` maxDD `-1.3925`
- `market_context_high->crypto_alt_1h` score `0.1526` n `199` status `ready` deltaP `5.308` edge `0.0887` maxDD `-4.9097`
- `market_context_high->equity_1h` score `-0.239` n `199` status `ready` deltaP `3.7892` edge `0.0342` maxDD `-2.6836`
- `market_context_high->metal_1h` score `-0.5453` n `199` status `ready` deltaP `6.2814` edge `0.0218` maxDD `-6.3532`
- `market_context_high->unknown_1h` score `-0.5552` n `199` status `ready` deltaP `2.988` edge `0.029` maxDD `-3.6151`
- `market_context_high->metal_4h` score `-0.577` n `199` status `ready` deltaP `12.3905` edge `0.1385` maxDD `-12.5349`
- `market_context_high->fx_1h` score `-0.6924` n `199` status `ready` deltaP `-3.8012` edge `-0.0002` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.738` n `199` status `ready` deltaP `-1.0539` edge `0.0087` maxDD `-1.7205`
- `market_context_high->fx_4h` score `-1.0002` n `199` status `ready` deltaP `-5.1913` edge `-0.0048` maxDD `-1.1056`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
