# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T00:37:19.238144+00:00`
- Price records: `672`
- Market context records: `2195`
- Flow alert records: `8209`
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

- `market_context_high->crypto_alt_4h` score `12.6493` n `132` status `ready` deltaP `36.0819` edge `0.9072` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.6376` n `132` status `ready` deltaP `41.5189` edge `0.746` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `5.4419` n `132` status `ready` deltaP `21.3738` edge `0.3789` maxDD `-2.4317`
- `news_risk_high->commodity_4h` score `3.8238` n `43` status `ready` deltaP `31.8526` edge `0.345` maxDD `-3.0367`
- `market_context_high->unknown_24h` score `3.5387` n `132` status `ready` deltaP `28.6774` edge `0.5852` maxDD `-32.8525`
- `market_context_high->equity_4h` score `3.4716` n `132` status `ready` deltaP `23.8729` edge `0.2396` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `3.1943` n `132` status `ready` deltaP `17.4152` edge `0.1978` maxDD `-1.817`
- `market_context_high->index_4h` score `2.9926` n `132` status `ready` deltaP `24.4872` edge `0.1545` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `2.9614` n `132` status `ready` deltaP `16.0588` edge `0.2261` maxDD `-4.9097`
- `market_context_high->index_24h` score `2.558` n `132` status `ready` deltaP `10.9059` edge `0.2633` maxDD `-4.1604`
- `market_context_high->crypto_major_24h` score `2.4318` n `132` status `ready` deltaP `19.8863` edge `1.0074` maxDD `-60.2561`
- `news_risk_high->fx_4h` score `2.1988` n `43` status `ready` deltaP `27.8892` edge `0.0157` maxDD `-0.1382`
- `market_context_high->metal_4h` score `1.4671` n `132` status `ready` deltaP `17.8954` edge `0.1417` maxDD `-4.7664`
- `news_risk_high->unknown_1h` score `1.3928` n `43` status `ready` deltaP `21.0451` edge `0.0227` maxDD `-1.7548`
- `news_risk_high->unknown_4h` score `1.2783` n `43` status `ready` deltaP `14.4675` edge `0.0824` maxDD `-2.7857`
- `news_risk_high->equity_4h` score `1.2741` n `43` status `ready` deltaP `-2.8361` edge `0.303` maxDD `-4.6598`
- `news_risk_high->commodity_1h` score `0.7549` n `43` status `ready` deltaP `10.7645` edge `0.093` maxDD `-2.1052`
- `market_context_high->equity_24h` score `0.7307` n `132` status `ready` deltaP `21.1174` edge `0.4047` maxDD `-33.1007`
- `news_risk_high->fx_1h` score `0.4381` n `43` status `ready` deltaP `7.8401` edge `0.0099` maxDD `-0.0524`
- `market_context_high->equity_1h` score `0.2681` n `132` status `ready` deltaP `8.7416` edge `0.0429` maxDD `-2.6402`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
