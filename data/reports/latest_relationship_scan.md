# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T15:52:32.987786+00:00`
- Price records: `672`
- Market context records: `8211`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5920`

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

- `news_risk_high->unknown_24h` score `8059.9263` n `43` status `ready` deltaP `36.9792` edge `671.414` maxDD `0.0`
- `market_context_high->equity_24h` score `21.1612` n `32` status `ready` deltaP `38.8889` edge `1.5952` maxDD `-4.9489`
- `market_context_high->crypto_major_24h` score `16.4231` n `32` status `ready` deltaP `32.2917` edge `1.2689` maxDD `-6.2467`
- `market_context_high->crypto_alt_24h` score `15.9044` n `32` status `ready` deltaP `32.8125` edge `1.1853` maxDD `-3.2944`
- `market_context_high->equity_4h` score `8.7942` n `32` status `ready` deltaP `47.1799` edge `0.4226` maxDD `-0.0094`
- `market_context_high->metal_24h` score `8.0711` n `32` status `ready` deltaP `45.1389` edge `0.3818` maxDD `-0.4771`
- `news_risk_high->equity_4h` score `7.3053` n `54` status `ready` deltaP `26.2308` edge `0.4936` maxDD `-3.4427`
- `market_context_high->crypto_major_4h` score `5.9178` n `32` status `ready` deltaP `25.686` edge `0.3569` maxDD `-1.1327`
- `market_context_high->index_24h` score `5.2624` n `32` status `ready` deltaP `33.1597` edge `0.2661` maxDD `-0.8902`
- `market_context_high->crypto_alt_4h` score `4.4525` n `32` status `ready` deltaP `19.8933` edge `0.267` maxDD `-0.6195`
- `market_context_high->index_4h` score `3.6729` n `32` status `ready` deltaP `37.1189` edge `0.0629` maxDD `-0.0092`
- `market_context_high->metal_4h` score `3.5816` n `32` status `ready` deltaP `35.5183` edge `0.0795` maxDD `-0.0926`
- `news_risk_high->equity_1h` score `3.1685` n `54` status `ready` deltaP `22.7268` edge `0.1434` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.6785` n `54` status `ready` deltaP `22.4198` edge `0.0928` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.6026` n `54` status `ready` deltaP `13.0703` edge `0.3159` maxDD `-2.8833`
- `market_context_high->fx_24h` score `2.3927` n `32` status `ready` deltaP `40.7986` edge `0.0768` maxDD `-0.363`
- `market_context_high->equity_1h` score `2.0688` n `32` status `ready` deltaP `11.1527` edge `0.1127` maxDD `-0.1718`
- `news_risk_high->crypto_major_1h` score `1.8894` n `54` status `ready` deltaP `13.1515` edge `0.1095` maxDD `-1.1783`
- `news_risk_high->crypto_alt_1h` score `1.8254` n `54` status `ready` deltaP `15.0033` edge `0.0955` maxDD `-1.1388`
- `news_risk_high->crypto_alt_4h` score `1.4157` n `54` status `ready` deltaP `17.2313` edge `0.2058` maxDD `-5.8012`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
