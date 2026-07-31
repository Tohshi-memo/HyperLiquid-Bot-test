# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T02:52:24.901014+00:00`
- Price records: `672`
- Market context records: `8473`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5828`

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

- `news_risk_high->unknown_24h` score `6266.5145` n `52` status `ready` deltaP `44.0438` edge `521.958` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.2969` n `61` status `ready` deltaP `22.8958` edge `0.4318` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.2384` n `61` status `ready` deltaP `18.6275` edge `0.0814` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.8152` n `64` status `ready` deltaP `16.701` edge `0.0876` maxDD `-2.4803`
- `news_risk_high->crypto_alt_4h` score `1.2672` n `61` status `ready` deltaP `16.6409` edge `0.1907` maxDD `-5.8012`
- `news_risk_high->crypto_major_4h` score `1.2367` n `61` status `ready` deltaP `6.8447` edge `0.1823` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `0.5856` n `64` status `ready` deltaP `9.9083` edge `0.0617` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3212` n `64` status `ready` deltaP `6.9143` edge `0.0463` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.1259` n `64` status `ready` deltaP `6.0348` edge `0.004` maxDD `-0.2475`
- `news_risk_high->fx_4h` score `0.0572` n `61` status `ready` deltaP `11.6429` edge `0.0229` maxDD `-0.6604`
- `news_risk_high->index_1h` score `0.0395` n `64` status `ready` deltaP `4.2197` edge `0.0086` maxDD `-0.5338`
- `news_risk_high->metal_1h` score `-0.2701` n `64` status `ready` deltaP `1.9087` edge `0.0051` maxDD `-0.5599`
- `news_risk_high->metal_4h` score `-0.4774` n `61` status `ready` deltaP `-2.0742` edge `0.0213` maxDD `-0.7801`
- `news_risk_high->commodity_1h` score `-1.501` n `64` status `ready` deltaP `-2.3578` edge `-0.0308` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.5609` n `52` status `ready` deltaP `-27.7244` edge `-0.0464` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-7.4224` n `61` status `ready` deltaP `-18.5526` edge `-0.1641` maxDD `-13.1269`
- `news_risk_high->metal_24h` score `-9.2576` n `52` status `ready` deltaP `-36.6186` edge `-0.2503` maxDD `-10.8302`
- `news_risk_high->commodity_24h` score `-12.9138` n `52` status `ready` deltaP `-13.3013` edge `-0.3935` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-14.2816` n `52` status `ready` deltaP `-34.4952` edge `-0.4099` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-40.2935` n `52` status `ready` deltaP `-29.8344` edge `-1.7064` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
