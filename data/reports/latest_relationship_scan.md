# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T05:07:26.820269+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4434`

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

- `market_context_high->unknown_24h` score `2073.9743` n `59` status `ready` deltaP `3.4483` edge `172.8082` maxDD `0.0`
- `news_risk_high->equity_24h` score `55.5855` n `50` status `ready` deltaP `60.7586` edge `4.2977` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `18.947` n `50` status `ready` deltaP `35.2414` edge `2.3085` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `16.4682` n `59` status `ready` deltaP `12.6622` edge `1.5003` maxDD `-13.3222`
- `news_risk_high->equity_4h` score `14.3496` n `50` status `ready` deltaP `43.4878` edge `1.0189` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `12.1619` n `59` status `ready` deltaP `36.5634` edge `1.6425` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `9.2212` n `50` status `ready` deltaP `21.069` edge `1.4923` maxDD `-29.0448`
- `news_risk_high->index_24h` score `8.3776` n `50` status `ready` deltaP `52.1379` edge `0.3809` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `7.6121` n `50` status `ready` deltaP `46.5517` edge `0.324` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.1853` n `50` status `ready` deltaP `45.7561` edge `0.1647` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.5324` n `50` status `ready` deltaP `26.9939` edge `0.3413` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `4.4926` n `50` status `ready` deltaP `22.5449` edge `0.2871` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `4.2489` n `50` status `ready` deltaP `21.9085` edge `0.3456` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `4.1433` n `50` status `ready` deltaP `37.4878` edge `0.1207` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.1334` n `50` status `ready` deltaP `29.372` edge `0.1003` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.1802` n `50` status `ready` deltaP `24.3952` edge `0.0445` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.5179` n `50` status `ready` deltaP `19.4431` edge `0.027` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.7965` n `50` status `ready` deltaP `18.3448` edge `0.1971` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.7368` n `50` status `ready` deltaP `16.3952` edge `0.0831` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.7009` n `50` status `ready` deltaP `18.2455` edge `0.0734` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
