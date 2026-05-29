# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T22:07:21.666639+00:00`
- Price records: `672`
- Market context records: `2285`
- Flow alert records: `8472`
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

- `news_risk_high->crypto_alt_24h` score `20.4109` n `43` status `ready` deltaP `50.0363` edge `1.4262` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `15.4968` n `43` status `ready` deltaP `40.2091` edge `1.0673` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `13.5595` n `43` status `ready` deltaP `29.7925` edge `0.9628` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.2698` n `43` status `ready` deltaP `19.7674` edge `0.7821` maxDD `-3.3119`
- `market_context_high->crypto_alt_4h` score `7.8489` n `159` status `ready` deltaP `25.3758` edge `0.7528` maxDD `-15.4319`
- `market_context_high->unknown_24h` score `7.7291` n `115` status `ready` deltaP `25.8529` edge `0.5129` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `7.7062` n `159` status `ready` deltaP `29.8933` edge `0.6239` maxDD `-10.1468`
- `news_risk_high->unknown_24h` score `7.2926` n `43` status `ready` deltaP `29.8974` edge `0.431` maxDD `-1.4744`
- `market_context_high->unknown_4h` score `5.7562` n `159` status `ready` deltaP `22.6127` edge `0.3899` maxDD `-1.8773`
- `market_context_high->crypto_major_24h` score `4.9537` n `115` status `ready` deltaP `13.4783` edge `0.9345` maxDD `-25.1408`
- `news_risk_high->commodity_4h` score `3.8252` n `43` status `ready` deltaP `32.6148` edge `0.3401` maxDD `-3.0367`
- `news_risk_high->index_24h` score `3.6266` n `43` status `ready` deltaP `11.5351` edge `0.2672` maxDD `-1.3507`
- `news_risk_high->commodity_24h` score `3.567` n `43` status `ready` deltaP `4.4614` edge `0.3492` maxDD `-3.202`
- `news_risk_high->fx_24h` score `3.5516` n `43` status `ready` deltaP `37.0559` edge `0.0674` maxDD `-0.1442`
- `market_context_high->index_24h` score `3.2369` n `115` status `ready` deltaP `13.3349` edge `0.2326` maxDD `-1.4737`
- `market_context_high->index_4h` score `2.4361` n `159` status `ready` deltaP `23.5484` edge `0.1286` maxDD `-2.2732`
- `news_risk_high->fx_4h` score `2.1636` n `43` status `ready` deltaP `27.5843` edge `0.0148` maxDD `-0.1382`
- `market_context_high->crypto_alt_1h` score `2.1182` n `159` status `ready` deltaP `13.2226` edge `0.2071` maxDD `-6.1656`
- `market_context_high->equity_4h` score `2.0636` n `159` status `ready` deltaP `17.9274` edge `0.1929` maxDD `-5.9024`
- `market_context_high->crypto_major_1h` score `1.8916` n `159` status `ready` deltaP `13.6717` edge `0.1859` maxDD `-4.2199`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
