# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T03:07:37.502128+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9932`

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

- `market_context_high->unknown_24h` score `37.3719` n `46` status `ready` deltaP `26.2983` edge `2.9433` maxDD `-0.0103`
- `market_context_high->crypto_alt_24h` score `10.0397` n `46` status `ready` deltaP `46.9505` edge `0.541` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `8.3719` n `46` status `ready` deltaP `39.4776` edge `0.4524` maxDD `-0.434`
- `market_context_high->unknown_4h` score `8.1266` n `81` status `ready` deltaP `5.4012` edge `0.6998` maxDD `-2.0206`
- `market_context_high->commodity_4h` score `1.1259` n `81` status `ready` deltaP `14.1975` edge `0.0838` maxDD `-2.7703`
- `news_risk_high->fx_24h` score `0.9788` n `31` status `ready` deltaP `11.6712` edge `0.069` maxDD `-1.5526`
- `news_risk_high->commodity_1h` score `0.822` n `31` status `ready` deltaP `18.191` edge `0.0053` maxDD `-0.6947`
- `market_context_high->fx_4h` score `0.332` n `81` status `ready` deltaP `17.9181` edge `0.0091` maxDD `-1.8797`
- `market_context_high->fx_1h` score `0.2874` n `88` status `ready` deltaP `9.1794` edge `-0.0024` maxDD `-0.7878`
- `market_context_high->commodity_1h` score `0.2828` n `88` status `ready` deltaP `6.1309` edge `0.0243` maxDD `-1.3282`
- `news_risk_high->fx_4h` score `0.0331` n `31` status `ready` deltaP `3.0635` edge `0.0341` maxDD `-0.356`
- `news_risk_high->index_1h` score `-0.1996` n `31` status `ready` deltaP `0.3477` edge `-0.0081` maxDD `-0.5845`
- `news_risk_high->crypto_alt_1h` score `-0.2438` n `31` status `ready` deltaP `9.6436` edge `-0.0315` maxDD `-3.1233`
- `news_risk_high->index_4h` score `-0.2937` n `31` status `ready` deltaP `-3.7225` edge `0.0384` maxDD `-0.3783`
- `news_risk_high->commodity_4h` score `-0.3206` n `31` status `ready` deltaP `8.0645` edge `-0.0304` maxDD `-1.6728`
- `news_risk_high->fx_1h` score `-0.365` n `31` status `ready` deltaP `-2.6608` edge `0.0021` maxDD `-0.1588`
- `market_context_high->index_1h` score `-0.4188` n `88` status `ready` deltaP `2.3272` edge `-0.0158` maxDD `-1.6054`
- `news_risk_high->unknown_4h` score `-0.466` n `31` status `ready` deltaP `-1.2097` edge `-0.0028` maxDD `-1.5766`
- `market_context_high->metal_1h` score `-0.4996` n `88` status `ready` deltaP `-1.0207` edge `-0.0078` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.6902` n `81` status `ready` deltaP `3.1316` edge `0.0141` maxDD `-3.211`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
