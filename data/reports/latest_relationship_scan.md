# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T00:37:26.781246+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4392`

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

- `market_context_high->unknown_24h` score `1645.0715` n `50` status `ready` deltaP `3.4483` edge `137.0663` maxDD `0.0`
- `news_risk_high->equity_24h` score `54.4486` n `50` status `ready` deltaP `59.2069` edge `4.2133` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `19.8213` n `50` status `ready` deltaP `37.6552` edge `2.4045` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `16.8978` n `50` status `ready` deltaP `12.4483` edge `1.5138` maxDD `-11.4241`
- `news_risk_high->equity_4h` score `14.6743` n `50` status `ready` deltaP `45.0122` edge `1.0358` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `12.5504` n `50` status `ready` deltaP `39.6552` edge `1.6717` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `9.4192` n `50` status `ready` deltaP `22.4483` edge `1.5085` maxDD `-29.0448`
- `news_risk_high->index_24h` score `8.1167` n `50` status `ready` deltaP `50.2414` edge `0.3718` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.9187` n `50` status `ready` deltaP `43.4483` edge `0.2869` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.4025` n `50` status `ready` deltaP `47.5854` edge `0.1706` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `4.6041` n `50` status `ready` deltaP `22.8443` edge `0.2944` maxDD `-3.7082`
- `news_risk_high->crypto_alt_4h` score `4.4632` n `50` status `ready` deltaP `26.3841` edge `0.3396` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.3256` n `50` status `ready` deltaP `21.7561` edge `0.353` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `4.1105` n `50` status `ready` deltaP `37.1829` edge `0.12` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.2147` n `50` status `ready` deltaP `30.1341` edge `0.102` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.3108` n `50` status `ready` deltaP `25.7425` edge `0.0464` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.5898` n `50` status `ready` deltaP `20.1916` edge `0.028` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.8698` n `50` status `ready` deltaP `18.3448` edge `0.2065` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.8458` n `50` status `ready` deltaP `17.5928` edge `0.0891` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.8272` n `50` status `ready` deltaP `19.2934` edge `0.0826` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
