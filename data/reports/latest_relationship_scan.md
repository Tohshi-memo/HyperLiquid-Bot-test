# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T18:07:31.767869+00:00`
- Price records: `672`
- Market context records: `2584`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9200`

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

- `market_context_high->unknown_24h` score `6.9942` n `127` status `ready` deltaP `18.4465` edge `0.4927` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `6.0771` n `146` status `ready` deltaP `26.5683` edge `0.5972` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `4.299` n `146` status `ready` deltaP `17.8124` edge `0.4205` maxDD `-10.1468`
- `market_context_high->crypto_alt_1h` score `1.436` n `146` status `ready` deltaP `11.73` edge `0.1602` maxDD `-6.1656`
- `market_context_high->unknown_4h` score `1.175` n `146` status `ready` deltaP `9.209` edge `0.1415` maxDD `-3.7312`
- `market_context_high->crypto_alt_24h` score `0.9606` n `127` status `ready` deltaP `2.6383` edge `0.7434` maxDD `-39.0265`
- `market_context_high->crypto_major_1h` score `0.9211` n `146` status `ready` deltaP `10.0607` edge `0.1291` maxDD `-4.2199`
- `market_context_high->index_24h` score `0.7699` n `127` status `ready` deltaP `7.9998` edge `0.1089` maxDD `-2.5127`
- `market_context_high->equity_24h` score `0.5511` n `127` status `ready` deltaP `17.5416` edge `-0.004` maxDD `-2.3615`
- `market_context_high->crypto_major_24h` score `0.4823` n `127` status `ready` deltaP `7.8398` edge `0.4729` maxDD `-28.7981`
- `market_context_high->index_4h` score `0.3256` n `146` status `ready` deltaP `9.4325` edge `0.0484` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1827` n `146` status `ready` deltaP `3.642` edge `0.0099` maxDD `-1.2855`
- `market_context_high->commodity_1h` score `-0.3823` n `146` status `ready` deltaP `5.502` edge `0.0193` maxDD `-4.3601`
- `market_context_high->unknown_1h` score `-0.432` n `146` status `ready` deltaP `1.6508` edge `0.0193` maxDD `-2.6375`
- `market_context_high->metal_4h` score `-0.535` n `146` status `ready` deltaP `4.9594` edge `0.0611` maxDD `-4.7664`
- `market_context_high->metal_1h` score `-0.662` n `146` status `ready` deltaP `0.8121` edge `0.0142` maxDD `-2.9823`
- `market_context_high->fx_1h` score `-0.688` n `146` status `ready` deltaP `-1.134` edge `0.0037` maxDD `-0.278`
- `market_context_high->fx_4h` score `-0.8938` n `146` status `ready` deltaP `-0.2255` edge `0.0128` maxDD `-0.8621`
- `market_context_high->equity_1h` score `-0.9116` n `146` status `ready` deltaP `-0.9761` edge `0.0144` maxDD `-2.7085`
- `market_context_high->fx_24h` score `-1.0037` n `127` status `ready` deltaP `2.2228` edge `0.0009` maxDD `-1.6157`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
