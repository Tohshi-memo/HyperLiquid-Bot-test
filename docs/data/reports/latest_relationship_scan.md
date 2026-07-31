# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T11:52:36.374730+00:00`
- Price records: `672`
- Market context records: `8512`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5882`

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

- `news_risk_high->unknown_24h` score `6276.6813` n `52` status `ready` deltaP `44.7383` edge `522.8006` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.6684` n `64` status `ready` deltaP `21.2652` edge `0.3903` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.9879` n `64` status `ready` deltaP `16.5015` edge `0.0747` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.6978` n `64` status `ready` deltaP `15.6531` edge `0.0848` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `0.876` n `64` status `ready` deltaP `5.8308` edge `0.151` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.8006` n `64` status `ready` deltaP `14.3293` edge `0.1463` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.5708` n `64` status `ready` deltaP `9.3095` edge `0.0638` maxDD `-1.8813`
- `market_context_high->equity_1h` score `0.3915` n `40` status `ready` deltaP `2.2156` edge `0.047` maxDD `-0.9985`
- `news_risk_high->crypto_major_1h` score `0.3376` n `64` status `ready` deltaP `6.6149` edge `0.0504` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.101` n `64` status `ready` deltaP `5.5857` edge `0.0038` maxDD `-0.2475`
- `market_context_high->commodity_1h` score `0.0642` n `40` status `ready` deltaP `9.2964` edge `0.0088` maxDD `-2.0038`
- `news_risk_high->index_1h` score `0.0395` n `64` status `ready` deltaP `4.2197` edge `0.0086` maxDD `-0.5338`
- `market_context_high->index_1h` score `0.0293` n `40` status `ready` deltaP `3.9072` edge `-0.0026` maxDD `-0.2417`
- `news_risk_high->fx_4h` score `-0.0026` n `64` status `ready` deltaP `11.1662` edge `0.0211` maxDD `-0.6604`
- `news_risk_high->metal_4h` score `-0.0666` n `64` status `ready` deltaP `1.1052` edge `0.0317` maxDD `-0.8085`
- `news_risk_high->metal_1h` score `-0.1395` n `64` status `ready` deltaP `3.1063` edge `0.008` maxDD `-0.5599`
- `market_context_high->crypto_major_1h` score `-0.2253` n `40` status `ready` deltaP `3.8024` edge `-0.0045` maxDD `-1.9791`
- `market_context_high->metal_1h` score `-0.2706` n `40` status `ready` deltaP `1.8563` edge `-0.01` maxDD `-0.6321`
- `market_context_high->fx_1h` score `-0.6875` n `40` status `ready` deltaP `-6.6018` edge `0.0024` maxDD `-0.3888`
- `market_context_high->crypto_alt_1h` score `-0.7889` n `40` status `ready` deltaP `-8.503` edge `0.0057` maxDD `-2.012`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
