# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T17:52:26.699992+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4248`

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

- `news_risk_high->equity_24h` score `53.459` n `50` status `ready` deltaP `59.1073` edge `4.1315` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `21.0661` n `50` status `ready` deltaP `40.699` edge `2.5438` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `18.3373` n `30` status `ready` deltaP `13.9561` edge `1.5895` maxDD `-8.6878`
- `news_risk_high->equity_4h` score `14.209` n `50` status `ready` deltaP `43.3354` edge `1.0082` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `12.2017` n `30` status `ready` deltaP `42.699` edge `1.6067` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `10.1438` n `50` status `ready` deltaP `24.6228` edge `1.5869` maxDD `-29.0448`
- `news_risk_high->index_24h` score `8.0127` n `50` status `ready` deltaP `50.1107` edge `0.364` maxDD `-0.4279`
- `market_context_high->unknown_24h` score `6.2955` n `30` status `ready` deltaP `3.9792` edge `0.4981` maxDD `0.0`
- `news_risk_high->commodity_24h` score `6.1525` n `50` status `ready` deltaP `41.1765` edge `0.2382` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.2001` n `50` status `ready` deltaP `46.061` edge `0.1639` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.9739` n `50` status `ready` deltaP `28.8232` edge `0.3659` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.5943` n `50` status `ready` deltaP `22.6707` edge `0.3693` maxDD `-9.0062`
- `news_risk_high->equity_1h` score `4.4483` n `50` status `ready` deltaP `21.9461` edge `0.2874` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `4.0163` n `50` status `ready` deltaP `36.7256` edge `0.1152` maxDD `-0.3611`
- `market_context_high->metal_24h` score `3.801` n `30` status `ready` deltaP `46.9435` edge `0.2635` maxDD `-3.7989`
- `news_risk_high->index_4h` score `3.002` n `50` status `ready` deltaP `28.0` edge `0.0985` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2736` n `50` status `ready` deltaP `25.5928` edge `0.0443` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.4424` n `50` status `ready` deltaP `18.5449` edge `0.0267` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.9225` n `50` status `ready` deltaP `18.2768` edge `0.2137` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.9058` n `50` status `ready` deltaP `18.1916` edge `0.0928` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
