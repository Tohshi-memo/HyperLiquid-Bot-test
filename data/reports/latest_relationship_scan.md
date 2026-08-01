# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T19:07:28.943457+00:00`
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

- `news_risk_high->unknown_24h` score `5189.7417` n `60` status `ready` deltaP `33.368` edge `432.2981` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `17.2492` n `53` status `ready` deltaP `55.8843` edge `1.1046` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `6.1352` n `62` status `ready` deltaP `22.3004` edge `0.4223` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.4956` n `62` status `ready` deltaP `21.8431` edge `0.0814` maxDD `-0.191`
- `market_context_high->commodity_24h` score `1.9365` n `53` status `ready` deltaP `29.0442` edge `0.2405` maxDD `-10.2019`
- `news_risk_high->crypto_major_4h` score `0.6633` n `62` status `ready` deltaP `6.427` edge `0.154` maxDD `-6.2784`
- `market_context_high->crypto_alt_4h` score `0.6317` n `53` status `ready` deltaP `9.0428` edge `0.1164` maxDD `-5.323`
- `news_risk_high->equity_1h` score `0.6217` n `68` status `ready` deltaP `8.7443` edge `0.0758` maxDD `-2.916`
- `market_context_high->fx_4h` score `0.2462` n `53` status `ready` deltaP `14.3207` edge `0.0157` maxDD `-1.3685`
- `news_risk_high->metal_4h` score `0.1698` n `62` status `ready` deltaP `5.3206` edge `0.0339` maxDD `-0.8085`
- `news_risk_high->fx_4h` score `0.1653` n `62` status `ready` deltaP `12.8295` edge `0.024` maxDD `-0.6604`
- `news_risk_high->crypto_alt_1h` score `0.1598` n `68` status `ready` deltaP `7.08` edge `0.0415` maxDD `-3.1233`
- `news_risk_high->crypto_alt_4h` score `0.0357` n `62` status `ready` deltaP `10.5035` edge `0.0972` maxDD `-7.6787`
- `market_context_high->fx_1h` score `-0.0029` n `53` status `ready` deltaP `7.3523` edge `0.001` maxDD `-0.6874`
- `market_context_high->commodity_1h` score `-0.0862` n `53` status `ready` deltaP `4.0278` edge `0.0162` maxDD `-1.3282`
- `news_risk_high->index_1h` score `-0.0917` n `68` status `ready` deltaP `1.8669` edge `0.0081` maxDD `-0.5845`
- `news_risk_high->fx_1h` score `-0.1035` n `68` status `ready` deltaP `2.2191` edge `0.0042` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1092` n `68` status `ready` deltaP `2.9148` edge `0.0069` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.1469` n `68` status `ready` deltaP `2.6682` edge `0.0354` maxDD `-3.762`
- `market_context_high->fx_24h` score `-0.1648` n `53` status `ready` deltaP `5.5001` edge `0.0402` maxDD `-2.506`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
