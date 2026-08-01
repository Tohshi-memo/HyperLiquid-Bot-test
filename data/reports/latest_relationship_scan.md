# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T17:52:24.236323+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5915`

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

- `news_risk_high->unknown_24h` score `5190.2273` n `60` status `ready` deltaP `33.8879` edge `432.3351` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `17.0082` n `53` status `ready` deltaP `55.0178` edge `1.0903` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `6.5392` n `60` status `ready` deltaP `24.065` edge `0.4442` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.6788` n `60` status `ready` deltaP `23.6077` edge `0.0849` maxDD `-0.191`
- `market_context_high->commodity_24h` score `2.044` n `53` status `ready` deltaP `29.9107` edge `0.2485` maxDD `-10.2019`
- `news_risk_high->crypto_major_4h` score `1.3518` n `60` status `ready` deltaP `8.2012` edge `0.1962` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.5829` n `60` status `ready` deltaP `12.2866` edge `0.132` maxDD `-5.8012`
- `market_context_high->crypto_alt_4h` score `0.5683` n `53` status `ready` deltaP `8.8904` edge `0.1093` maxDD `-5.323`
- `news_risk_high->equity_1h` score `0.5463` n `68` status `ready` deltaP `7.9958` edge `0.0745` maxDD `-2.916`
- `news_risk_high->fx_4h` score `0.2535` n `60` status `ready` deltaP `13.8415` edge `0.0246` maxDD `-0.6604`
- `market_context_high->fx_4h` score `0.2058` n `53` status `ready` deltaP `13.5585` edge `0.0156` maxDD `-1.3685`
- `news_risk_high->metal_4h` score `0.1701` n `60` status `ready` deltaP `5.1321` edge `0.0352` maxDD `-0.8085`
- `news_risk_high->crypto_alt_1h` score `0.131` n `68` status `ready` deltaP `7.08` edge `0.0378` maxDD `-3.1233`
- `market_context_high->fx_1h` score `-0.0161` n `53` status `ready` deltaP `7.2026` edge `0.0009` maxDD `-0.6874`
- `news_risk_high->index_1h` score `-0.1003` n `68` status `ready` deltaP `1.7172` edge `0.008` maxDD `-0.5845`
- `news_risk_high->fx_1h` score `-0.112` n `68` status `ready` deltaP `2.0694` edge `0.0041` maxDD `-0.2475`
- `market_context_high->commodity_1h` score `-0.115` n `53` status `ready` deltaP `3.5787` edge `0.0155` maxDD `-1.3282`
- `news_risk_high->metal_1h` score `-0.1419` n `68` status `ready` deltaP `2.316` edge `0.0067` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.196` n `68` status `ready` deltaP `2.3688` edge `0.0311` maxDD `-3.762`
- `market_context_high->fx_24h` score `-0.2223` n `53` status `ready` deltaP `4.6335` edge `0.0386` maxDD `-2.506`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
