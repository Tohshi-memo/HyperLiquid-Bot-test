# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T12:52:26.717395+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4458`

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

- `market_context_high->unknown_1h` score `24978.3242` n `57` status `ready` deltaP `-0.3467` edge `2081.5455` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `16863.8999` n `57` status `ready` deltaP `4.418` edge `1405.3094` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1300.7566` n `31` status `ready` deltaP `3.728` edge `108.3891` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1097.647` n `31` status `ready` deltaP `4.701` edge `91.4449` maxDD `-0.119`
- `news_risk_high->equity_24h` score `45.1228` n `31` status `ready` deltaP `50.0` edge `3.4269` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `36.9873` n `31` status `ready` deltaP `48.6111` edge `2.7582` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `32.6032` n `31` status `ready` deltaP `48.7847` edge `2.3917` maxDD `0.0`
- `news_risk_high->metal_24h` score `13.3958` n `31` status `ready` deltaP `50.6105` edge `0.8064` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `10.315` n `31` status `ready` deltaP `32.9564` edge `0.6881` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `10.1414` n `31` status `ready` deltaP `21.5775` edge `0.7883` maxDD `-5.2957`
- `news_risk_high->index_24h` score `7.0704` n `31` status `ready` deltaP `48.0903` edge `0.2686` maxDD `0.0`
- `news_risk_high->fx_24h` score `6.2813` n `31` status `ready` deltaP `53.1698` edge `0.1818` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `6.1692` n `31` status `ready` deltaP `11.1379` edge `0.8584` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.7087` n `31` status `ready` deltaP `18.7898` edge `0.2025` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.2767` n `31` status `ready` deltaP `34.4808` edge `0.0692` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6507` n `31` status `ready` deltaP `31.0943` edge `0.0221` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.3395` n `31` status `ready` deltaP `8.9627` edge `0.2863` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.9255` n `31` status `ready` deltaP `7.4657` edge `0.2328` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5415` n `31` status `ready` deltaP `29.2833` edge `0.0303` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.4279` n `31` status `ready` deltaP `19.9793` edge `0.1056` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
