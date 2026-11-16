# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T18:52:25.753322+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4370`

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

- `news_risk_high->equity_24h` score `53.5386` n `50` status `ready` deltaP `59.1572` edge `4.1378` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `20.8141` n `50` status `ready` deltaP `40.038` edge `2.5159` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `18.0435` n `30` status `ready` deltaP `13.2988` edge `1.5694` maxDD `-8.6878`
- `news_risk_high->equity_4h` score `14.3252` n `50` status `ready` deltaP `43.7078` edge `1.0154` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `11.9497` n `30` status `ready` deltaP `42.038` edge `1.5788` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `9.9529` n `50` status `ready` deltaP `23.9655` edge `1.5668` maxDD `-29.0448`
- `news_risk_high->index_24h` score `8.0263` n `50` status `ready` deltaP `50.1762` edge `0.3647` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.2362` n `50` status `ready` deltaP `41.2781` edge `0.2445` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.2751` n `50` status `ready` deltaP `46.5784` edge `0.1667` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.9232` n `50` status `ready` deltaP `28.5784` edge `0.3633` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.5592` n `50` status `ready` deltaP `22.4262` edge `0.368` maxDD `-9.0062`
- `news_risk_high->equity_1h` score `4.49` n `50` status `ready` deltaP `22.1674` edge `0.2894` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `4.0398` n `50` status `ready` deltaP `36.7945` edge `0.1167` maxDD `-0.3611`
- `market_context_high->metal_24h` score `3.7934` n `30` status `ready` deltaP `46.9776` edge `0.2623` maxDD `-3.7989`
- `news_risk_high->index_4h` score `3.0578` n `50` status `ready` deltaP `28.5327` edge `0.0996` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2864` n `50` status `ready` deltaP `25.6622` edge `0.0449` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.4888` n `50` status `ready` deltaP `19.0643` edge `0.0271` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.9149` n `50` status `ready` deltaP `18.3109` edge `0.2125` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.8845` n `50` status `ready` deltaP `17.9611` edge `0.0916` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.816` n `50` status `ready` deltaP `19.2138` edge `0.0817` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
