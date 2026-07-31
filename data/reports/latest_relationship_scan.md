# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T22:52:34.830208+00:00`
- Price records: `672`
- Market context records: `8560`
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

- `news_risk_high->unknown_24h` score `5076.8438` n `61` status `ready` deltaP `40.6648` edge `422.8413` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.6947` n `64` status `ready` deltaP `20.1982` edge `0.3996` maxDD `-3.4427`
- `market_context_high->crypto_alt_4h` score `2.0468` n `62` status `ready` deltaP `14.2752` edge `0.1711` maxDD `-5.323`
- `news_risk_high->index_4h` score `2.0303` n `64` status `ready` deltaP `16.8064` edge `0.0762` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.7541` n `64` status `ready` deltaP `16.4016` edge `0.0845` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `1.0964` n `64` status `ready` deltaP `7.3552` edge `0.1691` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.7394` n `64` status `ready` deltaP `13.872` edge `0.1415` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.4975` n `64` status `ready` deltaP `8.7107` edge `0.0584` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3688` n `64` status `ready` deltaP `7.064` edge `0.0514` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.0815` n `64` status `ready` deltaP `5.1366` edge `0.0043` maxDD `-0.2475`
- `news_risk_high->fx_4h` score `0.0412` n `64` status `ready` deltaP `11.6235` edge `0.0217` maxDD `-0.6604`
- `news_risk_high->index_1h` score `0.0083` n `64` status `ready` deltaP `3.6209` edge `0.0086` maxDD `-0.5338`
- `news_risk_high->metal_4h` score `-0.038` n `64` status `ready` deltaP `1.7149` edge `0.0313` maxDD `-0.8085`
- `news_risk_high->metal_1h` score `-0.1096` n `64` status `ready` deltaP `3.5554` edge `0.0075` maxDD `-0.5599`
- `market_context_high->fx_4h` score `-0.127` n `62` status `ready` deltaP `8.4481` edge `0.0127` maxDD `-1.3685`
- `market_context_high->fx_1h` score `-0.2832` n `62` status `ready` deltaP `2.062` edge `0.0002` maxDD `-0.6874`
- `market_context_high->commodity_1h` score `-0.3184` n `62` status `ready` deltaP `4.0081` edge `-0.005` maxDD `-2.0038`
- `market_context_high->crypto_alt_1h` score `-0.4792` n `62` status `ready` deltaP `-2.3276` edge `0.0168` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.7704` n `62` status `ready` deltaP `0.6471` edge `-0.0156` maxDD `-1.5667`
- `market_context_high->metal_1h` score `-0.9505` n `62` status `ready` deltaP `-2.6946` edge `-0.0118` maxDD `-1.6224`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
