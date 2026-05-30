# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T00:52:23.693016+00:00`
- Price records: `672`
- Market context records: `2298`
- Flow alert records: `8506`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9289`

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

- `news_risk_high->crypto_alt_24h` score `20.5837` n `43` status `ready` deltaP `50.0363` edge `1.4406` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `15.5971` n `43` status `ready` deltaP `40.3827` edge `1.0745` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `13.5667` n `43` status `ready` deltaP `29.7925` edge `0.9634` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.3574` n `43` status `ready` deltaP `19.7674` edge `0.7894` maxDD `-3.3119`
- `market_context_high->crypto_alt_4h` score `7.6191` n `159` status `ready` deltaP `24.9185` edge `0.7367` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `7.6005` n `159` status `ready` deltaP `29.7409` edge `0.6161` maxDD `-10.1468`
- `market_context_high->unknown_24h` score `7.3569` n `115` status `ready` deltaP `24.2904` edge `0.4923` maxDD `-1.626`
- `news_risk_high->unknown_24h` score `6.9204` n `43` status `ready` deltaP `28.3349` edge `0.4104` maxDD `-1.4744`
- `market_context_high->unknown_4h` score `5.6274` n `159` status `ready` deltaP `22.3079` edge `0.3812` maxDD `-1.8773`
- `market_context_high->crypto_major_24h` score `5.0107` n `115` status `ready` deltaP `13.4783` edge `0.9418` maxDD `-25.1408`
- `news_risk_high->commodity_4h` score `3.886` n `43` status `ready` deltaP `32.6148` edge `0.3479` maxDD `-3.0367`
- `news_risk_high->index_24h` score `3.7094` n `43` status `ready` deltaP `11.5351` edge `0.2741` maxDD `-1.3507`
- `news_risk_high->fx_24h` score `3.4311` n `43` status `ready` deltaP `36.0142` edge `0.0643` maxDD `-0.1442`
- `market_context_high->index_24h` score `3.3197` n `115` status `ready` deltaP `13.3349` edge `0.2395` maxDD `-1.4737`
- `news_risk_high->commodity_24h` score `3.2838` n `43` status `ready` deltaP `4.4614` edge `0.3256` maxDD `-3.202`
- `market_context_high->index_4h` score `2.2735` n `159` status `ready` deltaP `22.1765` edge `0.1242` maxDD `-2.2732`
- `news_risk_high->fx_4h` score `2.2318` n `43` status `ready` deltaP `28.3465` edge `0.0154` maxDD `-0.1382`
- `market_context_high->crypto_alt_1h` score `2.0798` n `159` status `ready` deltaP `13.2226` edge `0.2039` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `1.8496` n `159` status `ready` deltaP `13.522` edge `0.1834` maxDD `-4.2199`
- `market_context_high->equity_4h` score `1.8185` n `159` status `ready` deltaP `16.7079` edge `0.1806` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
