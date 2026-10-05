# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T00:22:27.752049+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5392`

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

- `market_context_high->unknown_1h` score `100.6207` n `97` status `ready` deltaP `0.1389` edge `8.4256` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `93.965` n `97` status `ready` deltaP `2.7564` edge `7.8432` maxDD `-0.4928`
- `news_risk_high->crypto_major_4h` score `9.7818` n `65` status `ready` deltaP `34.076` edge `0.6083` maxDD `-0.6258`
- `market_context_high->crypto_major_24h` score `7.5126` n `47` status `ready` deltaP `26.8617` edge `0.5122` maxDD `-4.5519`
- `news_risk_high->crypto_alt_4h` score `6.8511` n `65` status `ready` deltaP `21.9207` edge `0.5592` maxDD `-6.4195`
- `market_context_high->crypto_alt_24h` score `6.5219` n `47` status `ready` deltaP `20.608` edge `0.5334` maxDD `-8.1838`
- `news_risk_high->equity_24h` score `5.2791` n `65` status `ready` deltaP `17.6309` edge `0.3324` maxDD `-0.1344`
- `market_context_high->crypto_major_4h` score `4.1153` n `97` status `ready` deltaP `18.057` edge `0.2929` maxDD `-3.294`
- `news_risk_high->index_24h` score `3.601` n `65` status `ready` deltaP `25.3472` edge `0.1311` maxDD `0.0`
- `news_risk_high->equity_4h` score `3.1521` n `65` status `ready` deltaP `22.5586` edge `0.1733` maxDD `-2.881`
- `news_risk_high->index_4h` score `3.0202` n `65` status `ready` deltaP `33.1332` edge `0.057` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.7374` n `65` status `ready` deltaP `11.3634` edge `0.1879` maxDD `-1.5096`
- `news_risk_high->metal_4h` score `2.2481` n `65` status `ready` deltaP `20.2979` edge `0.0936` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.1669` n `65` status `ready` deltaP `26.6651` edge `0.0178` maxDD `-0.1997`
- `market_context_high->crypto_major_1h` score `1.999` n `97` status `ready` deltaP `14.2818` edge `0.1164` maxDD `-2.2692`
- `news_risk_high->crypto_alt_1h` score `1.5726` n `65` status `ready` deltaP `5.3178` edge `0.1475` maxDD `-2.4854`
- `market_context_high->fx_4h` score `1.4796` n `97` status `ready` deltaP `25.7355` edge `0.0274` maxDD `-0.3868`
- `market_context_high->fx_24h` score `1.4248` n `47` status `ready` deltaP `26.5884` edge `0.1072` maxDD `-1.8102`
- `market_context_high->fx_1h` score `0.9791` n `97` status `ready` deltaP `15.166` edge `0.0069` maxDD `-0.113`
- `market_context_high->crypto_alt_4h` score `0.9643` n `97` status `ready` deltaP `3.7764` edge `0.2341` maxDD `-7.6465`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
