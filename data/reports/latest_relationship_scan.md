# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T07:22:26.223793+00:00`
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

- `news_risk_high->equity_24h` score `49.2802` n `50` status `ready` deltaP `52.7569` edge `3.8256` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `21.134` n `50` status `ready` deltaP `40.6389` edge `2.5529` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `11.9842` n `50` status `ready` deltaP `37.6951` edge `0.8604` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `9.4292` n `50` status `ready` deltaP `22.8194` edge `1.5073` maxDD `-29.0448`
- `news_risk_high->index_24h` score `7.1749` n `50` status `ready` deltaP `44.4236` edge `0.3321` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.1182` n `50` status `ready` deltaP `40.9722` edge `0.2367` maxDD `0.0`
- `news_risk_high->metal_4h` score `4.9722` n `50` status `ready` deltaP `44.2317` edge `0.1571` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.1872` n `50` status `ready` deltaP `20.5366` edge `0.3496` maxDD `-9.0062`
- `news_risk_high->crypto_alt_4h` score `4.0654` n `50` status `ready` deltaP `25.9268` edge `0.3095` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `3.8546` n `50` status `ready` deltaP `19.8503` edge `0.2519` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.7292` n `50` status `ready` deltaP `34.5915` edge `0.1055` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.4927` n `50` status `ready` deltaP `23.8841` edge `0.0835` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2365` n `50` status `ready` deltaP `25.2934` edge `0.0432` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.234` n `50` status `ready` deltaP `16.4491` edge `0.0233` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.9854` n `50` status `ready` deltaP `18.9028` edge `0.2176` maxDD `-7.3825`
- `news_risk_high->crypto_major_1h` score `0.8076` n `50` status `ready` deltaP `19.5928` edge `0.0781` maxDD `-7.0808`
- `news_risk_high->crypto_alt_1h` score `0.7834` n `50` status `ready` deltaP `17.8922` edge `0.0791` maxDD `-6.1688`
- `news_risk_high->commodity_1h` score `0.255` n `50` status `ready` deltaP `3.1976` edge `0.0334` maxDD `-0.3438`
- `market_context_high->metal_1h` score `-0.9879` n `67` status `ready` deltaP `-3.423` edge `-0.0039` maxDD `-1.7817`
- `market_context_high->fx_1h` score `-1.1694` n `67` status `ready` deltaP `-6.703` edge `0.0003` maxDD `-0.2448`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
