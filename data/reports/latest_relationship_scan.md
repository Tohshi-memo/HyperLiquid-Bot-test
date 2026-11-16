# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T17:07:28.853865+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4244`

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

- `news_risk_high->equity_24h` score `53.4038` n `50` status `ready` deltaP `59.1073` edge `4.1269` maxDD `-3.6503`
- `market_context_high->unknown_24h` score `21.5259` n `30` status `ready` deltaP `3.9792` edge `1.7673` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `21.2772` n `50` status `ready` deltaP `41.218` edge `2.5674` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `18.5528` n `30` status `ready` deltaP `14.4752` edge `1.604` maxDD `-8.6878`
- `news_risk_high->equity_4h` score `14.1698` n `50` status `ready` deltaP `43.2511` edge `1.0055` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `12.4127` n `30` status `ready` deltaP `43.218` edge `1.6303` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `10.2839` n `50` status `ready` deltaP `25.1419` edge `1.6014` maxDD `-29.0448`
- `news_risk_high->index_24h` score `8.0067` n `50` status `ready` deltaP `50.1107` edge `0.3635` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.1273` n `50` status `ready` deltaP `41.1765` edge `0.2361` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.1528` n `50` status `ready` deltaP `45.6651` edge `0.1626` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `5.0751` n `50` status `ready` deltaP `29.1872` edge `0.3719` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.6967` n `50` status `ready` deltaP `23.035` edge `0.3754` maxDD `-9.0062`
- `news_risk_high->equity_1h` score `4.4135` n `50` status `ready` deltaP `21.7964` edge `0.2855` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `4.029` n `50` status `ready` deltaP `36.7945` edge `0.1158` maxDD `-0.3611`
- `market_context_high->metal_24h` score `3.815` n `30` status `ready` deltaP `46.9435` edge `0.2653` maxDD `-3.7989`
- `news_risk_high->index_4h` score `2.9656` n `50` status `ready` deltaP `27.6195` edge `0.098` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.306` n `50` status `ready` deltaP `25.8922` edge `0.045` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.4137` n `50` status `ready` deltaP `18.2455` edge `0.0263` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.9612` n `50` status `ready` deltaP `18.6407` edge `0.0969` maxDD `-6.1688`
- `news_risk_high->metal_24h` score `0.9365` n `50` status `ready` deltaP `18.2768` edge `0.2155` maxDD `-7.3825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
