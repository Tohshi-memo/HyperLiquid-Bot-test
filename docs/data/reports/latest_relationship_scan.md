# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T04:37:31.583551+00:00`
- Price records: `672`
- Market context records: `5110`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10328`

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

- `market_context_high->unknown_24h` score `21.6527` n `74` status `ready` deltaP `28.2517` edge `1.6503` maxDD `-1.4072`
- `market_context_high->unknown_4h` score `8.2385` n `112` status `ready` deltaP `22.9747` edge `0.6356` maxDD `-5.5109`
- `market_context_high->unknown_1h` score `7.1663` n `124` status `ready` deltaP `5.3458` edge `0.6257` maxDD `-2.7986`
- `market_context_high->crypto_alt_4h` score `5.2476` n `112` status `ready` deltaP `14.8519` edge `0.4982` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `2.5208` n `112` status `ready` deltaP `13.2186` edge `0.4643` maxDD `-14.0065`
- `market_context_high->crypto_alt_1h` score `0.9478` n `124` status `ready` deltaP `6.6351` edge `0.1309` maxDD `-5.0257`
- `market_context_high->equity_1h` score `0.4956` n `124` status `ready` deltaP `8.813` edge `0.0641` maxDD `-2.745`
- `market_context_high->crypto_major_1h` score `0.4478` n `124` status `ready` deltaP `7.5092` edge `0.1319` maxDD `-6.9639`
- `market_context_high->metal_1h` score `0.2695` n `124` status `ready` deltaP `8.5812` edge `0.027` maxDD `-1.3057`
- `market_context_high->equity_4h` score `0.155` n `112` status `ready` deltaP `6.1411` edge `0.1428` maxDD `-7.4425`
- `market_context_high->index_1h` score `-0.005` n `124` status `ready` deltaP `5.6452` edge `0.0121` maxDD `-1.0296`
- `market_context_high->metal_4h` score `-0.4137` n `112` status `ready` deltaP `3.8981` edge `0.062` maxDD `-4.6157`
- `market_context_high->index_4h` score `-0.5375` n `112` status `ready` deltaP `2.8092` edge `0.0241` maxDD `-2.9391`
- `market_context_high->fx_1h` score `-0.6636` n `124` status `ready` deltaP `-3.0423` edge `-0.0007` maxDD `-0.7944`
- `market_context_high->commodity_1h` score `-0.7178` n `124` status `ready` deltaP `2.1538` edge `0.0016` maxDD `-2.062`
- `market_context_high->commodity_24h` score `-0.8529` n `74` status `ready` deltaP `11.036` edge `0.0576` maxDD `-12.2414`
- `market_context_high->fx_4h` score `-1.0353` n `112` status `ready` deltaP `-3.8763` edge `0.0004` maxDD `-1.9169`
- `market_context_high->fx_24h` score `-1.4439` n `74` status `ready` deltaP `-2.1444` edge `-0.0078` maxDD `-1.5252`
- `market_context_high->commodity_4h` score `-2.1786` n `112` status `ready` deltaP `1.9817` edge `-0.0238` maxDD `-7.3435`
- `market_context_high->metal_24h` score `-3.7941` n `74` status `ready` deltaP `-4.7204` edge `0.0251` maxDD `-29.4045`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
