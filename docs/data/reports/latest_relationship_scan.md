# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T12:22:29.738276+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4482`

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

- `market_context_high->unknown_1h` score `24021.6467` n `59` status `ready` deltaP `0.0101` edge `2001.82` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `16178.6434` n `59` status `ready` deltaP `4.537` edge `1348.2039` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1300.5706` n `31` status `ready` deltaP `3.728` edge `108.3736` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1100.2678` n `31` status `ready` deltaP `4.701` edge `91.6633` maxDD `-0.119`
- `news_risk_high->equity_24h` score `45.2646` n `31` status `ready` deltaP `50.3472` edge `3.4364` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `36.9813` n `31` status `ready` deltaP `48.6111` edge `2.7577` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `32.5768` n `31` status `ready` deltaP `48.7847` edge `2.3895` maxDD `0.0`
- `news_risk_high->metal_24h` score `13.4404` n `31` status `ready` deltaP `50.9577` edge `0.8078` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `10.327` n `31` status `ready` deltaP `32.9564` edge `0.6891` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `10.1282` n `31` status `ready` deltaP `21.5775` edge `0.7872` maxDD `-5.2957`
- `news_risk_high->index_24h` score `7.0903` n `31` status `ready` deltaP `48.2639` edge `0.2691` maxDD `0.0`
- `news_risk_high->fx_24h` score `6.3162` n `31` status `ready` deltaP `53.517` edge `0.1824` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `6.1645` n `31` status `ready` deltaP `11.1379` edge `0.8578` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.6931` n `31` status `ready` deltaP `18.7898` edge `0.2012` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.2621` n `31` status `ready` deltaP `34.3283` edge `0.069` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6351` n `31` status `ready` deltaP `30.9446` edge `0.0218` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.3449` n `31` status `ready` deltaP `8.9627` edge `0.287` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.9357` n `31` status `ready` deltaP `7.4657` edge `0.2341` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5314` n `31` status `ready` deltaP `29.1336` edge `0.03` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.4413` n `31` status `ready` deltaP `20.1318` edge `0.1063` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
