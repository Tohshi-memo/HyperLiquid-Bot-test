# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T22:22:24.610059+00:00`
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

- `market_context_high->unknown_24h` score `784.0305` n `49` status `ready` deltaP `3.9861` edge `65.3093` maxDD `0.0`
- `news_risk_high->equity_24h` score `46.4733` n `50` status `ready` deltaP `50.565` edge `3.6063` maxDD `-3.6503`
- `market_context_high->equity_24h` score `39.9117` n `49` status `ready` deltaP `42.1568` edge `3.1991` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `34.4047` n `49` status `ready` deltaP `60.2766` edge `2.5729` maxDD `-6.2814`
- `market_context_high->unknown_4h` score `22.4239` n `69` status `ready` deltaP `8.9939` edge `1.8087` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `22.3431` n `50` status `ready` deltaP `44.1352` edge `2.6846` maxDD `-6.8139`
- `market_context_high->crypto_major_24h` score `14.5292` n `49` status `ready` deltaP `18.7883` edge `1.5429` maxDD `-31.9242`
- `news_risk_high->equity_4h` score `11.7022` n `50` status `ready` deltaP `36.7805` edge `0.843` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `9.2921` n `50` status `ready` deltaP `20.6031` edge `1.5045` maxDD `-29.0448`
- `market_context_high->index_24h` score `7.9185` n `49` status `ready` deltaP `48.1237` edge `0.3477` maxDD `-0.0251`
- `news_risk_high->index_24h` score `6.7067` n `50` status `ready` deltaP `42.2461` edge `0.3076` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.3076` n `50` status `ready` deltaP `41.0745` edge `0.2518` maxDD `0.0`
- `market_context_high->metal_24h` score `5.9725` n `49` status `ready` deltaP `60.3544` edge `0.4525` maxDD `-3.7989`
- `news_risk_high->metal_4h` score `4.8746` n `50` status `ready` deltaP `43.9268` edge `0.151` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.4636` n `50` status `ready` deltaP `20.8415` edge `0.3706` maxDD `-9.0062`
- `news_risk_high->crypto_alt_4h` score `4.0108` n `50` status `ready` deltaP `25.4695` edge `0.308` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `3.8065` n `50` status `ready` deltaP `20.1497` edge `0.2459` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.6198` n `50` status `ready` deltaP `33.5244` edge `0.1035` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.3994` n `50` status `ready` deltaP `23.122` edge `0.0808` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.1418` n `50` status `ready` deltaP `24.5449` edge `0.0403` maxDD `-0.3692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
