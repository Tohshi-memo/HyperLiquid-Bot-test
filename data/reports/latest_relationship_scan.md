# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T04:07:26.190166+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11522`

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

- `news_risk_high->unknown_24h` score `2358.6384` n `108` status `ready` deltaP `1.2153` edge `196.5451` maxDD `0.0`
- `market_context_high->unknown_1h` score `77.2251` n `44` status `ready` deltaP `10.3022` edge `6.3714` maxDD `-0.0395`
- `market_context_high->crypto_major_24h` score `51.9166` n `44` status `ready` deltaP `29.3245` edge `4.166` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `28.0914` n `44` status `ready` deltaP `14.9148` edge `2.2795` maxDD `-2.7051`
- `market_context_high->equity_24h` score `27.85` n `44` status `ready` deltaP `36.0954` edge `2.1116` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.8367` n `44` status `ready` deltaP `33.144` edge `0.4409` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.8027` n `44` status `ready` deltaP `33.3491` edge `0.1184` maxDD `-0.2401`
- `market_context_high->index_4h` score `3.2824` n `44` status `ready` deltaP `36.7655` edge `0.0355` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.8849` n `44` status `ready` deltaP `17.2117` edge `0.1633` maxDD `-1.3444`
- `market_context_high->crypto_alt_4h` score `1.2244` n `44` status `ready` deltaP `8.8553` edge `0.1056` maxDD `-3.3417`
- `market_context_high->crypto_major_1h` score `1.0892` n `44` status `ready` deltaP `9.1181` edge `0.1034` maxDD `-4.5405`
- `market_context_high->equity_1h` score `1.0335` n `44` status `ready` deltaP `11.7175` edge `0.0483` maxDD `-1.5564`
- `market_context_high->crypto_major_4h` score `0.8754` n `44` status `ready` deltaP `6.9152` edge `0.1173` maxDD `-5.2359`
- `news_risk_high->metal_24h` score `0.8105` n `108` status `ready` deltaP `20.8912` edge `0.1294` maxDD `-6.8481`
- `market_context_high->index_1h` score `0.7493` n `44` status `ready` deltaP `11.5678` edge `0.009` maxDD `-0.2275`
- `news_risk_high->index_24h` score `0.7177` n `108` status `ready` deltaP `13.1945` edge `0.0372` maxDD `-2.2287`
- `market_context_high->metal_1h` score `0.2575` n `44` status `ready` deltaP `6.3146` edge `0.011` maxDD `-0.1976`
- `market_context_high->fx_1h` score `0.1625` n `44` status `ready` deltaP `7.5122` edge `0.0064` maxDD `-0.1854`
- `market_context_high->crypto_alt_1h` score `0.0666` n `44` status `ready` deltaP `4.4502` edge `0.0648` maxDD `-5.7799`
- `news_risk_high->index_1h` score `-0.1538` n `142` status `ready` deltaP `1.9967` edge `0.003` maxDD `-0.3305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
