# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T01:52:16.356918+00:00`
- Price records: `672`
- Market context records: `2302`
- Flow alert records: `8518`
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

- `news_risk_high->crypto_alt_24h` score `20.6077` n `43` status `ready` deltaP `50.0363` edge `1.4426` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `15.7198` n `43` status `ready` deltaP `41.0772` edge `1.0801` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `13.5883` n `43` status `ready` deltaP `29.7925` edge `0.9652` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.3262` n `43` status `ready` deltaP `19.7674` edge `0.7868` maxDD `-3.3119`
- `market_context_high->crypto_alt_4h` score `7.4587` n `159` status `ready` deltaP `24.3087` edge `0.7274` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `7.4521` n `159` status `ready` deltaP `29.1311` edge `0.6078` maxDD `-10.1468`
- `market_context_high->unknown_24h` score `7.2438` n `115` status `ready` deltaP `23.596` edge `0.4875` maxDD `-1.626`
- `news_risk_high->unknown_24h` score `6.8073` n `43` status `ready` deltaP `27.6405` edge `0.4056` maxDD `-1.4744`
- `market_context_high->unknown_4h` score `5.5734` n `159` status `ready` deltaP `22.3079` edge `0.3767` maxDD `-1.8773`
- `market_context_high->crypto_major_24h` score `4.9904` n `115` status `ready` deltaP `13.4783` edge `0.9392` maxDD `-25.1408`
- `news_risk_high->commodity_4h` score `3.8962` n `43` status `ready` deltaP `32.6148` edge `0.3492` maxDD `-3.0367`
- `news_risk_high->index_24h` score `3.7442` n `43` status `ready` deltaP `11.5351` edge `0.277` maxDD `-1.3507`
- `news_risk_high->fx_24h` score `3.4275` n `43` status `ready` deltaP `36.0142` edge `0.064` maxDD `-0.1442`
- `market_context_high->index_24h` score `3.3545` n `115` status `ready` deltaP `13.3349` edge `0.2424` maxDD `-1.4737`
- `news_risk_high->commodity_24h` score `3.0762` n `43` status `ready` deltaP `4.4614` edge `0.3083` maxDD `-3.202`
- `market_context_high->index_4h` score `2.2238` n `159` status `ready` deltaP `21.7192` edge `0.1231` maxDD `-2.2732`
- `news_risk_high->fx_4h` score `2.2196` n `43` status `ready` deltaP `28.1941` edge `0.0154` maxDD `-0.1382`
- `market_context_high->crypto_alt_1h` score `1.9455` n `159` status `ready` deltaP `12.6238` edge `0.1967` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `1.7429` n `159` status `ready` deltaP `12.9232` edge `0.1785` maxDD `-4.2199`
- `market_context_high->equity_4h` score `1.7229` n `159` status `ready` deltaP `16.0982` edge `0.1767` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
