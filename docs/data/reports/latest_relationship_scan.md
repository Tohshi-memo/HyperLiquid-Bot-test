# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T07:22:56.172006+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11632`

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

- `market_context_high->unknown_24h` score `14.6713` n `88` status `ready` deltaP `12.4053` edge `1.1442` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.6259` n `90` status `ready` deltaP `1.9004` edge `0.5557` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.592` n `90` status `ready` deltaP `17.3849` edge `0.1014` maxDD `-2.7703`
- `market_context_high->fx_24h` score `1.1762` n `88` status `ready` deltaP `27.7304` edge `0.0865` maxDD `-4.3126`
- `market_context_high->metal_24h` score `1.0553` n `88` status `ready` deltaP `1.9255` edge `0.2393` maxDD `-2.6802`
- `market_context_high->commodity_1h` score `0.2919` n `92` status `ready` deltaP `5.8839` edge `0.0267` maxDD `-1.3282`
- `market_context_high->fx_4h` score `0.0727` n `90` status `ready` deltaP `13.1572` edge `0.0076` maxDD `-1.8797`
- `market_context_high->fx_1h` score `-0.0007` n `92` status `ready` deltaP `5.8514` edge `-0.0041` maxDD `-0.7973`
- `market_context_high->metal_1h` score `-0.4734` n `92` status `ready` deltaP `-0.5923` edge `-0.0073` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.6167` n `92` status `ready` deltaP `-0.9242` edge `-0.0195` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.8458` n `90` status `ready` deltaP `2.2696` edge `-0.0001` maxDD `-3.211`
- `market_context_high->crypto_alt_1h` score `-0.8555` n `92` status `ready` deltaP `-3.1828` edge `-0.0174` maxDD `-3.0178`
- `market_context_high->crypto_alt_24h` score `-1.1098` n `88` status `ready` deltaP `3.3933` edge `-0.0206` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-1.3539` n `90` status `ready` deltaP `1.3516` edge `-0.0436` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.8133` n `92` status `ready` deltaP `3.0136` edge `-0.099` maxDD `-10.619`
- `market_context_high->index_24h` score `-2.0787` n `88` status `ready` deltaP `-7.8914` edge `0.0056` maxDD `-7.8922`
- `market_context_high->index_4h` score `-2.1155` n `90` status `ready` deltaP `-13.0454` edge `-0.0588` maxDD `-4.7021`
- `market_context_high->unknown_1h` score `-3.2751` n `92` status `ready` deltaP `3.0396` edge `-0.2485` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.318` n `92` status `ready` deltaP `-10.7199` edge `-0.0677` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.3936` n `88` status `ready` deltaP `8.0492` edge `-0.0772` maxDD `-49.6923`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
