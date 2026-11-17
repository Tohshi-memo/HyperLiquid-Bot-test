# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T13:52:25.339662+00:00`
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

- `market_context_high->unknown_24h` score `1723.4648` n `89` status `ready` deltaP `3.4602` edge `143.599` maxDD `0.0`
- `news_risk_high->equity_24h` score `59.0132` n `50` status `ready` deltaP `66.7197` edge `4.5436` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `17.2155` n `50` status `ready` deltaP `29.4533` edge `2.1251` maxDD `-6.8139`
- `market_context_high->crypto_major_24h` score `14.6097` n `89` status `ready` deltaP `44.487` edge `1.9035` maxDD `-22.8301`
- `news_risk_high->equity_4h` score `14.1864` n `50` status `ready` deltaP `43.4878` edge `1.0053` maxDD `-7.0416`
- `market_context_high->crypto_alt_24h` score `13.7425` n `89` status `ready` deltaP `29.1027` edge `1.7802` maxDD `-13.3222`
- `news_risk_high->index_24h` score `9.1798` n `50` status `ready` deltaP `58.0692` edge `0.4082` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `9.0502` n `50` status `ready` deltaP `52.4221` edge `0.4047` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `8.1664` n `50` status `ready` deltaP `15.7993` edge `1.3922` maxDD `-29.0448`
- `news_risk_high->metal_4h` score `4.9382` n `50` status `ready` deltaP `43.9268` edge `0.1563` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `4.4578` n `50` status `ready` deltaP `22.5449` edge `0.2842` maxDD `-3.7082`
- `news_risk_high->crypto_alt_4h` score `4.3066` n `50` status `ready` deltaP `25.9268` edge `0.3296` maxDD `-9.4848`
- `news_risk_high->commodity_4h` score `3.6366` n `50` status `ready` deltaP `33.5244` edge `0.1049` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `3.604` n `50` status `ready` deltaP `19.622` edge `0.3071` maxDD `-9.0062`
- `news_risk_high->index_4h` score `3.0774` n `50` status `ready` deltaP `28.7622` edge `0.0997` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.1706` n `50` status `ready` deltaP `24.3952` edge `0.0437` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.47` n `50` status `ready` deltaP `18.8443` edge `0.027` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.9481` n `50` status `ready` deltaP `20.1799` edge `0.2043` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.7352` n `50` status `ready` deltaP `16.5449` edge `0.0819` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.6541` n `50` status `ready` deltaP `18.0958` edge `0.0684` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
