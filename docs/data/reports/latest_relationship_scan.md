# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T15:22:19.398536+00:00`
- Price records: `672`
- Market context records: `2256`
- Flow alert records: `8388`
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

- `news_risk_high->crypto_alt_24h` score `23.213` n `43` status `ready` deltaP `53.6821` edge `1.6354` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `15.958` n `43` status `ready` deltaP `43.3341` edge `1.0849` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.3678` n `43` status `ready` deltaP `34.3063` edge `1.0834` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `12.8209` n `43` status `ready` deltaP `24.2813` edge `0.9646` maxDD `-3.3119`
- `market_context_high->unknown_24h` score `9.8393` n `115` status `ready` deltaP `30.5404` edge `0.6575` maxDD `-1.626`
- `news_risk_high->unknown_24h` score `9.4028` n `43` status `ready` deltaP `34.5849` edge `0.5756` maxDD `-1.4744`
- `market_context_high->crypto_alt_4h` score `8.1762` n `139` status `ready` deltaP `27.2778` edge `0.7674` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `7.8673` n `139` status `ready` deltaP `32.9718` edge `0.6168` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `6.612` n `115` status `ready` deltaP `17.9922` edge `1.117` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `5.4459` n `139` status `ready` deltaP `21.4182` edge `0.372` maxDD `-1.8773`
- `news_risk_high->index_24h` score `3.7824` n `43` status `ready` deltaP `12.4031` edge `0.2744` maxDD `-1.3507`
- `news_risk_high->commodity_4h` score `3.7601` n `43` status `ready` deltaP `32.1575` edge `0.3348` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.6567` n `43` status `ready` deltaP `37.2295` edge `0.075` maxDD `-0.1442`
- `market_context_high->index_4h` score `3.5982` n `139` status `ready` deltaP `28.6663` edge `0.1564` maxDD `-1.1461`
- `market_context_high->index_24h` score `3.3928` n `115` status `ready` deltaP `14.2029` edge `0.2398` maxDD `-1.4737`
- `market_context_high->equity_24h` score `3.0067` n `115` status `ready` deltaP `21.8493` edge `0.2576` maxDD `-6.8828`
- `news_risk_high->commodity_24h` score `2.9747` n `43` status `ready` deltaP `1.8572` edge `0.3172` maxDD `-3.202`
- `market_context_high->equity_4h` score `2.2616` n `139` status `ready` deltaP `19.1426` edge `0.2013` maxDD `-5.9024`
- `market_context_high->crypto_alt_1h` score `2.0885` n `151` status `ready` deltaP `13.9618` edge `0.1997` maxDD `-6.1656`
- `news_risk_high->fx_4h` score `2.0661` n `43` status `ready` deltaP `26.3648` edge `0.0148` maxDD `-0.1382`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
