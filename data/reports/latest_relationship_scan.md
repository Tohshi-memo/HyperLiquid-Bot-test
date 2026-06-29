# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T05:07:28.549791+00:00`
- Price records: `672`
- Market context records: `5113`
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

- `market_context_high->unknown_24h` score `21.7704` n `74` status `ready` deltaP `28.5989` edge `1.6578` maxDD `-1.4072`
- `market_context_high->unknown_4h` score `7.7748` n `114` status `ready` deltaP `21.9325` edge `0.6039` maxDD `-5.5109`
- `market_context_high->unknown_1h` score `7.5718` n `126` status `ready` deltaP `6.0498` edge `0.6548` maxDD `-2.7986`
- `market_context_high->crypto_alt_4h` score `5.2292` n `114` status `ready` deltaP `14.832` edge `0.4968` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `2.4878` n `114` status `ready` deltaP `13.2301` edge `0.46` maxDD `-14.0065`
- `market_context_high->crypto_alt_1h` score `0.7581` n `126` status `ready` deltaP `5.9144` edge `0.1199` maxDD `-5.0257`
- `market_context_high->equity_1h` score `0.4313` n `126` status `ready` deltaP `8.1908` edge `0.06` maxDD `-2.745`
- `market_context_high->crypto_major_1h` score `0.3164` n `126` status `ready` deltaP `6.8268` edge `0.1196` maxDD `-6.9639`
- `market_context_high->metal_1h` score `0.2234` n `126` status `ready` deltaP `8.0102` edge `0.0249` maxDD `-1.3057`
- `market_context_high->equity_4h` score `0.1573` n `114` status `ready` deltaP `6.2153` edge `0.1426` maxDD `-7.4425`
- `market_context_high->index_1h` score `-0.0423` n `126` status `ready` deltaP `5.0613` edge `0.0112` maxDD `-1.0296`
- `market_context_high->metal_4h` score `-0.4488` n `114` status `ready` deltaP `3.3884` edge `0.0609` maxDD `-4.6157`
- `market_context_high->index_4h` score `-0.5279` n `114` status `ready` deltaP `3.0086` edge `0.024` maxDD `-2.9391`
- `market_context_high->fx_1h` score `-0.6674` n `126` status `ready` deltaP `-3.1152` edge `-0.0007` maxDD `-0.7944`
- `market_context_high->commodity_1h` score `-0.7919` n `126` status `ready` deltaP `1.3473` edge `0.0008` maxDD `-2.062`
- `market_context_high->commodity_24h` score `-0.8568` n `74` status `ready` deltaP `11.036` edge `0.0571` maxDD `-12.2414`
- `market_context_high->fx_4h` score `-0.9866` n `114` status `ready` deltaP `-3.0889` edge `0.0014` maxDD `-1.9169`
- `market_context_high->fx_24h` score `-1.4753` n `74` status `ready` deltaP `-2.4916` edge `-0.0081` maxDD `-1.5252`
- `market_context_high->commodity_4h` score `-2.1492` n `114` status `ready` deltaP `2.2437` edge `-0.0231` maxDD `-7.3435`
- `market_context_high->metal_24h` score `-3.8074` n `74` status `ready` deltaP `-4.7204` edge `0.0234` maxDD `-29.4045`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
