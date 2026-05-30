# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T10:22:18.158289+00:00`
- Price records: `672`
- Market context records: `2339`
- Flow alert records: `8623`
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

- `news_risk_high->crypto_alt_24h` score `20.9137` n `43` status `ready` deltaP `50.0363` edge `1.4681` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `16.7046` n `43` status `ready` deltaP `43.6813` edge `1.1448` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.4019` n `43` status `ready` deltaP `29.7925` edge `1.033` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.6886` n `43` status `ready` deltaP `19.7674` edge `0.817` maxDD `-3.3119`
- `market_context_high->crypto_major_24h` score `9.854` n `135` status `ready` deltaP `18.8889` edge `1.0845` maxDD `-25.1408`
- `news_risk_high->unknown_24h` score `7.3833` n `43` status `ready` deltaP `27.6405` edge `0.4536` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `7.1988` n `135` status `ready` deltaP `24.1436` edge `0.4801` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `6.5556` n `159` status `ready` deltaP `22.7843` edge `0.6623` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `6.4948` n `159` status `ready` deltaP `25.6251` edge `0.5514` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `5.3928` n `159` status `ready` deltaP `21.8505` edge `0.3647` maxDD `-1.8773`
- `news_risk_high->index_24h` score `4.498` n `43` status `ready` deltaP `11.8823` edge `0.3375` maxDD `-1.3507`
- `news_risk_high->commodity_4h` score `4.0223` n `43` status `ready` deltaP `34.2916` edge `0.3542` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.415` n `43` status `ready` deltaP `36.1879` edge `0.0618` maxDD `-0.1442`
- `market_context_high->index_24h` score `3.3998` n `135` status `ready` deltaP `15.7755` edge `0.2299` maxDD `-1.4737`
- `market_context_high->equity_24h` score `2.2124` n `135` status `ready` deltaP `19.5255` edge `0.2069` maxDD `-6.8828`
- `news_risk_high->fx_4h` score `2.0697` n `43` status `ready` deltaP `26.3648` edge `0.0151` maxDD `-0.1382`
- `market_context_high->index_4h` score `1.9822` n `159` status `ready` deltaP `19.585` edge `0.1172` maxDD `-2.2732`
- `market_context_high->crypto_alt_1h` score `1.7389` n `163` status `ready` deltaP `12.3214` edge `0.1815` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `1.5219` n `163` status `ready` deltaP `12.3214` edge `0.1641` maxDD `-4.2199`
- `news_risk_high->commodity_24h` score `1.2491` n `43` status `ready` deltaP `4.2878` edge `0.1572` maxDD `-3.202`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
