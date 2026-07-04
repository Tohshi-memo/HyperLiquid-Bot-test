# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T16:37:29.477687+00:00`
- Price records: `672`
- Market context records: `5682`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8758`

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

- `market_context_high->equity_24h` score `1.8418` n `204` status `ready` deltaP `15.9416` edge `0.5551` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `0.8608` n `254` status `ready` deltaP `11.6706` edge `0.2167` maxDD `-13.4882`
- `market_context_high->crypto_alt_4h` score `0.4214` n `254` status `ready` deltaP `8.749` edge `0.1578` maxDD `-9.1473`
- `market_context_high->equity_4h` score `0.1762` n `254` status `ready` deltaP `5.7519` edge `0.1402` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2682` n `266` status `ready` deltaP `1.8065` edge `0.0012` maxDD `-0.4764`
- `market_context_high->crypto_alt_1h` score `-0.4262` n `266` status `ready` deltaP `2.8713` edge `0.0415` maxDD `-5.0257`
- `market_context_high->metal_1h` score `-0.4881` n `266` status `ready` deltaP `0.8318` edge `-0.0006` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.5225` n `266` status `ready` deltaP `4.1624` edge `0.0294` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.6043` n `266` status `ready` deltaP `0.6855` edge `0.0048` maxDD `-0.9472`
- `market_context_high->crypto_major_1h` score `-0.6511` n `266` status `ready` deltaP `4.2884` edge `0.0417` maxDD `-6.9639`
- `market_context_high->commodity_1h` score `-0.9127` n `266` status `ready` deltaP `0.5988` edge `-0.0035` maxDD `-3.7906`
- `market_context_high->fx_24h` score `-1.1332` n `204` status `ready` deltaP `13.9093` edge `0.0471` maxDD `-3.0744`
- `market_context_high->fx_4h` score `-1.1669` n `254` status `ready` deltaP `4.0258` edge `0.007` maxDD `-1.3415`
- `market_context_high->index_4h` score `-1.2715` n `254` status `ready` deltaP `-0.5473` edge `0.0078` maxDD `-3.04`
- `market_context_high->index_24h` score `-2.5045` n `204` status `ready` deltaP `6.2091` edge `0.038` maxDD `-17.0388`
- `market_context_high->metal_4h` score `-2.879` n `254` status `ready` deltaP `-11.7354` edge `-0.0533` maxDD `-11.6719`
- `market_context_high->commodity_4h` score `-3.7904` n `254` status `ready` deltaP `-2.4618` edge `-0.0319` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.8671` n `204` status `ready` deltaP `3.8705` edge `0.0143` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-8.3042` n `204` status `ready` deltaP `-12.3264` edge `-0.2479` maxDD `-32.7652`
- `market_context_high->commodity_24h` score `-12.0388` n `204` status `ready` deltaP `-9.9061` edge `-0.0763` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
