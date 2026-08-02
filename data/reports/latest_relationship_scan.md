# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-02T03:52:32.091871+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5932`

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

- `news_risk_high->unknown_24h` score `5188.8226` n `60` status `ready` deltaP `33.7146` edge `432.2192` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `18.88` n `53` status `ready` deltaP `60.9103` edge `1.207` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `4.6881` n `68` status `ready` deltaP `17.1359` edge `0.3528` maxDD `-3.4427`
- `market_context_high->commodity_24h` score `1.7665` n `53` status `ready` deltaP `27.4844` edge `0.2291` maxDD `-10.2019`
- `news_risk_high->index_4h` score `1.6957` n `68` status `ready` deltaP `16.5261` edge `0.0692` maxDD `-0.3783`
- `market_context_high->crypto_alt_4h` score `0.7095` n `53` status `ready` deltaP `9.805` edge `0.1213` maxDD `-5.323`
- `news_risk_high->equity_1h` score `0.6791` n `68` status `ready` deltaP `10.2413` edge `0.0706` maxDD `-2.916`
- `market_context_high->fx_4h` score `0.307` n `53` status `ready` deltaP `15.2353` edge `0.0174` maxDD `-1.3685`
- `market_context_high->fx_24h` score `0.2201` n `53` status `ready` deltaP `11.566` edge `0.0491` maxDD `-2.506`
- `news_risk_high->metal_4h` score `0.1125` n `68` status `ready` deltaP `5.165` edge `0.0276` maxDD `-0.8085`
- `news_risk_high->fx_4h` score `0.0945` n `68` status `ready` deltaP `11.9889` edge `0.0237` maxDD `-0.6604`
- `news_risk_high->crypto_alt_1h` score `0.0656` n `68` status `ready` deltaP `6.1818` edge `0.0354` maxDD `-3.1233`
- `market_context_high->fx_1h` score `0.0366` n `53` status `ready` deltaP `7.8014` edge `0.0013` maxDD `-0.6874`
- `market_context_high->commodity_1h` score `0.0252` n `53` status `ready` deltaP `5.0757` edge `0.0235` maxDD `-1.3282`
- `news_risk_high->index_1h` score `-0.0684` n `68` status `ready` deltaP `2.4657` edge `0.0071` maxDD `-0.5845`
- `news_risk_high->fx_1h` score `-0.0778` n `68` status `ready` deltaP `2.6682` edge `0.0045` maxDD `-0.2475`
- `market_context_high->commodity_4h` score `-0.134` n `53` status `ready` deltaP `3.7247` edge `0.0455` maxDD `-3.0005`
- `news_risk_high->metal_1h` score `-0.1427` n `68` status `ready` deltaP `2.4657` edge `0.0056` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.2701` n `68` status `ready` deltaP `1.6203` edge `0.0266` maxDD `-3.762`
- `news_risk_high->commodity_1h` score `-0.6077` n `68` status `ready` deltaP `3.7161` edge `-0.0247` maxDD `-2.9058`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
