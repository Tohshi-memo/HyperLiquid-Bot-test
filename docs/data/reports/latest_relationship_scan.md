# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-02T04:07:31.322493+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5932`

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

- `news_risk_high->unknown_24h` score `5188.8226` n `60` status `ready` deltaP `33.7146` edge `432.2192` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `18.9215` n `53` status `ready` deltaP `61.0836` edge `1.2093` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `4.6591` n `68` status `ready` deltaP `16.9835` edge `0.3514` maxDD `-3.4427`
- `market_context_high->commodity_24h` score `1.7758` n `53` status `ready` deltaP `27.4844` edge `0.2303` maxDD `-10.2019`
- `news_risk_high->index_4h` score `1.6921` n `68` status `ready` deltaP `16.5261` edge `0.0689` maxDD `-0.3783`
- `market_context_high->crypto_alt_4h` score `0.7048` n `53` status `ready` deltaP `9.805` edge `0.1207` maxDD `-5.323`
- `news_risk_high->equity_1h` score `0.6911` n `68` status `ready` deltaP `10.391` edge `0.0706` maxDD `-2.916`
- `market_context_high->fx_4h` score `0.3165` n `53` status `ready` deltaP `15.3877` edge `0.0176` maxDD `-1.3685`
- `market_context_high->fx_24h` score `0.2322` n `53` status `ready` deltaP `11.7393` edge `0.0495` maxDD `-2.506`
- `news_risk_high->metal_4h` score `0.111` n `68` status `ready` deltaP `5.165` edge `0.0274` maxDD `-0.8085`
- `news_risk_high->fx_4h` score `0.109` n `68` status `ready` deltaP `12.1413` edge `0.0239` maxDD `-0.6604`
- `news_risk_high->crypto_alt_1h` score `0.0741` n `68` status `ready` deltaP `6.3315` edge `0.0355` maxDD `-3.1233`
- `market_context_high->fx_1h` score `0.051` n `53` status `ready` deltaP `7.9511` edge `0.0015` maxDD `-0.6874`
- `market_context_high->commodity_1h` score `0.0167` n `53` status `ready` deltaP `4.926` edge `0.0234` maxDD `-1.3282`
- `news_risk_high->fx_1h` score `-0.0684` n `68` status `ready` deltaP `2.8179` edge `0.0047` maxDD `-0.2475`
- `news_risk_high->index_1h` score `-0.0692` n `68` status `ready` deltaP `2.4657` edge `0.007` maxDD `-0.5845`
- `market_context_high->commodity_4h` score `-0.1215` n `53` status `ready` deltaP `3.7247` edge `0.0471` maxDD `-3.0005`
- `news_risk_high->metal_1h` score `-0.1427` n `68` status `ready` deltaP `2.4657` edge `0.0056` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.2693` n `68` status `ready` deltaP `1.6203` edge `0.0267` maxDD `-3.762`
- `news_risk_high->commodity_1h` score `-0.6163` n `68` status `ready` deltaP `3.5664` edge `-0.0248` maxDD `-2.9058`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
