# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T22:37:27.555510+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8336`

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

- `market_context_high->unknown_24h` score `807.4557` n `48` status `ready` deltaP `3.9861` edge `67.2614` maxDD `0.0`
- `news_risk_high->equity_24h` score `46.5357` n `50` status `ready` deltaP `50.565` edge `3.6115` maxDD `-3.6503`
- `market_context_high->equity_24h` score `39.6389` n `48` status `ready` deltaP `41.7317` edge `3.1792` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `34.3607` n `48` status `ready` deltaP `59.9364` edge `2.5715` maxDD `-6.2814`
- `market_context_high->unknown_4h` score `27.1855` n `68` status `ready` deltaP `8.9939` edge `2.2055` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `22.2428` n `50` status `ready` deltaP `43.9619` edge `2.6729` maxDD `-6.8139`
- `market_context_high->crypto_major_24h` score `14.923` n `48` status `ready` deltaP `19.2952` edge `1.5604` maxDD `-30.9696`
- `news_risk_high->equity_4h` score `11.6732` n `50` status `ready` deltaP `36.628` edge `0.8416` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `9.2492` n `50` status `ready` deltaP `20.6031` edge `1.499` maxDD `-29.0448`
- `market_context_high->index_24h` score `7.8675` n `48` status `ready` deltaP `47.9961` edge `0.3443` maxDD `-0.0251`
- `news_risk_high->index_24h` score `6.7175` n `50` status `ready` deltaP `42.2461` edge `0.3085` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.2992` n `50` status `ready` deltaP `41.0745` edge `0.2511` maxDD `0.0`
- `market_context_high->metal_24h` score `5.8717` n `48` status `ready` deltaP `59.9293` edge `0.4424` maxDD `-3.7989`
- `news_risk_high->metal_4h` score `4.8806` n `50` status `ready` deltaP `43.9268` edge `0.1515` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.3938` n `50` status `ready` deltaP `20.689` edge `0.3658` maxDD `-9.0062`
- `news_risk_high->crypto_alt_4h` score `3.965` n `50` status `ready` deltaP `25.3171` edge `0.3052` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `3.779` n `50` status `ready` deltaP `20.0` edge `0.2446` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.6174` n `50` status `ready` deltaP `33.5244` edge `0.1033` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.3994` n `50` status `ready` deltaP `23.122` edge `0.0808` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.1274` n `50` status `ready` deltaP `24.3952` edge `0.0401` maxDD `-0.3692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
