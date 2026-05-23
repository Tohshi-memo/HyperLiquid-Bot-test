# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T06:52:18.342098+00:00`
- Price records: `672`
- Market context records: `1605`
- Flow alert records: `6534`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8814`

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

- `market_context_high->metal_24h` score `13.858` n `184` status `ready` deltaP `30.4121` edge `1.0563` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `12.5095` n `184` status `ready` deltaP `26.7738` edge `1.0656` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.2478` n `184` status `ready` deltaP `26.57` edge `0.8243` maxDD `-10.1291`
- `market_context_high->equity_24h` score `5.1908` n `184` status `ready` deltaP `21.0523` edge `0.5249` maxDD `-14.2815`
- `market_context_high->index_24h` score `4.2093` n `184` status `ready` deltaP `22.5317` edge `0.3092` maxDD `-5.3574`
- `market_context_high->equity_4h` score `1.2269` n `198` status `ready` deltaP `10.5892` edge `0.1411` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `0.1637` n `198` status `ready` deltaP `12.9219` edge `0.2668` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `0.0574` n `198` status `ready` deltaP `9.0817` edge `0.2177` maxDD `-13.3376`
- `market_context_high->fx_24h` score `-0.1815` n `184` status `ready` deltaP `7.8125` edge `0.0377` maxDD `-1.3925`
- `market_context_high->crypto_alt_1h` score `-0.3567` n `198` status `ready` deltaP `0.6351` edge `0.0524` maxDD `-4.1892`
- `market_context_high->equity_1h` score `-0.5596` n `198` status `ready` deltaP `0.7077` edge `0.0295` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.5892` n `198` status `ready` deltaP `-1.2913` edge `-0.0037` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.6832` n `198` status `ready` deltaP `0.4265` edge `0.0034` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.7524` n `198` status `ready` deltaP `4.7874` edge `0.0052` maxDD `-6.3532`
- `market_context_high->commodity_1h` score `-0.7755` n `198` status `ready` deltaP `-1.0479` edge `-0.0003` maxDD `-4.7041`
- `market_context_high->crypto_major_1h` score `-0.9001` n `198` status `ready` deltaP `-0.8422` edge `0.0259` maxDD `-6.1883`
- `market_context_high->index_4h` score `-0.94` n `198` status `ready` deltaP `-0.0646` edge `0.031` maxDD `-3.7119`
- `market_context_high->metal_4h` score `-1.3952` n `198` status `ready` deltaP `9.2433` edge `0.0913` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-1.4167` n `198` status `ready` deltaP `-11.0911` edge `-0.0148` maxDD `-1.4313`
- `market_context_high->commodity_4h` score `-5.2008` n `198` status `ready` deltaP `-14.2754` edge `-0.1089` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
