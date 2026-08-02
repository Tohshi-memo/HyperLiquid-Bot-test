# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-02T02:52:36.857259+00:00`
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

- `news_risk_high->unknown_24h` score `5188.8202` n `60` status `ready` deltaP `33.7146` edge `432.219` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `18.7708` n `53` status `ready` deltaP `60.9103` edge `1.1979` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `4.7553` n `68` status `ready` deltaP `17.1359` edge `0.3584` maxDD `-3.4427`
- `market_context_high->commodity_24h` score `1.7259` n `53` status `ready` deltaP `27.4844` edge `0.2239` maxDD `-10.2019`
- `news_risk_high->index_4h` score `1.7125` n `68` status `ready` deltaP `16.5261` edge `0.0706` maxDD `-0.3783`
- `market_context_high->crypto_alt_4h` score `0.7399` n `53` status `ready` deltaP `9.805` edge `0.1252` maxDD `-5.323`
- `news_risk_high->equity_1h` score `0.6552` n `68` status `ready` deltaP `9.9419` edge `0.0706` maxDD `-2.916`
- `market_context_high->fx_4h` score `0.2968` n `53` status `ready` deltaP `15.0829` edge `0.0171` maxDD `-1.3685`
- `market_context_high->fx_24h` score `0.1715` n `53` status `ready` deltaP `10.8727` edge `0.0475` maxDD `-2.506`
- `news_risk_high->metal_4h` score `0.1188` n `68` status `ready` deltaP `5.165` edge `0.0284` maxDD `-0.8085`
- `news_risk_high->fx_4h` score `0.0787` n `68` status `ready` deltaP `11.8365` edge `0.0234` maxDD `-0.6604`
- `news_risk_high->crypto_alt_1h` score `0.0523` n `68` status `ready` deltaP `6.0321` edge `0.0347` maxDD `-3.1233`
- `market_context_high->commodity_1h` score `0.0104` n `53` status `ready` deltaP `5.0757` edge `0.0216` maxDD `-1.3282`
- `market_context_high->fx_1h` score `-0.0029` n `53` status `ready` deltaP `7.3523` edge `0.001` maxDD `-0.6874`
- `news_risk_high->index_1h` score `-0.0668` n `68` status `ready` deltaP `2.4657` edge `0.0073` maxDD `-0.5845`
- `news_risk_high->fx_1h` score `-0.1035` n `68` status `ready` deltaP `2.2191` edge `0.0042` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1396` n `68` status `ready` deltaP `2.4657` edge `0.006` maxDD `-0.5599`
- `market_context_high->commodity_4h` score `-0.1949` n `53` status `ready` deltaP `3.5722` edge `0.0387` maxDD `-3.0005`
- `news_risk_high->crypto_major_1h` score `-0.2677` n `68` status `ready` deltaP `1.6203` edge `0.0269` maxDD `-3.762`
- `news_risk_high->commodity_1h` score `-0.6226` n `68` status `ready` deltaP `3.7161` edge `-0.0266` maxDD `-2.9058`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
