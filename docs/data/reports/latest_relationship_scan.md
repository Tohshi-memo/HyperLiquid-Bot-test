# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-02T21:52:27.943825+00:00`
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

- `news_risk_high->unknown_24h` score `5001.6978` n `61` status `ready` deltaP `23.8245` edge `416.6914` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `15.9651` n `40` status `ready` deltaP `53.8889` edge `1.0109` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `11.097` n `40` status `ready` deltaP `51.3194` edge `0.5954` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `4.5061` n `61` status `ready` deltaP `15.5363` edge `0.3483` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.5108` n `61` status `ready` deltaP `14.4692` edge `0.0675` maxDD `-0.3783`
- `market_context_high->commodity_4h` score `1.0131` n `40` status `ready` deltaP `13.2927` edge `0.1259` maxDD `-2.7703`
- `market_context_high->crypto_alt_4h` score `0.7545` n `40` status `ready` deltaP `8.3537` edge `0.1316` maxDD `-4.9116`
- `market_context_high->fx_4h` score `0.6464` n `40` status `ready` deltaP `20.4573` edge `0.0261` maxDD `-1.3685`
- `market_context_high->commodity_1h` score `0.5331` n `41` status `ready` deltaP `10.333` edge `0.0369` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.4879` n `41` status `ready` deltaP `14.4625` edge `0.0039` maxDD `-0.6874`
- `news_risk_high->equity_1h` score `0.2725` n `61` status `ready` deltaP `6.4641` edge `0.0619` maxDD `-2.916`
- `news_risk_high->fx_1h` score `-0.0326` n `61` status `ready` deltaP `3.5069` edge `0.0047` maxDD `-0.2475`
- `news_risk_high->fx_4h` score `-0.0404` n `61` status `ready` deltaP `10.4983` edge `0.0224` maxDD `-0.6604`
- `news_risk_high->index_1h` score `-0.1283` n `61` status `ready` deltaP `1.7032` edge `0.0045` maxDD `-0.5845`
- `news_risk_high->metal_4h` score `-0.2225` n `61` status `ready` deltaP `1.8118` edge `0.007` maxDD `-0.8085`
- `news_risk_high->crypto_alt_1h` score `-0.2339` n `61` status `ready` deltaP `4.0984` edge `0.0109` maxDD `-3.1233`
- `market_context_high->crypto_alt_1h` score `-0.3275` n `41` status `ready` deltaP `1.2195` edge `0.0126` maxDD `-3.0178`
- `news_risk_high->commodity_1h` score `-0.3298` n `61` status `ready` deltaP `5.8948` edge `-0.0138` maxDD `-2.0891`
- `news_risk_high->metal_1h` score `-0.3817` n `61` status `ready` deltaP `-1.1264` edge `-0.0011` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.5717` n `61` status `ready` deltaP `-0.2209` edge `0.0002` maxDD `-3.762`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
