# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T01:37:30.546703+00:00`
- Price records: `672`
- Market context records: `8573`
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

- `news_risk_high->unknown_24h` score `4751.5936` n `64` status `ready` deltaP `39.0625` edge `395.7478` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.9596` n `64` status `ready` deltaP `21.875` edge `0.4105` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.1774` n `64` status `ready` deltaP `18.3308` edge `0.0783` maxDD `-0.191`
- `market_context_high->crypto_alt_4h` score `1.9694` n `62` status `ready` deltaP `13.8178` edge `0.1677` maxDD `-5.323`
- `news_risk_high->equity_1h` score `1.7493` n `64` status `ready` deltaP `16.4016` edge `0.0841` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `1.1422` n `64` status `ready` deltaP `7.9649` edge `0.1709` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.6891` n `64` status `ready` deltaP `13.4146` edge `0.1381` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.4391` n `64` status `ready` deltaP `8.1119` edge `0.0549` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3727` n `64` status `ready` deltaP `7.2137` edge `0.0509` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.1072` n `64` status `ready` deltaP `5.5857` edge `0.0046` maxDD `-0.2475`
- `news_risk_high->fx_4h` score `0.0606` n `64` status `ready` deltaP `11.7759` edge `0.0223` maxDD `-0.6604`
- `news_risk_high->index_1h` score `0.0177` n `64` status `ready` deltaP `3.7706` edge `0.0088` maxDD `-0.5338`
- `news_risk_high->metal_4h` score `-0.0349` n `64` status `ready` deltaP `1.7149` edge `0.0317` maxDD `-0.8085`
- `market_context_high->fx_4h` score `-0.1076` n `62` status `ready` deltaP `8.6005` edge `0.0133` maxDD `-1.3685`
- `news_risk_high->metal_1h` score `-0.1096` n `64` status `ready` deltaP `3.5554` edge `0.0075` maxDD `-0.5599`
- `market_context_high->fx_1h` score `-0.2575` n `62` status `ready` deltaP `2.5111` edge `0.0005` maxDD `-0.6874`
- `market_context_high->commodity_1h` score `-0.3099` n `62` status `ready` deltaP `4.1578` edge `-0.0049` maxDD `-2.0038`
- `market_context_high->crypto_alt_1h` score `-0.5377` n `62` status `ready` deltaP `-2.9264` edge `0.0133` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.7561` n `62` status `ready` deltaP `0.7968` edge `-0.0154` maxDD `-1.5667`
- `market_context_high->metal_1h` score `-0.9505` n `62` status `ready` deltaP `-2.6946` edge `-0.0118` maxDD `-1.6224`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
