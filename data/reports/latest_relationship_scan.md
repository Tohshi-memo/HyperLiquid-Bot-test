# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T19:22:25.497972+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4143`

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

- `news_risk_high->equity_4h` score `2.1929` n `93` status `ready` deltaP `16.2012` edge `0.2637` maxDD `-4.2454`
- `news_risk_high->index_4h` score `0.9902` n `93` status `ready` deltaP `15.5996` edge `0.0263` maxDD `-0.4888`
- `news_risk_high->equity_1h` score `0.7358` n `93` status `ready` deltaP `7.0166` edge `0.1025` maxDD `-1.396`
- `news_risk_high->index_1h` score `0.3917` n `93` status `ready` deltaP `12.937` edge `0.0093` maxDD `-0.2931`
- `news_risk_high->crypto_major_4h` score `-0.1969` n `93` status `ready` deltaP `3.5946` edge `0.1194` maxDD `-9.1553`
- `news_risk_high->metal_1h` score `-0.2246` n `93` status `ready` deltaP `1.3409` edge `-0.002` maxDD `-0.5256`
- `news_risk_high->equity_24h` score `-0.2816` n `93` status `ready` deltaP `28.2663` edge `0.9341` maxDD `-86.0244`
- `news_risk_high->crypto_alt_1h` score `-0.3298` n `93` status `ready` deltaP `4.4846` edge `0.0506` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.3838` n `93` status `ready` deltaP `-1.3537` edge `-0.0002` maxDD `-0.1984`
- `news_risk_high->index_24h` score `-0.3952` n `93` status `ready` deltaP `1.0418` edge `0.1436` maxDD `-6.6786`
- `news_risk_high->fx_4h` score `-0.4423` n `93` status `ready` deltaP `0.595` edge `-0.0018` maxDD `-0.376`
- `news_risk_high->crypto_major_1h` score `-0.5556` n `93` status `ready` deltaP `-0.5924` edge `0.0266` maxDD `-4.1772`
- `news_risk_high->crypto_alt_4h` score `-0.8348` n `93` status `ready` deltaP `-0.0722` edge `0.1571` maxDD `-14.0916`
- `news_risk_high->metal_4h` score `-0.8878` n `93` status `ready` deltaP `0.7392` edge `-0.0282` maxDD `-1.5773`
- `news_risk_high->fx_24h` score `-1.2633` n `93` status `ready` deltaP `-10.2159` edge `0.0163` maxDD `-0.2778`
- `news_risk_high->metal_24h` score `-2.8683` n `93` status `ready` deltaP `4.452` edge `-0.2078` maxDD `-8.5019`
- `news_risk_high->commodity_1h` score `-3.2761` n `93` status `ready` deltaP `-19.1166` edge `-0.0143` maxDD `-2.8344`
- `news_risk_high->commodity_4h` score `-4.4634` n `93` status `ready` deltaP `-26.826` edge `-0.0095` maxDD `-6.022`
- `news_risk_high->crypto_major_24h` score `-6.3819` n `93` status `ready` deltaP `-16.1663` edge `0.1399` maxDD `-50.6925`
- `news_risk_high->commodity_24h` score `-9.4533` n `93` status `ready` deltaP `-25.2287` edge `-0.0128` maxDD `-31.2095`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
