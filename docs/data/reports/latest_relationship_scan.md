# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T08:22:31.428672+00:00`
- Price records: `672`
- Market context records: `5436`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11450`

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

- `market_context_high->equity_24h` score `4.5615` n `185` status `ready` deltaP `11.8694` edge `0.6546` maxDD `-21.6219`
- `market_context_high->crypto_major_24h` score `4.1792` n `185` status `ready` deltaP `19.1536` edge `0.6746` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `3.785` n `196` status `ready` deltaP `16.7652` edge `0.4329` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `2.9832` n `196` status `ready` deltaP `12.1329` edge `0.3318` maxDD `-9.46`
- `market_context_high->equity_4h` score `2.8834` n `196` status `ready` deltaP `12.9666` edge `0.3177` maxDD `-7.4425`
- `market_context_high->equity_1h` score `0.5681` n `196` status `ready` deltaP `8.5299` edge `0.087` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.1701` n `196` status `ready` deltaP `6.9321` edge `0.0173` maxDD `-0.9472`
- `market_context_high->fx_24h` score `0.1535` n `185` status `ready` deltaP `10.1295` edge `0.0348` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `-0.1713` n `196` status `ready` deltaP `2.0072` edge `0.0685` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.2461` n `196` status `ready` deltaP `3.0215` edge `0.0839` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.3027` n `196` status `ready` deltaP `3.5989` edge `0.0183` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.5275` n `196` status `ready` deltaP `0.6935` edge `0.0003` maxDD `-0.577`
- `market_context_high->index_4h` score `-0.8137` n `196` status `ready` deltaP `7.3824` edge `0.0439` maxDD `-2.874`
- `market_context_high->index_24h` score `-1.0614` n `185` status `ready` deltaP `16.1627` edge `0.1024` maxDD `-12.5551`
- `market_context_high->fx_4h` score `-1.1758` n `196` status `ready` deltaP `0.2894` edge `0.0026` maxDD `-1.5345`
- `market_context_high->commodity_1h` score `-1.526` n `196` status `ready` deltaP `-3.7822` edge `-0.0075` maxDD `-3.5563`
- `market_context_high->metal_4h` score `-2.693` n `196` status `ready` deltaP `-8.5802` edge `-0.0356` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.4191` n `196` status `ready` deltaP `-8.1943` edge `-0.0498` maxDD `-14.1062`
- `market_context_high->crypto_alt_24h` score `-6.5045` n `185` status `ready` deltaP `9.8658` edge `0.2619` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.4143` n `185` status `ready` deltaP `-5.7742` edge `-0.1743` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
