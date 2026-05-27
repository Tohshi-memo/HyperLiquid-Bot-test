# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T20:37:18.273161+00:00`
- Price records: `672`
- Market context records: `2073`
- Flow alert records: `7864`
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

- `market_context_high->crypto_major_4h` score `9.7971` n `205` status `ready` deltaP `34.9086` edge `0.6367` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `9.1915` n `205` status `ready` deltaP `27.439` edge `0.6975` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `6.7892` n `205` status `ready` deltaP `22.3475` edge `0.4917` maxDD `-2.6599`
- `market_context_high->unknown_24h` score `6.3747` n `204` status `ready` deltaP `20.5594` edge `0.9262` maxDD `-35.8966`
- `market_context_high->equity_4h` score `3.5196` n `205` status `ready` deltaP `19.2073` edge `0.2747` maxDD `-5.0894`
- `market_context_high->index_4h` score `2.0301` n `205` status `ready` deltaP `15.3354` edge `0.1353` maxDD `-1.8022`
- `market_context_high->crypto_major_1h` score `1.8565` n `205` status `ready` deltaP `14.1631` edge `0.1589` maxDD `-3.2225`
- `market_context_high->equity_24h` score `1.8453` n `204` status `ready` deltaP `21.0784` edge `0.5031` maxDD `-33.1875`
- `market_context_high->index_24h` score `1.5935` n `204` status `ready` deltaP `9.9192` edge `0.1895` maxDD `-4.1604`
- `market_context_high->crypto_alt_1h` score `1.5298` n `205` status `ready` deltaP `11.3188` edge `0.1634` maxDD `-4.9097`
- `market_context_high->crypto_major_24h` score `0.6331` n `204` status `ready` deltaP `21.3957` edge `0.7687` maxDD `-62.3533`
- `market_context_high->unknown_1h` score `0.454` n `205` status `ready` deltaP `5.3542` edge `0.0741` maxDD `-3.0902`
- `market_context_high->equity_1h` score `0.4166` n `205` status `ready` deltaP `7.9583` edge `0.0605` maxDD `-2.6402`
- `market_context_high->index_1h` score `-0.0437` n `205` status `ready` deltaP `4.4998` edge `0.0254` maxDD `-1.3898`
- `market_context_high->fx_24h` score `-0.2244` n `204` status `ready` deltaP `14.1003` edge `0.0266` maxDD `-2.811`
- `market_context_high->metal_4h` score `-0.5462` n `205` status `ready` deltaP `11.7988` edge `0.1377` maxDD `-11.9502`
- `market_context_high->metal_1h` score `-0.7454` n `205` status `ready` deltaP `4.2186` edge `0.0285` maxDD `-5.166`
- `market_context_high->fx_1h` score `-0.847` n `205` status `ready` deltaP `-1.2918` edge `0.0008` maxDD `-0.3548`
- `market_context_high->fx_4h` score `-1.4528` n `205` status `ready` deltaP `-4.9085` edge `-0.0002` maxDD `-1.0513`
- `market_context_high->metal_24h` score `-1.7069` n `204` status `ready` deltaP `11.2168` edge `0.1731` maxDD `-23.2095`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
