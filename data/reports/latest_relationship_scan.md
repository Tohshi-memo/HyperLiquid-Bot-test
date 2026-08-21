# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T23:37:26.851062+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14774`

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

- `market_context_high->unknown_1h` score `1.417` n `133` status `ready` deltaP `9.286` edge `0.0789` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.4446` n `133` status `ready` deltaP `22.6148` edge `-0.0698` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.1668` n `133` status `ready` deltaP `9.277` edge `0.0098` maxDD `-0.3539`
- `market_context_high->index_1h` score `0.1592` n `133` status `ready` deltaP `10.3068` edge `0.0048` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.0864` n `133` status `ready` deltaP `3.0773` edge `0.0043` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.2163` n `133` status `ready` deltaP `6.5643` edge `0.0355` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.309` n `133` status `ready` deltaP `1.1312` edge `-0.0053` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.3554` n `133` status `ready` deltaP `5.4041` edge `-0.02` maxDD `-1.5942`
- `market_context_high->index_4h` score `-0.6006` n `133` status `ready` deltaP `2.4689` edge `0.0101` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.6059` n `133` status `ready` deltaP `-0.2464` edge `0.009` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.6674` n `133` status `ready` deltaP `-4.4212` edge `0.0005` maxDD `-1.1941`
- `market_context_high->crypto_alt_1h` score `-0.7976` n `133` status `ready` deltaP `0.5696` edge `0.0099` maxDD `-2.413`
- `market_context_high->commodity_24h` score `-1.1453` n `105` status `ready` deltaP `-1.4881` edge `0.0978` maxDD `-4.666`
- `market_context_high->crypto_major_1h` score `-1.3559` n `133` status `ready` deltaP `-1.4002` edge `-0.062` maxDD `-4.1996`
- `market_context_high->crypto_alt_4h` score `-1.6284` n `133` status `ready` deltaP `3.8981` edge `-0.0347` maxDD `-5.4926`
- `market_context_high->equity_4h` score `-1.8366` n `133` status `ready` deltaP `-1.9726` edge `0.0582` maxDD `-16.1079`
- `market_context_high->fx_24h` score `-2.3539` n `105` status `ready` deltaP `-5.5308` edge `0.0017` maxDD `-2.2121`
- `market_context_high->index_24h` score `-4.3749` n `105` status `ready` deltaP `-8.1994` edge `-0.056` maxDD `-18.6848`
- `market_context_high->crypto_major_4h` score `-4.4415` n `133` status `ready` deltaP `-0.1249` edge `-0.2672` maxDD `-3.1677`
- `market_context_high->metal_24h` score `-4.8785` n `105` status `ready` deltaP `-18.4574` edge `-0.1716` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
