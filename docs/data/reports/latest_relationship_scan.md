# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T15:39:18.062177+00:00`
- Price records: `672`
- Market context records: `3087`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6911`

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

- `market_context_high->crypto_alt_24h` score `16.966` n `86` status `ready` deltaP `12.7664` edge `2.5312` maxDD `-26.6275`
- `market_context_high->commodity_24h` score `15.0474` n `86` status `ready` deltaP `45.6113` edge `0.9927` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `14.1557` n `86` status `ready` deltaP `21.1362` edge `1.0852` maxDD `-1.7175`
- `market_context_high->index_24h` score `11.8172` n `86` status `ready` deltaP `34.5203` edge `0.936` maxDD `-11.5093`
- `market_context_high->equity_24h` score `9.1862` n `86` status `ready` deltaP `22.2707` edge `1.4637` maxDD `-30.0893`
- `market_context_high->commodity_4h` score `2.9886` n `120` status `ready` deltaP `18.2927` edge `0.1729` maxDD `-1.9973`
- `market_context_high->unknown_4h` score `0.0384` n `120` status `ready` deltaP `3.4553` edge `0.0855` maxDD `-3.7602`
- `market_context_high->commodity_1h` score `-0.1153` n `124` status `ready` deltaP `0.9224` edge `0.0265` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.5005` n `124` status `ready` deltaP `3.9164` edge `0.016` maxDD `-4.5023`
- `market_context_high->crypto_alt_1h` score `-0.7125` n `124` status `ready` deltaP `4.0661` edge `0.0945` maxDD `-14.7034`
- `market_context_high->unknown_1h` score `-0.9827` n `124` status `ready` deltaP `1.4536` edge `-0.0185` maxDD `-3.1801`
- `market_context_high->fx_24h` score `-1.0289` n `86` status `ready` deltaP `0.8277` edge `-0.0054` maxDD `-0.5357`
- `market_context_high->fx_1h` score `-1.1926` n `124` status `ready` deltaP `-8.9869` edge `-0.0022` maxDD `-0.3147`
- `market_context_high->equity_1h` score `-1.2026` n `124` status `ready` deltaP `-1.1059` edge `0.0005` maxDD `-8.7845`
- `market_context_high->fx_4h` score `-1.306` n `120` status `ready` deltaP `-11.5752` edge `-0.0059` maxDD `-1.0829`
- `market_context_high->index_4h` score `-1.4077` n `120` status `ready` deltaP `9.6341` edge `0.0462` maxDD `-17.6057`
- `market_context_high->crypto_major_1h` score `-1.9584` n `124` status `ready` deltaP `0.1931` edge `0.0618` maxDD `-15.1032`
- `market_context_high->metal_1h` score `-2.3818` n `124` status `ready` deltaP `-7.1567` edge `-0.0114` maxDD `-7.4828`
- `market_context_high->crypto_alt_4h` score `-3.2928` n `120` status `ready` deltaP `16.4431` edge `0.2727` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-3.8082` n `120` status `ready` deltaP `8.0284` edge `-0.0179` maxDD `-36.242`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
