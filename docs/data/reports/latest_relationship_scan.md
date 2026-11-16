# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T08:07:33.859314+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4038`

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

- `news_risk_high->equity_24h` score `49.6159` n `50` status `ready` deltaP `53.2778` edge `3.8501` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `21.1012` n `50` status `ready` deltaP `40.6389` edge `2.5487` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `12.0712` n `50` status `ready` deltaP `38.1524` edge `0.8646` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `9.4963` n `50` status `ready` deltaP `22.8194` edge `1.5159` maxDD `-29.0448`
- `news_risk_high->index_24h` score `7.2351` n `50` status `ready` deltaP `44.7708` edge `0.3348` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.1038` n `50` status `ready` deltaP `40.9722` edge `0.2355` maxDD `0.0`
- `news_risk_high->metal_4h` score `4.9722` n `50` status `ready` deltaP `44.2317` edge `0.1571` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.1618` n `50` status `ready` deltaP `20.3841` edge `0.3485` maxDD `-9.0062`
- `news_risk_high->crypto_alt_4h` score `4.1548` n `50` status `ready` deltaP `26.3841` edge `0.3139` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `3.7719` n `50` status `ready` deltaP `19.4012` edge `0.248` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.7122` n `50` status `ready` deltaP `34.439` edge `0.1051` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.5207` n `50` status `ready` deltaP `24.189` edge `0.0838` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2029` n `50` status `ready` deltaP `24.994` edge `0.0424` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.1909` n `50` status `ready` deltaP `16.0` edge `0.0227` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.9909` n `50` status `ready` deltaP `18.9028` edge `0.2183` maxDD `-7.3825`
- `news_risk_high->crypto_major_1h` score `0.7648` n `50` status `ready` deltaP `19.2934` edge `0.0746` maxDD `-7.0808`
- `news_risk_high->crypto_alt_1h` score `0.7382` n `50` status `ready` deltaP `17.5928` edge `0.0753` maxDD `-6.1688`
- `news_risk_high->commodity_1h` score `0.2682` n `50` status `ready` deltaP `3.3473` edge `0.0335` maxDD `-0.3438`
- `market_context_high->metal_1h` score `-0.6902` n `67` status `ready` deltaP `-0.7373` edge `0.003` maxDD `-1.7817`
- `market_context_high->metal_4h` score `-1.3098` n `59` status `ready` deltaP `3.9944` edge `-0.0319` maxDD `-4.3103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
