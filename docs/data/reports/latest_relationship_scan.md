# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T04:22:35.386571+00:00`
- Price records: `672`
- Market context records: `5109`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10340`

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

- `market_context_high->unknown_24h` score `21.0503` n `75` status `ready` deltaP `28.2222` edge `1.6003` maxDD `-1.4072`
- `market_context_high->unknown_4h` score `8.2133` n `112` status `ready` deltaP `22.9747` edge `0.6335` maxDD `-5.5109`
- `market_context_high->unknown_1h` score `7.1399` n `124` status `ready` deltaP `5.3458` edge `0.6235` maxDD `-2.7986`
- `market_context_high->crypto_alt_4h` score `5.1348` n `112` status `ready` deltaP `14.8519` edge `0.4888` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `2.4787` n `112` status `ready` deltaP `13.2186` edge `0.4589` maxDD `-14.0065`
- `market_context_high->crypto_alt_1h` score `1.0471` n `124` status `ready` deltaP `7.2919` edge `0.1348` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.521` n `124` status `ready` deltaP `8.1659` edge `0.1369` maxDD `-6.9639`
- `market_context_high->equity_1h` score `0.5034` n `124` status `ready` deltaP `8.813` edge `0.0651` maxDD `-2.745`
- `market_context_high->metal_1h` score `0.3302` n `124` status `ready` deltaP `9.238` edge `0.0304` maxDD `-1.3057`
- `market_context_high->equity_4h` score `0.1566` n `112` status `ready` deltaP `6.1411` edge `0.143` maxDD `-7.4425`
- `market_context_high->index_1h` score `-0.0034` n `124` status `ready` deltaP `5.6452` edge `0.0123` maxDD `-1.0296`
- `market_context_high->metal_4h` score `-0.402` n `112` status `ready` deltaP `3.8981` edge `0.0635` maxDD `-4.6157`
- `market_context_high->index_4h` score `-0.5367` n `112` status `ready` deltaP `2.8092` edge `0.0242` maxDD `-2.9391`
- `market_context_high->fx_1h` score `-0.6985` n `124` status `ready` deltaP `-3.6991` edge `-0.0008` maxDD `-0.7944`
- `market_context_high->commodity_1h` score `-0.719` n `124` status `ready` deltaP `2.1538` edge `0.0015` maxDD `-2.062`
- `market_context_high->commodity_24h` score `-1.0128` n `75` status `ready` deltaP `10.3333` edge `0.0522` maxDD `-12.7413`
- `market_context_high->fx_4h` score `-1.0385` n `112` status `ready` deltaP `-3.8763` edge `0.0` maxDD `-1.9169`
- `market_context_high->fx_24h` score `-1.4894` n `75` status `ready` deltaP `-2.5834` edge `-0.008` maxDD `-1.5779`
- `market_context_high->commodity_4h` score `-2.1738` n `112` status `ready` deltaP `1.9817` edge `-0.0234` maxDD `-7.3435`
- `market_context_high->metal_24h` score `-3.9561` n `75` status `ready` deltaP `-5.1528` edge `0.0203` maxDD `-30.1178`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
