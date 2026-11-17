# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T00:22:36.208532+00:00`
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

- `market_context_high->unknown_24h` score `1575.7247` n `49` status `ready` deltaP `3.4483` edge `131.2874` maxDD `0.0`
- `news_risk_high->equity_24h` score `54.3874` n `50` status `ready` deltaP `59.2069` edge `4.2082` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `19.858` n `50` status `ready` deltaP `37.6552` edge `2.4092` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `17.0678` n `49` status `ready` deltaP `13.1422` edge `1.5185` maxDD `-11.0372`
- `news_risk_high->equity_4h` score `14.6767` n `50` status `ready` deltaP `45.0122` edge `1.036` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `12.6445` n `49` status `ready` deltaP `40.8797` edge `1.6756` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `9.4302` n `50` status `ready` deltaP `22.4483` edge `1.5099` maxDD `-29.0448`
- `news_risk_high->index_24h` score `8.1107` n `50` status `ready` deltaP `50.2414` edge `0.3713` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.8833` n `50` status `ready` deltaP `43.2759` edge `0.2851` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.4183` n `50` status `ready` deltaP `47.7378` edge `0.1709` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `4.6065` n `50` status `ready` deltaP `22.8443` edge `0.2946` maxDD `-3.7082`
- `news_risk_high->crypto_alt_4h` score `4.4692` n `50` status `ready` deltaP `26.3841` edge `0.3401` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.3328` n `50` status `ready` deltaP `21.7561` edge `0.3536` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `4.1129` n `50` status `ready` deltaP `37.1829` edge `0.1202` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.2159` n `50` status `ready` deltaP `30.1341` edge `0.1021` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.324` n `50` status `ready` deltaP `25.8922` edge `0.0465` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.6018` n `50` status `ready` deltaP `20.3413` edge `0.028` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.8706` n `50` status `ready` deltaP `18.3448` edge `0.2066` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.8599` n `50` status `ready` deltaP `17.7425` edge `0.0899` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.8264` n `50` status `ready` deltaP `19.2934` edge `0.0825` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
