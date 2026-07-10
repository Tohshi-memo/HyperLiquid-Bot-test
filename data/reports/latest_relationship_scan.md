# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T14:52:32.303079+00:00`
- Price records: `672`
- Market context records: `6293`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11116`

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

- `news_risk_high->crypto_alt_24h` score `15.225` n `32` status `ready` deltaP `43.2292` edge `0.9953` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `5.9677` n `32` status `ready` deltaP `50.5208` edge `0.1605` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1901` n `32` status `ready` deltaP `43.8262` edge `0.0616` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `4.1211` n `32` status `ready` deltaP `16.6667` edge `0.4952` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `2.942` n `32` status `ready` deltaP `27.2569` edge `0.084` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.4003` n `32` status `ready` deltaP `28.8922` edge `0.0213` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.4273` n `32` status `ready` deltaP `14.2777` edge `0.1345` maxDD `-2.0691`
- `market_context_high->unknown_1h` score `1.2749` n `208` status `ready` deltaP `-0.4865` edge `0.2103` maxDD `-3.7317`
- `news_risk_high->crypto_alt_1h` score `0.9205` n `32` status `ready` deltaP `11.7702` edge `0.0857` maxDD `-1.6923`
- `market_context_high->equity_4h` score `0.2538` n `196` status `ready` deltaP `6.9562` edge `0.0665` maxDD `-2.671`
- `market_context_high->unknown_4h` score `0.0313` n `196` status `ready` deltaP `-4.3741` edge `0.285` maxDD `-11.925`
- `market_context_high->metal_4h` score `-0.1719` n `196` status `ready` deltaP `7.2144` edge `0.0339` maxDD `-2.7056`
- `market_context_high->metal_24h` score `-0.1837` n `178` status `ready` deltaP `19.9789` edge `0.1001` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.3399` n `32` status `ready` deltaP `6.5972` edge `-0.0004` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.4318` n `208` status `ready` deltaP `3.256` edge `0.0007` maxDD `-1.8877`
- `market_context_high->commodity_1h` score `-0.4985` n `208` status `ready` deltaP `-0.0864` edge `-0.0001` maxDD `-1.7253`
- `market_context_high->fx_1h` score `-0.7082` n `208` status `ready` deltaP `-0.9155` edge `-0.0019` maxDD `-0.748`
- `news_risk_high->metal_1h` score `-0.734` n `32` status `ready` deltaP `-2.994` edge `-0.0244` maxDD `-1.6464`
- `market_context_high->commodity_4h` score `-0.8989` n `196` status `ready` deltaP `-3.4128` edge `0.0033` maxDD `-1.6629`
- `market_context_high->crypto_alt_1h` score `-0.9661` n `208` status `ready` deltaP `4.799` edge `0.0194` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
