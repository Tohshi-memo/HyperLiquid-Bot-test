# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T10:07:26.764458+00:00`
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

- `market_context_high->unknown_24h` score `2034.4715` n `79` status `ready` deltaP `3.4483` edge `169.5163` maxDD `0.0`
- `news_risk_high->equity_24h` score `57.6254` n `50` status `ready` deltaP `64.2069` edge `4.4447` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `17.8574` n `50` status `ready` deltaP `31.7931` edge `2.1918` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `14.6907` n `50` status `ready` deltaP `44.7073` edge `1.0392` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `14.1787` n `79` status `ready` deltaP `43.4134` edge `1.8554` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `12.9715` n `79` status `ready` deltaP `26.0366` edge `1.7018` maxDD `-13.3222`
- `news_risk_high->index_24h` score `8.8587` n `50` status `ready` deltaP `55.5862` edge `0.398` maxDD `-0.4279`
- `news_risk_high->crypto_alt_24h` score `8.6546` n `50` status `ready` deltaP `18.1379` edge `1.4392` maxDD `-29.0448`
- `news_risk_high->commodity_24h` score `8.4508` n `50` status `ready` deltaP `50.0` edge `0.3709` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.0412` n `50` status `ready` deltaP `44.689` edge `0.1598` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `4.7168` n `50` status `ready` deltaP `23.5928` edge `0.2988` maxDD `-3.7082`
- `news_risk_high->crypto_alt_4h` score `4.484` n `50` status `ready` deltaP `26.689` edge `0.3393` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.0318` n `50` status `ready` deltaP `20.9939` edge `0.3336` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `3.8865` n `50` status `ready` deltaP `35.6585` edge `0.1115` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.2195` n `50` status `ready` deltaP `30.1341` edge `0.1024` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2317` n `50` status `ready` deltaP `24.994` edge `0.0448` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.579` n `50` status `ready` deltaP `20.0419` edge `0.0281` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.835` n `50` status `ready` deltaP `17.1437` edge `0.0907` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.7796` n `50` status `ready` deltaP `18.994` edge `0.0785` maxDD `-7.0808`
- `news_risk_high->metal_24h` score `0.7478` n `50` status `ready` deltaP `17.8276` edge `0.1943` maxDD `-7.3825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
