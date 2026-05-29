# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T01:07:20.359178+00:00`
- Price records: `672`
- Market context records: `2197`
- Flow alert records: `8215`
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

- `market_context_high->crypto_alt_4h` score `12.601` n `132` status `ready` deltaP `35.777` edge `0.9052` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.6` n `132` status `ready` deltaP `41.214` edge `0.7449` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `5.4383` n `132` status `ready` deltaP `21.3738` edge `0.3786` maxDD `-2.4317`
- `news_risk_high->commodity_4h` score `3.8364` n `43` status `ready` deltaP `32.0051` edge `0.3456` maxDD `-3.0367`
- `market_context_high->unknown_24h` score `3.4545` n `132` status `ready` deltaP `28.3302` edge `0.5805` maxDD `-32.8525`
- `market_context_high->equity_4h` score `3.4438` n `132` status `ready` deltaP `23.7205` edge `0.2383` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `3.1691` n `132` status `ready` deltaP `17.2655` edge `0.1967` maxDD `-1.817`
- `market_context_high->index_4h` score `3.0156` n `132` status `ready` deltaP `24.6397` edge `0.1554` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `2.9063` n `132` status `ready` deltaP `15.7594` edge `0.2235` maxDD `-4.9097`
- `market_context_high->index_24h` score `2.5424` n `132` status `ready` deltaP `10.9059` edge `0.262` maxDD `-4.1604`
- `market_context_high->crypto_major_24h` score `2.3475` n `132` status `ready` deltaP `19.5391` edge `0.9989` maxDD `-60.2561`
- `news_risk_high->fx_4h` score `2.1988` n `43` status `ready` deltaP `27.8892` edge `0.0157` maxDD `-0.1382`
- `market_context_high->metal_4h` score `1.4295` n `132` status `ready` deltaP `17.5905` edge `0.1406` maxDD `-4.7664`
- `news_risk_high->unknown_1h` score `1.3556` n `43` status `ready` deltaP `20.7457` edge `0.0216` maxDD `-1.7548`
- `news_risk_high->unknown_4h` score `1.2747` n `43` status `ready` deltaP `14.4675` edge `0.0821` maxDD `-2.7857`
- `news_risk_high->equity_4h` score `1.256` n `43` status `ready` deltaP `-2.9885` edge `0.3017` maxDD `-4.6598`
- `news_risk_high->commodity_1h` score `0.765` n `43` status `ready` deltaP `10.9142` edge `0.0933` maxDD `-2.1052`
- `market_context_high->equity_24h` score `0.5517` n `132` status `ready` deltaP `20.7702` edge `0.3921` maxDD `-33.1007`
- `news_risk_high->fx_1h` score `0.4381` n `43` status `ready` deltaP `7.8401` edge `0.0099` maxDD `-0.0524`
- `market_context_high->equity_1h` score `0.2873` n `132` status `ready` deltaP `8.8913` edge `0.0435` maxDD `-2.6402`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
