# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T16:07:32.795419+00:00`
- Price records: `672`
- Market context records: `5056`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10292`

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

- `market_context_high->unknown_1h` score `12.0832` n `100` status `ready` deltaP `3.9042` edge `1.031` maxDD `-1.674`
- `market_context_high->unknown_4h` score `8.8955` n `100` status `ready` deltaP `21.6463` edge `0.6992` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `5.5119` n `100` status `ready` deltaP `16.811` edge `0.4856` maxDD `-7.7348`
- `market_context_high->crypto_major_4h` score `5.1574` n `100` status `ready` deltaP `15.9634` edge `0.4818` maxDD `-8.3416`
- `market_context_high->crypto_major_1h` score `0.8974` n `100` status `ready` deltaP `7.6407` edge `0.1126` maxDD `-4.4335`
- `market_context_high->metal_4h` score `0.7888` n `100` status `ready` deltaP `8.9451` edge `0.114` maxDD `-1.9651`
- `market_context_high->equity_1h` score `0.5079` n `100` status `ready` deltaP `7.8982` edge `0.0698` maxDD `-2.5875`
- `market_context_high->equity_4h` score `0.4829` n `100` status `ready` deltaP `4.8293` edge `0.1637` maxDD `-6.3852`
- `market_context_high->metal_1h` score `0.383` n `100` status `ready` deltaP `6.7904` edge `0.0363` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.2169` n `100` status `ready` deltaP `5.6467` edge `0.0907` maxDD `-5.3758`
- `market_context_high->fx_24h` score `-0.0717` n `76` status `ready` deltaP `8.7902` edge `0.0084` maxDD `-1.7626`
- `market_context_high->index_4h` score `-0.1281` n `100` status `ready` deltaP `4.1159` edge `0.038` maxDD `-1.0893`
- `market_context_high->commodity_1h` score `-0.3453` n `100` status `ready` deltaP `1.0958` edge `0.0144` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.4696` n `100` status `ready` deltaP `0.2994` edge `0.0119` maxDD `-0.5946`
- `market_context_high->commodity_4h` score `-0.758` n `100` status `ready` deltaP `7.9939` edge `0.0088` maxDD `-5.021`
- `market_context_high->fx_4h` score `-1.0288` n `100` status `ready` deltaP `-4.5244` edge `-0.0028` maxDD `-1.2484`
- `market_context_high->fx_1h` score `-1.4803` n `100` status `ready` deltaP `-8.6048` edge `-0.005` maxDD `-0.5464`
- `market_context_high->metal_24h` score `-3.5283` n `76` status `ready` deltaP `6.3962` edge `0.0505` maxDD `-32.9721`
- `market_context_high->unknown_24h` score `-3.5798` n `76` status `ready` deltaP `27.3209` edge `-0.4462` maxDD `-1.4072`
- `market_context_high->commodity_24h` score `-4.5455` n `76` status `ready` deltaP `0.3107` edge `-0.0882` maxDD `-26.7306`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
