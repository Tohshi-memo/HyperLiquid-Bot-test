# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T17:07:25.668541+00:00`
- Price records: `672`
- Market context records: `2059`
- Flow alert records: `7820`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9125`

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

- `market_context_high->crypto_major_4h` score `9.5952` n `205` status `ready` deltaP `33.689` edge `0.628` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `8.9004` n `205` status `ready` deltaP `25.9147` edge `0.6834` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `6.4499` n `205` status `ready` deltaP `20.6707` edge `0.4746` maxDD `-2.6599`
- `market_context_high->unknown_24h` score `4.2412` n `205` status `ready` deltaP `18.2066` edge `0.7641` maxDD `-35.8966`
- `market_context_high->equity_4h` score `3.4882` n `205` status `ready` deltaP `19.0854` edge `0.2729` maxDD `-5.0894`
- `market_context_high->index_4h` score `2.0143` n `205` status `ready` deltaP `15.2134` edge `0.1348` maxDD `-1.8022`
- `market_context_high->crypto_major_1h` score `1.7551` n `206` status `ready` deltaP `13.7056` edge `0.1535` maxDD `-3.2225`
- `market_context_high->equity_24h` score `1.3692` n `205` status `ready` deltaP `19.086` edge `0.4767` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `1.3637` n `206` status `ready` deltaP `10.5619` edge `0.1546` maxDD `-4.9097`
- `market_context_high->index_24h` score `1.197` n `205` status `ready` deltaP `7.588` edge `0.172` maxDD `-4.1604`
- `market_context_high->equity_1h` score `0.4225` n `206` status `ready` deltaP `8.2714` edge `0.0589` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `0.3288` n `206` status `ready` deltaP `5.1087` edge `0.0653` maxDD `-3.0902`
- `market_context_high->index_1h` score `-0.0947` n `206` status `ready` deltaP `3.9068` edge `0.0251` maxDD `-1.3898`
- `market_context_high->crypto_major_24h` score `-0.2294` n `205` status `ready` deltaP `19.2995` edge `0.7108` maxDD `-62.3533`
- `market_context_high->fx_24h` score `-0.3344` n `205` status `ready` deltaP `13.0255` edge `0.0246` maxDD `-2.811`
- `market_context_high->metal_4h` score `-0.6165` n `205` status `ready` deltaP `11.1586` edge `0.1365` maxDD `-11.9812`
- `market_context_high->metal_1h` score `-0.7811` n `206` status `ready` deltaP `3.9969` edge `0.027` maxDD `-5.166`
- `market_context_high->fx_1h` score `-0.8035` n `206` status `ready` deltaP `-0.7485` edge `0.0008` maxDD `-0.3548`
- `market_context_high->fx_4h` score `-1.4174` n `205` status `ready` deltaP `-4.4512` edge `-0.0003` maxDD `-1.0513`
- `market_context_high->commodity_1h` score `-1.9582` n `206` status `ready` deltaP `1.9417` edge `-0.0082` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
