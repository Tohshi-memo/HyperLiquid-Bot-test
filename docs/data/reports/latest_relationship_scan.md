# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T00:22:25.250589+00:00`
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

- `market_context_high->unknown_24h` score `37.4232` n `46` status `ready` deltaP `26.8192` edge `2.9441` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `11.4992` n `70` status `ready` deltaP `11.6333` edge `0.9281` maxDD `-1.4578`
- `market_context_high->crypto_alt_24h` score `10.3397` n `46` status `ready` deltaP `48.1658` edge `0.5579` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `8.5907` n `46` status `ready` deltaP `41.3873` edge `0.4579` maxDD `-0.434`
- `news_risk_high->fx_24h` score `1.0457` n `31` status `ready` deltaP `12.192` edge `0.0711` maxDD `-1.5526`
- `news_risk_high->commodity_1h` score `0.8734` n `31` status `ready` deltaP `18.9395` edge `0.0069` maxDD `-0.6947`
- `market_context_high->commodity_4h` score `0.6319` n `70` status `ready` deltaP `9.9434` edge `0.071` maxDD `-2.7703`
- `market_context_high->fx_4h` score `0.5485` n `70` status `ready` deltaP `21.7378` edge `0.0114` maxDD `-1.8797`
- `market_context_high->fx_1h` score `0.4009` n `82` status `ready` deltaP `12.8158` edge `0.0008` maxDD `-0.7878`
- `market_context_high->commodity_1h` score `0.2712` n `82` status `ready` deltaP `6.0756` edge `0.0237` maxDD `-1.3282`
- `news_risk_high->fx_4h` score `0.071` n `31` status `ready` deltaP `3.6733` edge `0.0349` maxDD `-0.356`
- `news_risk_high->commodity_4h` score `-0.1676` n `31` status `ready` deltaP `9.4365` edge `-0.0268` maxDD `-1.6728`
- `news_risk_high->index_1h` score `-0.1747` n `31` status `ready` deltaP `0.7968` edge `-0.0079` maxDD `-0.5845`
- `news_risk_high->crypto_alt_1h` score `-0.2219` n `31` status `ready` deltaP `9.7933` edge `-0.0297` maxDD `-3.1233`
- `market_context_high->index_1h` score `-0.2616` n `82` status `ready` deltaP `4.4947` edge `-0.0101` maxDD `-1.6054`
- `news_risk_high->index_4h` score `-0.2707` n `31` status `ready` deltaP `-3.57` edge `0.0393` maxDD `-0.3783`
- `news_risk_high->fx_1h` score `-0.3408` n `31` status `ready` deltaP `-2.2117` edge `0.0022` maxDD `-0.1588`
- `market_context_high->metal_1h` score `-0.4505` n `82` status `ready` deltaP `-0.1059` edge `-0.0076` maxDD `-1.6224`
- `news_risk_high->unknown_4h` score `-0.5051` n `31` status `ready` deltaP `-1.3621` edge `-0.0068` maxDD `-1.5766`
- `news_risk_high->equity_4h` score `-0.7156` n `31` status `ready` deltaP `-16.7781` edge `0.1218` maxDD `-2.8999`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
