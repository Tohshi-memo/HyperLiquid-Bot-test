# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T17:37:30.092742+00:00`
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

- `news_risk_high->unknown_24h` score `5190.3299` n `60` status `ready` deltaP `34.0612` edge `432.3425` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `16.9584` n `53` status `ready` deltaP `54.8445` edge `1.0873` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `6.521` n `60` status `ready` deltaP `23.9126` edge `0.4437` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.6654` n `60` status `ready` deltaP `23.4553` edge `0.0848` maxDD `-0.191`
- `market_context_high->commodity_24h` score `2.0678` n `53` status `ready` deltaP `30.084` edge `0.2504` maxDD `-10.2019`
- `news_risk_high->crypto_major_4h` score `1.3471` n `60` status `ready` deltaP `8.2012` edge `0.1956` maxDD `-3.5385`
- `news_risk_high->equity_1h` score `0.6937` n `67` status `ready` deltaP `8.7899` edge `0.0764` maxDD `-2.842`
- `news_risk_high->crypto_alt_4h` score `0.579` n `60` status `ready` deltaP `12.2866` edge `0.1315` maxDD `-5.8012`
- `market_context_high->crypto_alt_4h` score `0.5644` n `53` status `ready` deltaP `8.8904` edge `0.1088` maxDD `-5.323`
- `news_risk_high->crypto_alt_1h` score `0.2807` n `67` status `ready` deltaP `7.7643` edge `0.0454` maxDD `-2.5604`
- `news_risk_high->fx_4h` score `0.2523` n `60` status `ready` deltaP `13.8415` edge `0.0245` maxDD `-0.6604`
- `market_context_high->fx_4h` score `0.205` n `53` status `ready` deltaP `13.5585` edge `0.0155` maxDD `-1.3685`
- `news_risk_high->metal_4h` score `0.1622` n `60` status `ready` deltaP `4.9796` edge `0.0352` maxDD `-0.8085`
- `market_context_high->fx_1h` score `-0.0161` n `53` status `ready` deltaP `7.2026` edge `0.0009` maxDD `-0.6874`
- `news_risk_high->crypto_major_1h` score `-0.0452` n `67` status `ready` deltaP `2.9873` edge `0.039` maxDD `-3.1769`
- `news_risk_high->index_1h` score `-0.0621` n `67` status `ready` deltaP `2.3796` edge `0.0083` maxDD `-0.5702`
- `news_risk_high->fx_1h` score `-0.0705` n `67` status `ready` deltaP `2.8376` edge `0.0043` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1036` n `67` status `ready` deltaP `2.9784` edge `0.0072` maxDD `-0.5599`
- `market_context_high->commodity_1h` score `-0.1057` n `53` status `ready` deltaP `3.7284` edge `0.0157` maxDD `-1.3282`
- `market_context_high->commodity_4h` score `-0.2217` n `53` status `ready` deltaP `4.182` edge `0.0312` maxDD `-3.0005`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
