# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T00:52:27.446099+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11444`

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

- `news_risk_high->unknown_24h` score `3409.5096` n `95` status `ready` deltaP `1.2153` edge `284.1177` maxDD `0.0`
- `market_context_high->unknown_1h` score `75.2115` n `44` status `ready` deltaP `10.1524` edge `6.2046` maxDD `-0.0395`
- `market_context_high->crypto_major_24h` score `51.0869` n `44` status `ready` deltaP `27.0676` edge `4.1119` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `27.7314` n `44` status `ready` deltaP `14.9148` edge `2.2495` maxDD `-2.7051`
- `market_context_high->equity_24h` score `27.676` n `44` status `ready` deltaP `36.0954` edge `2.0971` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.6673` n `44` status `ready` deltaP `31.5815` edge `0.4372` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.647` n `44` status `ready` deltaP `31.613` edge `0.117` maxDD `-0.2401`
- `market_context_high->index_4h` score `3.4419` n `44` status `ready` deltaP `38.5947` edge `0.0366` maxDD `-0.2323`
- `market_context_high->equity_4h` score `3.114` n `44` status `ready` deltaP `19.041` edge `0.1702` maxDD `-1.3444`
- `market_context_high->crypto_alt_4h` score `1.5377` n `44` status `ready` deltaP `9.9224` edge `0.1246` maxDD `-3.3417`
- `news_risk_high->index_24h` score `1.3121` n `95` status `ready` deltaP `18.0647` edge `0.0501` maxDD `-2.2287`
- `market_context_high->crypto_major_1h` score `1.2031` n `44` status `ready` deltaP `9.4175` edge `0.1109` maxDD `-4.5405`
- `market_context_high->crypto_major_4h` score `1.1588` n `44` status `ready` deltaP `7.9823` edge `0.1338` maxDD `-5.2359`
- `news_risk_high->metal_24h` score `1.1203` n `95` status `ready` deltaP `25.9192` edge `0.1356` maxDD `-6.8481`
- `market_context_high->equity_1h` score `1.1031` n `44` status `ready` deltaP `12.1666` edge `0.0511` maxDD `-1.5564`
- `market_context_high->index_1h` score `0.7912` n `44` status `ready` deltaP `12.0169` edge `0.0095` maxDD `-0.2275`
- `market_context_high->metal_1h` score `0.2719` n `44` status `ready` deltaP `6.4643` edge `0.0112` maxDD `-0.1976`
- `market_context_high->fx_1h` score `0.1391` n `44` status `ready` deltaP `7.0631` edge `0.0064` maxDD `-0.1854`
- `market_context_high->crypto_alt_1h` score `0.1339` n `44` status `ready` deltaP `4.1508` edge `0.0724` maxDD `-5.7799`
- `news_risk_high->index_1h` score `-0.1297` n `139` status `ready` deltaP `2.2229` edge `0.0035` maxDD `-0.3305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
