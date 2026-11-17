# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T07:22:28.099791+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4116`

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

- `market_context_high->unknown_24h` score `2392.1075` n `68` status `ready` deltaP `3.4483` edge `199.3193` maxDD `0.0`
- `news_risk_high->equity_24h` score `56.4477` n `50` status `ready` deltaP `62.3103` edge `4.3592` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `18.4576` n `50` status `ready` deltaP `33.6897` edge `2.2561` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `14.5452` n `50` status `ready` deltaP `44.4024` edge `1.0291` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `13.4578` n `68` status `ready` deltaP `40.3956` edge `1.7831` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `12.0688` n `68` status `ready` deltaP `20.1521` edge `1.6253` maxDD `-13.3222`
- `news_risk_high->crypto_alt_24h` score `9.0402` n `50` status `ready` deltaP `20.0345` edge `1.476` maxDD `-29.0448`
- `news_risk_high->index_24h` score `8.5918` n `50` status `ready` deltaP `53.6897` edge `0.3884` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `8.0111` n `50` status `ready` deltaP `48.1034` edge `0.3469` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.0652` n `50` status `ready` deltaP `44.689` edge `0.1618` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `4.6472` n `50` status `ready` deltaP `23.4431` edge `0.294` maxDD `-3.7082`
- `news_risk_high->crypto_alt_4h` score `4.4624` n `50` status `ready` deltaP `26.689` edge `0.3375` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.0774` n `50` status `ready` deltaP `20.9939` edge `0.3374` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `4.0743` n `50` status `ready` deltaP `37.0305` edge `0.118` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.2391` n `50` status `ready` deltaP `30.439` edge `0.102` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.221` n `50` status `ready` deltaP `24.8443` edge `0.0449` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.5754` n `50` status `ready` deltaP `20.0419` edge `0.0278` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.7991` n `50` status `ready` deltaP `16.8443` edge `0.0881` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.7633` n `50` status `ready` deltaP `18.6946` edge `0.0784` maxDD `-7.0808`
- `news_risk_high->metal_24h` score `0.7236` n `50` status `ready` deltaP `17.4828` edge `0.1935` maxDD `-7.3825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
