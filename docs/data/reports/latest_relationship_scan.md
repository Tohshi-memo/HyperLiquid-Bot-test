# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T00:52:17.066173+00:00`
- Price records: `672`
- Market context records: `2196`
- Flow alert records: `8212`
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

- `market_context_high->crypto_alt_4h` score `12.6251` n `132` status `ready` deltaP `35.9295` edge `0.9062` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.6194` n `132` status `ready` deltaP `41.3664` edge `0.7455` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `5.4407` n `132` status `ready` deltaP `21.3738` edge `0.3788` maxDD `-2.4317`
- `news_risk_high->commodity_4h` score `3.8238` n `43` status `ready` deltaP `31.8526` edge `0.345` maxDD `-3.0367`
- `market_context_high->unknown_24h` score `3.4972` n `132` status `ready` deltaP `28.5038` edge `0.5829` maxDD `-32.8525`
- `market_context_high->equity_4h` score `3.4632` n `132` status `ready` deltaP `23.8729` edge `0.2389` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `3.1727` n `132` status `ready` deltaP `17.2655` edge `0.197` maxDD `-1.817`
- `market_context_high->index_4h` score `2.9986` n `132` status `ready` deltaP `24.4872` edge `0.155` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `2.9315` n `132` status `ready` deltaP `15.9091` edge `0.2246` maxDD `-4.9097`
- `market_context_high->index_24h` score `2.5496` n `132` status `ready` deltaP `10.9059` edge `0.2626` maxDD `-4.1604`
- `market_context_high->crypto_major_24h` score `2.3908` n `132` status `ready` deltaP `19.7127` edge `1.0033` maxDD `-60.2561`
- `news_risk_high->fx_4h` score `2.1988` n `43` status `ready` deltaP `27.8892` edge `0.0157` maxDD `-0.1382`
- `market_context_high->metal_4h` score `1.4513` n `132` status `ready` deltaP `17.743` edge `0.1414` maxDD `-4.7664`
- `news_risk_high->unknown_1h` score `1.3688` n `43` status `ready` deltaP `20.8954` edge `0.0217` maxDD `-1.7548`
- `news_risk_high->unknown_4h` score `1.2771` n `43` status `ready` deltaP `14.4675` edge `0.0823` maxDD `-2.7857`
- `news_risk_high->equity_4h` score `1.2686` n `43` status `ready` deltaP `-2.8361` edge `0.3023` maxDD `-4.6598`
- `news_risk_high->commodity_1h` score `0.7549` n `43` status `ready` deltaP `10.7645` edge `0.093` maxDD `-2.1052`
- `market_context_high->equity_24h` score `0.64` n `132` status `ready` deltaP `20.9438` edge `0.3983` maxDD `-33.1007`
- `news_risk_high->fx_1h` score `0.4381` n `43` status `ready` deltaP `7.8401` edge `0.0099` maxDD `-0.0524`
- `market_context_high->equity_1h` score `0.2705` n `132` status `ready` deltaP `8.7416` edge `0.0431` maxDD `-2.6402`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
