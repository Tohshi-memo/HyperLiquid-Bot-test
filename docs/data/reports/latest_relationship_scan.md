# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T05:52:26.135670+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12725`

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

- `market_context_high->unknown_24h` score `18700.6859` n `55` status `ready` deltaP `13.3775` edge `1558.3065` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `378.1874` n `82` status `ready` deltaP `-4.502` edge `31.5878` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `17.7597` n `82` status `ready` deltaP `31.8851` edge `1.3162` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `17.7378` n `82` status `ready` deltaP `37.9362` edge `1.3723` maxDD `-9.098`
- `market_context_high->equity_24h` score `10.9392` n `55` status `ready` deltaP `49.3056` edge `0.5829` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `9.7969` n `55` status `ready` deltaP `19.8674` edge `0.7667` maxDD `-3.9523`
- `news_risk_high->equity_24h` score `6.7301` n `82` status `ready` deltaP `18.8178` edge `0.6134` maxDD `-6.5742`
- `news_risk_high->index_24h` score `6.2881` n `82` status `ready` deltaP `44.2157` edge `0.2469` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `4.7067` n `82` status `ready` deltaP `25.2668` edge `0.2692` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `4.299` n `55` status `ready` deltaP `42.1875` edge `0.077` maxDD `0.0`
- `market_context_high->index_24h` score `4.114` n `55` status `ready` deltaP `43.7058` edge `0.0907` maxDD `-0.1391`
- `market_context_high->metal_24h` score `0.664` n `55` status `ready` deltaP `10.2557` edge `0.1114` maxDD `-2.2386`
- `risk_on_high->crypto_alt_4h` score `0.2769` n `59` status `ready` deltaP `10.2547` edge `0.1346` maxDD `-6.7304`
- `risk_on_and_context->crypto_alt_4h` score `0.2769` n `59` status `ready` deltaP `10.2547` edge `0.1346` maxDD `-6.7304`
- `news_risk_high->index_4h` score `0.2695` n `82` status `ready` deltaP `10.2134` edge `0.0293` maxDD `-0.6935`
- `risk_on_high->fx_1h` score `0.1208` n `65` status `ready` deltaP `4.8526` edge `0.0033` maxDD `-0.0464`
- `risk_on_and_context->fx_1h` score `0.1208` n `65` status `ready` deltaP `4.8526` edge `0.0033` maxDD `-0.0464`
- `risk_on_high->metal_1h` score `-0.1239` n `65` status `ready` deltaP `3.1644` edge `0.0016` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `-0.1239` n `65` status `ready` deltaP `3.1644` edge `0.0016` maxDD `-0.3081`
- `market_context_high->fx_1h` score `-0.1639` n `125` status `ready` deltaP `2.9449` edge `-0.0017` maxDD `-0.5274`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
