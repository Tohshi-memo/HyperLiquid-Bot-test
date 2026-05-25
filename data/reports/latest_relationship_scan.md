# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T10:52:18.081655+00:00`
- Price records: `672`
- Market context records: `1835`
- Flow alert records: `7182`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4488`

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

- `market_context_high->crypto_alt_4h` score `6.9422` n `194` status `ready` deltaP `22.9931` edge `0.5397` maxDD `-5.1574`
- `market_context_high->metal_24h` score `6.5245` n `178` status `ready` deltaP `25.6808` edge `0.6151` maxDD `-12.7414`
- `market_context_high->crypto_major_4h` score `6.45` n `194` status `ready` deltaP `26.5511` edge `0.4851` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `4.3924` n `194` status `ready` deltaP `17.1344` edge `0.4542` maxDD `-9.8581`
- `market_context_high->index_24h` score `3.4695` n `178` status `ready` deltaP `17.6947` edge `0.294` maxDD `-4.1604`
- `market_context_high->equity_4h` score `2.9308` n `194` status `ready` deltaP `16.4382` edge `0.2441` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `2.7279` n `178` status `ready` deltaP `14.56` edge `0.6623` maxDD `-35.8966`
- `market_context_high->equity_24h` score `1.8328` n `178` status `ready` deltaP `14.8466` edge `0.5436` maxDD `-33.1875`
- `market_context_high->index_4h` score `0.8464` n `194` status `ready` deltaP `12.3649` edge `0.097` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.3894` n `196` status `ready` deltaP `5.8903` edge `0.0918` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.2103` n `196` status `ready` deltaP `5.7742` edge `0.0904` maxDD `-4.9097`
- `market_context_high->crypto_major_24h` score `0.1409` n `178` status `ready` deltaP `18.8593` edge `0.7446` maxDD `-62.3533`
- `market_context_high->fx_24h` score `-0.0641` n `178` status `ready` deltaP `12.1294` edge `0.0187` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.143` n `196` status `ready` deltaP `3.9839` edge `0.0409` maxDD `-2.6836`
- `market_context_high->unknown_1h` score `-0.5295` n `196` status `ready` deltaP `3.0399` edge `0.0308` maxDD `-3.6151`
- `market_context_high->metal_4h` score `-0.6043` n `194` status `ready` deltaP `12.7845` edge `0.1336` maxDD `-12.5349`
- `market_context_high->metal_1h` score `-0.6415` n `196` status `ready` deltaP `4.9248` edge `0.0185` maxDD `-6.3532`
- `market_context_high->index_1h` score `-0.6633` n `196` status `ready` deltaP `-0.5255` edge `0.0114` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.7402` n `196` status `ready` deltaP `-4.5857` edge `-0.0011` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-1.0564` n `194` status `ready` deltaP `-5.7927` edge `-0.008` maxDD `-1.1056`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
