# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T06:07:27.074530+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4408`

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

- `market_context_high->unknown_24h` score `2276.2799` n `63` status `ready` deltaP `3.4483` edge `189.667` maxDD `0.0`
- `news_risk_high->equity_24h` score `55.9659` n `50` status `ready` deltaP `61.4483` edge `4.3248` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `18.7286` n `50` status `ready` deltaP `34.5517` edge `2.2851` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `17.5772` n `63` status `ready` deltaP `16.5791` edge `1.5666` maxDD `-13.3222`
- `news_risk_high->equity_4h` score `14.4208` n `50` status `ready` deltaP `43.7927` edge `1.0228` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `12.8913` n `63` status `ready` deltaP `38.4565` edge `1.7234` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `9.1638` n `50` status `ready` deltaP `20.8966` edge `1.4861` maxDD `-29.0448`
- `news_risk_high->index_24h` score `8.4736` n `50` status `ready` deltaP `52.8276` edge `0.3843` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `7.7909` n `50` status `ready` deltaP `47.2414` edge `0.3343` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.1173` n `50` status `ready` deltaP `45.1463` edge `0.1631` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `4.5801` n `50` status `ready` deltaP `23.1437` edge `0.2904` maxDD `-3.7082`
- `news_risk_high->crypto_alt_4h` score `4.5048` n `50` status `ready` deltaP `26.9939` edge `0.339` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.2092` n `50` status `ready` deltaP `21.7561` edge `0.3433` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `4.1421` n `50` status `ready` deltaP `37.4878` edge `0.1206` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.193` n `50` status `ready` deltaP `29.9817` edge `0.1012` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.191` n `50` status `ready` deltaP `24.5449` edge `0.0444` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.5574` n `50` status `ready` deltaP `19.8922` edge `0.0273` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.7672` n `50` status `ready` deltaP `16.6946` edge `0.085` maxDD `-6.1688`
- `news_risk_high->metal_24h` score `0.7556` n `50` status `ready` deltaP `17.8276` edge `0.1953` maxDD `-7.3825`
- `news_risk_high->crypto_major_1h` score `0.7282` n `50` status `ready` deltaP `18.5449` edge `0.0749` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
