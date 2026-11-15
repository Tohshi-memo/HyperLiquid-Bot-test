# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T22:52:23.849046+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8592`

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

- `market_context_high->unknown_24h` score `830.8905` n `47` status `ready` deltaP `3.9861` edge `69.2143` maxDD `0.0`
- `news_risk_high->equity_24h` score `46.6053` n `50` status `ready` deltaP `50.565` edge `3.6173` maxDD `-3.6503`
- `market_context_high->equity_24h` score `39.247` n `47` status `ready` deltaP `41.2884` edge `3.1495` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `34.0827` n `47` status `ready` deltaP `59.5818` edge `2.5507` maxDD `-6.2814`
- `market_context_high->unknown_4h` score `30.1531` n `67` status `ready` deltaP `8.9939` edge `2.4528` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `22.1573` n `50` status `ready` deltaP `43.7886` edge `2.6631` maxDD `-6.8139`
- `market_context_high->crypto_major_24h` score `14.9335` n `47` status `ready` deltaP `19.8312` edge `1.5577` maxDD `-30.9696`
- `news_risk_high->equity_4h` score `11.6732` n `50` status `ready` deltaP `36.628` edge `0.8416` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `9.2235` n `50` status `ready` deltaP `20.6031` edge `1.4957` maxDD `-29.0448`
- `market_context_high->index_24h` score `7.8017` n `47` status `ready` deltaP `47.8631` edge `0.3397` maxDD `-0.0251`
- `news_risk_high->index_24h` score `6.7271` n `50` status `ready` deltaP `42.2461` edge `0.3093` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.2932` n `50` status `ready` deltaP `41.0745` edge `0.2506` maxDD `0.0`
- `market_context_high->metal_24h` score `5.7573` n `47` status `ready` deltaP `59.486` edge `0.4307` maxDD `-3.7989`
- `news_risk_high->metal_4h` score `4.8902` n `50` status `ready` deltaP `43.9268` edge `0.1523` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.3516` n `50` status `ready` deltaP `20.5366` edge `0.3633` maxDD `-9.0062`
- `news_risk_high->crypto_alt_4h` score `3.959` n `50` status `ready` deltaP `25.3171` edge `0.3047` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `3.7586` n `50` status `ready` deltaP `19.8503` edge `0.2439` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.6186` n `50` status `ready` deltaP `33.5244` edge `0.1034` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.4018` n `50` status `ready` deltaP `23.122` edge `0.081` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.1143` n `50` status `ready` deltaP `24.2455` edge `0.04` maxDD `-0.3692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
