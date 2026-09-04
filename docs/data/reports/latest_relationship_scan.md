# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T15:37:26.795731+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10784`

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

- `risk_on_high->unknown_4h` score `20.3812` n `133` status `ready` deltaP `7.779` edge `1.7084` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `20.3812` n `133` status `ready` deltaP `7.779` edge `1.7084` maxDD `-2.2797`
- `risk_on_high->unknown_1h` score `11.4837` n `133` status `ready` deltaP `-1.353` edge `1.0237` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `11.4837` n `133` status `ready` deltaP `-1.353` edge `1.0237` maxDD `-1.95`
- `market_context_high->unknown_4h` score `9.4703` n `207` status `ready` deltaP `9.0794` edge `0.7982` maxDD `-2.563`
- `market_context_high->unknown_1h` score `9.3082` n `212` status `ready` deltaP `-0.7288` edge `0.8436` maxDD `-2.0446`
- `news_risk_high->crypto_alt_24h` score `2.05` n `56` status `ready` deltaP `18.254` edge `0.0761` maxDD `-0.8236`
- `news_risk_high->commodity_4h` score `1.6165` n `56` status `ready` deltaP `13.3493` edge `0.0658` maxDD `-0.2737`
- `news_risk_high->commodity_24h` score `1.1612` n `56` status `ready` deltaP `10.2679` edge `0.0456` maxDD `-0.0495`
- `news_risk_high->index_1h` score `0.3686` n `56` status `ready` deltaP `8.7682` edge `0.0047` maxDD `-0.2715`
- `news_risk_high->equity_1h` score `0.3079` n `56` status `ready` deltaP `6.9504` edge `0.0376` maxDD `-1.2241`
- `risk_on_high->metal_1h` score `0.1109` n `133` status `ready` deltaP `12.4128` edge `0.0027` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.1109` n `133` status `ready` deltaP `12.4128` edge `0.0027` maxDD `-1.699`
- `news_risk_high->commodity_1h` score `0.072` n `56` status `ready` deltaP `7.2498` edge `0.0023` maxDD `-0.9036`
- `market_context_high->equity_24h` score `0.0149` n `167` status `ready` deltaP `12.8108` edge `0.3504` maxDD `-20.7654`
- `risk_on_high->index_1h` score `-0.177` n `133` status `ready` deltaP `3.693` edge `-0.0028` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.177` n `133` status `ready` deltaP `3.693` edge `-0.0028` maxDD `-0.5605`
- `news_risk_high->fx_4h` score `-0.2284` n `56` status `ready` deltaP `4.5514` edge `-0.0013` maxDD `-1.1796`
- `news_risk_high->equity_24h` score `-0.2642` n `56` status `ready` deltaP `2.2569` edge `0.0644` maxDD `-5.0655`
- `news_risk_high->metal_1h` score `-0.2743` n `56` status `ready` deltaP `2.0744` edge `-0.0067` maxDD `-1.3833`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
