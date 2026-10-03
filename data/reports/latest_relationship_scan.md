# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T22:52:33.328110+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4252`

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

- `market_context_high->unknown_1h` score `381.2047` n `50` status `ready` deltaP `12.8204` edge `31.6865` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `321.5888` n `50` status `ready` deltaP `12.8049` edge `26.7137` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `13.434` n `50` status `ready` deltaP `29.286` edge `1.0946` maxDD `-11.6271`
- `market_context_high->crypto_major_24h` score `11.3655` n `50` status `ready` deltaP `36.5927` edge `0.8448` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `10.7122` n `62` status `ready` deltaP `29.7842` edge `0.7426` maxDD `-2.8784`
- `news_risk_high->crypto_major_4h` score `10.4786` n `68` status `ready` deltaP `38.1815` edge `0.639` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.339` n `68` status `ready` deltaP `26.3092` edge `0.5706` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.0787` n `50` status `ready` deltaP `16.4756` edge `0.5504` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.6224` n `50` status `ready` deltaP `15.4268` edge `0.4946` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.533` n `62` status `ready` deltaP `32.9429` edge `0.174` maxDD `-0.2696`
- `news_risk_high->equity_4h` score `3.8303` n `68` status `ready` deltaP `26.9637` edge `0.2007` maxDD `-2.9013`
- `market_context_high->crypto_alt_1h` score `3.0816` n `50` status `ready` deltaP `13.3054` edge `0.2344` maxDD `-3.6376`
- `market_context_high->fx_4h` score `3.0346` n `50` status `ready` deltaP `34.061` edge `0.0393` maxDD `-0.0791`
- `news_risk_high->index_4h` score `2.9473` n `68` status `ready` deltaP `32.2364` edge `0.0569` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.8935` n `68` status `ready` deltaP `12.9095` edge `0.1906` maxDD `-1.5096`
- `market_context_high->crypto_major_1h` score `2.8287` n `50` status `ready` deltaP `12.2036` edge `0.1994` maxDD `-2.2692`
- `news_risk_high->metal_4h` score `2.399` n `68` status `ready` deltaP `20.4448` edge `0.1052` maxDD `-0.993`
- `news_risk_high->index_1h` score `1.9599` n `68` status `ready` deltaP `24.1987` edge `0.017` maxDD `-0.1997`
- `market_context_high->equity_24h` score `1.535` n `50` status `ready` deltaP `9.0745` edge `0.3225` maxDD `-11.8957`
- `market_context_high->fx_1h` score `1.5334` n `50` status `ready` deltaP `21.3892` edge `0.0116` maxDD `-0.113`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
