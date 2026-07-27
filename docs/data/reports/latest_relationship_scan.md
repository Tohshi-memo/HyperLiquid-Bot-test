# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T12:03:07.945280+00:00`
- Price records: `672`
- Market context records: `8089`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11784`

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

- `market_context_high->equity_24h` score `20.3221` n `87` status `ready` deltaP `36.9051` edge `1.5385` maxDD `-4.9489`
- `market_context_high->equity_4h` score `8.395` n `87` status `ready` deltaP `32.4205` edge `0.5314` maxDD `-2.5032`
- `market_context_high->metal_24h` score `8.2868` n `87` status `ready` deltaP `35.8752` edge `0.4514` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.8475` n `42` status `ready` deltaP `32.0921` edge `0.4505` maxDD `-0.1727`
- `news_risk_high->crypto_major_4h` score `3.6592` n `42` status `ready` deltaP `15.5415` edge `0.2564` maxDD `-2.0729`
- `news_risk_high->equity_1h` score `3.5601` n `43` status `ready` deltaP `28.9305` edge `0.1354` maxDD `-1.1944`
- `market_context_high->index_4h` score `3.3171` n `87` status `ready` deltaP `31.7406` edge `0.0836` maxDD `-0.5022`
- `market_context_high->index_24h` score `3.0805` n `87` status `ready` deltaP `19.7454` edge `0.1921` maxDD `-1.3621`
- `news_risk_high->unknown_1h` score `2.7829` n `43` status `ready` deltaP `4.6059` edge `0.2289` maxDD `-0.8826`
- `news_risk_high->index_4h` score `2.5617` n `42` status `ready` deltaP `23.1199` edge `0.0784` maxDD `-0.191`
- `market_context_high->equity_1h` score `2.4749` n `87` status `ready` deltaP `15.3245` edge `0.1474` maxDD `-2.1322`
- `market_context_high->metal_4h` score `2.2695` n `87` status `ready` deltaP `20.8438` edge `0.1124` maxDD `-0.979`
- `market_context_high->fx_24h` score `2.2232` n `87` status `ready` deltaP `29.9886` edge `0.0557` maxDD `-0.6283`
- `news_risk_high->metal_4h` score `1.3474` n `42` status `ready` deltaP `14.1115` edge `0.065` maxDD `-0.7433`
- `market_context_high->index_1h` score `1.2153` n `87` status `ready` deltaP `15.87` edge `0.0222` maxDD `-0.4716`
- `market_context_high->crypto_alt_4h` score `0.8471` n `87` status `ready` deltaP `6.1817` edge `0.1411` maxDD `-3.9374`
- `news_risk_high->crypto_major_1h` score `0.7947` n `43` status `ready` deltaP `3.6381` edge `0.0817` maxDD `-1.1783`
- `market_context_high->metal_1h` score `0.7883` n `87` status `ready` deltaP `11.0744` edge `0.0297` maxDD `-0.6936`
- `market_context_high->commodity_24h` score `0.7127` n `87` status `ready` deltaP `26.0124` edge `0.2065` maxDD `-15.7497`
- `market_context_high->crypto_major_1h` score `0.6418` n `87` status `ready` deltaP `9.9198` edge `0.0284` maxDD `-1.6171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
