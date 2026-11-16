# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T05:37:34.601723+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8982`

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

- `news_risk_high->equity_24h` score `48.517` n `50` status `ready` deltaP `51.5417` edge `3.7701` maxDD `-3.6503`
- `market_context_high->unknown_4h` score `36.1804` n `64` status `ready` deltaP `3.3537` edge `3.0035` maxDD `-0.1993`
- `news_risk_high->crypto_major_24h` score `21.1628` n `50` status `ready` deltaP `40.6389` edge `2.5566` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `11.8542` n `50` status `ready` deltaP `37.3902` edge `0.8516` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `9.2045` n `50` status `ready` deltaP `21.6042` edge `1.4866` maxDD `-29.0448`
- `news_risk_high->index_24h` score `7.0069` n `50` status `ready` deltaP `43.2083` edge `0.3262` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.1698` n `50` status `ready` deltaP `40.9722` edge `0.241` maxDD `0.0`
- `news_risk_high->metal_4h` score `4.983` n `50` status `ready` deltaP `44.2317` edge `0.158` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.1524` n `50` status `ready` deltaP `20.5366` edge `0.3467` maxDD `-9.0062`
- `news_risk_high->equity_1h` score `3.9289` n `50` status `ready` deltaP `20.2994` edge `0.2551` maxDD `-3.7082`
- `news_risk_high->crypto_alt_4h` score `3.8978` n `50` status `ready` deltaP `25.3171` edge `0.2996` maxDD `-9.4848`
- `news_risk_high->commodity_4h` score `3.8175` n `50` status `ready` deltaP `35.2012` edge `0.1088` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.4588` n `50` status `ready` deltaP `23.5793` edge `0.0827` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2688` n `50` status `ready` deltaP `25.5928` edge `0.0439` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.2771` n `50` status `ready` deltaP `16.8982` edge `0.0239` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.9847` n `50` status `ready` deltaP `18.9028` edge `0.2175` maxDD `-7.3825`
- `news_risk_high->crypto_major_1h` score `0.8614` n `50` status `ready` deltaP `20.0419` edge `0.082` maxDD `-7.0808`
- `news_risk_high->crypto_alt_1h` score `0.8161` n `50` status `ready` deltaP `18.1916` edge `0.0813` maxDD `-6.1688`
- `news_risk_high->commodity_1h` score `0.3569` n `50` status `ready` deltaP `4.0958` edge `0.0359` maxDD `-0.3438`
- `market_context_high->crypto_alt_4h` score `-0.619` n `64` status `ready` deltaP `4.1921` edge `0.1737` maxDD `-17.1476`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
