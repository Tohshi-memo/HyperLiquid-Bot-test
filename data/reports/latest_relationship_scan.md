# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T14:37:28.616664+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4470`

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

- `market_context_high->unknown_1h` score `27088.5096` n `53` status `ready` deltaP `0.5959` edge `2257.388` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `18414.7551` n `53` status `ready` deltaP `4.1532` edge `1534.5491` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1279.5502` n `31` status `ready` deltaP `3.5783` edge `106.6229` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1100.815` n `31` status `ready` deltaP `4.701` edge `91.7089` maxDD `-0.119`
- `news_risk_high->equity_24h` score `44.3272` n `31` status `ready` deltaP `48.7847` edge `3.3687` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `36.8433` n `31` status `ready` deltaP `48.6111` edge `2.7462` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `32.62` n `31` status `ready` deltaP `48.7847` edge `2.3931` maxDD `0.0`
- `news_risk_high->metal_24h` score `13.1906` n `31` status `ready` deltaP `49.3952` edge `0.7974` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.1674` n `31` status `ready` deltaP `22.1872` edge `0.7864` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `9.9965` n `31` status `ready` deltaP `32.499` edge `0.6646` maxDD `-2.1911`
- `news_risk_high->index_24h` score `6.9295` n `31` status `ready` deltaP `47.0486` edge `0.2638` maxDD `0.0`
- `news_risk_high->fx_24h` score `6.1624` n `31` status `ready` deltaP `51.9545` edge `0.18` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `6.1236` n `31` status `ready` deltaP `11.5952` edge `0.8495` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.3632` n `31` status `ready` deltaP `18.3407` edge `0.1767` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.2405` n `31` status `ready` deltaP `34.3283` edge `0.0672` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.5956` n `31` status `ready` deltaP `30.7949` edge `0.0195` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.2162` n `31` status `ready` deltaP `8.9627` edge `0.2705` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.8725` n `31` status `ready` deltaP `7.9148` edge `0.223` maxDD `-1.5232`
- `market_context_high->fx_4h` score `1.8485` n `53` status `ready` deltaP `25.2991` edge `0.0264` maxDD `-0.2813`
- `news_risk_high->metal_1h` score `1.4932` n `31` status `ready` deltaP `28.8342` edge `0.0271` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
