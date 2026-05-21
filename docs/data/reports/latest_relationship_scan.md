# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T22:52:17.289733+00:00`
- Price records: `672`
- Market context records: `1469`
- Flow alert records: `6137`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8809`

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

- `market_context_high->crypto_alt_24h` score `13.2023` n `169` status `ready` deltaP `28.9541` edge `1.1088` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `12.0813` n `169` status `ready` deltaP `27.6997` edge `0.9353` maxDD `-8.0553`
- `market_context_high->metal_24h` score `11.1138` n `169` status `ready` deltaP `15.2346` edge `0.9913` maxDD `-6.3373`
- `market_context_high->equity_24h` score `4.4013` n `169` status `ready` deltaP `13.4492` edge `0.5098` maxDD `-14.2815`
- `market_context_high->index_24h` score `4.263` n `169` status `ready` deltaP `20.1882` edge `0.3293` maxDD `-5.3574`
- `market_context_high->equity_4h` score `1.5794` n `221` status `ready` deltaP `7.3819` edge `0.1654` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.2811` n `169` status `ready` deltaP `12.2298` edge `0.0468` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.1304` n `221` status `ready` deltaP `1.9881` edge `0.0359` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.1382` n `221` status `ready` deltaP `3.179` edge `0.0138` maxDD `-1.7205`
- `market_context_high->crypto_alt_4h` score `-0.1544` n `221` status `ready` deltaP `11.6233` edge `0.2416` maxDD `-19.5565`
- `market_context_high->index_4h` score `-0.3898` n `221` status `ready` deltaP `1.5479` edge `0.0661` maxDD `-3.7119`
- `market_context_high->fx_1h` score `-0.494` n `221` status `ready` deltaP `0.3895` edge `-0.0027` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.5096` n `221` status `ready` deltaP `2.0701` edge `0.0461` maxDD `-4.1892`
- `market_context_high->crypto_major_4h` score `-1.0356` n `221` status `ready` deltaP `5.5934` edge `0.1473` maxDD `-13.3376`
- `market_context_high->fx_4h` score `-1.0459` n `221` status `ready` deltaP `-4.1607` edge `-0.0093` maxDD `-1.4313`
- `market_context_high->commodity_1h` score `-1.1944` n `221` status `ready` deltaP `-1.1244` edge `0.0001` maxDD `-4.7041`
- `market_context_high->metal_1h` score `-1.2334` n `221` status `ready` deltaP `4.6353` edge `-0.0001` maxDD `-6.3532`
- `market_context_high->crypto_major_1h` score `-1.5421` n `221` status `ready` deltaP `-0.3488` edge `0.0095` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.7927` n `221` status `ready` deltaP `7.904` edge `0.0671` maxDD `-12.5349`
- `market_context_high->commodity_4h` score `-4.0429` n `221` status `ready` deltaP `-11.5337` edge `-0.0698` maxDD `-17.3969`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
