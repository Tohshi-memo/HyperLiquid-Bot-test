# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T07:37:32.158105+00:00`
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

- `market_context_high->unknown_24h` score `2380.4699` n `69` status `ready` deltaP `3.4483` edge `198.3495` maxDD `0.0`
- `news_risk_high->equity_24h` score `56.5431` n `50` status `ready` deltaP `62.4828` edge `4.366` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `18.4049` n `50` status `ready` deltaP `33.5172` edge `2.2505` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `14.5802` n `50` status `ready` deltaP `44.5549` edge `1.031` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `13.5137` n `69` status `ready` deltaP `40.7346` edge `1.788` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `12.1667` n `69` status `ready` deltaP `20.7896` edge `1.6336` maxDD `-13.3222`
- `news_risk_high->crypto_alt_24h` score `9.0086` n `50` status `ready` deltaP `19.8621` edge `1.4731` maxDD `-29.0448`
- `news_risk_high->index_24h` score `8.614` n `50` status `ready` deltaP `53.8621` edge `0.3891` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `8.0501` n `50` status `ready` deltaP `48.2759` edge `0.349` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.0604` n `50` status `ready` deltaP `44.689` edge `0.1614` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `4.622` n `50` status `ready` deltaP `23.2934` edge `0.2929` maxDD `-3.7082`
- `news_risk_high->crypto_alt_4h` score `4.4636` n `50` status `ready` deltaP `26.689` edge `0.3376` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.069` n `50` status `ready` deltaP `20.9939` edge `0.3367` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `4.0501` n `50` status `ready` deltaP `36.878` edge `0.117` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.2415` n `50` status `ready` deltaP `30.439` edge `0.1022` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2198` n `50` status `ready` deltaP `24.8443` edge `0.0448` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.5622` n `50` status `ready` deltaP `19.8922` edge `0.0277` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.7835` n `50` status `ready` deltaP `16.6946` edge `0.0871` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.7453` n `50` status `ready` deltaP `18.5449` edge `0.0771` maxDD `-7.0808`
- `news_risk_high->metal_24h` score `0.7221` n `50` status `ready` deltaP `17.4828` edge `0.1933` maxDD `-7.3825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
