# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T15:22:30.264372+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11634`

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

- `news_risk_high->unknown_24h` score `53.7433` n `50` status `ready` deltaP `11.6118` edge `4.4012` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `31.7523` n `50` status `ready` deltaP `42.9671` edge `2.4037` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `11.0548` n `56` status `ready` deltaP `22.8223` edge `0.7833` maxDD `-0.1374`
- `news_risk_high->equity_24h` score `5.4631` n `50` status `ready` deltaP `30.1005` edge `0.3474` maxDD `-4.7584`
- `news_risk_high->metal_24h` score `4.3802` n `50` status `ready` deltaP `43.9272` edge `0.0764` maxDD `-0.0053`
- `news_risk_high->crypto_major_24h` score `4.2314` n `50` status `ready` deltaP `21.2617` edge `0.2602` maxDD `-2.6128`
- `news_risk_high->fx_4h` score `3.9749` n `56` status `ready` deltaP `46.2108` edge `0.0322` maxDD `-0.0559`
- `market_context_high->metal_24h` score `2.9712` n `123` status `ready` deltaP `27.228` edge `0.168` maxDD `-3.1535`
- `market_context_high->unknown_24h` score `2.7891` n `123` status `ready` deltaP `5.1077` edge `0.2716` maxDD `-3.1917`
- `market_context_high->unknown_4h` score `2.6015` n `123` status `ready` deltaP `18.0894` edge `0.1369` maxDD `-0.5894`
- `news_risk_high->index_24h` score `2.3614` n `50` status `ready` deltaP `26.9948` edge `0.0319` maxDD `-0.2064`
- `news_risk_high->unknown_1h` score `2.2255` n `57` status `ready` deltaP `13.1632` edge `0.1334` maxDD `-0.8558`
- `news_risk_high->fx_1h` score `1.5014` n `57` status `ready` deltaP `20.1754` edge `0.0076` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.0951` n `123` status `ready` deltaP `8.4563` edge `0.0799` maxDD `-1.6015`
- `news_risk_high->equity_1h` score `0.957` n `57` status `ready` deltaP `14.2295` edge `0.0154` maxDD `-0.4409`
- `news_risk_high->equity_4h` score `0.7834` n `56` status `ready` deltaP `19.4469` edge `0.0471` maxDD `-2.105`
- `news_risk_high->metal_4h` score `0.5973` n `56` status `ready` deltaP `13.3929` edge `0.0136` maxDD `-0.249`
- `news_risk_high->commodity_1h` score `0.531` n `57` status `ready` deltaP `14.3555` edge `0.0044` maxDD `-0.5618`
- `news_risk_high->metal_1h` score `0.3953` n `57` status `ready` deltaP `7.2959` edge `0.0069` maxDD `-0.1413`
- `news_risk_high->index_4h` score `0.0892` n `56` status `ready` deltaP `7.0993` edge `0.0` maxDD `-0.1919`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
