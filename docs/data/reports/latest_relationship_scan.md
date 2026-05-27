# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T07:07:31.326345+00:00`
- Price records: `672`
- Market context records: `2019`
- Flow alert records: `7704`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9085`

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

- `market_context_high->crypto_major_4h` score `8.9195` n `205` status `ready` deltaP `30.7927` edge `0.591` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `8.403` n `205` status `ready` deltaP `24.5427` edge `0.6511` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `5.9205` n `205` status `ready` deltaP `18.689` edge `0.4437` maxDD `-2.6599`
- `market_context_high->equity_4h` score `2.9153` n `205` status `ready` deltaP `16.7988` edge `0.2404` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `1.4769` n `205` status `ready` deltaP `12.0286` edge `0.1415` maxDD `-3.2225`
- `market_context_high->index_4h` score `1.3278` n `205` status `ready` deltaP `12.3171` edge `0.0969` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `1.173` n `205` status `ready` deltaP `9.6334` edge `0.1449` maxDD `-4.9097`
- `market_context_high->unknown_24h` score `0.2132` n `189` status `ready` deltaP `15.9917` edge `0.4432` maxDD `-35.8966`
- `market_context_high->equity_1h` score `0.2032` n `205` status `ready` deltaP `6.9104` edge `0.0497` maxDD `-2.6402`
- `market_context_high->equity_24h` score `0.0804` n `189` status `ready` deltaP `14.8719` edge `0.3974` maxDD `-33.1875`
- `market_context_high->unknown_1h` score `0.0266` n `205` status `ready` deltaP `3.7462` edge `0.0492` maxDD `-3.0902`
- `market_context_high->metal_24h` score `-0.0168` n `189` status `ready` deltaP `11.903` edge `0.164` maxDD `-12.9139`
- `market_context_high->index_24h` score `-0.1599` n `189` status `ready` deltaP `3.1819` edge `0.0883` maxDD `-4.1604`
- `market_context_high->fx_24h` score `-0.2294` n `189` status `ready` deltaP `13.0518` edge `0.0254` maxDD `-2.1887`
- `market_context_high->index_1h` score `-0.3301` n `205` status `ready` deltaP `2.2543` edge `0.0165` maxDD `-1.3898`
- `market_context_high->fx_1h` score `-0.8386` n `205` status `ready` deltaP `-1.1421` edge `0.0005` maxDD `-0.3548`
- `market_context_high->metal_1h` score `-0.9833` n `205` status `ready` deltaP `3.0597` edge `0.0164` maxDD `-5.166`
- `market_context_high->fx_4h` score `-1.5246` n `205` status `ready` deltaP `-5.6707` edge `-0.0011` maxDD `-1.0513`
- `market_context_high->metal_4h` score `-1.5588` n `205` status `ready` deltaP `7.1952` edge `0.0844` maxDD `-11.9812`
- `market_context_high->commodity_1h` score `-1.827` n `205` status `ready` deltaP `3.0546` edge `0.0012` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
