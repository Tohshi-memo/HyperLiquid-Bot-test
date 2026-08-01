# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T07:07:26.345683+00:00`
- Price records: `672`
- Market context records: `8596`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5898`

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

- `news_risk_high->unknown_24h` score `4749.1281` n `64` status `ready` deltaP `35.2431` edge `395.5678` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.8512` n `64` status `ready` deltaP `20.6555` edge `0.4096` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.2274` n `64` status `ready` deltaP `18.9405` edge `0.0784` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.7936` n `64` status `ready` deltaP `16.8507` edge `0.0848` maxDD `-2.4803`
- `market_context_high->crypto_alt_4h` score `1.5039` n `62` status `ready` deltaP `11.0739` edge `0.1472` maxDD `-5.323`
- `news_risk_high->crypto_major_4h` score `1.0116` n `64` status `ready` deltaP `6.593` edge `0.1633` maxDD `-3.5385`
- `news_risk_high->crypto_alt_1h` score `0.3978` n `64` status `ready` deltaP `7.6628` edge `0.0526` maxDD `-1.8813`
- `news_risk_high->crypto_alt_4h` score `0.3865` n `64` status `ready` deltaP `10.6707` edge `0.1176` maxDD `-5.8012`
- `news_risk_high->crypto_major_1h` score `0.3586` n `64` status `ready` deltaP `7.064` edge `0.0501` maxDD `-2.0972`
- `news_risk_high->fx_4h` score `0.1118` n `64` status `ready` deltaP `12.3857` edge `0.0225` maxDD `-0.6604`
- `news_risk_high->fx_1h` score `0.1056` n `64` status `ready` deltaP `5.5857` edge `0.0044` maxDD `-0.2475`
- `news_risk_high->metal_4h` score `0.0641` n `64` status `ready` deltaP `3.5442` edge `0.0322` maxDD `-0.8085`
- `news_risk_high->index_1h` score `0.034` n `64` status `ready` deltaP `4.07` edge `0.0089` maxDD `-0.5338`
- `market_context_high->fx_4h` score `-0.0565` n `62` status `ready` deltaP `9.2103` edge `0.0135` maxDD `-1.3685`
- `news_risk_high->metal_1h` score `-0.1215` n `64` status `ready` deltaP `3.4057` edge `0.0075` maxDD `-0.5599`
- `market_context_high->fx_1h` score `-0.2591` n `62` status `ready` deltaP `2.5111` edge `0.0003` maxDD `-0.6874`
- `market_context_high->commodity_1h` score `-0.2873` n `62` status `ready` deltaP `4.6069` edge `-0.005` maxDD `-2.0038`
- `market_context_high->crypto_alt_1h` score `-0.579` n `62` status `ready` deltaP `-3.3755` edge `0.011` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.7309` n `62` status `ready` deltaP `1.0962` edge `-0.0153` maxDD `-1.5667`
- `market_context_high->metal_1h` score `-0.9625` n `62` status `ready` deltaP `-2.8443` edge `-0.0118` maxDD `-1.6224`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
