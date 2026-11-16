# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T20:07:35.100125+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4400`

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

- `market_context_high->unknown_24h` score `126.6136` n `32` status `ready` deltaP `3.9655` edge `10.5247` maxDD `0.0`
- `news_risk_high->equity_24h` score `53.6338` n `50` status `ready` deltaP `59.2069` edge `4.1454` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `20.5552` n `50` status `ready` deltaP `39.3793` edge `2.4871` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `18.2587` n `32` status `ready` deltaP `13.8578` edge `1.5836` maxDD `-8.6878`
- `news_risk_high->equity_4h` score `14.3945` n `50` status `ready` deltaP `44.079` edge `1.0187` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `12.2311` n `32` status `ready` deltaP `43.8793` edge `1.6026` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `9.7858` n `50` status `ready` deltaP `23.4828` edge `1.5486` maxDD `-29.0448`
- `news_risk_high->index_24h` score `8.0399` n `50` status `ready` deltaP `50.2414` edge `0.3654` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.3415` n `50` status `ready` deltaP `41.3793` edge `0.2526` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.3404` n `50` status `ready` deltaP `47.0942` edge `0.1687` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.7796` n `50` status `ready` deltaP `27.8784` edge `0.356` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.4593` n `50` status `ready` deltaP `22.1824` edge `0.3613` maxDD `-9.0062`
- `news_risk_high->equity_1h` score `4.454` n `50` status `ready` deltaP `21.8685` edge `0.2884` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `4.0621` n `50` status `ready` deltaP `36.8632` edge `0.1181` maxDD `-0.3611`
- `market_context_high->metal_24h` score `3.4537` n `32` status `ready` deltaP `42.8448` edge `0.2463` maxDD `-3.7989`
- `news_risk_high->index_4h` score `3.1233` n `50` status `ready` deltaP `29.2158` edge `0.1005` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2852` n `50` status `ready` deltaP `25.6622` edge `0.0448` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.5139` n `50` status `ready` deltaP `19.3632` edge `0.0272` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.9034` n `50` status `ready` deltaP `18.3448` edge `0.2108` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.8969` n `50` status `ready` deltaP `18.2601` edge `0.0912` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
