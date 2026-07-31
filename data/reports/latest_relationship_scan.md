# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T10:37:31.492538+00:00`
- Price records: `672`
- Market context records: `8507`
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

- `news_risk_high->unknown_24h` score `6275.3589` n `52` status `ready` deltaP `44.7383` edge `522.6904` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.9982` n `64` status `ready` deltaP `22.0274` edge `0.4127` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.0485` n `64` status `ready` deltaP `16.9588` edge `0.0767` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.7529` n `64` status `ready` deltaP `16.1022` edge `0.0864` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `0.9345` n `64` status `ready` deltaP `5.8308` edge `0.1585` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.8702` n `64` status `ready` deltaP `14.4817` edge `0.1542` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.5942` n `64` status `ready` deltaP `9.6089` edge `0.0648` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3766` n `64` status `ready` deltaP `7.064` edge `0.0524` maxDD `-2.0972`
- `market_context_high->equity_1h` score `0.3242` n `35` status `ready` deltaP `2.6647` edge `0.0384` maxDD `-0.9985`
- `market_context_high->index_1h` score `0.1624` n `35` status `ready` deltaP `6.4072` edge `-0.0022` maxDD `-0.2417`
- `news_risk_high->fx_1h` score `0.1259` n `64` status `ready` deltaP `6.0348` edge `0.004` maxDD `-0.2475`
- `news_risk_high->fx_4h` score `0.0522` n `64` status `ready` deltaP `11.7759` edge `0.0216` maxDD `-0.6604`
- `news_risk_high->index_1h` score `0.0395` n `64` status `ready` deltaP `4.2197` edge `0.0086` maxDD `-0.5338`
- `news_risk_high->metal_4h` score `-0.0674` n `64` status `ready` deltaP `1.1052` edge `0.0316` maxDD `-0.8085`
- `news_risk_high->metal_1h` score `-0.1167` n `64` status `ready` deltaP `3.4057` edge `0.0079` maxDD `-0.5599`
- `market_context_high->metal_1h` score `-0.276` n `35` status `ready` deltaP `1.4414` edge `-0.0082` maxDD `-0.6101`
- `market_context_high->crypto_major_1h` score `-0.3452` n `35` status `ready` deltaP `3.5372` edge `-0.0181` maxDD `-1.9791`
- `market_context_high->commodity_1h` score `-0.3639` n `35` status `ready` deltaP `3.3747` edge `-0.0066` maxDD `-2.0038`
- `market_context_high->crypto_alt_1h` score `-0.7585` n `35` status `ready` deltaP `-8.2036` edge `0.0076` maxDD `-2.012`
- `market_context_high->fx_1h` score `-0.9614` n `35` status `ready` deltaP `-11.5098` edge `0.0` maxDD `-0.3888`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
