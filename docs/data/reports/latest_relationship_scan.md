# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T07:22:17.009815+00:00`
- Price records: `672`
- Market context records: `2325`
- Flow alert records: `8586`
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

- `news_risk_high->crypto_alt_24h` score `20.7481` n `43` status `ready` deltaP `50.0363` edge `1.4543` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `16.361` n `43` status `ready` deltaP `42.9869` edge `1.1208` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.0791` n `43` status `ready` deltaP `29.7925` edge `1.0061` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.4414` n `43` status `ready` deltaP `19.7674` edge `0.7964` maxDD `-3.3119`
- `market_context_high->unknown_24h` score `7.5643` n `123` status `ready` deltaP `23.988` edge `0.5116` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `6.9871` n `159` status `ready` deltaP `23.3941` edge `0.6942` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `6.9603` n `159` status `ready` deltaP `27.4543` edge `0.578` maxDD `-10.1468`
- `news_risk_high->unknown_24h` score `6.929` n `43` status `ready` deltaP `27.4669` edge `0.4169` maxDD `-1.4744`
- `market_context_high->crypto_major_24h` score `5.624` n `123` status `ready` deltaP `15.8537` edge `1.0046` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `5.2747` n `159` status `ready` deltaP `21.3932` edge `0.3579` maxDD `-1.8773`
- `news_risk_high->index_24h` score `4.216` n `43` status `ready` deltaP `11.8823` edge `0.314` maxDD `-1.3507`
- `news_risk_high->commodity_4h` score `4.0049` n `43` status `ready` deltaP `33.9868` edge `0.354` maxDD `-3.0367`
- `market_context_high->index_24h` score `3.4552` n `123` status `ready` deltaP `14.1133` edge `0.2456` maxDD `-1.4737`
- `news_risk_high->fx_24h` score `3.4083` n `43` status `ready` deltaP `36.0142` edge `0.0624` maxDD `-0.1442`
- `news_risk_high->fx_4h` score `2.1964` n `43` status `ready` deltaP `27.8892` edge `0.0155` maxDD `-0.1382`
- `market_context_high->index_4h` score `2.14` n `159` status `ready` deltaP `20.957` edge `0.1212` maxDD `-2.2732`
- `market_context_high->crypto_alt_1h` score `1.9083` n `159` status `ready` deltaP `12.4741` edge `0.1946` maxDD `-6.1656`
- `news_risk_high->commodity_24h` score `1.8611` n `43` status `ready` deltaP `4.2878` edge `0.2082` maxDD `-3.202`
- `market_context_high->equity_24h` score `1.7037` n `123` status `ready` deltaP `18.297` edge `0.1727` maxDD `-6.8828`
- `market_context_high->crypto_major_1h` score `1.6481` n `159` status `ready` deltaP `12.4741` edge `0.1736` maxDD `-4.2199`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
