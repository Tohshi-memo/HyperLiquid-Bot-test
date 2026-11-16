# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T05:52:25.880661+00:00`
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

- `news_risk_high->equity_24h` score `48.6137` n `50` status `ready` deltaP `51.7153` edge `3.777` maxDD `-3.6503`
- `market_context_high->unknown_4h` score `35.9581` n `64` status `ready` deltaP `1.9436` edge `3.0006` maxDD `-0.3637`
- `news_risk_high->crypto_major_24h` score `21.1582` n `50` status `ready` deltaP `40.6389` edge `2.556` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `11.8494` n `50` status `ready` deltaP `37.3902` edge `0.8512` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `9.2315` n `50` status `ready` deltaP `21.7778` edge `1.4889` maxDD `-29.0448`
- `news_risk_high->index_24h` score `7.028` n `50` status `ready` deltaP `43.3819` edge `0.3268` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.159` n `50` status `ready` deltaP `40.9722` edge `0.2401` maxDD `0.0`
- `news_risk_high->metal_4h` score `4.9806` n `50` status `ready` deltaP `44.2317` edge `0.1578` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.144` n `50` status `ready` deltaP `20.5366` edge `0.346` maxDD `-9.0062`
- `news_risk_high->equity_1h` score `3.9253` n `50` status `ready` deltaP `20.2994` edge `0.2548` maxDD `-3.7082`
- `news_risk_high->crypto_alt_4h` score `3.876` n `50` status `ready` deltaP `25.1646` edge `0.2988` maxDD `-9.4848`
- `news_risk_high->commodity_4h` score `3.7969` n `50` status `ready` deltaP `35.0488` edge `0.1081` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.4576` n `50` status `ready` deltaP `23.5793` edge `0.0826` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.27` n `50` status `ready` deltaP `25.5928` edge `0.044` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.2759` n `50` status `ready` deltaP `16.8982` edge `0.0238` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.9847` n `50` status `ready` deltaP `18.9028` edge `0.2175` maxDD `-7.3825`
- `news_risk_high->crypto_major_1h` score `0.8591` n `50` status `ready` deltaP `20.0419` edge `0.0817` maxDD `-7.0808`
- `news_risk_high->crypto_alt_1h` score `0.8161` n `50` status `ready` deltaP `18.1916` edge `0.0813` maxDD `-6.1688`
- `news_risk_high->commodity_1h` score `0.3401` n `50` status `ready` deltaP `3.9461` edge `0.0355` maxDD `-0.3438`
- `market_context_high->crypto_alt_4h` score `-0.4857` n `64` status `ready` deltaP `5.6021` edge `0.1814` maxDD `-17.1476`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
