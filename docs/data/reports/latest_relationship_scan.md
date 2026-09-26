# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T00:52:30.111087+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11662`

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

- `news_risk_high->unknown_24h` score `1737.9827` n `88` status `ready` deltaP `-0.7892` edge `144.8416` maxDD `-0.0226`
- `market_context_high->unknown_1h` score `71.3962` n `47` status `ready` deltaP `8.1698` edge `5.9023` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `49.947` n `47` status `ready` deltaP `28.3392` edge `4.0126` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `31.4296` n `47` status `ready` deltaP `24.782` edge `2.4919` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.1115` n `47` status `ready` deltaP `32.1587` edge `1.9138` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.5698` n `47` status `ready` deltaP `34.242` edge `0.4155` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.7059` n `47` status `ready` deltaP `31.2389` edge `0.1244` maxDD `-0.2401`
- `market_context_high->equity_4h` score `2.7181` n `47` status `ready` deltaP `17.2969` edge `0.153` maxDD `-1.3444`
- `market_context_high->index_4h` score `2.525` n `47` status `ready` deltaP `29.1483` edge `0.0315` maxDD `-0.2323`
- `market_context_high->crypto_alt_4h` score `1.3399` n `47` status `ready` deltaP `11.0599` edge `0.1047` maxDD `-3.3417`
- `market_context_high->equity_1h` score `1.1176` n `47` status `ready` deltaP `12.8137` edge `0.048` maxDD `-1.5564`
- `market_context_high->index_1h` score `0.8553` n `47` status `ready` deltaP `13.4125` edge `0.0097` maxDD `-0.2275`
- `news_risk_high->metal_24h` score `0.828` n `88` status `ready` deltaP `24.9526` edge `0.1059` maxDD `-6.9545`
- `news_risk_high->crypto_alt_1h` score `0.7265` n `117` status `ready` deltaP `9.2252` edge `0.0901` maxDD `-4.2849`
- `market_context_high->fx_1h` score `0.4973` n `47` status `ready` deltaP `10.4089` edge `0.0077` maxDD `-0.1854`
- `market_context_high->crypto_major_4h` score `0.4044` n `47` status `ready` deltaP `4.5375` edge `0.0939` maxDD `-5.2359`
- `market_context_high->crypto_major_1h` score `0.2739` n `47` status `ready` deltaP `4.7522` edge `0.0729` maxDD `-4.5405`
- `market_context_high->fx_4h` score `0.0469` n `47` status `ready` deltaP `9.4739` edge `0.0075` maxDD `-0.6736`
- `market_context_high->metal_1h` score `0.004` n `47` status `ready` deltaP `3.2775` edge `0.0103` maxDD `-0.1976`
- `news_risk_high->index_1h` score `-0.0607` n `117` status `ready` deltaP `3.0107` edge `0.0047` maxDD `-0.3863`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
