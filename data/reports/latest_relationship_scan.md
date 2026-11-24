# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T23:07:27.722561+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4068`

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

- `market_context_high->unknown_1h` score `32271.173` n `45` status `ready` deltaP `1.5668` edge `2689.2634` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `22005.3445` n `45` status `ready` deltaP `3.1776` edge `1833.7714` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `1036.218` n `31` status `ready` deltaP `1.7819` edge `86.3572` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `752.397` n `31` status `ready` deltaP `4.3962` edge `62.6761` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `38.6447` n `31` status `ready` deltaP `50.1736` edge `2.8859` maxDD `0.0`
- `news_risk_high->equity_24h` score `37.5435` n `31` status `ready` deltaP `43.9236` edge `2.8358` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `34.3883` n `31` status `ready` deltaP `48.9583` edge `2.5393` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.8393` n `31` status `ready` deltaP `27.0653` edge `0.8932` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.0846` n `31` status `ready` deltaP `41.2355` edge `0.6763` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `10.3282` n `31` status `ready` deltaP `34.1759` edge `0.6809` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.3189` n `31` status `ready` deltaP `17.6927` edge `0.9621` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.8022` n `31` status `ready` deltaP `49.1768` edge `0.1685` maxDD `-0.0262`
- `news_risk_high->index_24h` score `5.5948` n `31` status `ready` deltaP `41.8403` edge `0.1873` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.68` n `31` status `ready` deltaP `18.9395` edge `0.1991` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.0441` n `31` status `ready` deltaP `32.8039` edge `0.061` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.7338` n `31` status `ready` deltaP `12.5555` edge `0.3129` maxDD `-1.6897`
- `market_context_high->fx_4h` score `2.7319` n `45` status `ready` deltaP `33.2893` edge `0.0342` maxDD `-0.2774`
- `news_risk_high->index_1h` score `2.5812` n `31` status `ready` deltaP `30.4955` edge `0.0203` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.4156` n `31` status `ready` deltaP `12.5555` edge `0.2617` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.635` n `31` status `ready` deltaP `30.6306` edge `0.0333` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
