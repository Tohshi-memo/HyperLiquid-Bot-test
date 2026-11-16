# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T07:07:28.695315+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7512`

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

- `news_risk_high->equity_24h` score `49.1631` n `50` status `ready` deltaP `52.5833` edge `3.817` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `21.1348` n `50` status `ready` deltaP `40.6389` edge `2.553` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `11.9444` n `50` status `ready` deltaP `37.5427` edge `0.8581` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `9.3921` n `50` status `ready` deltaP `22.6458` edge `1.5037` maxDD `-29.0448`
- `news_risk_high->index_24h` score `7.149` n `50` status `ready` deltaP `44.25` edge `0.3311` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.123` n `50` status `ready` deltaP `40.9722` edge `0.2371` maxDD `0.0`
- `news_risk_high->metal_4h` score `4.9722` n `50` status `ready` deltaP `44.2317` edge `0.1571` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.1776` n `50` status `ready` deltaP `20.5366` edge `0.3488` maxDD `-9.0062`
- `news_risk_high->crypto_alt_4h` score `4.0208` n `50` status `ready` deltaP `25.7744` edge `0.3068` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `3.881` n `50` status `ready` deltaP `20.0` edge `0.2531` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.7328` n `50` status `ready` deltaP `34.5915` edge `0.1058` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.477` n `50` status `ready` deltaP `23.7317` edge `0.0832` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2389` n `50` status `ready` deltaP `25.2934` edge `0.0434` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.2472` n `50` status `ready` deltaP `16.5988` edge `0.0234` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.9839` n `50` status `ready` deltaP `18.9028` edge `0.2174` maxDD `-7.3825`
- `news_risk_high->crypto_major_1h` score `0.8232` n `50` status `ready` deltaP `19.7425` edge `0.0791` maxDD `-7.0808`
- `news_risk_high->crypto_alt_1h` score `0.7904` n `50` status `ready` deltaP `17.8922` edge `0.08` maxDD `-6.1688`
- `news_risk_high->commodity_1h` score `0.2562` n `50` status `ready` deltaP `3.1976` edge `0.0335` maxDD `-0.3438`
- `market_context_high->metal_1h` score `-1.0083` n `67` status `ready` deltaP `-3.423` edge `-0.0056` maxDD `-1.7817`
- `market_context_high->fx_1h` score `-1.2792` n `67` status `ready` deltaP `-8.0459` edge `0.0001` maxDD `-0.2448`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
