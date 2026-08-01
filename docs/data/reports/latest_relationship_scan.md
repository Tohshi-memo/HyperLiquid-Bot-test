# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T07:22:44.927217+00:00`
- Price records: `672`
- Market context records: `8598`
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

- `news_risk_high->unknown_24h` score `4749.011` n `64` status `ready` deltaP `35.0694` edge `395.5592` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.85` n `64` status `ready` deltaP `20.6555` edge `0.4095` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.2396` n `64` status `ready` deltaP `19.093` edge `0.0784` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.7948` n `64` status `ready` deltaP `16.8507` edge `0.0849` maxDD `-2.4803`
- `market_context_high->crypto_alt_4h` score `1.5173` n `62` status `ready` deltaP `11.2264` edge `0.1473` maxDD `-5.323`
- `news_risk_high->crypto_major_4h` score `1.0226` n `64` status `ready` deltaP `6.7454` edge `0.1637` maxDD `-3.5385`
- `news_risk_high->crypto_alt_1h` score `0.4072` n `64` status `ready` deltaP `7.8125` edge `0.0528` maxDD `-1.8813`
- `news_risk_high->crypto_alt_4h` score `0.3952` n `64` status `ready` deltaP `10.8232` edge `0.1177` maxDD `-5.8012`
- `news_risk_high->crypto_major_1h` score `0.3594` n `64` status `ready` deltaP `7.064` edge `0.0502` maxDD `-2.0972`
- `news_risk_high->fx_4h` score `0.124` n `64` status `ready` deltaP `12.5381` edge `0.0225` maxDD `-0.6604`
- `news_risk_high->fx_1h` score `0.1134` n `64` status `ready` deltaP `5.7354` edge `0.0044` maxDD `-0.2475`
- `news_risk_high->metal_4h` score `0.0641` n `64` status `ready` deltaP `3.5442` edge `0.0322` maxDD `-0.8085`
- `news_risk_high->index_1h` score `0.034` n `64` status `ready` deltaP `4.07` edge `0.0089` maxDD `-0.5338`
- `market_context_high->fx_4h` score `-0.0443` n `62` status `ready` deltaP `9.3627` edge `0.0135` maxDD `-1.3685`
- `news_risk_high->metal_1h` score `-0.1215` n `64` status `ready` deltaP `3.4057` edge `0.0075` maxDD `-0.5599`
- `market_context_high->fx_1h` score `-0.2513` n `62` status `ready` deltaP `2.6608` edge `0.0003` maxDD `-0.6874`
- `market_context_high->commodity_1h` score `-0.2795` n `62` status `ready` deltaP `4.7566` edge `-0.005` maxDD `-2.0038`
- `market_context_high->crypto_alt_1h` score `-0.5696` n `62` status `ready` deltaP `-3.2258` edge `0.0112` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.7309` n `62` status `ready` deltaP `1.0962` edge `-0.0153` maxDD `-1.5667`
- `market_context_high->metal_1h` score `-0.9625` n `62` status `ready` deltaP `-2.8443` edge `-0.0118` maxDD `-1.6224`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
