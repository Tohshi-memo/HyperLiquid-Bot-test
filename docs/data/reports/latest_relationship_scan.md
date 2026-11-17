# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T08:52:32.037313+00:00`
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

- `market_context_high->unknown_24h` score `2212.9463` n `74` status `ready` deltaP `3.4483` edge `184.3892` maxDD `0.0`
- `news_risk_high->equity_24h` score `57.0584` n `50` status `ready` deltaP `63.3448` edge `4.4032` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `18.1269` n `50` status `ready` deltaP `32.6552` edge `2.2206` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `14.6307` n `50` status `ready` deltaP `44.7073` edge `1.0342` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `13.8882` n `74` status `ready` deltaP `42.2228` edge `1.8261` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `12.6726` n `74` status `ready` deltaP `23.6486` edge `1.6794` maxDD `-13.3222`
- `news_risk_high->crypto_alt_24h` score `8.8211` n `50` status `ready` deltaP `19.0` edge `1.4548` maxDD `-29.0448`
- `news_risk_high->index_24h` score `8.7345` n `50` status `ready` deltaP `54.7241` edge `0.3934` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `8.2606` n `50` status `ready` deltaP `49.1379` edge `0.3608` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.0412` n `50` status `ready` deltaP `44.689` edge `0.1598` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `4.6065` n `50` status `ready` deltaP `23.1437` edge `0.2926` maxDD `-3.7082`
- `news_risk_high->crypto_alt_4h` score `4.4516` n `50` status `ready` deltaP `26.689` edge `0.3366` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.0342` n `50` status `ready` deltaP `20.9939` edge `0.3338` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `3.9495` n `50` status `ready` deltaP `36.1159` edge `0.1137` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.2159` n `50` status `ready` deltaP `30.1341` edge `0.1021` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2042` n `50` status `ready` deltaP `24.6946` edge `0.0445` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.5371` n `50` status `ready` deltaP `19.5928` edge `0.0276` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.8085` n `50` status `ready` deltaP `16.994` edge `0.0883` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.7843` n `50` status `ready` deltaP `18.994` edge `0.0791` maxDD `-7.0808`
- `news_risk_high->metal_24h` score `0.7115` n `50` status `ready` deltaP `17.3103` edge `0.1931` maxDD `-7.3825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
