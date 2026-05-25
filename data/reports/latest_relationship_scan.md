# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T15:22:16.981325+00:00`
- Price records: `672`
- Market context records: `1854`
- Flow alert records: `7237`
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

- `market_context_high->crypto_alt_4h` score `6.4999` n `199` status `ready` deltaP `21.2893` edge `0.5142` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `5.914` n `199` status `ready` deltaP `24.666` edge `0.453` maxDD `-4.9684`
- `market_context_high->metal_24h` score `5.5601` n `178` status `ready` deltaP `23.0767` edge `0.5521` maxDD `-12.7414`
- `market_context_high->unknown_4h` score `4.2183` n `199` status `ready` deltaP `17.0433` edge `0.4403` maxDD `-9.8581`
- `market_context_high->index_24h` score `2.7618` n `178` status `ready` deltaP `14.7433` edge `0.2547` maxDD `-4.1604`
- `market_context_high->unknown_24h` score `2.5079` n `178` status `ready` deltaP `13.8655` edge `0.6486` maxDD `-35.8966`
- `market_context_high->equity_4h` score `2.1712` n `199` status `ready` deltaP `14.2771` edge `0.1952` maxDD `-5.0894`
- `market_context_high->equity_24h` score `0.6444` n `178` status `ready` deltaP `11.7216` edge `0.4654` maxDD `-33.1875`
- `market_context_high->index_4h` score `0.4503` n `199` status `ready` deltaP `10.398` edge `0.0771` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.1742` n `199` status `ready` deltaP `4.3993` edge `0.0838` maxDD `-3.2225`
- `market_context_high->crypto_major_24h` score `0.1591` n `178` status `ready` deltaP `19.2065` edge `0.7438` maxDD `-62.3533`
- `market_context_high->fx_24h` score `0.0948` n `178` status `ready` deltaP `13.1711` edge `0.025` maxDD `-1.3925`
- `market_context_high->crypto_alt_1h` score `-0.0248` n `199` status `ready` deltaP `4.2601` edge `0.0809` maxDD `-4.9097`
- `market_context_high->equity_1h` score `-0.2259` n `199` status `ready` deltaP `4.0886` edge `0.0333` maxDD `-2.6836`
- `market_context_high->unknown_1h` score `-0.4773` n `199` status `ready` deltaP `3.2874` edge `0.0335` maxDD `-3.6151`
- `market_context_high->metal_1h` score `-0.613` n `199` status `ready` deltaP `5.3832` edge `0.0191` maxDD `-6.3532`
- `market_context_high->metal_4h` score `-0.6684` n `199` status `ready` deltaP `12.238` edge `0.1319` maxDD `-12.5349`
- `market_context_high->index_1h` score `-0.6961` n `199` status `ready` deltaP `-0.6048` edge `0.0092` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.7033` n `199` status `ready` deltaP `-3.9509` edge `-0.0006` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-1.0097` n `199` status `ready` deltaP `-5.3438` edge `-0.005` maxDD `-1.1056`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
