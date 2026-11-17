# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T11:07:44.644763+00:00`
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

- `market_context_high->unknown_24h` score `1903.1759` n `83` status `ready` deltaP `3.4483` edge `158.575` maxDD `0.0`
- `news_risk_high->equity_24h` score `58.0838` n `50` status `ready` deltaP `64.8966` edge `4.4783` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `17.7073` n `50` status `ready` deltaP `31.2759` edge `2.176` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `14.6655` n `50` status `ready` deltaP `44.7073` edge `1.0371` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `14.0834` n `83` status `ready` deltaP `43.1554` edge `1.8449` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `13.0181` n `83` status `ready` deltaP `26.6327` edge `1.7038` maxDD `-13.3222`
- `news_risk_high->index_24h` score `8.9547` n `50` status `ready` deltaP `56.2759` edge `0.4014` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `8.6248` n `50` status `ready` deltaP `50.6897` edge `0.3808` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `8.5465` n `50` status `ready` deltaP `17.6207` edge `1.4288` maxDD `-29.0448`
- `news_risk_high->metal_4h` score `5.0364` n `50` status `ready` deltaP `44.689` edge `0.1594` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `4.7108` n `50` status `ready` deltaP `23.5928` edge `0.2983` maxDD `-3.7082`
- `news_risk_high->crypto_alt_4h` score `4.5008` n `50` status `ready` deltaP `26.689` edge `0.3407` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.039` n `50` status `ready` deltaP `20.9939` edge `0.3342` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `3.8331` n `50` status `ready` deltaP `35.2012` edge `0.1101` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.2171` n `50` status `ready` deltaP `30.1341` edge `0.1022` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.1994` n `50` status `ready` deltaP `24.6946` edge `0.0441` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.5407` n `50` status `ready` deltaP `19.5928` edge `0.0279` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.8139` n `50` status `ready` deltaP `16.8443` edge `0.09` maxDD `-6.1688`
- `news_risk_high->metal_24h` score `0.7879` n `50` status `ready` deltaP `18.3448` edge `0.196` maxDD `-7.3825`
- `news_risk_high->crypto_major_1h` score `0.7796` n `50` status `ready` deltaP `18.994` edge `0.0785` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
