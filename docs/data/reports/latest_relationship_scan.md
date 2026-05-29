# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T20:37:19.127935+00:00`
- Price records: `672`
- Market context records: `2278`
- Flow alert records: `8453`
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

- `news_risk_high->crypto_alt_24h` score `20.6127` n `43` status `ready` deltaP `50.3835` edge `1.4407` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `15.5517` n `43` status `ready` deltaP `40.73` edge `1.0684` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `13.8234` n `43` status `ready` deltaP `30.6605` edge `0.979` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.5169` n `43` status `ready` deltaP `20.6355` edge `0.7969` maxDD `-3.3119`
- `market_context_high->unknown_24h` score `8.0213` n `115` status `ready` deltaP `26.8946` edge `0.5303` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `7.9281` n `159` status `ready` deltaP `25.3758` edge `0.7594` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `7.7326` n `159` status `ready` deltaP `29.8933` edge `0.6261` maxDD `-10.1468`
- `news_risk_high->unknown_24h` score `7.5848` n `43` status `ready` deltaP `30.9391` edge `0.4484` maxDD `-1.4744`
- `market_context_high->unknown_4h` score `5.5331` n `159` status `ready` deltaP `21.6981` edge `0.3774` maxDD `-1.8773`
- `market_context_high->crypto_major_24h` score `5.1143` n `115` status `ready` deltaP `14.3464` edge `0.9493` maxDD `-25.1408`
- `news_risk_high->commodity_4h` score `3.8002` n `43` status `ready` deltaP `32.6148` edge `0.3369` maxDD `-3.0367`
- `news_risk_high->index_24h` score `3.6947` n `43` status `ready` deltaP `12.0559` edge `0.2694` maxDD `-1.3507`
- `news_risk_high->fx_24h` score `3.5871` n `43` status `ready` deltaP `37.2295` edge `0.0692` maxDD `-0.1442`
- `news_risk_high->commodity_24h` score `3.4876` n `43` status `ready` deltaP `4.1142` edge `0.3449` maxDD `-3.202`
- `market_context_high->index_24h` score `3.305` n `115` status `ready` deltaP `13.8557` edge `0.2348` maxDD `-1.4737`
- `market_context_high->index_4h` score `2.5099` n `159` status `ready` deltaP `24.0058` edge `0.1317` maxDD `-2.2732`
- `market_context_high->crypto_alt_1h` score `2.2729` n `159` status `ready` deltaP `13.522` edge `0.218` maxDD `-6.1656`
- `market_context_high->equity_4h` score `2.206` n `159` status `ready` deltaP `18.5372` edge `0.2007` maxDD `-5.9024`
- `news_risk_high->fx_4h` score `2.0868` n `43` status `ready` deltaP `26.6697` edge `0.0145` maxDD `-0.1382`
- `market_context_high->crypto_major_1h` score `1.9588` n `159` status `ready` deltaP `13.6717` edge `0.1915` maxDD `-4.2199`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
