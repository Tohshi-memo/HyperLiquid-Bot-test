# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T23:22:29.202386+00:00`
- Price records: `672`
- Market context records: `5088`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10352`

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

- `market_context_high->unknown_24h` score `15.159` n `75` status `ready` deltaP `27.1805` edge `1.1163` maxDD `-1.4072`
- `market_context_high->unknown_1h` score `9.6862` n `108` status `ready` deltaP `2.0293` edge `0.8578` maxDD `-2.7986`
- `market_context_high->unknown_4h` score `8.8923` n `96` status `ready` deltaP `21.9512` edge `0.6969` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `5.3599` n `96` status `ready` deltaP `15.4472` edge `0.4783` maxDD `-7.4366`
- `market_context_high->crypto_major_4h` score `4.3073` n `96` status `ready` deltaP `13.9735` edge `0.475` maxDD `-12.4039`
- `market_context_high->equity_4h` score `2.4795` n `96` status `ready` deltaP `14.126` edge `0.2256` maxDD `-6.3852`
- `market_context_high->equity_1h` score `1.1928` n `108` status `ready` deltaP `10.9614` edge `0.0795` maxDD `-2.5875`
- `market_context_high->index_4h` score `0.4905` n `96` status `ready` deltaP `10.2134` edge `0.0489` maxDD `-1.0893`
- `market_context_high->index_1h` score `0.4615` n `108` status `ready` deltaP `7.5848` edge `0.0177` maxDD `-0.3843`
- `market_context_high->metal_1h` score `0.3854` n `108` status `ready` deltaP `10.224` edge `0.0309` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.285` n `108` status `ready` deltaP `4.8736` edge `0.1002` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.2266` n `108` status `ready` deltaP `6.1654` edge `0.1125` maxDD `-6.9639`
- `market_context_high->metal_4h` score `0.1897` n `96` status `ready` deltaP `7.1393` edge `0.0859` maxDD `-2.067`
- `market_context_high->commodity_4h` score `-0.8205` n `96` status `ready` deltaP `7.3424` edge `0.0001` maxDD `-4.3937`
- `market_context_high->commodity_1h` score `-0.8505` n `108` status `ready` deltaP `-0.2329` edge `0.0014` maxDD `-1.6576`
- `market_context_high->fx_24h` score `-1.2495` n `75` status `ready` deltaP `-1.8889` edge `-0.007` maxDD `-1.7626`
- `market_context_high->commodity_24h` score `-1.3839` n `75` status `ready` deltaP `10.3333` edge `0.0499` maxDD `-15.0303`
- `market_context_high->fx_1h` score `-1.7892` n `108` status `ready` deltaP `-11.9705` edge `-0.0052` maxDD `-0.7944`
- `market_context_high->fx_4h` score `-2.1904` n `96` status `ready` deltaP `-9.9594` edge `-0.0106` maxDD `-1.776`
- `market_context_high->metal_24h` score `-4.5291` n `75` status `ready` deltaP `-5.5` edge `0.0015` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
