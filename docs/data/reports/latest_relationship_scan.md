# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T09:37:44.377381+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4096`

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

- `market_context_high->unknown_24h` score `2105.6615` n `77` status `ready` deltaP `3.4483` edge `175.4488` maxDD `0.0`
- `news_risk_high->equity_24h` score `57.4034` n `50` status `ready` deltaP `63.8621` edge `4.4285` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `17.9557` n `50` status `ready` deltaP `32.1379` edge `2.2021` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `14.6835` n `50` status `ready` deltaP `44.7073` edge `1.0386` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `14.0628` n `77` status `ready` deltaP `42.9691` edge `1.8435` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `12.8473` n `77` status `ready` deltaP `25.1322` edge `1.6919` maxDD `-13.3222`
- `news_risk_high->index_24h` score `8.8107` n `50` status `ready` deltaP `55.2414` edge `0.3963` maxDD `-0.4279`
- `news_risk_high->crypto_alt_24h` score `8.7162` n `50` status `ready` deltaP `18.4828` edge `1.4448` maxDD `-29.0448`
- `news_risk_high->commodity_24h` score `8.3704` n `50` status `ready` deltaP `49.6552` edge `0.3665` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.0412` n `50` status `ready` deltaP `44.689` edge `0.1598` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `4.7072` n `50` status `ready` deltaP `23.5928` edge `0.298` maxDD `-3.7082`
- `news_risk_high->crypto_alt_4h` score `4.4696` n `50` status `ready` deltaP `26.689` edge `0.3381` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.0318` n `50` status `ready` deltaP `20.9939` edge `0.3336` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `3.9107` n `50` status `ready` deltaP `35.811` edge `0.1125` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.2195` n `50` status `ready` deltaP `30.1341` edge `0.1024` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2317` n `50` status `ready` deltaP `24.994` edge `0.0448` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.579` n `50` status `ready` deltaP `20.0419` edge `0.0281` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.8225` n `50` status `ready` deltaP `16.994` edge `0.0901` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.7851` n `50` status `ready` deltaP `18.994` edge `0.0792` maxDD `-7.0808`
- `news_risk_high->metal_24h` score `0.7462` n `50` status `ready` deltaP `17.8276` edge `0.1941` maxDD `-7.3825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
