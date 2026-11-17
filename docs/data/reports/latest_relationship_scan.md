# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T07:52:34.642169+00:00`
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

- `market_context_high->unknown_24h` score `2369.1671` n `70` status `ready` deltaP `3.4483` edge `197.4076` maxDD `0.0`
- `news_risk_high->equity_24h` score `56.6409` n `50` status `ready` deltaP `62.6552` edge `4.373` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `18.3554` n `50` status `ready` deltaP `33.3448` edge `2.2453` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `14.6079` n `50` status `ready` deltaP `44.7073` edge `1.0323` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `13.5844` n `70` status `ready` deltaP `41.0591` edge `1.7949` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `12.2743` n `70` status `ready` deltaP `21.404` edge `1.6433` maxDD `-13.3222`
- `news_risk_high->crypto_alt_24h` score `8.9802` n `50` status `ready` deltaP `19.6897` edge `1.4706` maxDD `-29.0448`
- `news_risk_high->index_24h` score `8.6374` n `50` status `ready` deltaP `54.0345` edge `0.3899` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `8.0915` n `50` status `ready` deltaP `48.4483` edge `0.3513` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.0556` n `50` status `ready` deltaP `44.689` edge `0.161` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `4.6017` n `50` status `ready` deltaP `23.1437` edge `0.2922` maxDD `-3.7082`
- `news_risk_high->crypto_alt_4h` score `4.4624` n `50` status `ready` deltaP `26.689` edge `0.3375` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.0642` n `50` status `ready` deltaP `20.9939` edge `0.3363` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `4.0271` n `50` status `ready` deltaP `36.7256` edge `0.1161` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.2415` n `50` status `ready` deltaP `30.439` edge `0.1022` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2054` n `50` status `ready` deltaP `24.6946` edge `0.0446` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.5491` n `50` status `ready` deltaP `19.7425` edge `0.0276` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.7843` n `50` status `ready` deltaP `16.6946` edge `0.0872` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.7453` n `50` status `ready` deltaP `18.5449` edge `0.0771` maxDD `-7.0808`
- `news_risk_high->metal_24h` score `0.7107` n `50` status `ready` deltaP `17.3103` edge `0.193` maxDD `-7.3825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
