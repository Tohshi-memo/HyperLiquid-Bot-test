# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T15:07:21.625098+00:00`
- Price records: `672`
- Market context records: `2255`
- Flow alert records: `8385`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9257`

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

- `news_risk_high->crypto_alt_24h` score `23.4057` n `43` status `ready` deltaP `53.8557` edge `1.6503` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `16.0091` n `43` status `ready` deltaP `43.5077` edge `1.088` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.4585` n `43` status `ready` deltaP `34.48` edge `1.0898` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `12.9872` n `43` status `ready` deltaP `24.4549` edge `0.9773` maxDD `-3.3119`
- `market_context_high->unknown_24h` score `9.9144` n `115` status `ready` deltaP `30.714` edge `0.6626` maxDD `-1.626`
- `news_risk_high->unknown_24h` score `9.4779` n `43` status `ready` deltaP `34.7585` edge `0.5807` maxDD `-1.4744`
- `market_context_high->crypto_alt_4h` score `8.2334` n `138` status `ready` deltaP `27.2269` edge `0.7725` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `7.8987` n `138` status `ready` deltaP `32.9887` edge `0.6193` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `6.7201` n `115` status `ready` deltaP `18.1658` edge `1.1297` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `5.4684` n `138` status `ready` deltaP `21.2045` edge `0.3753` maxDD `-1.8773`
- `news_risk_high->index_24h` score `3.8011` n `43` status `ready` deltaP `12.5767` edge `0.2748` maxDD `-1.3507`
- `news_risk_high->commodity_4h` score `3.7585` n `43` status `ready` deltaP `32.1575` edge `0.3346` maxDD `-3.0367`
- `market_context_high->index_4h` score `3.7174` n `138` status `ready` deltaP `29.1446` edge `0.1592` maxDD `-0.8303`
- `news_risk_high->fx_24h` score `3.6591` n `43` status `ready` deltaP `37.2295` edge `0.0752` maxDD `-0.1442`
- `market_context_high->index_24h` score `3.4115` n `115` status `ready` deltaP `14.3765` edge `0.2402` maxDD `-1.4737`
- `market_context_high->equity_24h` score `3.0974` n `115` status `ready` deltaP `22.023` edge `0.264` maxDD `-6.8828`
- `news_risk_high->commodity_24h` score `2.9308` n `43` status `ready` deltaP `1.6836` edge `0.3147` maxDD `-3.202`
- `market_context_high->equity_4h` score `2.2758` n `138` status `ready` deltaP `19.1543` edge `0.2024` maxDD `-5.9024`
- `news_risk_high->fx_4h` score `2.0673` n `43` status `ready` deltaP `26.3648` edge `0.0149` maxDD `-0.1382`
- `market_context_high->crypto_alt_1h` score `1.9799` n `150` status `ready` deltaP `13.7146` edge `0.1923` maxDD `-6.1656`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
