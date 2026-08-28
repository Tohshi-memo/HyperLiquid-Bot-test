# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T13:37:28.877389+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11609`

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

- `news_risk_high->unknown_24h` score `53.6305` n `50` status `ready` deltaP `11.6118` edge `4.3918` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `31.3169` n `50` status `ready` deltaP `41.7539` edge `2.3755` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `10.9264` n `56` status `ready` deltaP `21.9077` edge `0.7787` maxDD `-0.1374`
- `news_risk_high->equity_24h` score `5.4415` n `50` status `ready` deltaP `30.1005` edge `0.3456` maxDD `-4.7584`
- `news_risk_high->metal_24h` score `4.596` n `50` status `ready` deltaP `45.1404` edge `0.0863` maxDD `-0.0053`
- `news_risk_high->fx_4h` score `3.9091` n `56` status `ready` deltaP `45.4486` edge `0.0318` maxDD `-0.0559`
- `news_risk_high->crypto_major_24h` score `3.5284` n `50` status `ready` deltaP `20.0485` edge `0.2097` maxDD `-2.6128`
- `market_context_high->metal_24h` score `2.6401` n `130` status `ready` deltaP `24.0635` edge `0.1615` maxDD `-3.1535`
- `news_risk_high->index_24h` score `2.4801` n `50` status `ready` deltaP `28.208` edge `0.0337` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.3813` n `130` status `ready` deltaP `18.0066` edge `0.1191` maxDD `-0.5894`
- `news_risk_high->unknown_1h` score `2.1988` n `56` status `ready` deltaP `12.8743` edge `0.1331` maxDD `-0.8558`
- `market_context_high->unknown_24h` score `2.0083` n `130` status `ready` deltaP `5.458` edge `0.2042` maxDD `-3.1917`
- `news_risk_high->fx_1h` score `1.4803` n `56` status `ready` deltaP `19.9423` edge `0.0074` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.1087` n `56` status `ready` deltaP `15.601` edge `0.0189` maxDD `-0.4409`
- `market_context_high->unknown_1h` score `0.9354` n `130` status `ready` deltaP `7.1051` edge `0.0756` maxDD `-1.6015`
- `news_risk_high->equity_4h` score `0.7834` n `56` status `ready` deltaP `19.4469` edge `0.0471` maxDD `-2.105`
- `news_risk_high->metal_4h` score `0.5535` n `56` status `ready` deltaP `12.9356` edge `0.013` maxDD `-0.249`
- `news_risk_high->commodity_1h` score `0.5194` n `56` status `ready` deltaP `14.1467` edge `0.0043` maxDD `-0.5618`
- `news_risk_high->metal_1h` score `0.3351` n `56` status `ready` deltaP `6.8435` edge `0.0049` maxDD `-0.1413`
- `news_risk_high->index_4h` score `0.1208` n `56` status `ready` deltaP `7.4042` edge `0.0006` maxDD `-0.1919`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
