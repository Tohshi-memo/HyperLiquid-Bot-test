# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T06:52:25.507396+00:00`
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

- `news_risk_high->unknown_24h` score `1708.7964` n `118` status `ready` deltaP `1.2153` edge `142.3916` maxDD `0.0`
- `market_context_high->unknown_1h` score `103.8058` n `48` status `ready` deltaP `10.4916` edge `8.5852` maxDD `-0.0395`
- `market_context_high->crypto_major_24h` score `52.6137` n `44` status `ready` deltaP `30.1926` edge `4.2183` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `28.7298` n `44` status `ready` deltaP `14.9148` edge `2.3327` maxDD `-2.7051`
- `market_context_high->equity_24h` score `28.0432` n `44` status `ready` deltaP `36.0954` edge `2.1277` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.9149` n `44` status `ready` deltaP `33.4912` edge `0.4451` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.892` n `44` status `ready` deltaP `34.3908` edge `0.1189` maxDD `-0.2401`
- `market_context_high->index_4h` score `3.1422` n `44` status `ready` deltaP `35.0886` edge `0.035` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.7315` n `44` status `ready` deltaP `15.5349` edge `0.1617` maxDD `-1.3444`
- `market_context_high->equity_1h` score `0.9791` n `48` status `ready` deltaP `11.7266` edge `0.0437` maxDD `-1.5564`
- `market_context_high->crypto_alt_4h` score `0.9732` n `44` status `ready` deltaP `7.6358` edge `0.0928` maxDD `-3.3417`
- `market_context_high->crypto_major_4h` score `0.8344` n `44` status `ready` deltaP `6.7628` edge `0.1149` maxDD `-5.2359`
- `market_context_high->crypto_major_1h` score `0.8171` n `48` status `ready` deltaP `7.8718` edge `0.1014` maxDD `-4.8632`
- `news_risk_high->metal_24h` score `0.6606` n `118` status `ready` deltaP `15.5927` edge `0.1242` maxDD `-6.8481`
- `news_risk_high->index_24h` score `0.6229` n `118` status `ready` deltaP `13.73` edge `0.0299` maxDD `-2.2287`
- `market_context_high->crypto_alt_1h` score `0.5855` n `48` status `ready` deltaP `7.2605` edge `0.0893` maxDD `-5.7799`
- `market_context_high->index_1h` score `0.5833` n `48` status `ready` deltaP `9.6432` edge `0.008` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.3678` n `48` status `ready` deltaP `11.3398` edge `0.0072` maxDD `-0.1854`
- `market_context_high->metal_1h` score `0.1342` n `48` status `ready` deltaP `4.9401` edge `0.0101` maxDD `-0.215`
- `news_risk_high->index_1h` score `-0.1686` n `141` status `ready` deltaP `1.7975` edge `0.003` maxDD `-0.3229`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
