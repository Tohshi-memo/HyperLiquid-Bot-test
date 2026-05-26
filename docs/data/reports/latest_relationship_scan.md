# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T22:22:19.510392+00:00`
- Price records: `672`
- Market context records: `1981`
- Flow alert records: `7595`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7584`

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

- `market_context_high->crypto_alt_4h` score `7.4024` n `234` status `ready` deltaP `22.5649` edge `0.5809` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.8588` n `234` status `ready` deltaP `26.3511` edge `0.5205` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `2.5095` n `234` status `ready` deltaP `13.743` edge `0.3199` maxDD `-9.8581`
- `market_context_high->equity_4h` score `2.1955` n `234` status `ready` deltaP `13.9058` edge `0.1997` maxDD `-5.0894`
- `market_context_high->metal_24h` score `1.815` n `199` status `ready` deltaP `16.268` edge `0.2854` maxDD `-12.7414`
- `market_context_high->unknown_24h` score `1.7161` n `199` status `ready` deltaP `16.7627` edge `0.5633` maxDD `-35.8966`
- `market_context_high->equity_24h` score `1.17` n `199` status `ready` deltaP `14.9463` edge `0.4877` maxDD `-33.1875`
- `market_context_high->crypto_major_1h` score `1.0255` n `234` status `ready` deltaP `9.5514` edge `0.1204` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.7944` n `234` status `ready` deltaP `8.2451` edge `0.1226` maxDD `-4.9097`
- `market_context_high->index_24h` score `0.4909` n `199` status `ready` deltaP `4.1922` edge `0.1358` maxDD `-4.1604`
- `market_context_high->crypto_major_24h` score `0.3256` n `199` status `ready` deltaP `19.4879` edge `0.7558` maxDD `-62.3533`
- `market_context_high->index_4h` score `0.0699` n `234` status `ready` deltaP `7.0682` edge `0.0676` maxDD `-3.7119`
- `market_context_high->fx_24h` score `-0.1796` n `199` status `ready` deltaP `10.446` edge `0.0203` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.2025` n `234` status `ready` deltaP `4.0509` edge `0.0355` maxDD `-2.6836`
- `market_context_high->fx_1h` score `-0.6678` n `234` status `ready` deltaP `-3.3126` edge `-0.0003` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.6808` n `234` status `ready` deltaP `-0.2635` edge `0.0082` maxDD `-1.7205`
- `market_context_high->fx_4h` score `-1.1784` n `234` status `ready` deltaP `-8.7542` edge `-0.0039` maxDD `-1.1056`
- `market_context_high->metal_1h` score `-1.3779` n `234` status `ready` deltaP `2.4989` edge `0.0021` maxDD `-6.3532`
- `market_context_high->unknown_1h` score `-1.4496` n `234` status `ready` deltaP `1.1081` edge `-0.033` maxDD `-3.6151`
- `market_context_high->commodity_1h` score `-1.8806` n `234` status `ready` deltaP `2.0088` edge `0.0013` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
