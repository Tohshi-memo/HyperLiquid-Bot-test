# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T08:37:41.274523+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4052`

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

- `market_context_high->unknown_24h` score `88.5974` n `30` status `ready` deltaP `3.9931` edge `7.3565` maxDD `0.0`
- `news_risk_high->equity_24h` score `49.8585` n `50` status `ready` deltaP `53.625` edge `3.868` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `21.1153` n `50` status `ready` deltaP `40.6389` edge `2.5505` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `17.4394` n `30` status `ready` deltaP `12.1527` edge `1.5267` maxDD `-8.6878`
- `market_context_high->crypto_major_24h` score `12.2508` n `30` status `ready` deltaP `42.6389` edge `1.6134` maxDD `-22.8301`
- `news_risk_high->equity_4h` score `12.1555` n `50` status `ready` deltaP `38.4573` edge `0.8696` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `9.5602` n `50` status `ready` deltaP `22.8194` edge `1.5241` maxDD `-29.0448`
- `news_risk_high->index_24h` score `7.2579` n `50` status `ready` deltaP `44.7708` edge `0.3367` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.0978` n `50` status `ready` deltaP `40.9722` edge `0.235` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.0038` n `50` status `ready` deltaP `44.5366` edge `0.1577` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.2764` n `50` status `ready` deltaP `26.689` edge `0.322` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.2306` n `50` status `ready` deltaP `20.689` edge `0.3522` maxDD `-9.0062`
- `market_context_high->metal_24h` score `3.8741` n `30` status `ready` deltaP `47.5695` edge `0.2687` maxDD `-3.7989`
- `news_risk_high->equity_1h` score `3.7767` n `50` status `ready` deltaP `19.4012` edge `0.2484` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.6758` n `50` status `ready` deltaP `34.1341` edge `0.1041` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.5511` n `50` status `ready` deltaP `24.4939` edge `0.0843` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2053` n `50` status `ready` deltaP `24.994` edge `0.0426` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.1789` n `50` status `ready` deltaP `15.8503` edge `0.0227` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.9956` n `50` status `ready` deltaP `18.9028` edge `0.2189` maxDD `-7.3825`
- `news_risk_high->crypto_major_1h` score `0.7928` n `50` status `ready` deltaP `19.5928` edge `0.0762` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
