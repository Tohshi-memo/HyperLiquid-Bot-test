# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T10:22:26.239828+00:00`
- Price records: `672`
- Market context records: `6488`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5869`

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

- `news_risk_high->crypto_alt_24h` score `12.7118` n `32` status `ready` deltaP `34.375` edge `0.8449` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.4866` n `32` status `ready` deltaP `53.9931` edge `0.1806` maxDD `0.0`
- `market_context_high->unknown_24h` score `6.311` n `159` status `ready` deltaP `15.5169` edge `0.7525` maxDD `-15.0689`
- `news_risk_high->crypto_major_24h` score `4.4842` n `32` status `ready` deltaP `17.7083` edge `0.5348` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `3.9532` n `38` status `ready` deltaP `42.0652` edge `0.0536` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `2.9539` n `32` status `ready` deltaP `28.125` edge `0.0792` maxDD `-0.3101`
- `market_context_high->unknown_1h` score `2.8914` n `180` status `ready` deltaP `-3.8922` edge `0.357` maxDD `-3.2083`
- `news_risk_high->fx_1h` score `1.855` n `38` status `ready` deltaP `23.2115` edge `0.0179` maxDD `-0.1113`
- `market_context_high->index_4h` score `0.6224` n `168` status `ready` deltaP `13.5453` edge `0.0292` maxDD `-0.4108`
- `news_risk_high->crypto_major_1h` score `0.5886` n `38` status `ready` deltaP `5.2001` edge `0.0945` maxDD `-2.6299`
- `market_context_high->unknown_4h` score `0.5664` n `168` status `ready` deltaP `-15.2003` edge `0.3891` maxDD `-10.5788`
- `market_context_high->commodity_24h` score `0.5526` n `159` status `ready` deltaP `7.9009` edge `0.1802` maxDD `-5.2791`
- `market_context_high->crypto_alt_4h` score `0.4475` n `168` status `ready` deltaP `9.8795` edge `0.1268` maxDD `-6.7632`
- `news_risk_high->crypto_alt_1h` score `0.0921` n `38` status `ready` deltaP `1.7334` edge `0.0512` maxDD `-2.0756`
- `market_context_high->metal_4h` score `0.0851` n `168` status `ready` deltaP `11.3966` edge `0.0441` maxDD `-2.7056`
- `market_context_high->equity_4h` score `-0.4502` n `168` status `ready` deltaP `8.4857` edge `0.0556` maxDD `-8.2573`
- `news_risk_high->index_24h` score `-0.4509` n `32` status `ready` deltaP `4.6875` edge `-0.0019` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.5538` n `180` status `ready` deltaP `0.835` edge `0.0012` maxDD `-1.8877`
- `market_context_high->crypto_alt_1h` score `-0.5626` n `180` status `ready` deltaP `6.324` edge `0.017` maxDD `-5.8368`
- `market_context_high->commodity_1h` score `-0.5895` n `180` status `ready` deltaP `-0.6853` edge `-0.0027` maxDD `-2.1314`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
