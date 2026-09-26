# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T14:07:31.129279+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11822`

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

- `news_risk_high->unknown_24h` score `4384.9946` n `85` status `ready` deltaP `0.3472` edge `365.4139` maxDD `0.0`
- `market_context_high->unknown_1h` score `69.2566` n `47` status `ready` deltaP `8.1698` edge `5.724` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `47.0069` n `47` status `ready` deltaP `22.2628` edge `3.8081` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `26.8712` n `47` status `ready` deltaP `17.3167` edge `2.1618` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.6388` n `47` status `ready` deltaP `33.2003` edge `1.9508` maxDD `-2.1786`
- `market_context_high->index_24h` score `6.9431` n `47` status `ready` deltaP `27.8184` edge `0.4061` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.3371` n `47` status `ready` deltaP `28.1139` edge `0.1145` maxDD `-0.2401`
- `market_context_high->index_4h` score `2.7687` n `47` status `ready` deltaP `32.0446` edge `0.0325` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.7387` n `47` status `ready` deltaP `17.4494` edge `0.1537` maxDD `-1.3444`
- `news_risk_high->crypto_alt_24h` score `2.6321` n `85` status `ready` deltaP `11.2091` edge `0.5398` maxDD `-29.2814`
- `news_risk_high->index_24h` score `2.2378` n `85` status `ready` deltaP `25.9661` edge `0.0704` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `1.473` n `85` status `ready` deltaP `31.2929` edge `0.145` maxDD `-6.8481`
- `market_context_high->crypto_alt_4h` score `1.2941` n `47` status `ready` deltaP `10.9075` edge `0.1019` maxDD `-3.3417`
- `market_context_high->equity_1h` score `1.0637` n `47` status `ready` deltaP `12.2149` edge `0.0475` maxDD `-1.5564`
- `market_context_high->crypto_major_4h` score `0.8347` n `47` status `ready` deltaP `6.9765` edge `0.1135` maxDD `-5.2359`
- `market_context_high->index_1h` score `0.8193` n `47` status `ready` deltaP `12.9634` edge `0.0097` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.4937` n `47` status `ready` deltaP `10.4089` edge `0.0074` maxDD `-0.1854`
- `market_context_high->crypto_major_1h` score `0.4849` n `47` status `ready` deltaP `6.2492` edge `0.0805` maxDD `-4.5405`
- `market_context_high->metal_1h` score `0.0523` n `47` status `ready` deltaP `4.1757` edge `0.0105` maxDD `-0.1976`
- `news_risk_high->index_1h` score `-0.0591` n `139` status `ready` deltaP `3.1211` edge `0.0034` maxDD `-0.3305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
