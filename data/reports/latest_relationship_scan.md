# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T19:07:28.149730+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4374`

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

- `news_risk_high->equity_24h` score `53.5494` n `50` status `ready` deltaP `59.1572` edge `4.1387` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `20.7576` n `50` status `ready` deltaP `39.8653` edge `2.5098` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `17.9841` n `30` status `ready` deltaP `13.126` edge `1.5656` maxDD `-8.6878`
- `news_risk_high->equity_4h` score `14.33` n `50` status `ready` deltaP `43.7078` edge `1.0158` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `11.8931` n `30` status `ready` deltaP `41.8653` edge `1.5727` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `9.9143` n `50` status `ready` deltaP `23.7927` edge `1.563` maxDD `-29.0448`
- `news_risk_high->index_24h` score `8.0275` n `50` status `ready` deltaP `50.1762` edge `0.3648` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.253` n `50` status `ready` deltaP `41.2781` edge `0.2459` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.2945` n `50` status `ready` deltaP `46.7306` edge `0.1673` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.8978` n `50` status `ready` deltaP `28.4262` edge `0.3622` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.552` n `50` status `ready` deltaP `22.4262` edge `0.3674` maxDD `-9.0062`
- `news_risk_high->equity_1h` score `4.4732` n `50` status `ready` deltaP `22.0179` edge `0.289` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `4.0434` n `50` status `ready` deltaP `36.7945` edge `0.117` maxDD `-0.3611`
- `market_context_high->metal_24h` score `3.7903` n `30` status `ready` deltaP `46.9776` edge `0.2619` maxDD `-3.7989`
- `news_risk_high->index_4h` score `3.0712` n `50` status `ready` deltaP `28.6849` edge `0.0997` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2864` n `50` status `ready` deltaP `25.6622` edge `0.0449` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.5008` n `50` status `ready` deltaP `19.2138` edge `0.0271` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.9118` n `50` status `ready` deltaP `18.3109` edge `0.2121` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.8829` n `50` status `ready` deltaP `17.9611` edge `0.0914` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.8059` n `50` status `ready` deltaP `19.0643` edge `0.0814` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
