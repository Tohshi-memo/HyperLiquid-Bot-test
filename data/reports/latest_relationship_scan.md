# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T17:07:26.936734+00:00`
- Price records: `672`
- Market context records: `7689`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14676`

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

- `market_context_high->equity_24h` score `3.1264` n `134` status `ready` deltaP `18.1523` edge `0.2737` maxDD `-6.0681`
- `market_context_high->crypto_major_4h` score `1.0309` n `135` status `ready` deltaP `14.5968` edge `0.1604` maxDD `-6.7444`
- `market_context_high->crypto_major_1h` score `0.9504` n `135` status `ready` deltaP `12.2222` edge `0.0424` maxDD `-1.5748`
- `market_context_high->equity_4h` score `0.594` n `135` status `ready` deltaP `2.9799` edge `0.2678` maxDD `-7.9205`
- `market_context_high->crypto_alt_4h` score `0.5837` n `135` status `ready` deltaP `7.4943` edge `0.1104` maxDD `-3.9374`
- `market_context_high->equity_1h` score `0.5559` n `135` status `ready` deltaP `7.7778` edge `0.0804` maxDD `-4.2072`
- `market_context_high->index_1h` score `0.3153` n `135` status `ready` deltaP `8.0981` edge `0.0153` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `-0.055` n `135` status `ready` deltaP `2.8998` edge `0.0274` maxDD `-2.1049`
- `market_context_high->index_4h` score `-0.1502` n `135` status `ready` deltaP `12.0693` edge `0.0461` maxDD `-1.3325`
- `market_context_high->fx_24h` score `-0.1512` n `134` status `ready` deltaP `10.3308` edge `0.0205` maxDD `-3.0343`
- `market_context_high->commodity_1h` score `-0.2802` n `135` status `ready` deltaP `2.7827` edge `0.004` maxDD `-0.6722`
- `market_context_high->fx_1h` score `-0.4081` n `135` status `ready` deltaP `0.8308` edge `-0.0008` maxDD `-0.4331`
- `market_context_high->commodity_4h` score `-0.4288` n `135` status `ready` deltaP `1.8926` edge `0.011` maxDD `-1.0817`
- `market_context_high->metal_1h` score `-0.8415` n `135` status `ready` deltaP `1.5912` edge `0.0196` maxDD `-0.6936`
- `market_context_high->metal_24h` score `-1.1111` n `135` status `ready` deltaP `1.6898` edge `0.1169` maxDD `-2.6605`
- `market_context_high->unknown_1h` score `-1.3209` n `135` status `ready` deltaP `-0.5201` edge `-0.0476` maxDD `-1.054`
- `market_context_high->fx_4h` score `-1.5339` n `135` status `ready` deltaP `-4.5769` edge `-0.0033` maxDD `-1.6936`
- `market_context_high->metal_4h` score `-1.5574` n `135` status `ready` deltaP `1.0016` edge `0.0728` maxDD `-1.7409`
- `market_context_high->commodity_24h` score `-1.606` n `134` status `ready` deltaP `5.9572` edge `-0.0152` maxDD `-7.0012`
- `market_context_high->unknown_4h` score `-2.6077` n `135` status `ready` deltaP `14.3778` edge `-0.1728` maxDD `-2.2285`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
