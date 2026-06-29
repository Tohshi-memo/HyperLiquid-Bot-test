# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T07:07:28.509952+00:00`
- Price records: `672`
- Market context records: `5121`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5560`

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

- `market_context_high->unknown_24h` score `26.2396` n `67` status `ready` deltaP `28.8583` edge `2.0285` maxDD `-1.4072`
- `market_context_high->unknown_1h` score `8.4391` n `126` status `ready` deltaP `7.9817` edge `0.7142` maxDD `-2.7986`
- `market_context_high->unknown_4h` score `7.3325` n `115` status `ready` deltaP `20.5593` edge `0.5762` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `5.4288` n `115` status `ready` deltaP `15.1829` edge `0.5111` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.8186` n `115` status `ready` deltaP `12.8791` edge `0.4616` maxDD `-14.0065`
- `market_context_high->crypto_alt_1h` score `0.9356` n `126` status `ready` deltaP `6.708` edge `0.1294` maxDD `-5.0257`
- `market_context_high->equity_1h` score `0.7511` n `126` status `ready` deltaP `8.1908` edge `0.0673` maxDD `-2.745`
- `market_context_high->crypto_major_1h` score `0.6955` n `126` status `ready` deltaP `7.6205` edge `0.1317` maxDD `-6.9639`
- `market_context_high->commodity_24h` score `0.4178` n `67` status `ready` deltaP `16.5423` edge `0.1056` maxDD `-8.319`
- `market_context_high->metal_1h` score `0.2289` n `126` status `ready` deltaP `8.0102` edge `0.0274` maxDD `-1.4501`
- `market_context_high->equity_4h` score `0.2177` n `115` status `ready` deltaP `6.6119` edge `0.1477` maxDD `-7.4425`
- `market_context_high->index_1h` score `0.0464` n `126` status `ready` deltaP `5.855` edge `0.0152` maxDD `-1.0296`
- `market_context_high->index_4h` score `-0.4784` n `115` status `ready` deltaP `3.4663` edge `0.0273` maxDD `-2.9391`
- `market_context_high->metal_4h` score `-0.5339` n `115` status `ready` deltaP `2.4271` edge `0.0564` maxDD `-4.6157`
- `market_context_high->fx_1h` score `-0.6487` n `126` status `ready` deltaP `-2.621` edge `-0.0016` maxDD `-0.7944`
- `market_context_high->commodity_1h` score `-0.9533` n `126` status `ready` deltaP `0.0594` edge `-0.0029` maxDD `-2.155`
- `market_context_high->fx_4h` score `-1.0444` n `115` status `ready` deltaP `-4.0654` edge `0.0005` maxDD `-1.9169`
- `market_context_high->fx_24h` score `-1.52` n `67` status `ready` deltaP `-3.0369` edge `-0.0095` maxDD `-1.4206`
- `market_context_high->metal_24h` score `-1.8381` n `67` status `ready` deltaP `-1.3319` edge `0.1115` maxDD `-20.3954`
- `market_context_high->commodity_4h` score `-2.492` n `115` status `ready` deltaP `-0.8537` edge `-0.0301` maxDD `-7.417`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
