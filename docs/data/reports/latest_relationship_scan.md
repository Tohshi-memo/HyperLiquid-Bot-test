# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T04:52:15.243530+00:00`
- Price records: `672`
- Market context records: `2315`
- Flow alert records: `8555`
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

- `news_risk_high->crypto_alt_24h` score `20.7085` n `43` status `ready` deltaP `50.0363` edge `1.451` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `16.0221` n `43` status `ready` deltaP `41.9452` edge `1.0995` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `13.8055` n `43` status `ready` deltaP `29.7925` edge `0.9833` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.3454` n `43` status `ready` deltaP `19.7674` edge `0.7884` maxDD `-3.3119`
- `market_context_high->unknown_24h` score `7.2527` n `115` status `ready` deltaP `23.4224` edge `0.4894` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `7.2193` n `159` status `ready` deltaP `23.8514` edge `0.7105` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `7.1907` n `159` status `ready` deltaP `28.369` edge `0.5911` maxDD `-10.1468`
- `news_risk_high->unknown_24h` score `6.8162` n `43` status `ready` deltaP `27.4669` edge `0.4075` maxDD `-1.4744`
- `market_context_high->unknown_4h` score `5.434` n `159` status `ready` deltaP `22.1554` edge `0.3661` maxDD `-1.8773`
- `market_context_high->crypto_major_24h` score `5.0029` n `115` status `ready` deltaP `13.4783` edge `0.9408` maxDD `-25.1408`
- `news_risk_high->commodity_4h` score `3.9568` n `43` status `ready` deltaP `33.377` edge `0.3519` maxDD `-3.0367`
- `news_risk_high->index_24h` score `3.9554` n `43` status `ready` deltaP `11.5351` edge `0.2946` maxDD `-1.3507`
- `market_context_high->index_24h` score `3.5657` n `115` status `ready` deltaP `13.3349` edge `0.26` maxDD `-1.4737`
- `news_risk_high->fx_24h` score `3.4131` n `43` status `ready` deltaP `36.0142` edge `0.0628` maxDD `-0.1442`
- `news_risk_high->commodity_24h` score `2.3951` n `43` status `ready` deltaP `4.2878` edge `0.2527` maxDD `-3.202`
- `market_context_high->index_4h` score `2.2735` n `159` status `ready` deltaP `22.1765` edge `0.1242` maxDD `-2.2732`
- `news_risk_high->fx_4h` score `2.1952` n `43` status `ready` deltaP `27.8892` edge `0.0154` maxDD `-0.1382`
- `market_context_high->crypto_alt_1h` score `1.9766` n `159` status `ready` deltaP `12.7735` edge `0.1983` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `1.7261` n `159` status `ready` deltaP `12.9232` edge `0.1771` maxDD `-4.2199`
- `market_context_high->equity_4h` score `1.5545` n `159` status `ready` deltaP `14.8787` edge `0.1708` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
