# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-02T03:07:29.042858+00:00`
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

- `news_risk_high->unknown_24h` score `5188.8214` n `60` status `ready` deltaP `33.7146` edge `432.2191` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `18.802` n `53` status `ready` deltaP `60.9103` edge `1.2005` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `4.7373` n `68` status `ready` deltaP `17.1359` edge `0.3569` maxDD `-3.4427`
- `market_context_high->commodity_24h` score `1.7361` n `53` status `ready` deltaP `27.4844` edge `0.2252` maxDD `-10.2019`
- `news_risk_high->index_4h` score `1.7089` n `68` status `ready` deltaP `16.5261` edge `0.0703` maxDD `-0.3783`
- `market_context_high->crypto_alt_4h` score `0.7321` n `53` status `ready` deltaP `9.805` edge `0.1242` maxDD `-5.323`
- `news_risk_high->equity_1h` score `0.6468` n `68` status `ready` deltaP `9.9419` edge `0.0699` maxDD `-2.916`
- `market_context_high->fx_4h` score `0.3055` n `53` status `ready` deltaP `15.2353` edge `0.0172` maxDD `-1.3685`
- `market_context_high->fx_24h` score `0.1837` n `53` status `ready` deltaP `11.046` edge `0.0479` maxDD `-2.506`
- `news_risk_high->metal_4h` score `0.1172` n `68` status `ready` deltaP `5.165` edge `0.0282` maxDD `-0.8085`
- `news_risk_high->fx_4h` score `0.0921` n `68` status `ready` deltaP `11.9889` edge `0.0235` maxDD `-0.6604`
- `news_risk_high->crypto_alt_1h` score `0.0554` n `68` status `ready` deltaP `6.0321` edge `0.0351` maxDD `-3.1233`
- `market_context_high->commodity_1h` score `0.0167` n `53` status `ready` deltaP `5.0757` edge `0.0224` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0102` n `53` status `ready` deltaP `7.502` edge `0.0011` maxDD `-0.6874`
- `news_risk_high->index_1h` score `-0.0684` n `68` status `ready` deltaP `2.4657` edge `0.0071` maxDD `-0.5845`
- `news_risk_high->fx_1h` score `-0.0949` n `68` status `ready` deltaP `2.3688` edge `0.0043` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1411` n `68` status `ready` deltaP `2.4657` edge `0.0058` maxDD `-0.5599`
- `market_context_high->commodity_4h` score `-0.1809` n `53` status `ready` deltaP `3.5722` edge `0.0405` maxDD `-3.0005`
- `news_risk_high->crypto_major_1h` score `-0.2677` n `68` status `ready` deltaP `1.6203` edge `0.0269` maxDD `-3.762`
- `news_risk_high->commodity_1h` score `-0.6163` n `68` status `ready` deltaP `3.7161` edge `-0.0258` maxDD `-2.9058`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
