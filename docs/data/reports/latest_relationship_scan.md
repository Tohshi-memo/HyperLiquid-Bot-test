# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T13:52:30.860364+00:00`
- Price records: `672`
- Market context records: `8202`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5904`

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

- `news_risk_high->unknown_24h` score `8264.0043` n `43` status `ready` deltaP `36.9792` edge `688.4205` maxDD `0.0`
- `market_context_high->equity_24h` score `22.3354` n `39` status `ready` deltaP `44.5513` edge `1.6553` maxDD `-4.9489`
- `market_context_high->equity_4h` score `10.039` n `40` status `ready` deltaP `46.5854` edge `0.5303` maxDD `-0.0094`
- `market_context_high->metal_24h` score `9.1152` n `39` status `ready` deltaP `46.875` edge `0.4471` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `8.106` n `39` status `ready` deltaP `20.4728` edge `1.05` maxDD `-6.1132`
- `news_risk_high->equity_4h` score `6.8465` n `54` status `ready` deltaP `25.0113` edge `0.4635` maxDD `-3.4427`
- `market_context_high->crypto_major_24h` score `6.1859` n `39` status `ready` deltaP `19.952` edge `0.9323` maxDD `-16.1129`
- `market_context_high->index_4h` score `4.1415` n `40` status `ready` deltaP `38.5366` edge `0.0925` maxDD `-0.0092`
- `market_context_high->metal_4h` score `3.9074` n `40` status `ready` deltaP `37.8659` edge `0.091` maxDD `-0.0926`
- `market_context_high->equity_1h` score `3.5065` n `40` status `ready` deltaP `18.2036` edge `0.1855` maxDD `-0.1718`
- `news_risk_high->equity_1h` score `3.0569` n `54` status `ready` deltaP `22.2777` edge `0.1371` maxDD `-1.1366`
- `market_context_high->index_24h` score `3.0018` n `39` status `ready` deltaP `27.9915` edge `0.2602` maxDD `-0.9576`
- `news_risk_high->crypto_major_4h` score `2.7202` n `54` status `ready` deltaP `13.8325` edge `0.3259` maxDD `-2.8833`
- `market_context_high->crypto_alt_4h` score `2.6434` n `40` status `ready` deltaP `9.5732` edge `0.2084` maxDD `-1.8218`
- `news_risk_high->index_4h` score `2.6191` n `54` status `ready` deltaP `21.9625` edge `0.0909` maxDD `-0.191`
- `news_risk_high->crypto_major_1h` score `2.0045` n `54` status `ready` deltaP `13.6006` edge `0.1161` maxDD `-1.1783`
- `market_context_high->fx_24h` score `1.8986` n `39` status `ready` deltaP `35.6304` edge `0.0707` maxDD `-0.5196`
- `news_risk_high->crypto_alt_1h` score `1.8794` n `54` status `ready` deltaP `15.153` edge `0.099` maxDD `-1.1388`
- `market_context_high->metal_1h` score `1.6585` n `40` status `ready` deltaP `18.503` edge `0.0323` maxDD `-0.0623`
- `market_context_high->crypto_major_4h` score `1.4773` n `40` status `ready` deltaP `12.0732` edge `0.2245` maxDD `-4.9134`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
