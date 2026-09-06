# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T05:37:28.790625+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10755`

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

- `news_risk_high->crypto_alt_24h` score `6.3759` n `33` status `ready` deltaP `27.8094` edge `0.3617` maxDD `-0.2615`
- `risk_on_high->unknown_4h` score `5.2953` n `145` status `ready` deltaP `-4.0748` edge `0.669` maxDD `-7.7112`
- `risk_on_and_context->unknown_4h` score `5.2953` n `145` status `ready` deltaP `-4.0748` edge `0.669` maxDD `-7.7112`
- `news_risk_high->crypto_major_4h` score `4.2125` n `33` status `ready` deltaP `21.1659` edge `0.2349` maxDD `-0.6635`
- `news_risk_high->commodity_24h` score `4.0183` n `33` status `ready` deltaP `20.1389` edge `0.2006` maxDD `0.0`
- `news_risk_high->metal_4h` score `2.4072` n `33` status `ready` deltaP `23.6419` edge `0.0651` maxDD `-0.7692`
- `news_risk_high->crypto_major_24h` score `2.3913` n `33` status `ready` deltaP `18.0556` edge `0.2508` maxDD `-11.0849`
- `news_risk_high->commodity_4h` score `2.0177` n `33` status `ready` deltaP `10.0749` edge `0.1169` maxDD `-0.2737`
- `risk_on_high->crypto_major_24h` score `1.8261` n `88` status `ready` deltaP `12.7525` edge `0.8817` maxDD `-47.9416`
- `risk_on_and_context->crypto_major_24h` score `1.8261` n `88` status `ready` deltaP `12.7525` edge `0.8817` maxDD `-47.9416`
- `news_risk_high->fx_24h` score `1.63` n `33` status `ready` deltaP `26.452` edge `0.0425` maxDD `-2.9744`
- `market_context_high->equity_24h` score `1.5076` n `171` status `ready` deltaP `13.4503` edge `0.3898` maxDD `-16.9737`
- `news_risk_high->index_1h` score `1.4341` n `33` status `ready` deltaP `17.0024` edge `0.0154` maxDD `-0.0724`
- `news_risk_high->equity_1h` score `1.4116` n `33` status `ready` deltaP `9.6308` edge `0.0925` maxDD `-0.7924`
- `news_risk_high->metal_1h` score `1.0509` n `33` status `ready` deltaP `12.1031` edge `0.0262` maxDD `-0.2118`
- `news_risk_high->crypto_major_1h` score `0.8613` n `33` status `ready` deltaP `3.6836` edge `0.0655` maxDD `-0.4628`
- `news_risk_high->crypto_alt_1h` score `0.2135` n `33` status `ready` deltaP `4.4684` edge `0.0145` maxDD `-0.7867`
- `news_risk_high->commodity_1h` score `0.0684` n `33` status `ready` deltaP `7.349` edge `0.0044` maxDD `-0.9036`
- `news_risk_high->crypto_alt_4h` score `-0.0849` n `33` status `ready` deltaP `1.7092` edge `0.0144` maxDD `-1.296`
- `risk_on_high->index_1h` score `-0.0998` n `145` status `ready` deltaP `5.2364` edge `-0.003` maxDD `-0.5764`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
