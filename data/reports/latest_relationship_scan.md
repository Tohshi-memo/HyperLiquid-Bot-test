# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T23:37:25.682489+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7053`

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

- `market_context_high->unknown_24h` score `7573.3543` n `55` status `ready` deltaP `1.3889` edge `631.1036` maxDD `0.0`
- `market_context_high->unknown_4h` score `337.1198` n `55` status `ready` deltaP `7.1757` edge `28.0498` maxDD `-0.0124`
- `market_context_high->unknown_1h` score `39.9518` n `55` status `ready` deltaP `4.3604` edge `3.3113` maxDD `-0.2178`
- `market_context_high->equity_24h` score `21.28` n `55` status `ready` deltaP `42.7999` edge `1.5116` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `13.2942` n `94` status `ready` deltaP `31.1355` edge `1.0359` maxDD `-6.8493`
- `market_context_high->index_24h` score `6.1884` n `55` status `ready` deltaP `49.3056` edge `0.187` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `6.1374` n `55` status `ready` deltaP `24.2073` edge `0.3795` maxDD `-1.6876`
- `market_context_high->commodity_24h` score `5.8885` n `55` status `ready` deltaP `40.7545` edge `0.2501` maxDD `-0.8203`
- `market_context_high->crypto_major_4h` score `5.5757` n `55` status `ready` deltaP `31.0449` edge `0.2913` maxDD `-1.6901`
- `market_context_high->equity_4h` score `3.3026` n `55` status `ready` deltaP `6.0477` edge `0.3051` maxDD `-2.283`
- `market_context_high->commodity_4h` score `3.0656` n `55` status `ready` deltaP `29.3902` edge `0.0846` maxDD `-0.3387`
- `news_risk_high->crypto_alt_4h` score `2.4595` n `126` status `ready` deltaP `10.0803` edge `0.2764` maxDD `-7.4246`
- `market_context_high->crypto_major_24h` score `2.3919` n `55` status `ready` deltaP `10.3378` edge `0.3054` maxDD `-3.0799`
- `market_context_high->crypto_alt_24h` score `1.9516` n `55` status `ready` deltaP `-4.1256` edge `0.4295` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.7603` n `55` status `ready` deltaP `20.6374` edge `0.0516` maxDD `-0.7323`
- `market_context_high->equity_1h` score `1.5692` n `55` status `ready` deltaP `3.4758` edge `0.1601` maxDD `-1.5336`
- `market_context_high->crypto_alt_1h` score `1.4111` n `55` status `ready` deltaP `3.7752` edge `0.1595` maxDD `-2.3659`
- `market_context_high->crypto_major_1h` score `1.4024` n `55` status `ready` deltaP `8.0321` edge `0.1243` maxDD `-2.2118`
- `market_context_high->metal_1h` score `0.987` n `55` status `ready` deltaP `12.2237` edge `0.0256` maxDD `-0.3209`
- `market_context_high->fx_1h` score `0.5646` n `55` status `ready` deltaP `13.6364` edge `-0.0001` maxDD `-0.1407`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
