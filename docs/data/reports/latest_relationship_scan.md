# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T13:07:14.774875+00:00`
- Price records: `672`
- Market context records: `1739`
- Flow alert records: `6910`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8842`

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

- `market_context_high->metal_24h` score `7.0131` n `154` status `ready` deltaP `25.9684` edge `0.6539` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `5.7903` n `196` status `ready` deltaP `20.3615` edge `0.5234` maxDD `-9.1295`
- `market_context_high->unknown_24h` score `4.7287` n `154` status `ready` deltaP `15.8703` edge `0.8203` maxDD `-35.8966`
- `market_context_high->index_24h` score `4.3107` n `154` status `ready` deltaP `18.4744` edge `0.3589` maxDD `-4.1604`
- `market_context_high->crypto_major_4h` score `4.1443` n `196` status `ready` deltaP `21.3477` edge `0.4436` maxDD `-10.9117`
- `market_context_high->unknown_4h` score `3.1169` n `196` status `ready` deltaP `13.7941` edge `0.3949` maxDD `-11.1695`
- `market_context_high->equity_4h` score `2.944` n `196` status `ready` deltaP `15.807` edge `0.2494` maxDD `-5.0894`
- `market_context_high->equity_24h` score `2.6092` n `154` status `ready` deltaP `16.9169` edge `0.5945` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.7477` n `196` status `ready` deltaP `7.4209` edge `0.1152` maxDD `-4.1892`
- `market_context_high->index_4h` score `0.6879` n `196` status `ready` deltaP `10.1886` edge `0.0983` maxDD `-3.7119`
- `market_context_high->crypto_major_24h` score `0.3217` n `154` status `ready` deltaP `20.2931` edge `0.7501` maxDD `-62.3533`
- `market_context_high->crypto_alt_24h` score `0.2321` n `154` status `ready` deltaP `21.4578` edge `1.0572` maxDD `-88.8062`
- `market_context_high->crypto_major_1h` score `0.1992` n `196` status `ready` deltaP `4.8974` edge `0.0913` maxDD `-3.9211`
- `market_context_high->equity_1h` score `0.0335` n `196` status `ready` deltaP `4.821` edge `0.0515` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.3054` n `196` status `ready` deltaP `2.8688` edge `0.0186` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.3187` n `196` status `ready` deltaP `12.1391` edge `0.1474` maxDD `-12.5349`
- `market_context_high->metal_1h` score `-0.5253` n `196` status `ready` deltaP `5.9453` edge `0.0266` maxDD `-6.3532`
- `market_context_high->fx_1h` score `-0.6646` n `196` status `ready` deltaP `-3.1162` edge `-0.0012` maxDD `-0.3914`
- `market_context_high->fx_24h` score `-0.7016` n `154` status `ready` deltaP `6.0354` edge `0.0062` maxDD `-1.3925`
- `market_context_high->unknown_1h` score `-1.5971` n `196` status `ready` deltaP `0.6385` edge `0.0096` maxDD `-7.7558`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
