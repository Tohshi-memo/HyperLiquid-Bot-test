# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T16:37:38.204761+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4206`

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

- `news_risk_high->equity_24h` score `53.3024` n `50` status `ready` deltaP `58.9343` edge `4.1196` maxDD `-3.6503`
- `market_context_high->unknown_24h` score `31.9431` n `30` status `ready` deltaP `3.9792` edge `2.6354` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `21.381` n `50` status `ready` deltaP `41.564` edge `2.5784` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `18.6393` n `30` status `ready` deltaP `14.8212` edge `1.6089` maxDD `-8.6878`
- `news_risk_high->equity_4h` score `14.1179` n `50` status `ready` deltaP `42.9467` edge `1.0032` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `12.5165` n `30` status `ready` deltaP `43.564` edge `1.6413` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `10.3401` n `50` status `ready` deltaP `25.4879` edge `1.6063` maxDD `-29.0448`
- `news_risk_high->index_24h` score `7.9856` n `50` status `ready` deltaP `49.9377` edge `0.3629` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.1177` n `50` status `ready` deltaP `41.1765` edge `0.2353` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `5.1678` n `50` status `ready` deltaP `29.4916` edge `0.3776` maxDD `-9.4848`
- `news_risk_high->metal_4h` score `5.1323` n `50` status `ready` deltaP `45.5129` edge `0.1619` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.7942` n `50` status `ready` deltaP `23.3394` edge `0.3815` maxDD `-9.0062`
- `news_risk_high->equity_1h` score `4.4051` n `50` status `ready` deltaP `21.7964` edge `0.2848` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `4.0036` n `50` status `ready` deltaP `36.6423` edge `0.1147` maxDD `-0.3611`
- `market_context_high->metal_24h` score `3.8197` n `30` status `ready` deltaP `46.9435` edge `0.2659` maxDD `-3.7989`
- `news_risk_high->index_4h` score `2.9388` n `50` status `ready` deltaP `27.3151` edge `0.0978` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.3072` n `50` status `ready` deltaP `25.8922` edge `0.0451` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.4005` n `50` status `ready` deltaP `18.0958` edge `0.0262` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.9923` n `50` status `ready` deltaP `18.9401` edge `0.0989` maxDD `-6.1688`
- `news_risk_high->metal_24h` score `0.9412` n `50` status `ready` deltaP `18.2768` edge `0.2161` maxDD `-7.3825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
