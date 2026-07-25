# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T08:07:25.936320+00:00`
- Price records: `672`
- Market context records: `7859`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14661`

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

- `market_context_high->equity_24h` score `11.1087` n `130` status `ready` deltaP `28.816` edge `0.8678` maxDD `-6.0681`
- `market_context_high->commodity_24h` score `1.3942` n `130` status `ready` deltaP `22.2342` edge `0.1263` maxDD `-7.0012`
- `market_context_high->equity_4h` score `1.3408` n `131` status `ready` deltaP `4.6536` edge `0.3224` maxDD `-6.8559`
- `market_context_high->crypto_major_4h` score `1.1604` n `131` status `ready` deltaP `14.4305` edge `0.1723` maxDD `-6.7444`
- `market_context_high->metal_24h` score `1.1294` n `131` status `ready` deltaP `9.0134` edge `0.2347` maxDD `-2.3869`
- `market_context_high->crypto_major_1h` score `1.0339` n `131` status `ready` deltaP `12.5954` edge `0.0463` maxDD `-1.5286`
- `market_context_high->fx_24h` score `0.8771` n `130` status `ready` deltaP `25.9063` edge `0.0485` maxDD `-3.0343`
- `market_context_high->crypto_alt_4h` score `0.7445` n `131` status `ready` deltaP `8.1688` edge `0.1193` maxDD `-3.9374`
- `market_context_high->equity_1h` score `0.6625` n `131` status `ready` deltaP `7.1144` edge `0.0937` maxDD `-4.2072`
- `market_context_high->commodity_4h` score `0.5647` n `131` status `ready` deltaP `9.5268` edge `0.0429` maxDD `-1.0817`
- `market_context_high->index_1h` score `0.4384` n `131` status `ready` deltaP `9.3667` edge `0.0171` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.2703` n `131` status `ready` deltaP `4.9321` edge `0.0329` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `0.1517` n `131` status `ready` deltaP `6.727` edge `0.0137` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.1562` n `131` status `ready` deltaP `11.2193` edge `0.051` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.2922` n `131` status `ready` deltaP `0.1937` edge `0.0` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.8508` n `131` status `ready` deltaP `1.385` edge `0.0202` maxDD `-0.6936`
- `market_context_high->index_24h` score `-1.1403` n `130` status `ready` deltaP `-4.3947` edge `0.0928` maxDD `-2.1093`
- `market_context_high->metal_4h` score `-1.2566` n `131` status `ready` deltaP `3.2768` edge `0.0789` maxDD `-1.4368`
- `market_context_high->fx_4h` score `-1.4402` n `131` status `ready` deltaP `-3.4211` edge `0.001` maxDD `-1.6936`
- `market_context_high->crypto_alt_24h` score `-1.581` n `131` status `ready` deltaP `16.0411` edge `0.2199` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
