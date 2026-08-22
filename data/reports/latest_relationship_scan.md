# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T09:22:26.879666+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14748`

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

- `market_context_high->unknown_1h` score `1.1922` n `136` status `ready` deltaP `7.331` edge `0.0732` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.4627` n `133` status `ready` deltaP `19.8709` edge `-0.05` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.0955` n `133` status `ready` deltaP `7.9051` edge `0.0098` maxDD `-0.3539`
- `market_context_high->index_1h` score `0.0807` n `136` status `ready` deltaP `8.7971` edge `0.0048` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.1292` n `136` status `ready` deltaP `2.1927` edge `0.0047` maxDD `-0.2043`
- `market_context_high->metal_4h` score `-0.2305` n `133` status `ready` deltaP `7.3858` edge `-0.0172` maxDD `-1.5942`
- `market_context_high->equity_1h` score `-0.241` n `136` status `ready` deltaP `5.9528` edge `0.0364` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.2633` n `136` status `ready` deltaP `1.9065` edge `-0.0046` maxDD `-0.6822`
- `market_context_high->index_4h` score `-0.6284` n `133` status `ready` deltaP `1.8591` edge `0.0106` maxDD `-2.618`
- `market_context_high->commodity_1h` score `-0.6815` n `136` status `ready` deltaP `-4.4514` edge `-0.0011` maxDD `-1.1941`
- `market_context_high->commodity_4h` score `-0.7107` n `133` status `ready` deltaP `-1.6184` edge `0.0047` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-1.3597` n `136` status `ready` deltaP `-1.0567` edge `-0.0094` maxDD `-3.7493`
- `market_context_high->commodity_24h` score `-1.568` n `110` status `ready` deltaP `-4.356` edge `0.0817` maxDD `-4.666`
- `market_context_high->crypto_alt_4h` score `-1.7039` n `133` status `ready` deltaP `4.9652` edge `-0.0481` maxDD `-5.4926`
- `market_context_high->equity_4h` score `-1.73` n `133` status `ready` deltaP `-1.3628` edge `0.0678` maxDD `-16.1079`
- `market_context_high->fx_24h` score `-2.3378` n `110` status `ready` deltaP `-5.5398` edge `0.0031` maxDD `-2.2121`
- `market_context_high->crypto_major_1h` score `-2.5283` n `136` status `ready` deltaP `-3.3594` edge `-0.0858` maxDD `-4.1996`
- `market_context_high->index_24h` score `-4.2506` n `110` status `ready` deltaP `-5.7197` edge `-0.0509` maxDD `-19.1405`
- `market_context_high->metal_24h` score `-5.18` n `110` status `ready` deltaP `-21.2721` edge `-0.1915` maxDD `-11.4635`
- `market_context_high->crypto_major_4h` score `-5.2273` n `133` status `ready` deltaP `-1.8017` edge `-0.3215` maxDD `-3.1677`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
