# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T07:37:15.741880+00:00`
- Price records: `672`
- Market context records: `2120`
- Flow alert records: `8000`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9149`

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

- `market_context_high->crypto_alt_4h` score `13.1493` n `161` status `ready` deltaP `37.2159` edge `0.9413` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.8929` n `161` status `ready` deltaP `41.5751` edge `0.7669` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `6.1002` n `161` status `ready` deltaP `24.5342` edge `0.4197` maxDD `-2.6599`
- `market_context_high->equity_4h` score `5.0538` n `161` status `ready` deltaP `25.9354` edge `0.3577` maxDD `-5.0894`
- `market_context_high->metal_4h` score `3.1751` n `161` status `ready` deltaP `21.6653` edge `0.2589` maxDD `-4.7664`
- `market_context_high->index_4h` score `3.1102` n `161` status `ready` deltaP `22.5364` edge `0.1773` maxDD `-1.8022`
- `market_context_high->index_24h` score `2.8619` n `160` status `ready` deltaP `12.4092` edge `0.2786` maxDD `-4.1604`
- `market_context_high->crypto_major_1h` score `2.789` n `161` status `ready` deltaP `16.5201` edge `0.1925` maxDD `-2.6172`
- `news_risk_high->unknown_1h` score `2.755` n `30` status `ready` deltaP `31.2375` edge `0.0516` maxDD `-1.7548`
- `market_context_high->crypto_alt_1h` score `2.6904` n `161` status `ready` deltaP `13.8255` edge `0.2184` maxDD `-4.9097`
- `market_context_high->equity_24h` score `1.9347` n `160` status `ready` deltaP `23.7997` edge `0.4924` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `1.5649` n `160` status `ready` deltaP `24.2625` edge `0.5007` maxDD `-35.8966`
- `news_risk_high->commodity_1h` score `1.0006` n `30` status `ready` deltaP `9.8503` edge `0.0857` maxDD `-2.1052`
- `market_context_high->crypto_major_24h` score `0.9937` n `160` status `ready` deltaP `20.4866` edge `0.8494` maxDD `-62.3533`
- `market_context_high->equity_1h` score `0.6588` n `161` status `ready` deltaP `8.93` edge `0.0742` maxDD `-2.6402`
- `market_context_high->metal_1h` score `0.4562` n `161` status `ready` deltaP `8.0411` edge `0.0514` maxDD `-2.3594`
- `market_context_high->unknown_1h` score `0.0862` n `161` status `ready` deltaP `5.0471` edge `0.0455` maxDD `-3.0902`
- `news_risk_high->fx_1h` score `0.0656` n `30` status `ready` deltaP `3.6327` edge `0.0069` maxDD `-0.0524`
- `market_context_high->metal_24h` score `-0.0205` n `160` status `ready` deltaP `10.7093` edge `0.3161` maxDD `-23.2095`
- `market_context_high->fx_24h` score `-0.0894` n `160` status `ready` deltaP `14.481` edge `0.0313` maxDD `-2.811`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
