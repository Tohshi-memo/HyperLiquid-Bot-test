# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T07:22:15.717944+00:00`
- Price records: `672`
- Market context records: `2020`
- Flow alert records: `7707`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9091`

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

- `market_context_high->crypto_major_4h` score `8.9291` n `205` status `ready` deltaP `30.7927` edge `0.5918` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `8.421` n `205` status `ready` deltaP `24.5427` edge `0.6526` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `5.9181` n `205` status `ready` deltaP `18.689` edge `0.4435` maxDD `-2.6599`
- `market_context_high->equity_4h` score `2.9455` n `205` status `ready` deltaP `16.9512` edge `0.2419` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `1.4817` n `205` status `ready` deltaP `12.0286` edge `0.1419` maxDD `-3.2225`
- `market_context_high->index_4h` score `1.3544` n `205` status `ready` deltaP `12.4695` edge `0.0981` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `1.185` n `205` status `ready` deltaP `9.6334` edge `0.1459` maxDD `-4.9097`
- `market_context_high->unknown_24h` score `0.3205` n `190` status `ready` deltaP `16.0724` edge `0.4516` maxDD `-35.8966`
- `market_context_high->equity_1h` score `0.2008` n `205` status `ready` deltaP `6.9104` edge `0.0495` maxDD `-2.6402`
- `market_context_high->equity_24h` score `0.1182` n `190` status `ready` deltaP `14.9693` edge `0.3999` maxDD `-33.1875`
- `market_context_high->unknown_1h` score `0.0266` n `205` status `ready` deltaP `3.7462` edge `0.0492` maxDD `-3.0902`
- `market_context_high->index_24h` score `-0.1154` n `190` status `ready` deltaP `3.2877` edge `0.0913` maxDD `-4.1604`
- `market_context_high->metal_24h` score `-0.1626` n `190` status `ready` deltaP `11.7177` edge `0.1624` maxDD `-13.6585`
- `market_context_high->fx_24h` score `-0.2212` n `190` status `ready` deltaP `13.1687` edge `0.0253` maxDD `-2.1887`
- `market_context_high->index_1h` score `-0.3277` n `205` status `ready` deltaP `2.2543` edge `0.0167` maxDD `-1.3898`
- `market_context_high->fx_1h` score `-0.8506` n `205` status `ready` deltaP `-1.2918` edge `0.0005` maxDD `-0.3548`
- `market_context_high->metal_1h` score `-0.9629` n `205` status `ready` deltaP `3.2094` edge `0.0171` maxDD `-5.166`
- `market_context_high->metal_4h` score `-1.5058` n `205` status `ready` deltaP `7.3476` edge `0.0878` maxDD `-11.9812`
- `market_context_high->fx_4h` score `-1.5392` n `205` status `ready` deltaP `-5.8232` edge `-0.0013` maxDD `-1.0513`
- `market_context_high->commodity_1h` score `-1.8161` n `205` status `ready` deltaP `3.2043` edge `0.0016` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
