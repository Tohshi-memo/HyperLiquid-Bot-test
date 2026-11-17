# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T14:22:33.617198+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3868`

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

- `market_context_high->unknown_24h` score `1667.9804` n `91` status `ready` deltaP `3.4602` edge `138.9753` maxDD `0.0`
- `news_risk_high->equity_24h` score `59.2233` n `50` status `ready` deltaP `67.0657` edge `4.5588` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `17.1086` n `50` status `ready` deltaP `29.1073` edge `2.1137` maxDD `-6.8139`
- `market_context_high->crypto_major_24h` score `14.8401` n `91` status `ready` deltaP `44.7337` edge `1.9314` maxDD `-22.8301`
- `news_risk_high->equity_4h` score `14.0804` n `50` status `ready` deltaP `43.1829` edge `0.9985` maxDD `-7.0416`
- `market_context_high->crypto_alt_24h` score `13.9761` n `91` status `ready` deltaP `29.6951` edge `1.8062` maxDD `-13.3222`
- `news_risk_high->index_24h` score `9.2254` n `50` status `ready` deltaP `58.4152` edge `0.4097` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `9.1259` n `50` status `ready` deltaP `52.7682` edge `0.4087` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `8.0875` n `50` status `ready` deltaP `15.4533` edge `1.3844` maxDD `-29.0448`
- `news_risk_high->metal_4h` score `4.8982` n `50` status `ready` deltaP `43.622` edge `0.155` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `4.441` n `50` status `ready` deltaP `22.5449` edge `0.2828` maxDD `-3.7082`
- `news_risk_high->crypto_alt_4h` score `4.1982` n `50` status `ready` deltaP `25.622` edge `0.3226` maxDD `-9.4848`
- `news_risk_high->commodity_4h` score `3.6414` n `50` status `ready` deltaP `33.5244` edge `0.1053` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `3.4488` n `50` status `ready` deltaP `19.3171` edge `0.2962` maxDD `-9.0062`
- `news_risk_high->index_4h` score `3.0458` n `50` status `ready` deltaP `28.4573` edge `0.0991` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.1587` n `50` status `ready` deltaP `24.2455` edge `0.0437` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.47` n `50` status `ready` deltaP `18.8443` edge `0.027` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.9755` n `50` status `ready` deltaP `20.526` edge `0.2055` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.7383` n `50` status `ready` deltaP `16.5449` edge `0.0823` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.6448` n `50` status `ready` deltaP `17.9461` edge `0.0682` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
