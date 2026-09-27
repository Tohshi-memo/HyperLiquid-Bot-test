# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T06:07:28.669776+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11712`

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

- `news_risk_high->unknown_24h` score `1829.6892` n `116` status `ready` deltaP `1.2153` edge `152.466` maxDD `0.0`
- `market_context_high->unknown_1h` score `103.8118` n `48` status `ready` deltaP `10.3418` edge `8.5867` maxDD `-0.0395`
- `market_context_high->crypto_major_24h` score `52.4469` n `44` status `ready` deltaP `30.1926` edge `4.2044` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `28.5402` n `44` status `ready` deltaP `14.9148` edge `2.3169` maxDD `-2.7051`
- `market_context_high->equity_24h` score `27.9856` n `44` status `ready` deltaP `36.0954` edge `2.1229` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.8993` n `44` status `ready` deltaP `33.4912` edge `0.4438` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.8782` n `44` status `ready` deltaP `34.2171` edge `0.1189` maxDD `-0.2401`
- `market_context_high->index_4h` score `3.18` n `44` status `ready` deltaP `35.546` edge `0.0351` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.7729` n `44` status `ready` deltaP `15.9922` edge `0.1621` maxDD `-1.3444`
- `market_context_high->crypto_alt_4h` score `1.077` n `44` status `ready` deltaP `8.0932` edge `0.0984` maxDD `-3.3417`
- `market_context_high->equity_1h` score `0.9803` n `48` status `ready` deltaP `11.7266` edge `0.0438` maxDD `-1.5564`
- `news_risk_high->metal_24h` score `0.9119` n `116` status `ready` deltaP `17.2892` edge `0.1255` maxDD `-6.8481`
- `market_context_high->crypto_major_4h` score `0.8744` n `44` status `ready` deltaP `7.0676` edge `0.1162` maxDD `-5.2359`
- `market_context_high->crypto_major_1h` score `0.8674` n `48` status `ready` deltaP `8.3209` edge `0.1026` maxDD `-4.8632`
- `market_context_high->crypto_alt_1h` score `0.6526` n `48` status `ready` deltaP `7.7096` edge `0.0919` maxDD `-5.7799`
- `news_risk_high->index_24h` score `0.6237` n `116` status `ready` deltaP `13.3501` edge `0.0325` maxDD `-2.2287`
- `market_context_high->index_1h` score `0.6085` n `48` status `ready` deltaP `9.9426` edge `0.0081` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.3444` n `48` status `ready` deltaP `10.8907` edge `0.0072` maxDD `-0.1854`
- `market_context_high->metal_1h` score `0.1473` n `48` status `ready` deltaP `5.0898` edge `0.0102` maxDD `-0.215`
- `news_risk_high->index_1h` score `-0.1778` n `142` status `ready` deltaP `1.6973` edge `0.003` maxDD `-0.3305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
