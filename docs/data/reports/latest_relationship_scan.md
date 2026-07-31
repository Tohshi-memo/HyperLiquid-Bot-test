# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T12:37:37.388578+00:00`
- Price records: `672`
- Market context records: `8515`
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

- `news_risk_high->unknown_24h` score `6277.4385` n `52` status `ready` deltaP `44.7383` edge `522.8637` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.5746` n `64` status `ready` deltaP `21.1128` edge `0.3835` maxDD `-3.4427`
- `market_context_high->equity_4h` score `4.1279` n `31` status `ready` deltaP `33.3104` edge `0.1415` maxDD `-0.8997`
- `news_risk_high->index_4h` score `1.9867` n `64` status `ready` deltaP `16.5015` edge `0.0746` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.7673` n `64` status `ready` deltaP `16.1022` edge `0.0876` maxDD `-2.4803`
- `market_context_high->crypto_major_4h` score `1.282` n `31` status `ready` deltaP `9.3086` edge `0.1696` maxDD `-2.7172`
- `market_context_high->crypto_alt_4h` score `1.2616` n `31` status `ready` deltaP `13.1196` edge `0.1413` maxDD `-3.6947`
- `news_risk_high->crypto_major_4h` score `0.8627` n `64` status `ready` deltaP `5.8308` edge `0.1493` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.7952` n `64` status `ready` deltaP `14.3293` edge `0.1456` maxDD `-5.8012`
- `market_context_high->index_4h` score `0.7639` n `31` status `ready` deltaP `10.9067` edge `0.0148` maxDD `-0.2417`
- `news_risk_high->crypto_alt_1h` score `0.5841` n `64` status `ready` deltaP `9.4592` edge `0.0645` maxDD `-1.8813`
- `market_context_high->metal_4h` score `0.5174` n `31` status `ready` deltaP `17.9435` edge `-0.0058` maxDD `-1.1327`
- `news_risk_high->crypto_major_1h` score `0.347` n `64` status `ready` deltaP `6.7646` edge `0.0506` maxDD `-2.0972`
- `market_context_high->commodity_1h` score `0.1661` n `43` status `ready` deltaP `10.0856` edge `0.0166` maxDD `-2.0038`
- `news_risk_high->fx_1h` score `0.0932` n `64` status `ready` deltaP `5.436` edge `0.0038` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.0659` n `64` status `ready` deltaP `4.6688` edge `0.009` maxDD `-0.5338`
- `news_risk_high->fx_4h` score `-0.005` n `64` status `ready` deltaP `11.1662` edge `0.0209` maxDD `-0.6604`
- `news_risk_high->metal_4h` score `-0.0342` n `64` status `ready` deltaP `1.5625` edge `0.0328` maxDD `-0.8085`
- `market_context_high->fx_4h` score `-0.0439` n `31` status `ready` deltaP `4.765` edge `0.0121` maxDD `-0.2932`
- `news_risk_high->metal_1h` score `-0.1131` n `64` status `ready` deltaP `3.4057` edge `0.0082` maxDD `-0.5599`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
