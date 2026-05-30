# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T04:22:19.534671+00:00`
- Price records: `672`
- Market context records: `2313`
- Flow alert records: `8549`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9291`

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

- `news_risk_high->crypto_alt_24h` score `20.6605` n `43` status `ready` deltaP `50.0363` edge `1.447` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `15.9415` n `43` status `ready` deltaP `41.598` edge `1.0951` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `13.7467` n `43` status `ready` deltaP `29.7925` edge `0.9784` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.2962` n `43` status `ready` deltaP `19.7674` edge `0.7843` maxDD `-3.3119`
- `market_context_high->crypto_alt_4h` score `7.2387` n `159` status `ready` deltaP `24.0038` edge `0.7111` maxDD `-15.4319`
- `market_context_high->unknown_24h` score `7.2299` n `115` status `ready` deltaP `23.4224` edge `0.4875` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `7.1955` n `159` status `ready` deltaP `28.369` edge `0.5915` maxDD `-10.1468`
- `news_risk_high->unknown_24h` score `6.7934` n `43` status `ready` deltaP `27.4669` edge `0.4056` maxDD `-1.4744`
- `market_context_high->unknown_4h` score `5.4412` n `159` status `ready` deltaP `22.1554` edge `0.3667` maxDD `-1.8773`
- `market_context_high->crypto_major_24h` score `4.9709` n `115` status `ready` deltaP `13.4783` edge `0.9367` maxDD `-25.1408`
- `news_risk_high->commodity_4h` score `3.9522` n `43` status `ready` deltaP `33.377` edge `0.3513` maxDD `-3.0367`
- `news_risk_high->index_24h` score `3.911` n `43` status `ready` deltaP `11.5351` edge `0.2909` maxDD `-1.3507`
- `market_context_high->index_24h` score `3.5213` n `115` status `ready` deltaP `13.3349` edge `0.2563` maxDD `-1.4737`
- `news_risk_high->fx_24h` score `3.4155` n `43` status `ready` deltaP `36.0142` edge `0.063` maxDD `-0.1442`
- `news_risk_high->commodity_24h` score `2.5043` n `43` status `ready` deltaP `4.2878` edge `0.2618` maxDD `-3.202`
- `market_context_high->index_4h` score `2.2735` n `159` status `ready` deltaP `22.1765` edge `0.1242` maxDD `-2.2732`
- `news_risk_high->fx_4h` score `2.183` n `43` status `ready` deltaP `27.7368` edge `0.0154` maxDD `-0.1382`
- `market_context_high->crypto_alt_1h` score `1.9323` n `159` status `ready` deltaP `12.6238` edge `0.1956` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `1.6913` n `159` status `ready` deltaP `12.7735` edge `0.1752` maxDD `-4.2199`
- `market_context_high->equity_4h` score `1.5885` n `159` status `ready` deltaP `15.1835` edge `0.1716` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
