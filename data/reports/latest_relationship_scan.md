# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T06:07:38.971118+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4874`

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

- `market_context_high->unknown_1h` score `340.824` n `50` status `ready` deltaP `9.5269` edge `28.3434` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `287.9021` n `50` status `ready` deltaP `8.8415` edge `23.9329` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `14.2271` n `62` status `ready` deltaP `38.9617` edge `0.9468` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `11.0699` n `50` status `ready` deltaP `36.1667` edge `0.823` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `8.503` n `62` status `ready` deltaP `34.319` edge `0.5366` maxDD `-2.8784`
- `market_context_high->crypto_alt_24h` score `8.4403` n `50` status `ready` deltaP `16.1875` edge `0.7664` maxDD `-11.6768`
- `market_context_high->crypto_major_4h` score `6.8257` n `50` status `ready` deltaP `17.5427` edge `0.5222` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.7777` n `50` status `ready` deltaP `15.5793` edge `0.4236` maxDD `-7.6792`
- `news_risk_high->crypto_alt_4h` score `3.483` n `87` status `ready` deltaP `13.3954` edge `0.3353` maxDD `-6.4152`
- `market_context_high->equity_24h` score `3.1698` n `50` status `ready` deltaP `15.2222` edge `0.4911` maxDD `-11.8957`
- `market_context_high->fx_4h` score `2.9057` n `50` status `ready` deltaP `32.689` edge `0.0377` maxDD `-0.0791`
- `market_context_high->crypto_alt_1h` score `2.7982` n `50` status `ready` deltaP `13.4551` edge `0.2098` maxDD `-3.6387`
- `market_context_high->crypto_major_1h` score `2.7913` n `50` status `ready` deltaP `13.5509` edge `0.1873` maxDD `-2.2692`
- `news_risk_high->equity_4h` score `1.9361` n `87` status `ready` deltaP `21.2766` edge `0.0891` maxDD `-2.9013`
- `market_context_high->fx_1h` score `1.4496` n `50` status `ready` deltaP `20.3413` edge `0.0116` maxDD `-0.113`
- `news_risk_high->commodity_24h` score `1.0694` n `62` status `ready` deltaP `19.2764` edge `0.121` maxDD `-3.9922`
- `market_context_high->index_24h` score `0.9868` n `50` status `ready` deltaP `15.6597` edge `0.0792` maxDD `-1.2338`
- `news_risk_high->crypto_alt_1h` score `0.7391` n `99` status `ready` deltaP `5.0309` edge `0.0843` maxDD `-2.4998`
- `market_context_high->fx_24h` score `0.4923` n `50` status `ready` deltaP `14.4306` edge `0.0687` maxDD `-1.8102`
- `news_risk_high->fx_24h` score `0.4609` n `62` status `ready` deltaP `13.7209` edge `0.022` maxDD `-0.3507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
