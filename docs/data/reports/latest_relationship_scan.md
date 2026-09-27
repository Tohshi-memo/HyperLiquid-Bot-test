# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T05:52:32.766379+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11760`

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

- `news_risk_high->unknown_24h` score `1891.8048` n `115` status `ready` deltaP `1.2153` edge `157.6423` maxDD `0.0`
- `market_context_high->unknown_1h` score `103.7398` n `48` status `ready` deltaP `10.3418` edge `8.5807` maxDD `-0.0395`
- `market_context_high->crypto_major_24h` score `52.3953` n `44` status `ready` deltaP `30.1926` edge `4.2001` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `28.4946` n `44` status `ready` deltaP `14.9148` edge `2.3131` maxDD `-2.7051`
- `market_context_high->equity_24h` score `27.9688` n `44` status `ready` deltaP `36.0954` edge `2.1215` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.8957` n `44` status `ready` deltaP `33.4912` edge `0.4435` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.8782` n `44` status `ready` deltaP `34.2171` edge `0.1189` maxDD `-0.2401`
- `market_context_high->index_4h` score `3.1934` n `44` status `ready` deltaP `35.6984` edge `0.0352` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.7875` n `44` status `ready` deltaP `16.1447` edge `0.1623` maxDD `-1.3444`
- `market_context_high->crypto_alt_4h` score `1.1108` n `44` status `ready` deltaP `8.2456` edge `0.1002` maxDD `-3.3417`
- `market_context_high->equity_1h` score `0.9922` n `48` status `ready` deltaP `11.8763` edge `0.0438` maxDD `-1.5564`
- `news_risk_high->metal_24h` score `0.9611` n `115` status `ready` deltaP `17.814` edge `0.1261` maxDD `-6.8481`
- `market_context_high->crypto_major_4h` score `0.8792` n `44` status `ready` deltaP `7.0676` edge `0.1166` maxDD `-5.2359`
- `market_context_high->crypto_major_1h` score `0.8734` n `48` status `ready` deltaP `8.3209` edge `0.1031` maxDD `-4.8632`
- `market_context_high->crypto_alt_1h` score `0.6754` n `48` status `ready` deltaP `7.8593` edge `0.0928` maxDD `-5.7799`
- `news_risk_high->index_24h` score `0.6153` n `115` status `ready` deltaP `13.1552` edge `0.0331` maxDD `-2.2287`
- `market_context_high->index_1h` score `0.6085` n `48` status `ready` deltaP `9.9426` edge `0.0081` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.3522` n `48` status `ready` deltaP `11.0404` edge `0.0072` maxDD `-0.1854`
- `market_context_high->metal_1h` score `0.1342` n `48` status `ready` deltaP `4.9401` edge `0.0101` maxDD `-0.215`
- `news_risk_high->index_1h` score `-0.1778` n `142` status `ready` deltaP `1.6973` edge `0.003` maxDD `-0.3305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
