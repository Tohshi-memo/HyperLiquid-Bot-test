# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T23:22:35.793739+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5036`

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

- `market_context_high->unknown_1h` score `97.5428` n `97` status `ready` deltaP `-0.0108` edge `8.1701` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `84.923` n `97` status `ready` deltaP `2.7564` edge `7.0897` maxDD `-0.4928`
- `news_risk_high->crypto_major_4h` score `9.9746` n `65` status `ready` deltaP `34.6857` edge `0.6203` maxDD `-0.6258`
- `market_context_high->crypto_major_24h` score `7.6432` n `46` status `ready` deltaP `27.3248` edge `0.52` maxDD `-4.5519`
- `news_risk_high->crypto_alt_4h` score `7.0847` n `65` status `ready` deltaP `22.5305` edge `0.5746` maxDD `-6.4195`
- `market_context_high->crypto_alt_24h` score `6.8741` n `46` status `ready` deltaP `20.8862` edge `0.5609` maxDD `-8.1838`
- `news_risk_high->equity_24h` score `5.6119` n `65` status `ready` deltaP `18.3254` edge `0.3555` maxDD `-0.1344`
- `market_context_high->crypto_major_4h` score `4.308` n `97` status `ready` deltaP `18.6667` edge `0.3049` maxDD `-3.294`
- `news_risk_high->index_24h` score `3.6642` n `65` status `ready` deltaP `25.8681` edge `0.1329` maxDD `0.0`
- `news_risk_high->equity_4h` score `3.3257` n `65` status `ready` deltaP `23.1684` edge `0.1837` maxDD `-2.881`
- `news_risk_high->index_4h` score `3.081` n `65` status `ready` deltaP `33.743` edge `0.058` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.7111` n `65` status `ready` deltaP `11.2137` edge `0.1867` maxDD `-1.5096`
- `news_risk_high->metal_4h` score `2.3425` n `65` status `ready` deltaP `20.9076` edge `0.0974` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.1417` n `65` status `ready` deltaP `26.3657` edge `0.0177` maxDD `-0.1997`
- `market_context_high->crypto_major_1h` score `1.9726` n `97` status `ready` deltaP `14.1321` edge `0.1152` maxDD `-2.2692`
- `news_risk_high->crypto_alt_1h` score `1.5618` n `65` status `ready` deltaP `5.3178` edge `0.1466` maxDD `-2.4854`
- `market_context_high->fx_4h` score `1.4504` n `97` status `ready` deltaP `25.4306` edge `0.027` maxDD `-0.3868`
- `market_context_high->fx_24h` score `1.3837` n `46` status `ready` deltaP `25.7096` edge `0.1078` maxDD `-1.8102`
- `market_context_high->crypto_alt_4h` score `1.1979` n `97` status `ready` deltaP `4.3862` edge `0.2495` maxDD `-7.6465`
- `market_context_high->fx_1h` score `0.9372` n `97` status `ready` deltaP `14.7169` edge `0.0064` maxDD `-0.113`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
