# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T07:52:38.695369+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7466`

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

- `news_risk_high->equity_24h` score `49.5012` n `50` status `ready` deltaP `53.1042` edge `3.8417` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `21.1028` n `50` status `ready` deltaP `40.6389` edge `2.5489` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `12.0422` n `50` status `ready` deltaP `38.0` edge `0.8632` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `9.4666` n `50` status `ready` deltaP `22.8194` edge `1.5121` maxDD `-29.0448`
- `news_risk_high->index_24h` score `7.2243` n `50` status `ready` deltaP `44.7708` edge `0.3339` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.111` n `50` status `ready` deltaP `40.9722` edge `0.2361` maxDD `0.0`
- `news_risk_high->metal_4h` score `4.9588` n `50` status `ready` deltaP `44.0793` edge `0.157` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.1582` n `50` status `ready` deltaP `20.3841` edge `0.3482` maxDD `-9.0062`
- `news_risk_high->crypto_alt_4h` score `4.1174` n `50` status `ready` deltaP `26.2317` edge `0.3118` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `3.7946` n `50` status `ready` deltaP `19.5509` edge `0.2489` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.7268` n `50` status `ready` deltaP `34.5915` edge `0.1053` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.5195` n `50` status `ready` deltaP `24.189` edge `0.0837` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2041` n `50` status `ready` deltaP `24.994` edge `0.0425` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.2052` n `50` status `ready` deltaP `16.1497` edge `0.0229` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.9886` n `50` status `ready` deltaP `18.9028` edge `0.218` maxDD `-7.3825`
- `news_risk_high->crypto_major_1h` score `0.7687` n `50` status `ready` deltaP `19.2934` edge `0.0751` maxDD `-7.0808`
- `news_risk_high->crypto_alt_1h` score `0.7437` n `50` status `ready` deltaP `17.5928` edge `0.076` maxDD `-6.1688`
- `news_risk_high->commodity_1h` score `0.2694` n `50` status `ready` deltaP `3.3473` edge `0.0336` maxDD `-0.3438`
- `market_context_high->metal_1h` score `-0.6998` n `67` status `ready` deltaP `-0.7373` edge `0.0022` maxDD `-1.7817`
- `market_context_high->metal_4h` score `-1.2353` n `60` status `ready` deltaP `4.746` edge `-0.0307` maxDD `-4.3103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
