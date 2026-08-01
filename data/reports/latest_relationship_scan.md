# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T18:37:30.099415+00:00`
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

- `news_risk_high->unknown_24h` score `5189.9482` n `60` status `ready` deltaP `33.7146` edge `432.313` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `17.1446` n `53` status `ready` deltaP `55.5377` edge `1.0982` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `6.595` n `60` status `ready` deltaP `24.5223` edge `0.4458` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.719` n `60` status `ready` deltaP `24.065` edge `0.0852` maxDD `-0.191`
- `market_context_high->commodity_24h` score `1.9803` n `53` status `ready` deltaP `29.3908` edge `0.2438` maxDD `-10.2019`
- `news_risk_high->crypto_major_4h` score `1.3737` n `60` status `ready` deltaP `8.2012` edge `0.199` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.6173` n `60` status `ready` deltaP `12.439` edge `0.1354` maxDD `-5.8012`
- `market_context_high->crypto_alt_4h` score `0.6028` n `53` status `ready` deltaP `9.0428` edge `0.1127` maxDD `-5.323`
- `news_risk_high->equity_1h` score `0.5918` n `68` status `ready` deltaP `8.4449` edge `0.0753` maxDD `-2.916`
- `news_risk_high->fx_4h` score `0.2912` n `60` status `ready` deltaP `14.2988` edge `0.0247` maxDD `-0.6604`
- `market_context_high->fx_4h` score `0.2304` n `53` status `ready` deltaP `14.0158` edge `0.0157` maxDD `-1.3685`
- `news_risk_high->metal_4h` score `0.1947` n `60` status `ready` deltaP `5.5894` edge `0.0353` maxDD `-0.8085`
- `news_risk_high->crypto_alt_1h` score `0.1458` n `68` status `ready` deltaP `7.08` edge `0.0397` maxDD `-3.1233`
- `market_context_high->fx_1h` score `-0.0041` n `53` status `ready` deltaP `7.3523` edge `0.0009` maxDD `-0.6874`
- `news_risk_high->index_1h` score `-0.0917` n `68` status `ready` deltaP `1.8669` edge `0.0081` maxDD `-0.5845`
- `market_context_high->commodity_1h` score `-0.094` n `53` status `ready` deltaP `3.8781` edge `0.0162` maxDD `-1.3282`
- `news_risk_high->fx_1h` score `-0.1043` n `68` status `ready` deltaP `2.2191` edge `0.0041` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.117` n `68` status `ready` deltaP `2.7651` edge `0.0069` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.1625` n `68` status `ready` deltaP `2.6682` edge `0.0334` maxDD `-3.762`
- `market_context_high->fx_24h` score `-0.1883` n `53` status `ready` deltaP `5.1535` edge `0.0395` maxDD `-2.506`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
