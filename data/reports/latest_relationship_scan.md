# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T07:52:31.522446+00:00`
- Price records: `672`
- Market context records: `5641`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8684`

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

- `market_context_high->equity_24h` score `2.765` n `175` status `ready` deltaP `14.252` edge `0.6433` maxDD `-31.6316`
- `market_context_high->fx_24h` score `1.3118` n `175` status `ready` deltaP `21.5515` edge `0.0631` maxDD `-1.4633`
- `market_context_high->crypto_major_4h` score `0.6264` n `237` status `ready` deltaP `9.9374` edge `0.2152` maxDD `-14.0065`
- `market_context_high->equity_4h` score `0.4771` n `237` status `ready` deltaP `7.5338` edge `0.1534` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `-0.2562` n `237` status `ready` deltaP `5.1547` edge `0.1292` maxDD `-9.46`
- `market_context_high->fx_1h` score `-0.2719` n `237` status `ready` deltaP `1.749` edge `0.0011` maxDD `-0.4764`
- `market_context_high->equity_1h` score `-0.3475` n `237` status `ready` deltaP `5.6154` edge `0.0343` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.5488` n `237` status `ready` deltaP `-0.4561` edge `0.0002` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.595` n `237` status `ready` deltaP `1.5861` edge `0.036` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.6049` n `237` status `ready` deltaP `4.2807` edge `0.0456` maxDD `-6.9639`
- `market_context_high->index_1h` score `-0.9537` n `237` status `ready` deltaP `0.2792` edge `0.0055` maxDD `-0.9472`
- `market_context_high->commodity_1h` score `-1.0429` n `237` status `ready` deltaP `-0.7283` edge `-0.0055` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.3343` n `237` status `ready` deltaP `0.9133` edge `0.0062` maxDD `-1.335`
- `market_context_high->index_4h` score `-1.9843` n `237` status `ready` deltaP `-1.0792` edge `0.009` maxDD `-3.04`
- `market_context_high->index_24h` score `-2.2869` n `175` status `ready` deltaP `10.8889` edge `0.0329` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-3.0108` n `237` status `ready` deltaP `-13.9118` edge `-0.0549` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-3.8396` n `237` status `ready` deltaP `-2.4924` edge `-0.0358` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.4891` n `175` status `ready` deltaP `4.4147` edge `0.0505` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-8.2729` n `175` status `ready` deltaP `-11.1647` edge `-0.2501` maxDD `-32.8874`
- `market_context_high->commodity_24h` score `-13.2045` n `175` status `ready` deltaP `-17.4574` edge `-0.1231` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
