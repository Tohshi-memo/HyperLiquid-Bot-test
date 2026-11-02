# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T06:07:28.272122+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5047`

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

- `market_context_high->unknown_24h` score `6747.0307` n `38` status `ready` deltaP `1.3889` edge `562.2433` maxDD `0.0`
- `market_context_high->unknown_4h` score `503.9777` n `43` status `ready` deltaP `8.8415` edge `41.9392` maxDD `0.0`
- `market_context_high->unknown_1h` score `111.1671` n `43` status `ready` deltaP `6.2666` edge `9.2332` maxDD `-0.2178`
- `market_context_high->equity_24h` score `19.0789` n `38` status `ready` deltaP `41.9865` edge `1.3336` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `13.939` n `94` status `ready` deltaP `34.2605` edge `1.0688` maxDD `-6.8493`
- `market_context_high->commodity_24h` score `7.1527` n `38` status `ready` deltaP `44.1063` edge `0.3331` maxDD `-0.8203`
- `market_context_high->index_24h` score `6.627` n `38` status `ready` deltaP `49.1319` edge `0.2247` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `6.3767` n `43` status `ready` deltaP `27.3185` edge `0.3787` maxDD `-1.6876`
- `market_context_high->equity_4h` score `5.6076` n `43` status `ready` deltaP `13.0212` edge `0.4507` maxDD `-2.283`
- `market_context_high->crypto_major_4h` score `5.0536` n `43` status `ready` deltaP `25.8686` edge `0.2823` maxDD `-1.6901`
- `news_risk_high->crypto_alt_4h` score `2.3256` n `126` status `ready` deltaP `9.4706` edge `0.2693` maxDD `-7.4246`
- `market_context_high->equity_1h` score `2.297` n `43` status `ready` deltaP `5.2152` edge `0.1967` maxDD `-1.2043`
- `market_context_high->metal_4h` score `2.0037` n `43` status `ready` deltaP `22.9297` edge `0.0566` maxDD `-0.7323`
- `market_context_high->crypto_alt_24h` score `1.8503` n `38` status `ready` deltaP `-7.1729` edge `0.3538` maxDD `-8.8096`
- `market_context_high->crypto_alt_1h` score `1.5126` n `43` status `ready` deltaP `3.7878` edge `0.1468` maxDD `-1.6799`
- `market_context_high->commodity_4h` score `1.3887` n `43` status `ready` deltaP `25.3332` edge `0.0504` maxDD `-1.633`
- `market_context_high->crypto_major_1h` score `1.3536` n `43` status `ready` deltaP `5.5146` edge `0.1167` maxDD `-1.2532`
- `market_context_high->index_4h` score `0.9247` n `43` status `ready` deltaP `13.1736` edge `0.0345` maxDD `-1.2876`
- `market_context_high->metal_1h` score `0.6733` n `43` status `ready` deltaP `9.4068` edge `0.0191` maxDD `-0.3895`
- `market_context_high->fx_1h` score `0.6059` n `43` status `ready` deltaP `12.9404` edge `0.009` maxDD `-0.0736`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
