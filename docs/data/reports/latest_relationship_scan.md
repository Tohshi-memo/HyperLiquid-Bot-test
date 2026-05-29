# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T16:52:20.469753+00:00`
- Price records: `672`
- Market context records: `2262`
- Flow alert records: `8407`
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

- `news_risk_high->crypto_alt_24h` score `22.0977` n `43` status `ready` deltaP `52.6405` edge `1.5494` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `15.7511` n `43` status `ready` deltaP `42.2925` edge `1.0746` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.7925` n `43` status `ready` deltaP `33.2647` edge `1.0424` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `11.8652` n `43` status `ready` deltaP `23.2396` edge `0.8919` maxDD `-3.3119`
- `market_context_high->unknown_24h` score `9.2172` n `115` status `ready` deltaP `29.4987` edge `0.6126` maxDD `-1.626`
- `news_risk_high->unknown_24h` score `8.7807` n `43` status `ready` deltaP `33.5432` edge `0.5307` maxDD `-1.4744`
- `market_context_high->crypto_alt_4h` score `8.4563` n `145` status `ready` deltaP `27.5241` edge `0.7891` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `8.1237` n `145` status `ready` deltaP `32.8312` edge `0.6391` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `5.9907` n `115` status `ready` deltaP `16.9505` edge `1.0443` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `5.3455` n `145` status `ready` deltaP `21.7241` edge `0.3616` maxDD `-1.8773`
- `news_risk_high->commodity_4h` score `3.7515` n `43` status `ready` deltaP `32.1575` edge `0.3337` maxDD `-3.0367`
- `news_risk_high->index_24h` score `3.7319` n `43` status `ready` deltaP `12.0559` edge `0.2725` maxDD `-1.3507`
- `news_risk_high->fx_24h` score `3.6399` n `43` status `ready` deltaP `37.2295` edge `0.0736` maxDD `-0.1442`
- `market_context_high->index_24h` score `3.3422` n `115` status `ready` deltaP `13.8557` edge `0.2379` maxDD `-1.4737`
- `news_risk_high->commodity_24h` score `3.1888` n `43` status `ready` deltaP `2.8989` edge `0.3281` maxDD `-3.202`
- `market_context_high->index_4h` score `2.956` n `145` status `ready` deltaP `25.9788` edge `0.1453` maxDD `-2.1063`
- `market_context_high->equity_24h` score `2.4314` n `115` status `ready` deltaP `20.8077` edge `0.2166` maxDD `-6.8828`
- `market_context_high->equity_4h` score `2.3452` n `145` status `ready` deltaP `19.0317` edge `0.209` maxDD `-5.9024`
- `market_context_high->crypto_alt_1h` score `2.331` n `157` status `ready` deltaP `14.1434` edge `0.2187` maxDD `-6.1656`
- `news_risk_high->fx_4h` score `2.0589` n `43` status `ready` deltaP `26.3648` edge `0.0142` maxDD `-0.1382`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
