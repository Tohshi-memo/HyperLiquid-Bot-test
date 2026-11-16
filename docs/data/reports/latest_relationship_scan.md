# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T10:37:29.400133+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4058`

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

- `market_context_high->unknown_24h` score `104.1614` n `30` status `ready` deltaP `3.9931` edge `8.6535` maxDD `0.0`
- `news_risk_high->equity_24h` score `50.9368` n `50` status `ready` deltaP `55.0139` edge `3.9486` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `21.3258` n `50` status `ready` deltaP `41.5069` edge `2.5717` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `18.0419` n `30` status `ready` deltaP `13.368` edge `1.5688` maxDD `-8.6878`
- `market_context_high->crypto_major_24h` score `12.4613` n `30` status `ready` deltaP `43.5069` edge `1.6346` maxDD `-22.8301`
- `news_risk_high->equity_4h` score `12.4281` n `50` status `ready` deltaP `39.5244` edge `0.8852` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `9.9518` n `50` status `ready` deltaP `24.0347` edge `1.5662` maxDD `-29.0448`
- `news_risk_high->index_24h` score `7.4547` n `50` status `ready` deltaP `45.9861` edge `0.345` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.0546` n `50` status `ready` deltaP `40.9722` edge `0.2314` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.0985` n `50` status `ready` deltaP `45.4512` edge `0.1595` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.6882` n `50` status `ready` deltaP `27.7561` edge `0.3492` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.4106` n `50` status `ready` deltaP `21.6037` edge `0.3611` maxDD `-9.0062`
- `news_risk_high->equity_1h` score `3.9661` n `50` status `ready` deltaP `20.4491` edge `0.2572` maxDD `-3.7082`
- `market_context_high->metal_24h` score `3.932` n `30` status `ready` deltaP `48.2639` edge `0.2715` maxDD `-3.7989`
- `news_risk_high->commodity_4h` score `3.659` n `50` status `ready` deltaP `34.1341` edge `0.1027` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.5777` n `50` status `ready` deltaP `24.6463` edge `0.0855` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2245` n `50` status `ready` deltaP `25.1437` edge `0.0432` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.2735` n `50` status `ready` deltaP `16.8982` edge `0.0236` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `1.0535` n `50` status `ready` deltaP `19.5972` edge `0.2217` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.8606` n `50` status `ready` deltaP `18.3413` edge `0.086` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
