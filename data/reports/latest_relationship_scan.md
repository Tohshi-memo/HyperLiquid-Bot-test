# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T05:37:19.653802+00:00`
- Price records: `672`
- Market context records: `2112`
- Flow alert records: `7976`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9160`

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

- `market_context_high->crypto_alt_4h` score `12.0561` n `169` status `ready` deltaP `34.0958` edge `0.871` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.2345` n `169` status `ready` deltaP `39.6901` edge `0.7246` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `5.9973` n `169` status `ready` deltaP `24.5381` edge `0.4111` maxDD `-2.6599`
- `market_context_high->equity_4h` score `4.5106` n `169` status `ready` deltaP `23.1202` edge `0.3312` maxDD `-5.0894`
- `market_context_high->index_4h` score `2.6778` n `169` status `ready` deltaP `19.247` edge `0.1632` maxDD `-1.8022`
- `market_context_high->metal_4h` score `2.6673` n `169` status `ready` deltaP `18.9177` edge `0.2349` maxDD `-4.7664`
- `market_context_high->index_24h` score `2.628` n `168` status `ready` deltaP `12.1561` edge `0.2608` maxDD `-4.1604`
- `market_context_high->crypto_major_1h` score `2.3047` n `169` status `ready` deltaP `15.5662` edge `0.1869` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `2.1791` n `169` status `ready` deltaP `12.4296` edge `0.2101` maxDD `-4.9097`
- `market_context_high->unknown_24h` score `1.9252` n `168` status `ready` deltaP `23.7416` edge `0.5342` maxDD `-35.8966`
- `market_context_high->equity_24h` score `1.8701` n `168` status `ready` deltaP `23.4574` edge `0.4893` maxDD `-33.1875`
- `market_context_high->equity_1h` score `0.8661` n `169` status `ready` deltaP `10.5765` edge `0.0805` maxDD `-2.6402`
- `market_context_high->crypto_major_24h` score `0.8144` n `168` status `ready` deltaP `20.9775` edge `0.7866` maxDD `-62.3533`
- `market_context_high->metal_1h` score `0.4953` n `169` status `ready` deltaP `8.3017` edge `0.053` maxDD `-2.3654`
- `market_context_high->index_1h` score `0.1027` n `169` status `ready` deltaP `5.2794` edge `0.0324` maxDD `-1.3898`
- `market_context_high->fx_24h` score `-0.0763` n `168` status `ready` deltaP `14.7636` edge `0.0311` maxDD `-2.811`
- `market_context_high->unknown_1h` score `-0.0998` n `169` status `ready` deltaP `4.5663` edge `0.0332` maxDD `-3.0902`
- `market_context_high->metal_24h` score `-0.1058` n `168` status `ready` deltaP `11.4682` edge `0.3001` maxDD `-23.2095`
- `market_context_high->fx_1h` score `-0.5977` n `169` status `ready` deltaP `-2.2136` edge `0.0009` maxDD `-0.3548`
- `market_context_high->fx_4h` score `-1.1271` n `169` status `ready` deltaP `-7.944` edge `-0.0034` maxDD `-1.0513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
