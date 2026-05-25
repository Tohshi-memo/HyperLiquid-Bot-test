# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T11:37:17.823842+00:00`
- Price records: `672`
- Market context records: `1838`
- Flow alert records: `7191`
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

- `market_context_high->crypto_alt_4h` score `6.907` n `196` status `ready` deltaP `23.0774` edge `0.5362` maxDD `-5.1574`
- `market_context_high->metal_24h` score `6.4626` n `178` status `ready` deltaP `25.5072` edge `0.6111` maxDD `-12.7414`
- `market_context_high->crypto_major_4h` score `6.3521` n `196` status `ready` deltaP `26.2569` edge `0.4789` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `4.3529` n `196` status `ready` deltaP `17.0608` edge `0.4514` maxDD `-9.8581`
- `market_context_high->index_24h` score `3.3925` n `178` status `ready` deltaP `17.3475` edge `0.2899` maxDD `-4.1604`
- `market_context_high->equity_4h` score `2.8376` n `196` status `ready` deltaP `16.2176` edge `0.2378` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `2.7027` n `178` status `ready` deltaP `14.56` edge `0.6602` maxDD `-35.8966`
- `market_context_high->equity_24h` score `1.6663` n `178` status `ready` deltaP `14.3258` edge `0.5332` maxDD `-33.1875`
- `market_context_high->index_4h` score `0.8111` n `196` status `ready` deltaP `12.2232` edge `0.095` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.3906` n `197` status `ready` deltaP `5.7395` edge `0.0929` maxDD `-3.2225`
- `market_context_high->crypto_major_24h` score `0.2522` n `178` status `ready` deltaP `19.3801` edge `0.7504` maxDD `-62.3533`
- `market_context_high->crypto_alt_1h` score `0.2324` n `197` status `ready` deltaP `5.7654` edge `0.0923` maxDD `-4.9097`
- `market_context_high->fx_24h` score `-0.0521` n `178` status `ready` deltaP `12.1294` edge `0.0197` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.1293` n `197` status `ready` deltaP `4.0207` edge `0.0418` maxDD `-2.6836`
- `market_context_high->unknown_1h` score `-0.4747` n `197` status `ready` deltaP `3.4097` edge `0.0329` maxDD `-3.6151`
- `market_context_high->metal_4h` score `-0.5386` n `196` status `ready` deltaP `13.2` edge `0.1363` maxDD `-12.5349`
- `market_context_high->metal_1h` score `-0.6066` n `197` status `ready` deltaP `5.2973` edge `0.0205` maxDD `-6.3532`
- `market_context_high->index_1h` score `-0.6585` n `197` status `ready` deltaP `-0.4498` edge `0.0113` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.742` n `197` status `ready` deltaP `-4.6209` edge `-0.0011` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-1.0537` n `196` status `ready` deltaP `-5.7398` edge `-0.008` maxDD `-1.1056`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
