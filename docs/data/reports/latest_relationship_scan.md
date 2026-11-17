# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T13:22:27.502381+00:00`
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

- `market_context_high->unknown_24h` score `1753.8879` n `88` status `ready` deltaP `3.4542` edge `146.1343` maxDD `0.0`
- `news_risk_high->equity_24h` score `58.8241` n `50` status `ready` deltaP `66.4111` edge `4.5299` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `17.266` n `50` status `ready` deltaP `29.6753` edge `2.1301` maxDD `-6.8139`
- `market_context_high->crypto_major_24h` score `14.4844` n `88` status `ready` deltaP `44.4026` edge `1.888` maxDD `-22.8301`
- `news_risk_high->equity_4h` score `14.2924` n `50` status `ready` deltaP `43.7927` edge `1.0121` maxDD `-7.0416`
- `market_context_high->crypto_alt_24h` score `13.5977` n `88` status `ready` deltaP `28.8389` edge `1.7634` maxDD `-13.3222`
- `news_risk_high->index_24h` score `9.1395` n `50` status `ready` deltaP `57.7755` edge `0.4068` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `8.9883` n `50` status `ready` deltaP `52.1589` edge `0.4013` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `8.1911` n `50` status `ready` deltaP `16.0207` edge `1.3939` maxDD `-29.0448`
- `news_risk_high->metal_4h` score `4.9442` n `50` status `ready` deltaP `43.9268` edge `0.1568` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `4.4566` n `50` status `ready` deltaP `22.5449` edge `0.2841` maxDD `-3.7082`
- `news_risk_high->crypto_alt_4h` score `4.4042` n `50` status `ready` deltaP `26.2317` edge `0.3357` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `3.7484` n `50` status `ready` deltaP `19.9268` edge `0.3171` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `3.6682` n `50` status `ready` deltaP `33.8293` edge `0.1055` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.1078` n `50` status `ready` deltaP `29.0671` edge `0.1002` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.1527` n `50` status `ready` deltaP `24.2455` edge `0.0432` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.4688` n `50` status `ready` deltaP `18.8443` edge `0.0269` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.9193` n `50` status `ready` deltaP `19.8653` edge `0.2027` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.7126` n `50` status `ready` deltaP `16.2455` edge `0.081` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.6557` n `50` status `ready` deltaP `18.0958` edge `0.0686` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
