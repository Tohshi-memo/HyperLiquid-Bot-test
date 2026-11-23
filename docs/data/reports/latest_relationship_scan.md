# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T14:07:45.691504+00:00`
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

- `market_context_high->unknown_1h` score `25995.4568` n `55` status `ready` deltaP `-0.7295` edge `2166.3091` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `17611.5496` n `55` status `ready` deltaP `4.2904` edge `1467.6144` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1292.389` n `31` status `ready` deltaP `3.728` edge `107.6918` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1101.115` n `31` status `ready` deltaP `4.701` edge `91.7339` maxDD `-0.119`
- `news_risk_high->equity_24h` score `44.7102` n `31` status `ready` deltaP `49.1319` edge `3.3983` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `37.0281` n `31` status `ready` deltaP `48.6111` edge `2.7616` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `32.7448` n `31` status `ready` deltaP `48.7847` edge `2.4035` maxDD `0.0`
- `news_risk_high->metal_24h` score `13.2676` n `31` status `ready` deltaP `49.7424` edge `0.8015` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.285` n `31` status `ready` deltaP `22.1872` edge `0.7962` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.2392` n `31` status `ready` deltaP `32.8039` edge `0.6828` maxDD `-2.1911`
- `news_risk_high->index_24h` score `6.9885` n `31` status `ready` deltaP `47.3958` edge `0.2664` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `6.2258` n `31` status `ready` deltaP `11.5952` edge `0.8626` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `6.1962` n `31` status `ready` deltaP `52.3018` edge `0.1805` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.5876` n `31` status `ready` deltaP `18.4904` edge `0.1944` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.2853` n `31` status `ready` deltaP `34.6332` edge `0.0689` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6279` n `31` status `ready` deltaP `30.9446` edge `0.0212` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.3114` n `31` status `ready` deltaP `8.9627` edge `0.2827` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.9473` n `31` status `ready` deltaP `7.9148` edge `0.2326` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5166` n `31` status `ready` deltaP `28.9839` edge `0.0291` maxDD `-0.2315`
- `market_context_high->fx_4h` score `1.5065` n `55` status `ready` deltaP `22.7605` edge `0.024` maxDD `-0.3492`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
