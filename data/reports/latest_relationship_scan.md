# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T20:54:43.426777+00:00`
- Price records: `672`
- Market context records: `2075`
- Flow alert records: `7867`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9146`

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

- `market_context_high->crypto_major_4h` score `9.8454` n `204` status `ready` deltaP `35.0012` edge `0.6401` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `9.2689` n `204` status `ready` deltaP `27.8216` edge `0.7014` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `6.8603` n `204` status `ready` deltaP `22.561` edge `0.4962` maxDD `-2.6599`
- `market_context_high->unknown_24h` score `6.1837` n `203` status `ready` deltaP `20.6624` edge `0.9096` maxDD `-35.8966`
- `market_context_high->equity_4h` score `3.5263` n `204` status `ready` deltaP `19.1117` edge `0.2759` maxDD `-5.0894`
- `market_context_high->index_4h` score `2.0223` n `204` status `ready` deltaP `15.223` edge `0.1354` maxDD `-1.8022`
- `market_context_high->crypto_major_1h` score `1.8946` n `204` status `ready` deltaP `14.3243` edge `0.161` maxDD `-3.2225`
- `market_context_high->equity_24h` score `1.8146` n `203` status `ready` deltaP `20.9939` edge `0.5011` maxDD `-33.1875`
- `market_context_high->index_24h` score `1.6096` n `203` status `ready` deltaP `10.0005` edge `0.1903` maxDD `-4.1604`
- `market_context_high->crypto_alt_1h` score `1.5631` n `204` status `ready` deltaP `11.48` edge `0.1651` maxDD `-4.9097`
- `market_context_high->crypto_major_24h` score `0.5619` n `203` status `ready` deltaP `21.2411` edge `0.7638` maxDD `-62.3533`
- `market_context_high->unknown_1h` score `0.4435` n `204` status `ready` deltaP `5.1485` edge `0.0746` maxDD `-3.0902`
- `market_context_high->equity_1h` score `0.4355` n `204` status `ready` deltaP `8.1338` edge `0.0609` maxDD `-2.6402`
- `market_context_high->index_1h` score `-0.0616` n `204` status `ready` deltaP `4.3061` edge `0.0252` maxDD `-1.3898`
- `market_context_high->fx_24h` score `-0.218` n `203` status `ready` deltaP `14.1357` edge `0.0269` maxDD `-2.811`
- `market_context_high->metal_4h` score `-0.5425` n `204` status `ready` deltaP `11.7407` edge `0.1384` maxDD `-11.9502`
- `market_context_high->metal_1h` score `-0.771` n `204` status `ready` deltaP `3.9891` edge `0.0279` maxDD `-5.166`
- `market_context_high->fx_1h` score `-0.8679` n `204` status `ready` deltaP `-1.5381` edge `0.0007` maxDD `-0.3548`
- `market_context_high->fx_4h` score `-1.4439` n `204` status `ready` deltaP `-4.8123` edge `-0.0001` maxDD `-1.0513`
- `market_context_high->metal_24h` score `-1.6959` n `203` status `ready` deltaP `11.2039` edge `0.1741` maxDD `-23.2095`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
