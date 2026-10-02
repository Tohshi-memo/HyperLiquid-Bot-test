# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T05:52:32.879888+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4882`

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

- `market_context_high->unknown_1h` score `340.8084` n `50` status `ready` deltaP `9.5269` edge `28.3421` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `287.9311` n `50` status `ready` deltaP `8.9939` edge `23.9343` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `14.572` n `63` status `ready` deltaP `39.0129` edge `0.9752` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `11.0723` n `50` status `ready` deltaP `36.1667` edge `0.8232` maxDD `-9.3299`
- `market_context_high->crypto_alt_24h` score `8.3803` n `50` status `ready` deltaP `16.1875` edge `0.7614` maxDD `-11.6768`
- `news_risk_high->equity_24h` score `8.1984` n `63` status `ready` deltaP `32.9365` edge `0.5246` maxDD `-2.8784`
- `market_context_high->crypto_major_4h` score `6.8341` n `50` status `ready` deltaP `17.5427` edge `0.5229` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.7717` n `50` status `ready` deltaP `15.5793` edge `0.4231` maxDD `-7.6792`
- `news_risk_high->crypto_alt_4h` score `3.519` n `87` status `ready` deltaP `13.3954` edge `0.3383` maxDD `-6.4152`
- `market_context_high->equity_24h` score `3.1776` n `50` status `ready` deltaP `15.2222` edge `0.4921` maxDD `-11.8957`
- `market_context_high->fx_4h` score `2.9045` n `50` status `ready` deltaP `32.689` edge `0.0376` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `2.7889` n `50` status `ready` deltaP `13.5509` edge `0.1871` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `2.7814` n `50` status `ready` deltaP `13.3054` edge `0.2094` maxDD `-3.6387`
- `news_risk_high->equity_4h` score `1.9373` n `87` status `ready` deltaP `21.2766` edge `0.0892` maxDD `-2.9013`
- `market_context_high->fx_1h` score `1.4484` n `50` status `ready` deltaP `20.3413` edge `0.0115` maxDD `-0.113`
- `news_risk_high->commodity_24h` score `1.1209` n `63` status `ready` deltaP `19.8909` edge `0.1235` maxDD `-3.9922`
- `market_context_high->index_24h` score `0.9762` n `50` status `ready` deltaP `15.4861` edge `0.079` maxDD `-1.2338`
- `news_risk_high->crypto_alt_1h` score `0.8379` n `99` status `ready` deltaP `5.8913` edge `0.0868` maxDD `-2.4998`
- `news_risk_high->metal_24h` score `0.5376` n `63` status `ready` deltaP `2.7033` edge `0.1783` maxDD `-2.192`
- `market_context_high->fx_24h` score `0.4899` n `50` status `ready` deltaP `14.4306` edge `0.0684` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
