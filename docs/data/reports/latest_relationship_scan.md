# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T08:07:18.032649+00:00`
- Price records: `672`
- Market context records: `2329`
- Flow alert records: `8595`
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

- `news_risk_high->crypto_alt_24h` score `20.7661` n `43` status `ready` deltaP `50.0363` edge `1.4558` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `16.4644` n `43` status `ready` deltaP `43.3341` edge `1.1271` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.1631` n `43` status `ready` deltaP `29.7925` edge `1.0131` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.4738` n `43` status `ready` deltaP `19.7674` edge `0.7991` maxDD `-3.3119`
- `market_context_high->unknown_24h` score `7.419` n `126` status `ready` deltaP `24.1816` edge `0.4982` maxDD `-1.626`
- `news_risk_high->unknown_24h` score `7.0394` n `43` status `ready` deltaP `27.4669` edge `0.4261` maxDD `-1.4744`
- `market_context_high->crypto_alt_4h` score `6.8755` n `159` status `ready` deltaP `23.3941` edge `0.6849` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `6.8397` n `159` status `ready` deltaP `26.997` edge `0.571` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `5.8418` n `126` status `ready` deltaP `16.6667` edge `1.0271` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `5.3059` n `159` status `ready` deltaP `21.3932` edge `0.3605` maxDD `-1.8773`
- `news_risk_high->index_24h` score `4.2784` n `43` status `ready` deltaP `11.8823` edge `0.3192` maxDD `-1.3507`
- `news_risk_high->commodity_4h` score `4.0152` n `43` status `ready` deltaP `34.1392` edge `0.3543` maxDD `-3.0367`
- `market_context_high->index_24h` score `3.4428` n `126` status `ready` deltaP `14.5585` edge `0.2416` maxDD `-1.4737`
- `news_risk_high->fx_24h` score `3.4083` n `43` status `ready` deltaP `36.0142` edge `0.0624` maxDD `-0.1442`
- `news_risk_high->fx_4h` score `2.1574` n `43` status `ready` deltaP `27.4319` edge `0.0153` maxDD `-0.1382`
- `market_context_high->index_4h` score `2.0854` n `159` status `ready` deltaP `20.4997` edge `0.1197` maxDD `-2.2732`
- `market_context_high->crypto_alt_1h` score `1.8891` n `159` status `ready` deltaP `12.3244` edge `0.194` maxDD `-6.1656`
- `market_context_high->equity_24h` score `1.8129` n `126` status `ready` deltaP `18.626` edge `0.1796` maxDD `-6.8828`
- `news_risk_high->commodity_24h` score `1.7195` n `43` status `ready` deltaP `4.2878` edge `0.1964` maxDD `-3.202`
- `market_context_high->crypto_major_1h` score `1.6433` n `159` status `ready` deltaP `12.4741` edge `0.1732` maxDD `-4.2199`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
