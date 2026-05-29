# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T18:52:23.901267+00:00`
- Price records: `672`
- Market context records: `2271`
- Flow alert records: `8432`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9287`

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

- `news_risk_high->crypto_alt_24h` score `21.2001` n `43` status `ready` deltaP `51.4252` edge `1.4827` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `15.7065` n `43` status `ready` deltaP `41.9452` edge `1.0732` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.241` n `43` status `ready` deltaP `31.8758` edge `1.0057` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `11.0521` n `43` status `ready` deltaP `21.8507` edge `0.8334` maxDD `-3.3119`
- `market_context_high->crypto_alt_4h` score `8.8841` n `153` status `ready` deltaP `27.711` edge `0.8235` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `8.5151` n `153` status `ready` deltaP `32.5492` edge `0.6736` maxDD `-10.1468`
- `market_context_high->unknown_24h` score `8.4977` n `115` status `ready` deltaP `28.1099` edge `0.5619` maxDD `-1.626`
- `news_risk_high->unknown_24h` score `8.0612` n `43` status `ready` deltaP `32.1544` edge `0.48` maxDD `-1.4744`
- `market_context_high->unknown_4h` score `5.5924` n `153` status `ready` deltaP `22.4404` edge `0.3774` maxDD `-1.8773`
- `market_context_high->crypto_major_24h` score `5.4622` n `115` status `ready` deltaP `15.5616` edge `0.9858` maxDD `-25.1408`
- `news_risk_high->index_24h` score `3.7771` n `43` status `ready` deltaP `12.5767` edge `0.2728` maxDD `-1.3507`
- `news_risk_high->commodity_4h` score `3.7632` n `43` status `ready` deltaP `32.1575` edge `0.3352` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.6159` n `43` status `ready` deltaP `37.2295` edge `0.0716` maxDD `-0.1442`
- `market_context_high->index_24h` score `3.3875` n `115` status `ready` deltaP `14.3765` edge `0.2382` maxDD `-1.4737`
- `news_risk_high->commodity_24h` score `3.2807` n `43` status `ready` deltaP `3.0725` edge `0.3346` maxDD `-3.202`
- `market_context_high->index_4h` score `2.618` n `153` status `ready` deltaP `24.3822` edge `0.1382` maxDD `-2.2732`
- `market_context_high->equity_4h` score `2.4853` n `153` status `ready` deltaP `18.9383` edge `0.2213` maxDD `-5.9024`
- `market_context_high->crypto_alt_1h` score `2.2885` n `159` status `ready` deltaP `13.6717` edge `0.2183` maxDD `-6.1656`
- `news_risk_high->fx_4h` score `2.0589` n `43` status `ready` deltaP `26.3648` edge `0.0142` maxDD `-0.1382`
- `market_context_high->crypto_major_1h` score `1.9648` n `159` status `ready` deltaP `13.6717` edge `0.192` maxDD `-4.2199`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
