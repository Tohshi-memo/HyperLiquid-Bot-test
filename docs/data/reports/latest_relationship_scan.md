# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T00:57:17.582773+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `7932`

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

- `market_context_high->unknown_24h` score `37.4364` n `46` status `ready` deltaP `26.8192` edge `2.9452` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `11.1351` n `72` status `ready` deltaP `12.3476` edge `0.893` maxDD `-1.4578`
- `market_context_high->crypto_alt_24h` score `10.321` n `46` status `ready` deltaP `47.9922` edge `0.5575` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `8.5485` n `46` status `ready` deltaP `41.0401` edge `0.4567` maxDD `-0.434`
- `news_risk_high->fx_24h` score `1.0433` n `31` status `ready` deltaP `12.192` edge `0.0709` maxDD `-1.5526`
- `news_risk_high->commodity_1h` score `0.8703` n `31` status `ready` deltaP `18.9395` edge `0.0065` maxDD `-0.6947`
- `market_context_high->commodity_4h` score `0.7332` n `72` status `ready` deltaP `10.7893` edge `0.0738` maxDD `-2.7703`
- `market_context_high->fx_4h` score `0.5238` n `72` status `ready` deltaP `21.3076` edge `0.0111` maxDD `-1.8797`
- `market_context_high->fx_1h` score `0.4947` n `84` status `ready` deltaP `11.4557` edge `-0.0003` maxDD `-0.7878`
- `market_context_high->commodity_1h` score `0.3944` n `84` status `ready` deltaP `7.15` edge `0.0268` maxDD `-1.3282`
- `news_risk_high->fx_4h` score `0.0623` n `31` status `ready` deltaP `3.5209` edge `0.0348` maxDD `-0.356`
- `news_risk_high->index_1h` score `-0.1723` n `31` status `ready` deltaP `0.7968` edge `-0.0076` maxDD `-0.5845`
- `news_risk_high->commodity_4h` score `-0.2004` n `31` status `ready` deltaP `9.1316` edge `-0.0275` maxDD `-1.6728`
- `news_risk_high->crypto_alt_1h` score `-0.2297` n `31` status `ready` deltaP `9.7933` edge `-0.0307` maxDD `-3.1233`
- `news_risk_high->index_4h` score `-0.2731` n `31` status `ready` deltaP `-3.57` edge `0.0391` maxDD `-0.3783`
- `news_risk_high->fx_1h` score `-0.3315` n `31` status `ready` deltaP `-2.062` edge `0.0024` maxDD `-0.1588`
- `market_context_high->index_1h` score `-0.3614` n `84` status `ready` deltaP `3.101` edge `-0.0136` maxDD `-1.6054`
- `market_context_high->metal_1h` score `-0.4621` n `84` status `ready` deltaP `-0.3136` edge `-0.0077` maxDD `-1.6224`
- `news_risk_high->unknown_4h` score `-0.5082` n `31` status `ready` deltaP `-1.3621` edge `-0.0072` maxDD `-1.5766`
- `news_risk_high->equity_4h` score `-0.736` n `31` status `ready` deltaP `-16.7781` edge `0.1201` maxDD `-2.8999`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
