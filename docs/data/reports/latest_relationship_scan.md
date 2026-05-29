# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T01:22:19.400297+00:00`
- Price records: `672`
- Market context records: `2198`
- Flow alert records: `8218`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9188`

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

- `market_context_high->crypto_alt_4h` score `12.6216` n `132` status `ready` deltaP `35.9295` edge `0.9059` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.623` n `132` status `ready` deltaP `41.3664` edge `0.7458` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `5.4443` n `132` status `ready` deltaP `21.3738` edge `0.3791` maxDD `-2.4317`
- `news_risk_high->commodity_4h` score `3.8269` n `43` status `ready` deltaP `31.8526` edge `0.3454` maxDD `-3.0367`
- `market_context_high->equity_4h` score `3.4256` n `132` status `ready` deltaP `23.568` edge `0.2378` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `3.4155` n `132` status `ready` deltaP `28.1566` edge `0.5784` maxDD `-32.8525`
- `market_context_high->crypto_major_1h` score `3.1883` n `132` status `ready` deltaP `17.4152` edge `0.1973` maxDD `-1.817`
- `market_context_high->index_4h` score `3.0338` n `132` status `ready` deltaP `24.7921` edge `0.1559` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `2.9027` n `132` status `ready` deltaP `15.7594` edge `0.2232` maxDD `-4.9097`
- `market_context_high->index_24h` score `2.5328` n `132` status `ready` deltaP `10.9059` edge `0.2612` maxDD `-4.1604`
- `market_context_high->crypto_major_24h` score `2.3065` n `132` status `ready` deltaP `19.3655` edge `0.9948` maxDD `-60.2561`
- `news_risk_high->fx_4h` score `2.1988` n `43` status `ready` deltaP `27.8892` edge `0.0157` maxDD `-0.1382`
- `market_context_high->metal_4h` score `1.3981` n `132` status `ready` deltaP `17.4381` edge `0.139` maxDD `-4.7664`
- `news_risk_high->unknown_1h` score `1.3688` n `43` status `ready` deltaP `20.8954` edge `0.0217` maxDD `-1.7548`
- `news_risk_high->unknown_4h` score `1.2807` n `43` status `ready` deltaP `14.4675` edge `0.0826` maxDD `-2.7857`
- `news_risk_high->equity_4h` score `1.2442` n `43` status `ready` deltaP `-3.141` edge `0.3012` maxDD `-4.6598`
- `news_risk_high->commodity_1h` score `0.7658` n `43` status `ready` deltaP `10.9142` edge `0.0934` maxDD `-2.1052`
- `market_context_high->equity_24h` score `0.4598` n `132` status `ready` deltaP `20.5966` edge `0.3856` maxDD `-33.1007`
- `news_risk_high->fx_1h` score `0.425` n `43` status `ready` deltaP `7.6904` edge `0.0098` maxDD `-0.0524`
- `market_context_high->equity_1h` score `0.3041` n `132` status `ready` deltaP `9.041` edge `0.0439` maxDD `-2.6402`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
