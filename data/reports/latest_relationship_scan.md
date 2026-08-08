# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-08T15:37:31.541777+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11573`

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

- `market_context_high->equity_24h` score `3.5683` n `98` status `ready` deltaP `3.6813` edge `0.5788` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.4998` n `98` status `ready` deltaP `11.1466` edge `0.1916` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.4812` n `103` status `ready` deltaP `14.1339` edge `0.0965` maxDD `-2.7169`
- `market_context_high->fx_24h` score `1.1703` n `98` status `ready` deltaP `26.8955` edge `0.0574` maxDD `-1.9329`
- `market_context_high->commodity_1h` score `1.0213` n `103` status `ready` deltaP `11.8365` edge `0.0405` maxDD `-0.7439`
- `market_context_high->index_24h` score `0.3969` n `98` status `ready` deltaP `7.7133` edge `0.1526` maxDD `-5.9181`
- `market_context_high->equity_1h` score `-0.4664` n `103` status `ready` deltaP `3.449` edge `0.021` maxDD `-4.6286`
- `market_context_high->fx_1h` score `-0.4986` n `103` status `ready` deltaP `2.0551` edge `-0.0057` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.5123` n `103` status `ready` deltaP `-3.6335` edge `-0.0067` maxDD `-0.7809`
- `market_context_high->index_4h` score `-0.6382` n `103` status `ready` deltaP `-1.5762` edge `-0.0108` maxDD `-1.1743`
- `market_context_high->metal_1h` score `-0.6397` n `103` status `ready` deltaP `-4.0099` edge `-0.0057` maxDD `-0.9664`
- `market_context_high->fx_4h` score `-0.8893` n `103` status `ready` deltaP `1.0226` edge `-0.0056` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-1.0383` n `103` status `ready` deltaP `-2.9156` edge `-0.0128` maxDD `-2.7373`
- `market_context_high->equity_4h` score `-1.9609` n `103` status `ready` deltaP `2.2836` edge `-0.0449` maxDD `-7.6983`
- `market_context_high->crypto_alt_1h` score `-2.0212` n `103` status `ready` deltaP `-11.4775` edge `-0.029` maxDD `-2.3669`
- `market_context_high->crypto_major_24h` score `-2.4274` n `98` status `ready` deltaP `5.4776` edge `-0.0983` maxDD `-14.2873`
- `market_context_high->crypto_major_1h` score `-2.5428` n `103` status `ready` deltaP `-8.4835` edge `-0.0557` maxDD `-4.6382`
- `market_context_high->crypto_alt_24h` score `-2.836` n `98` status `ready` deltaP `-14.4274` edge `-0.1231` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-4.2628` n `103` status `ready` deltaP `-11.6461` edge `-0.1124` maxDD `-6.5487`
- `market_context_high->crypto_major_4h` score `-7.9633` n `103` status `ready` deltaP `-14.7111` edge `-0.2264` maxDD `-18.1307`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
