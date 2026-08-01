# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T19:22:27.996543+00:00`
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

- `news_risk_high->unknown_24h` score `5189.6402` n `60` status `ready` deltaP `33.1947` edge `432.2908` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `17.3002` n `53` status `ready` deltaP `56.0577` edge `1.1077` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `5.9264` n `63` status `ready` deltaP `21.2495` edge `0.4119` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.3911` n `63` status `ready` deltaP `20.7922` edge `0.0797` maxDD `-0.191`
- `market_context_high->commodity_24h` score `1.915` n `53` status `ready` deltaP `28.8709` edge `0.2389` maxDD `-10.2019`
- `market_context_high->crypto_alt_4h` score `0.6536` n `53` status `ready` deltaP `9.1953` edge `0.1182` maxDD `-5.323`
- `news_risk_high->equity_1h` score `0.6361` n `68` status `ready` deltaP `8.894` edge `0.076` maxDD `-2.916`
- `news_risk_high->crypto_major_4h` score `0.3465` n `63` status `ready` deltaP `5.5822` edge `0.1345` maxDD `-7.5162`
- `market_context_high->fx_4h` score `0.2549` n `53` status `ready` deltaP `14.4731` edge `0.0158` maxDD `-1.3685`
- `news_risk_high->metal_4h` score `0.1918` n `63` status `ready` deltaP `5.8339` edge `0.0333` maxDD `-0.8085`
- `news_risk_high->crypto_alt_1h` score `0.1661` n `68` status `ready` deltaP `7.08` edge `0.0423` maxDD `-3.1233`
- `news_risk_high->fx_4h` score `0.1063` n `63` status `ready` deltaP `12.1371` edge `0.0237` maxDD `-0.6604`
- `market_context_high->fx_1h` score `-0.0029` n `53` status `ready` deltaP `7.3523` edge `0.001` maxDD `-0.6874`
- `news_risk_high->index_1h` score `-0.0839` n `68` status `ready` deltaP `2.0166` edge `0.0081` maxDD `-0.5845`
- `market_context_high->commodity_1h` score `-0.0963` n `53` status `ready` deltaP `3.8781` edge `0.0159` maxDD `-1.3282`
- `news_risk_high->fx_1h` score `-0.1035` n `68` status `ready` deltaP `2.2191` edge `0.0042` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1178` n `68` status `ready` deltaP `2.7651` edge `0.0068` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.143` n `68` status `ready` deltaP `2.6682` edge `0.0359` maxDD `-3.762`
- `market_context_high->fx_24h` score `-0.1526` n `53` status `ready` deltaP `5.6734` edge `0.0406` maxDD `-2.506`
- `news_risk_high->crypto_alt_4h` score `-0.2376` n `63` status `ready` deltaP `9.7344` edge `0.0813` maxDD `-8.7995`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
