# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T23:37:30.928863+00:00`
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

- `news_risk_high->unknown_24h` score `5188.6563` n `60` status `ready` deltaP `31.9815` edge `432.2169` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `18.0879` n `53` status `ready` deltaP `59.0039` edge `1.1537` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `4.8573` n `68` status `ready` deltaP `17.1359` edge `0.3669` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.7439` n `68` status `ready` deltaP `16.6786` edge `0.0722` maxDD `-0.3783`
- `market_context_high->commodity_24h` score `1.7361` n `53` status `ready` deltaP `27.4844` edge `0.2252` maxDD `-10.2019`
- `market_context_high->crypto_alt_4h` score `0.7633` n `53` status `ready` deltaP `9.805` edge `0.1282` maxDD `-5.323`
- `news_risk_high->equity_1h` score `0.7092` n `68` status `ready` deltaP `9.9419` edge `0.0751` maxDD `-2.916`
- `market_context_high->fx_4h` score `0.2145` n `53` status `ready` deltaP `13.7109` edge `0.0157` maxDD `-1.3685`
- `news_risk_high->metal_4h` score `0.1242` n `68` status `ready` deltaP `5.165` edge `0.0291` maxDD `-0.8085`
- `news_risk_high->crypto_alt_1h` score `0.0874` n `68` status `ready` deltaP `6.0321` edge `0.0392` maxDD `-3.1233`
- `market_context_high->fx_24h` score `0.0279` n `53` status `ready` deltaP `8.6197` edge `0.0441` maxDD `-2.506`
- `market_context_high->fx_1h` score `-0.0137` n `53` status `ready` deltaP `7.2026` edge `0.0011` maxDD `-0.6874`
- `news_risk_high->index_1h` score `-0.0287` n `68` status `ready` deltaP `3.0645` edge `0.0082` maxDD `-0.5845`
- `news_risk_high->fx_4h` score `-0.0479` n `68` status `ready` deltaP `10.4645` edge `0.022` maxDD `-0.6604`
- `market_context_high->commodity_1h` score `-0.0691` n `53` status `ready` deltaP `4.3272` edge `0.0164` maxDD `-1.3282`
- `news_risk_high->fx_1h` score `-0.1105` n `68` status `ready` deltaP `2.0694` edge `0.0043` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1442` n `68` status `ready` deltaP `2.316` edge `0.0064` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.2326` n `68` status `ready` deltaP `1.6203` edge `0.0314` maxDD `-3.762`
- `market_context_high->commodity_4h` score `-0.266` n `53` status `ready` deltaP `3.4198` edge `0.0306` maxDD `-3.0005`
- `market_context_high->crypto_alt_1h` score `-0.6238` n `53` status `ready` deltaP `-4.5673` edge `0.0132` maxDD `-3.0178`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
