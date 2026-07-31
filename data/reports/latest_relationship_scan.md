# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T19:22:34.257683+00:00`
- Price records: `672`
- Market context records: `8543`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5925`

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

- `news_risk_high->unknown_24h` score `5564.6238` n `57` status `ready` deltaP `42.6353` edge `463.4765` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.5963` n `64` status `ready` deltaP `20.1982` edge `0.3914` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.9305` n `64` status `ready` deltaP `15.7393` edge `0.075` maxDD `-0.191`
- `market_context_high->crypto_alt_4h` score `1.7651` n `58` status `ready` deltaP `11.5643` edge `0.1657` maxDD `-5.323`
- `news_risk_high->equity_1h` score `1.5947` n `64` status `ready` deltaP `15.3537` edge `0.0782` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `0.9793` n `64` status `ready` deltaP `6.2881` edge `0.1612` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.6933` n `64` status `ready` deltaP `13.7195` edge `0.1366` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.4656` n `64` status `ready` deltaP `8.2616` edge `0.0573` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3477` n `64` status `ready` deltaP `6.7646` edge `0.0507` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.0768` n `64` status `ready` deltaP `5.1366` edge `0.0037` maxDD `-0.2475`
- `news_risk_high->index_1h` score `-0.0221` n `64` status `ready` deltaP `3.1718` edge `0.0077` maxDD `-0.5338`
- `news_risk_high->metal_4h` score `-0.0444` n `64` status `ready` deltaP `1.5625` edge `0.0315` maxDD `-0.8085`
- `news_risk_high->fx_4h` score `-0.0939` n `64` status `ready` deltaP `10.0991` edge `0.0206` maxDD `-0.6604`
- `news_risk_high->metal_1h` score `-0.2006` n `64` status `ready` deltaP `2.5075` edge `0.0069` maxDD `-0.5599`
- `market_context_high->fx_1h` score `-0.2879` n `62` status `ready` deltaP `2.062` edge `-0.0004` maxDD `-0.6874`
- `market_context_high->commodity_1h` score `-0.3013` n `62` status `ready` deltaP `4.0081` edge `-0.0028` maxDD `-2.0038`
- `market_context_high->fx_4h` score `-0.3891` n `58` status `ready` deltaP `3.3642` edge `0.0073` maxDD `-1.3685`
- `market_context_high->crypto_alt_1h` score `-0.5112` n `62` status `ready` deltaP `-2.7767` edge `0.0157` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.8172` n `62` status `ready` deltaP `0.198` edge `-0.0165` maxDD `-1.5667`
- `market_context_high->metal_4h` score `-1.0254` n `58` status `ready` deltaP `0.6466` edge `-0.0123` maxDD `-3.211`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
