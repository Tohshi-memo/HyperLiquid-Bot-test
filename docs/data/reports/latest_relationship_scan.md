# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T10:37:29.734264+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8522`

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

- `news_risk_high->crypto_major_24h` score `54.5179` n `72` status `ready` deltaP `34.0277` edge `4.4055` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `47.7856` n `72` status `ready` deltaP `38.5417` edge `3.8631` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `36.9517` n `144` status `ready` deltaP `-2.185` edge `3.1172` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `11.1441` n `72` status `ready` deltaP `43.5764` edge `0.6424` maxDD `-0.0053`
- `risk_on_high->commodity_24h` score `8.2304` n `52` status `ready` deltaP `44.9653` edge `0.3861` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.2304` n `52` status `ready` deltaP `44.9653` edge `0.3861` maxDD `0.0`
- `risk_on_high->unknown_4h` score `8.1991` n `52` status `ready` deltaP `-9.076` edge `0.7663` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `8.1991` n `52` status `ready` deltaP `-9.076` edge `0.7663` maxDD `-0.4694`
- `market_context_high->commodity_24h` score `7.0122` n `144` status `ready` deltaP `38.0209` edge `0.3834` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `6.6377` n `81` status `ready` deltaP `23.0974` edge `0.5201` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.6947` n `81` status `ready` deltaP `20.4456` edge `0.3807` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `3.4052` n `87` status `ready` deltaP `18.8743` edge `0.2045` maxDD `-2.058`
- `risk_on_high->commodity_4h` score `2.7135` n `52` status `ready` deltaP `32.235` edge `0.0462` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.7135` n `52` status `ready` deltaP `32.235` edge `0.0462` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.5614` n `144` status `ready` deltaP `28.0149` edge `0.0685` maxDD `-0.345`
- `news_risk_high->crypto_major_1h` score `2.3291` n `87` status `ready` deltaP `18.6713` edge `0.1219` maxDD `-2.8494`
- `news_risk_high->metal_24h` score `1.9017` n `72` status `ready` deltaP `24.4792` edge `0.0797` maxDD `-2.4203`
- `news_risk_high->fx_4h` score `1.2071` n `81` status `ready` deltaP `13.5407` edge `0.0322` maxDD `-0.084`
- `market_context_high->commodity_1h` score `1.104` n `144` status `ready` deltaP `16.1095` edge `0.0223` maxDD `-0.3491`
- `news_risk_high->equity_1h` score `0.7201` n `87` status `ready` deltaP `9.3692` edge `0.0381` maxDD `-0.9112`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
