# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-02T21:37:27.009621+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5918`

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

- `news_risk_high->unknown_24h` score `4999.6974` n `61` status `ready` deltaP `23.8245` edge `416.5247` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `16.0342` n `40` status `ready` deltaP `54.0625` edge `1.0155` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `11.0898` n `40` status `ready` deltaP `51.3194` edge `0.5948` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `4.5303` n `61` status `ready` deltaP `15.6887` edge `0.3493` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.5242` n `61` status `ready` deltaP `14.6216` edge `0.0676` maxDD `-0.3783`
- `market_context_high->commodity_4h` score `1.0147` n `40` status `ready` deltaP `13.2927` edge `0.1261` maxDD `-2.7703`
- `market_context_high->crypto_alt_4h` score `0.7545` n `40` status `ready` deltaP `8.3537` edge `0.1316` maxDD `-4.9116`
- `market_context_high->fx_4h` score `0.6472` n `40` status `ready` deltaP `20.4573` edge `0.0262` maxDD `-1.3685`
- `market_context_high->commodity_1h` score `0.5363` n `41` status `ready` deltaP `10.333` edge `0.0373` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.4879` n `41` status `ready` deltaP `14.4625` edge `0.0039` maxDD `-0.6874`
- `news_risk_high->equity_1h` score `0.2677` n `61` status `ready` deltaP `6.4641` edge `0.0615` maxDD `-2.916`
- `news_risk_high->fx_1h` score `-0.0326` n `61` status `ready` deltaP `3.5069` edge `0.0047` maxDD `-0.2475`
- `news_risk_high->fx_4h` score `-0.0392` n `61` status `ready` deltaP `10.4983` edge `0.0225` maxDD `-0.6604`
- `news_risk_high->index_1h` score `-0.1291` n `61` status `ready` deltaP `1.7032` edge `0.0044` maxDD `-0.5845`
- `news_risk_high->metal_4h` score `-0.2225` n `61` status `ready` deltaP `1.8118` edge `0.007` maxDD `-0.8085`
- `news_risk_high->crypto_alt_1h` score `-0.2386` n `61` status `ready` deltaP `4.0984` edge `0.0103` maxDD `-3.1233`
- `news_risk_high->commodity_1h` score `-0.3267` n `61` status `ready` deltaP `5.8948` edge `-0.0134` maxDD `-2.0891`
- `market_context_high->crypto_alt_1h` score `-0.3322` n `41` status `ready` deltaP `1.2195` edge `0.012` maxDD `-3.0178`
- `news_risk_high->metal_1h` score `-0.3825` n `61` status `ready` deltaP `-1.1264` edge `-0.0012` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.5772` n `61` status `ready` deltaP `-0.2209` edge `-0.0005` maxDD `-3.762`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
