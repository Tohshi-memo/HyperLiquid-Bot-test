# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T03:07:28.781660+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8696`

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

- `market_context_high->unknown_24h` score `1349.9457` n `30` status `ready` deltaP `3.9861` edge `112.4689` maxDD `0.0`
- `news_risk_high->equity_24h` score `47.7753` n `50` status `ready` deltaP `50.565` edge `3.7148` maxDD `-3.6503`
- `market_context_high->unknown_4h` score `40.9869` n `64` status `ready` deltaP `6.1738` edge `3.383` maxDD `-0.02`
- `market_context_high->crypto_alt_24h` score `29.0007` n `30` status `ready` deltaP `49.9364` edge `2.1915` maxDD `-6.2814`
- `market_context_high->equity_24h` score `28.0837` n `30` status `ready` deltaP `29.2317` edge `2.2996` maxDD `-9.0005`
- `news_risk_high->crypto_major_24h` score `21.3239` n `50` status `ready` deltaP `42.0555` edge `2.5678` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `11.913` n `50` status `ready` deltaP `37.3902` edge `0.8565` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `10.4743` n `30` status `ready` deltaP `14.0555` edge `1.1666` maxDD `-27.3292`
- `news_risk_high->crypto_alt_24h` score `9.0643` n `50` status `ready` deltaP `20.6031` edge `1.4753` maxDD `-29.0448`
- `news_risk_high->index_24h` score `6.8651` n `50` status `ready` deltaP `42.2461` edge `0.3208` maxDD `-0.4279`
- `market_context_high->index_24h` score `6.4191` n `30` status `ready` deltaP `44.2461` edge `0.2486` maxDD `-0.0251`
- `news_risk_high->commodity_24h` score `6.262` n `50` status `ready` deltaP `41.0745` edge `0.248` maxDD `0.0`
- `news_risk_high->metal_4h` score `4.9868` n `50` status `ready` deltaP `44.3841` edge `0.1573` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.3664` n `50` status `ready` deltaP `20.8415` edge `0.3625` maxDD `-9.0062`
- `news_risk_high->crypto_alt_4h` score `4.1564` n `50` status `ready` deltaP `25.7744` edge `0.3181` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `3.9133` n `50` status `ready` deltaP `20.2994` edge `0.2538` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.8983` n `50` status `ready` deltaP `35.5061` edge `0.1135` maxDD `-0.3611`
- `market_context_high->metal_24h` score `3.6819` n `30` status `ready` deltaP `47.4293` edge `0.245` maxDD `-3.7989`
- `news_risk_high->index_4h` score `2.4588` n `50` status `ready` deltaP `23.5793` edge `0.0827` maxDD `-0.7999`
- `market_context_high->fx_24h` score `2.3885` n `30` status `ready` deltaP `39.896` edge `0.0814` maxDD `-0.292`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
