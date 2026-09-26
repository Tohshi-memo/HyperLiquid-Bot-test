# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T19:37:26.503646+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11754`

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

- `news_risk_high->unknown_24h` score `4436.478` n `85` status `ready` deltaP `1.2153` edge `369.6984` maxDD `0.0`
- `market_context_high->unknown_1h` score `71.7153` n `47` status `ready` deltaP `8.4693` edge `5.9269` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `46.3215` n `47` status `ready` deltaP `20.7003` edge `3.7614` maxDD `-2.4756`
- `market_context_high->equity_24h` score `25.4732` n `47` status `ready` deltaP `31.9851` edge `1.9451` maxDD `-2.1786`
- `market_context_high->crypto_alt_24h` score `25.1239` n `47` status `ready` deltaP `14.8862` edge `2.0324` maxDD `-2.7051`
- `market_context_high->index_24h` score `6.7603` n `47` status `ready` deltaP `25.9087` edge `0.4036` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.2497` n `47` status `ready` deltaP `27.2459` edge `0.113` maxDD `-0.2401`
- `market_context_high->index_4h` score `2.8333` n `47` status `ready` deltaP `32.8068` edge `0.0328` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.7947` n `47` status `ready` deltaP `18.0591` edge `0.1543` maxDD `-1.3444`
- `news_risk_high->index_24h` score `2.055` n `85` status `ready` deltaP `24.0564` edge `0.0679` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `1.4162` n `85` status `ready` deltaP `30.4249` edge `0.1435` maxDD `-6.8481`
- `market_context_high->equity_1h` score `1.1284` n `47` status `ready` deltaP `12.9634` edge `0.0479` maxDD `-1.5564`
- `news_risk_high->crypto_alt_24h` score `0.8849` n `85` status `ready` deltaP `8.7786` edge `0.4104` maxDD `-29.2814`
- `market_context_high->crypto_alt_4h` score `0.8104` n `47` status `ready` deltaP `8.9258` edge `0.0748` maxDD `-3.3417`
- `market_context_high->index_1h` score `0.8086` n `47` status `ready` deltaP `12.8137` edge `0.0098` maxDD `-0.2275`
- `market_context_high->crypto_major_1h` score `0.4597` n `47` status `ready` deltaP `6.2492` edge `0.0784` maxDD `-4.5405`
- `market_context_high->crypto_major_4h` score `0.4096` n `47` status `ready` deltaP `4.8423` edge `0.0923` maxDD `-5.2359`
- `market_context_high->fx_1h` score `0.3967` n `47` status `ready` deltaP `9.2113` edge `0.0073` maxDD `-0.1854`
- `market_context_high->metal_1h` score `0.0523` n `47` status `ready` deltaP `4.1757` edge `0.0105` maxDD `-0.1976`
- `news_risk_high->index_1h` score `-0.0699` n `139` status `ready` deltaP `2.9714` edge `0.0035` maxDD `-0.3305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
