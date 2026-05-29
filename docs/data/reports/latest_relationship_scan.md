# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T21:04:23.353157+00:00`
- Price records: `672`
- Market context records: `2280`
- Flow alert records: `8459`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9287`

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

- `news_risk_high->crypto_alt_24h` score `20.4613` n `43` status `ready` deltaP `50.0363` edge `1.4304` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `15.5294` n `43` status `ready` deltaP `40.5563` edge `1.0677` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `13.7068` n `43` status `ready` deltaP `30.3133` edge `0.9716` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.3787` n `43` status `ready` deltaP `20.2882` edge `0.7877` maxDD `-3.3119`
- `market_context_high->unknown_24h` score `7.9107` n `115` status `ready` deltaP `26.5474` edge `0.5234` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `7.8729` n `159` status `ready` deltaP `25.3758` edge `0.7548` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `7.7074` n `159` status `ready` deltaP `29.8933` edge `0.624` maxDD `-10.1468`
- `news_risk_high->unknown_24h` score `7.4742` n `43` status `ready` deltaP `30.5919` edge `0.4415` maxDD `-1.4744`
- `market_context_high->unknown_4h` score `5.6126` n `159` status `ready` deltaP `22.003` edge `0.382` maxDD `-1.8773`
- `market_context_high->crypto_major_24h` score `5.0245` n `115` status `ready` deltaP `13.9991` edge `0.9401` maxDD `-25.1408`
- `news_risk_high->commodity_4h` score `3.8065` n `43` status `ready` deltaP `32.6148` edge `0.3377` maxDD `-3.0367`
- `news_risk_high->index_24h` score `3.6477` n `43` status `ready` deltaP `11.7087` edge `0.2678` maxDD `-1.3507`
- `news_risk_high->fx_24h` score `3.5799` n `43` status `ready` deltaP `37.2295` edge `0.0686` maxDD `-0.1442`
- `news_risk_high->commodity_24h` score `3.5562` n `43` status `ready` deltaP `4.4614` edge `0.3483` maxDD `-3.202`
- `market_context_high->index_24h` score `3.258` n `115` status `ready` deltaP `13.5085` edge `0.2332` maxDD `-1.4737`
- `market_context_high->index_4h` score `2.4833` n `159` status `ready` deltaP `23.8533` edge `0.1305` maxDD `-2.2732`
- `market_context_high->crypto_alt_1h` score `2.183` n `159` status `ready` deltaP `13.2226` edge `0.2125` maxDD `-6.1656`
- `market_context_high->equity_4h` score `2.1456` n `159` status `ready` deltaP `18.2323` edge `0.1977` maxDD `-5.9024`
- `news_risk_high->fx_4h` score `2.1124` n `43` status `ready` deltaP `26.9746` edge `0.0146` maxDD `-0.1382`
- `market_context_high->crypto_major_1h` score `1.9228` n `159` status `ready` deltaP `13.6717` edge `0.1885` maxDD `-4.2199`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
