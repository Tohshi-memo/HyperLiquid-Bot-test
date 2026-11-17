# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T11:22:28.188777+00:00`
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

- `market_context_high->unknown_24h` score `1901.9859` n `83` status `ready` deltaP `3.4542` edge `158.4758` maxDD `0.0`
- `news_risk_high->equity_24h` score `58.146` n `50` status `ready` deltaP `65.0294` edge `4.4826` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `17.6865` n `50` status `ready` deltaP `31.057` edge `2.1748` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `14.6319` n `50` status `ready` deltaP `44.7073` edge `1.0343` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `14.151` n `83` status `ready` deltaP `44.1413` edge `1.847` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `13.0889` n `83` status `ready` deltaP `27.6193` edge `1.7063` maxDD `-13.3222`
- `news_risk_high->index_24h` score `8.9689` n `50` status `ready` deltaP `56.3938` edge `0.4018` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `8.6498` n `50` status `ready` deltaP `50.7772` edge `0.3823` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `8.5344` n `50` status `ready` deltaP `17.4024` edge `1.4287` maxDD `-29.0448`
- `news_risk_high->metal_4h` score `5.0352` n `50` status `ready` deltaP `44.689` edge `0.1593` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `4.6796` n `50` status `ready` deltaP `23.4431` edge `0.2967` maxDD `-3.7082`
- `news_risk_high->crypto_alt_4h` score `4.4936` n `50` status `ready` deltaP `26.689` edge `0.3401` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.027` n `50` status `ready` deltaP `20.9939` edge `0.3332` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `3.8137` n `50` status `ready` deltaP `35.0488` edge `0.1095` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.2026` n `50` status `ready` deltaP `29.9817` edge `0.102` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.185` n `50` status `ready` deltaP `24.5449` edge `0.0439` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.5263` n `50` status `ready` deltaP `19.4431` edge `0.0277` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.8006` n `50` status `ready` deltaP `18.4836` edge `0.1967` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.7937` n `50` status `ready` deltaP `16.6946` edge `0.0884` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.7523` n `50` status `ready` deltaP `18.6946` edge `0.077` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
