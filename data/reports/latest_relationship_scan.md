# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-02T00:07:35.280601+00:00`
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

- `news_risk_high->unknown_24h` score `5188.6913` n `60` status `ready` deltaP `32.3281` edge `432.2175` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `18.2105` n `53` status `ready` deltaP `59.3505` edge `1.1616` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `4.8525` n `68` status `ready` deltaP `17.1359` edge `0.3665` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.7427` n `68` status `ready` deltaP `16.6786` edge `0.0721` maxDD `-0.3783`
- `market_context_high->commodity_24h` score `1.7306` n `53` status `ready` deltaP `27.4844` edge `0.2245` maxDD `-10.2019`
- `market_context_high->crypto_alt_4h` score `0.7688` n `53` status `ready` deltaP `9.805` edge `0.1289` maxDD `-5.323`
- `news_risk_high->equity_1h` score `0.7211` n `68` status `ready` deltaP `10.0916` edge `0.0751` maxDD `-2.916`
- `market_context_high->fx_4h` score `0.2311` n `53` status `ready` deltaP `14.0158` edge `0.0158` maxDD `-1.3685`
- `news_risk_high->metal_4h` score `0.1242` n `68` status `ready` deltaP `5.165` edge `0.0291` maxDD `-0.8085`
- `news_risk_high->crypto_alt_1h` score `0.096` n `68` status `ready` deltaP `6.1818` edge `0.0393` maxDD `-3.1233`
- `market_context_high->fx_24h` score `0.0498` n `53` status `ready` deltaP `8.9663` edge `0.0446` maxDD `-2.506`
- `market_context_high->fx_1h` score `0.0007` n `53` status `ready` deltaP `7.3523` edge `0.0013` maxDD `-0.6874`
- `news_risk_high->fx_4h` score `-0.0223` n `68` status `ready` deltaP `10.7694` edge `0.0221` maxDD `-0.6604`
- `news_risk_high->index_1h` score `-0.0287` n `68` status `ready` deltaP `3.0645` edge `0.0082` maxDD `-0.5845`
- `market_context_high->commodity_1h` score `-0.0512` n `53` status `ready` deltaP `4.6266` edge `0.0167` maxDD `-1.3282`
- `news_risk_high->fx_1h` score `-0.1011` n `68` status `ready` deltaP `2.2191` edge `0.0045` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1287` n `68` status `ready` deltaP `2.6154` edge `0.0064` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.2225` n `68` status `ready` deltaP `1.77` edge `0.0317` maxDD `-3.762`
- `market_context_high->commodity_4h` score `-0.259` n `53` status `ready` deltaP `3.4198` edge `0.0315` maxDD `-3.0005`
- `market_context_high->crypto_alt_1h` score `-0.6152` n `53` status `ready` deltaP `-4.4176` edge `0.0133` maxDD `-3.0178`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
