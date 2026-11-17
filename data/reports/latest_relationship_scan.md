# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T11:37:26.178181+00:00`
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

- `market_context_high->unknown_24h` score `1875.8763` n `84` status `ready` deltaP `3.4542` edge `156.3` maxDD `0.0`
- `news_risk_high->equity_24h` score `58.2306` n `50` status `ready` deltaP `65.2021` edge `4.4885` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `17.637` n `50` status `ready` deltaP `30.8843` edge `2.1696` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `14.5718` n `50` status `ready` deltaP `44.5549` edge `1.0303` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `14.2005` n `84` status `ready` deltaP `44.3129` edge `1.8522` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `13.1777` n `84` status `ready` deltaP `27.9916` edge `1.7152` maxDD `-13.3222`
- `news_risk_high->index_24h` score `8.9911` n `50` status `ready` deltaP `56.5665` edge `0.4025` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `8.6984` n `50` status `ready` deltaP `50.9499` edge `0.3852` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `8.4927` n `50` status `ready` deltaP `17.2297` edge `1.4245` maxDD `-29.0448`
- `news_risk_high->metal_4h` score `5.0328` n `50` status `ready` deltaP `44.689` edge `0.1591` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `4.6292` n `50` status `ready` deltaP `23.2934` edge `0.2935` maxDD `-3.7082`
- `news_risk_high->crypto_alt_4h` score `4.4694` n `50` status `ready` deltaP `26.5366` edge `0.3391` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `3.9944` n `50` status `ready` deltaP `20.8415` edge `0.3315` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `3.7979` n `50` status `ready` deltaP `34.8963` edge `0.1092` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.1856` n `50` status `ready` deltaP `29.8293` edge `0.1016` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.1706` n `50` status `ready` deltaP `24.3952` edge `0.0437` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.5107` n `50` status `ready` deltaP `19.2934` edge `0.0274` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.8151` n `50` status `ready` deltaP `18.6563` edge `0.1974` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.7687` n `50` status `ready` deltaP `16.5449` edge `0.0862` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.7274` n `50` status `ready` deltaP `18.5449` edge `0.0748` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
