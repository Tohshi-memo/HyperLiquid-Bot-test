# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T11:37:27.312224+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `9954`

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

- `market_context_high->unknown_24h` score `545.5002` n `65` status `ready` deltaP `3.2929` edge `45.4364` maxDD `0.0`
- `news_risk_high->equity_24h` score `44.4086` n `50` status `ready` deltaP `48.8319` edge `3.4458` maxDD `-3.6503`
- `market_context_high->equity_24h` score `38.9286` n `65` status `ready` deltaP `43.9088` edge `3.1055` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `31.756` n `65` status `ready` deltaP `59.1174` edge `2.3599` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `23.723` n `50` status `ready` deltaP `46.3882` edge `2.8465` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `12.3033` n `50` status `ready` deltaP `39.5244` edge `0.8748` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `8.3985` n `50` status `ready` deltaP `16.9636` edge `1.4142` maxDD `-29.0448`
- `market_context_high->index_24h` score `7.7214` n `65` status `ready` deltaP `46.3592` edge `0.3432` maxDD `-0.0383`
- `news_risk_high->commodity_24h` score `7.142` n `50` status `ready` deltaP `47.1404` edge `0.2809` maxDD `0.0`
- `news_risk_high->index_24h` score `6.3293` n `50` status `ready` deltaP `40.513` edge `0.2877` maxDD `-0.4279`
- `market_context_high->metal_24h` score `6.2849` n `65` status `ready` deltaP `59.3121` edge `0.4995` maxDD `-3.7989`
- `market_context_high->unknown_4h` score `5.8541` n `82` status `ready` deltaP `8.8415` edge `0.4289` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `5.4501` n `50` status `ready` deltaP `23.7378` edge `0.4335` maxDD `-9.0062`
- `news_risk_high->metal_4h` score `4.9951` n `50` status `ready` deltaP `45.2988` edge `0.1519` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.7738` n `50` status `ready` deltaP `28.061` edge `0.3543` maxDD `-9.4848`
- `market_context_high->crypto_major_24h` score `4.1084` n `65` status `ready` deltaP `13.0036` edge `1.2387` maxDD `-72.6417`
- `news_risk_high->equity_1h` score `4.0139` n `50` status `ready` deltaP `21.6467` edge `0.2532` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.5868` n `50` status `ready` deltaP `33.0671` edge `0.1038` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.7498` n `50` status `ready` deltaP `26.9329` edge `0.0846` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2855` n `50` status `ready` deltaP `26.1916` edge `0.0413` maxDD `-0.3692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
