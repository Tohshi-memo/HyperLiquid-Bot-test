# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T05:07:27.966309+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11726`

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

- `news_risk_high->unknown_24h` score `2084.6016` n `112` status `ready` deltaP `1.2153` edge `173.7087` maxDD `0.0`
- `market_context_high->unknown_1h` score `95.9011` n `45` status `ready` deltaP `10.3527` edge `7.9274` maxDD `-0.0395`
- `market_context_high->crypto_major_24h` score `52.211` n `44` status `ready` deltaP `30.019` edge `4.1859` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `28.3434` n `44` status `ready` deltaP `14.9148` edge `2.3005` maxDD `-2.7051`
- `market_context_high->equity_24h` score `27.9196` n `44` status `ready` deltaP `36.0954` edge `2.1174` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.8813` n `44` status `ready` deltaP `33.4912` edge `0.4423` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.8631` n `44` status `ready` deltaP `34.0435` edge `0.1188` maxDD `-0.2401`
- `market_context_high->index_4h` score `3.2312` n `44` status `ready` deltaP `36.1557` edge `0.0353` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.8301` n `44` status `ready` deltaP `16.602` edge `0.1628` maxDD `-1.3444`
- `market_context_high->crypto_alt_4h` score `1.1798` n `44` status `ready` deltaP `8.7029` edge `0.1029` maxDD `-3.3417`
- `news_risk_high->metal_24h` score `1.0956` n `112` status `ready` deltaP `19.2708` edge `0.1276` maxDD `-6.8481`
- `market_context_high->equity_1h` score `1.0546` n `45` status `ready` deltaP `12.1757` edge `0.047` maxDD `-1.5564`
- `market_context_high->crypto_major_4h` score `0.8658` n `44` status `ready` deltaP `6.9152` edge `0.1165` maxDD `-5.2359`
- `market_context_high->crypto_major_1h` score `0.8487` n `45` status `ready` deltaP `7.9042` edge `0.0975` maxDD `-4.691`
- `market_context_high->index_1h` score `0.7728` n `45` status `ready` deltaP `11.8763` edge `0.0089` maxDD `-0.2275`
- `news_risk_high->index_24h` score `0.5861` n `112` status `ready` deltaP `12.5496` edge `0.0347` maxDD `-2.2287`
- `market_context_high->metal_1h` score `0.2074` n `45` status `ready` deltaP `5.7518` edge `0.0107` maxDD `-0.2073`
- `market_context_high->fx_1h` score `0.2028` n `45` status `ready` deltaP `8.2734` edge `0.0065` maxDD `-0.1854`
- `market_context_high->crypto_alt_1h` score `0.1861` n `45` status `ready` deltaP `5.6587` edge `0.0667` maxDD `-5.7799`
- `news_risk_high->index_1h` score `-0.1898` n `142` status `ready` deltaP `1.5476` edge `0.003` maxDD `-0.3305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
