# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T03:07:17.849322+00:00`
- Price records: `672`
- Market context records: `2307`
- Flow alert records: `8533`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9290`

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

- `news_risk_high->crypto_alt_24h` score `20.6041` n `43` status `ready` deltaP `50.0363` edge `1.4423` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `15.8316` n `43` status `ready` deltaP `41.4244` edge `1.0871` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `13.6315` n `43` status `ready` deltaP `29.7925` edge `0.9688` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.259` n `43` status `ready` deltaP `19.7674` edge `0.7812` maxDD `-3.3119`
- `market_context_high->crypto_alt_4h` score `7.3217` n `159` status `ready` deltaP `24.1563` edge `0.717` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `7.2979` n `159` status `ready` deltaP `28.6738` edge `0.598` maxDD `-10.1468`
- `market_context_high->unknown_24h` score `7.2023` n `115` status `ready` deltaP `23.4224` edge `0.4852` maxDD `-1.626`
- `news_risk_high->unknown_24h` score `6.7658` n `43` status `ready` deltaP `27.4669` edge `0.4033` maxDD `-1.4744`
- `market_context_high->unknown_4h` score `5.5122` n `159` status `ready` deltaP `22.3079` edge `0.3716` maxDD `-1.8773`
- `market_context_high->crypto_major_24h` score `4.9467` n `115` status `ready` deltaP `13.4783` edge `0.9336` maxDD `-25.1408`
- `news_risk_high->commodity_4h` score `3.9103` n `43` status `ready` deltaP `32.7673` edge `0.35` maxDD `-3.0367`
- `news_risk_high->index_24h` score `3.8114` n `43` status `ready` deltaP `11.5351` edge `0.2826` maxDD `-1.3507`
- `market_context_high->index_24h` score `3.4217` n `115` status `ready` deltaP `13.3349` edge `0.248` maxDD `-1.4737`
- `news_risk_high->fx_24h` score `3.4215` n `43` status `ready` deltaP `36.0142` edge `0.0635` maxDD `-0.1442`
- `news_risk_high->commodity_24h` score `2.7827` n `43` status `ready` deltaP `4.2878` edge `0.285` maxDD `-3.202`
- `market_context_high->index_4h` score `2.2238` n `159` status `ready` deltaP `21.7192` edge `0.1231` maxDD `-2.2732`
- `news_risk_high->fx_4h` score `2.2196` n `43` status `ready` deltaP `28.1941` edge `0.0154` maxDD `-0.1382`
- `market_context_high->crypto_alt_1h` score `1.8064` n `159` status `ready` deltaP `12.025` edge `0.1891` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `1.6242` n `159` status `ready` deltaP `12.3244` edge `0.1726` maxDD `-4.2199`
- `market_context_high->equity_4h` score `1.6175` n `159` status `ready` deltaP `15.336` edge `0.173` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
