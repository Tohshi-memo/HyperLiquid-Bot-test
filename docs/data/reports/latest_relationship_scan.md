# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T03:07:17.982013+00:00`
- Price records: `672`
- Market context records: `2205`
- Flow alert records: `8239`
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

- `market_context_high->crypto_alt_4h` score `12.6989` n `132` status `ready` deltaP `36.3868` edge `0.9093` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.7064` n `132` status `ready` deltaP `41.8237` edge `0.7497` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `5.4683` n `132` status `ready` deltaP `21.3738` edge `0.3811` maxDD `-2.4317`
- `news_risk_high->commodity_4h` score `3.819` n `43` status `ready` deltaP `31.7002` edge `0.3454` maxDD `-3.0367`
- `market_context_high->equity_4h` score `3.3794` n `132` status `ready` deltaP `23.1107` edge `0.237` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `3.2386` n `132` status `ready` deltaP `17.7146` edge `0.1995` maxDD `-1.817`
- `market_context_high->index_4h` score `3.1516` n `132` status `ready` deltaP `25.8592` edge `0.1586` maxDD `-1.8022`
- `market_context_high->unknown_24h` score `3.1096` n `132` status `ready` deltaP `27.2886` edge `0.5587` maxDD `-32.8525`
- `market_context_high->crypto_alt_1h` score `2.9135` n `132` status `ready` deltaP `15.7594` edge `0.2241` maxDD `-4.9097`
- `market_context_high->index_24h` score `2.444` n `132` status `ready` deltaP `10.9059` edge `0.2538` maxDD `-4.1604`
- `news_risk_high->fx_4h` score `2.2` n `43` status `ready` deltaP `27.8892` edge `0.0158` maxDD `-0.1382`
- `market_context_high->crypto_major_24h` score `1.9996` n `132` status `ready` deltaP `18.3238` edge `0.9624` maxDD `-60.2561`
- `news_risk_high->unknown_1h` score `1.4359` n `43` status `ready` deltaP `21.3445` edge `0.0243` maxDD `-1.7548`
- `news_risk_high->unknown_4h` score `1.3047` n `43` status `ready` deltaP `14.4675` edge `0.0846` maxDD `-2.7857`
- `market_context_high->metal_4h` score `1.2565` n `132` status `ready` deltaP `16.5235` edge `0.1333` maxDD `-4.7664`
- `news_risk_high->equity_4h` score `1.2142` n `43` status `ready` deltaP `-3.5983` edge `0.3004` maxDD `-4.6598`
- `news_risk_high->commodity_1h` score `0.7728` n `43` status `ready` deltaP `11.0639` edge `0.0933` maxDD `-2.1052`
- `news_risk_high->fx_1h` score `0.4753` n `43` status `ready` deltaP `8.2892` edge `0.01` maxDD `-0.0524`
- `market_context_high->equity_1h` score `0.346` n `132` status `ready` deltaP `9.4901` edge `0.0444` maxDD `-2.6402`
- `news_risk_high->equity_1h` score `0.1986` n `43` status `ready` deltaP `4.8566` edge `0.0451` maxDD `-1.8278`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
