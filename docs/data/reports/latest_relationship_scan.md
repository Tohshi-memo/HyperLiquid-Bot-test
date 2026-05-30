# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T10:07:20.218179+00:00`
- Price records: `672`
- Market context records: `2338`
- Flow alert records: `8620`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9176`

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

- `news_risk_high->crypto_alt_24h` score `20.9005` n `43` status `ready` deltaP `50.0363` edge `1.467` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `16.6818` n `43` status `ready` deltaP `43.6813` edge `1.1429` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.3755` n `43` status `ready` deltaP `29.7925` edge `1.0308` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.6622` n `43` status `ready` deltaP `19.7674` edge `0.8148` maxDD `-3.3119`
- `market_context_high->crypto_major_24h` score `9.7406` n `134` status `ready` deltaP `18.6567` edge `1.0766` maxDD `-25.1408`
- `news_risk_high->unknown_24h` score `7.3557` n `43` status `ready` deltaP `27.6405` edge `0.4513` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `7.1975` n `134` status `ready` deltaP `24.0827` edge `0.4804` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `6.5942` n `159` status `ready` deltaP `22.9368` edge `0.6645` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `6.5262` n `159` status `ready` deltaP `25.7775` edge `0.553` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `5.388` n `159` status `ready` deltaP `21.8505` edge `0.3643` maxDD `-1.8773`
- `news_risk_high->index_24h` score `4.4716` n `43` status `ready` deltaP `11.8823` edge `0.3353` maxDD `-1.3507`
- `news_risk_high->commodity_4h` score `4.0136` n `43` status `ready` deltaP `34.1392` edge `0.3541` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.4162` n `43` status `ready` deltaP `36.1879` edge `0.0619` maxDD `-0.1442`
- `market_context_high->index_24h` score `3.4004` n `134` status `ready` deltaP `15.6483` edge `0.2308` maxDD `-1.4737`
- `market_context_high->equity_24h` score `2.1605` n `134` status `ready` deltaP `19.4315` edge `0.2032` maxDD `-6.8828`
- `news_risk_high->fx_4h` score `2.0819` n `43` status `ready` deltaP `26.5173` edge `0.0151` maxDD `-0.1382`
- `market_context_high->index_4h` score `1.9834` n `159` status `ready` deltaP `19.585` edge `0.1173` maxDD `-2.2732`
- `market_context_high->crypto_alt_1h` score `1.7681` n `162` status `ready` deltaP `12.2514` edge `0.1844` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `1.5391` n `162` status `ready` deltaP `12.2514` edge `0.166` maxDD `-4.2199`
- `news_risk_high->commodity_24h` score `1.2959` n `43` status `ready` deltaP `4.2878` edge `0.1611` maxDD `-3.202`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
