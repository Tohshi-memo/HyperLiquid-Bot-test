# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T07:52:18.913596+00:00`
- Price records: `672`
- Market context records: `2328`
- Flow alert records: `8592`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9168`

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

- `news_risk_high->crypto_alt_24h` score `20.7589` n `43` status `ready` deltaP `50.0363` edge `1.4552` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `16.4404` n `43` status `ready` deltaP `43.3341` edge `1.1251` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.1331` n `43` status `ready` deltaP `29.7925` edge `1.0106` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.457` n `43` status `ready` deltaP `19.7674` edge `0.7977` maxDD `-3.3119`
- `market_context_high->unknown_24h` score `7.4487` n `125` status `ready` deltaP `24.1181` edge `0.5011` maxDD `-1.626`
- `news_risk_high->unknown_24h` score `7.0058` n `43` status `ready` deltaP `27.4669` edge `0.4233` maxDD `-1.4744`
- `market_context_high->crypto_alt_4h` score `6.9103` n `159` status `ready` deltaP `23.3941` edge `0.6878` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `6.8795` n `159` status `ready` deltaP `27.1494` edge `0.5733` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `5.778` n `125` status `ready` deltaP `16.4` edge `1.0207` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `5.2781` n `159` status `ready` deltaP `21.2408` edge `0.3592` maxDD `-1.8773`
- `news_risk_high->index_24h` score `4.2568` n `43` status `ready` deltaP `11.8823` edge `0.3174` maxDD `-1.3507`
- `news_risk_high->commodity_4h` score `4.0144` n `43` status `ready` deltaP `34.1392` edge `0.3542` maxDD `-3.0367`
- `market_context_high->index_24h` score `3.4455` n `125` status `ready` deltaP `14.4125` edge `0.2428` maxDD `-1.4737`
- `news_risk_high->fx_24h` score `3.4083` n `43` status `ready` deltaP `36.0142` edge `0.0624` maxDD `-0.1442`
- `news_risk_high->fx_4h` score `2.1708` n `43` status `ready` deltaP `27.5843` edge `0.0154` maxDD `-0.1382`
- `market_context_high->index_4h` score `2.1024` n `159` status `ready` deltaP `20.6521` edge `0.1201` maxDD `-2.2732`
- `market_context_high->crypto_alt_1h` score `1.9071` n `159` status `ready` deltaP `12.4741` edge `0.1945` maxDD `-6.1656`
- `market_context_high->equity_24h` score `1.779` n `125` status `ready` deltaP `18.5181` edge `0.1775` maxDD `-6.8828`
- `news_risk_high->commodity_24h` score `1.7651` n `43` status `ready` deltaP `4.2878` edge `0.2002` maxDD `-3.202`
- `market_context_high->crypto_major_1h` score `1.6457` n `159` status `ready` deltaP `12.4741` edge `0.1734` maxDD `-4.2199`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
