# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T02:07:31.663477+00:00`
- Price records: `672`
- Market context records: `8575`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5919`

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

- `news_risk_high->unknown_24h` score `4751.4458` n `64` status `ready` deltaP `38.7153` edge `395.7378` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.9778` n `64` status `ready` deltaP `22.0274` edge `0.411` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.1774` n `64` status `ready` deltaP `18.3308` edge `0.0783` maxDD `-0.191`
- `market_context_high->crypto_alt_4h` score `1.9186` n `62` status `ready` deltaP `13.513` edge `0.1655` maxDD `-5.323`
- `news_risk_high->equity_1h` score `1.7625` n `64` status `ready` deltaP `16.5513` edge `0.0842` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `1.1296` n `64` status `ready` deltaP `7.8125` edge `0.1703` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.6561` n `64` status `ready` deltaP `13.1098` edge `0.1359` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.4282` n `64` status `ready` deltaP `7.9622` edge `0.0545` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3649` n `64` status `ready` deltaP `7.064` edge `0.0509` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.0986` n `64` status `ready` deltaP `5.436` edge `0.0045` maxDD `-0.2475`
- `news_risk_high->fx_4h` score `0.0594` n `64` status `ready` deltaP `11.7759` edge `0.0222` maxDD `-0.6604`
- `news_risk_high->index_1h` score `0.0083` n `64` status `ready` deltaP `3.6209` edge `0.0086` maxDD `-0.5338`
- `news_risk_high->metal_4h` score `-0.0349` n `64` status `ready` deltaP `1.7149` edge `0.0317` maxDD `-0.8085`
- `market_context_high->fx_4h` score `-0.1088` n `62` status `ready` deltaP `8.6005` edge `0.0132` maxDD `-1.3685`
- `news_risk_high->metal_1h` score `-0.1215` n `64` status `ready` deltaP `3.4057` edge `0.0075` maxDD `-0.5599`
- `market_context_high->fx_1h` score `-0.2661` n `62` status `ready` deltaP `2.3614` edge `0.0004` maxDD `-0.6874`
- `market_context_high->commodity_1h` score `-0.3107` n `62` status `ready` deltaP `4.1578` edge `-0.005` maxDD `-2.0038`
- `market_context_high->crypto_alt_1h` score `-0.5486` n `62` status `ready` deltaP `-3.0761` edge `0.0129` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.7704` n `62` status `ready` deltaP `0.6471` edge `-0.0156` maxDD `-1.5667`
- `market_context_high->metal_1h` score `-0.9625` n `62` status `ready` deltaP `-2.8443` edge `-0.0118` maxDD `-1.6224`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
