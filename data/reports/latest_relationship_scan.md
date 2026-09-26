# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T01:22:27.938445+00:00`
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

- `news_risk_high->unknown_24h` score `1998.0047` n `88` status `ready` deltaP `-0.7892` edge `166.5101` maxDD `-0.0226`
- `market_context_high->unknown_1h` score `71.443` n `47` status `ready` deltaP `8.3196` edge `5.9052` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `49.8664` n `47` status `ready` deltaP `27.992` edge `4.0082` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `31.3852` n `47` status `ready` deltaP `24.782` edge `2.4882` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.1537` n `47` status `ready` deltaP `32.5059` edge `1.915` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.5487` n `47` status `ready` deltaP `34.0684` edge `0.4149` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.7035` n `47` status `ready` deltaP `31.2389` edge `0.1242` maxDD `-0.2401`
- `market_context_high->equity_4h` score `2.7181` n `47` status `ready` deltaP `17.2969` edge `0.153` maxDD `-1.3444`
- `market_context_high->index_4h` score `2.525` n `47` status `ready` deltaP `29.1483` edge `0.0315` maxDD `-0.2323`
- `market_context_high->crypto_alt_4h` score `1.2989` n `47` status `ready` deltaP `10.9075` edge `0.1023` maxDD `-3.3417`
- `market_context_high->equity_1h` score `1.1344` n `47` status `ready` deltaP `12.9634` edge `0.0484` maxDD `-1.5564`
- `market_context_high->index_1h` score `0.8565` n `47` status `ready` deltaP `13.4125` edge `0.0098` maxDD `-0.2275`
- `news_risk_high->metal_24h` score `0.8381` n `88` status `ready` deltaP `24.9526` edge `0.1072` maxDD `-6.9545`
- `market_context_high->fx_1h` score `0.5213` n `47` status `ready` deltaP `10.7083` edge `0.0077` maxDD `-0.1854`
- `market_context_high->crypto_major_4h` score `0.3718` n `47` status `ready` deltaP `4.385` edge `0.0922` maxDD `-5.2359`
- `market_context_high->crypto_major_1h` score `0.3123` n `47` status `ready` deltaP `5.0516` edge `0.0741` maxDD `-4.5405`
- `news_risk_high->crypto_alt_1h` score `0.3053` n `117` status `ready` deltaP `7.8152` edge `0.0781` maxDD `-4.2849`
- `market_context_high->fx_4h` score `0.0591` n `47` status `ready` deltaP `9.6264` edge `0.0075` maxDD `-0.6736`
- `market_context_high->metal_1h` score `0.0204` n `47` status `ready` deltaP `3.5769` edge `0.0104` maxDD `-0.1976`
- `news_risk_high->index_24h` score `-0.0044` n `88` status `ready` deltaP `10.9059` edge `0.0358` maxDD `-2.392`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
