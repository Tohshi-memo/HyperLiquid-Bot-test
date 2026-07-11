# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T23:22:24.787771+00:00`
- Price records: `672`
- Market context records: `6440`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5875`

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

- `news_risk_high->crypto_alt_24h` score `11.5801` n `32` status `ready` deltaP `29.5139` edge `0.783` maxDD `-0.5131`
- `market_context_high->unknown_24h` score `8.8632` n `145` status `ready` deltaP `21.1698` edge `0.9275` maxDD `-15.0689`
- `news_risk_high->fx_24h` score `6.3975` n `32` status `ready` deltaP `53.2986` edge `0.1778` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1096` n `32` status `ready` deltaP `42.7591` edge `0.062` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `4.0409` n `32` status `ready` deltaP `34.7222` edge `0.1258` maxDD `-0.3101`
- `news_risk_high->crypto_major_24h` score `3.2004` n `32` status `ready` deltaP `11.1111` edge `0.4142` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.4326` n `32` status `ready` deltaP `29.3413` edge `0.021` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.4757` n `32` status `ready` deltaP `13.6789` edge `0.1447` maxDD `-2.0691`
- `market_context_high->unknown_1h` score `1.473` n `188` status `ready` deltaP `-4.972` edge `0.246` maxDD `-3.2083`
- `news_risk_high->crypto_alt_1h` score `0.8607` n `32` status `ready` deltaP `9.8241` edge `0.091` maxDD `-1.6923`
- `market_context_high->index_4h` score `0.0313` n `188` status `ready` deltaP `7.1159` edge `0.0228` maxDD `-0.4108`
- `market_context_high->metal_4h` score `-0.2203` n `188` status `ready` deltaP `7.5247` edge `0.0403` maxDD `-2.7056`
- `news_risk_high->unknown_1h` score `-0.2801` n `32` status `ready` deltaP `6.5307` edge `-0.0324` maxDD `-0.7581`
- `news_risk_high->metal_1h` score `-0.5558` n `32` status `ready` deltaP `0.4491` edge `-0.0245` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.5723` n `188` status `ready` deltaP `0.4491` edge `0.0014` maxDD `-1.8877`
- `market_context_high->commodity_1h` score `-0.6165` n `188` status `ready` deltaP `-1.1148` edge `-0.0033` maxDD `-2.1314`
- `market_context_high->equity_4h` score `-0.62` n `188` status `ready` deltaP `6.6003` edge `0.0464` maxDD `-8.2573`
- `market_context_high->metal_24h` score `-0.6267` n `145` status `ready` deltaP `12.8256` edge `0.091` maxDD `-11.8809`
- `market_context_high->unknown_4h` score `-0.6696` n `188` status `ready` deltaP `-14.8093` edge `0.2835` maxDD `-10.5788`
- `news_risk_high->index_24h` score `-0.7052` n `32` status `ready` deltaP `1.0417` edge `-0.0102` maxDD `-2.3058`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
