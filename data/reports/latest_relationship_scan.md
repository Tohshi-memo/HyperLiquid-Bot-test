# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-02T02:22:32.708684+00:00`
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

- `news_risk_high->unknown_24h` score `5188.8027` n `60` status `ready` deltaP `33.5413` edge `432.2187` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `18.6946` n `53` status `ready` deltaP `60.737` edge `1.1927` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `4.7901` n `68` status `ready` deltaP `17.1359` edge `0.3613` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.7331` n `68` status `ready` deltaP `16.6786` edge `0.0713` maxDD `-0.3783`
- `market_context_high->commodity_24h` score `1.7142` n `53` status `ready` deltaP `27.4844` edge `0.2224` maxDD `-10.2019`
- `market_context_high->crypto_alt_4h` score `0.7532` n `53` status `ready` deltaP `9.805` edge `0.1269` maxDD `-5.323`
- `news_risk_high->equity_1h` score `0.6804` n `68` status `ready` deltaP `9.9419` edge `0.0727` maxDD `-2.916`
- `market_context_high->fx_4h` score `0.2786` n `53` status `ready` deltaP `14.778` edge `0.0168` maxDD `-1.3685`
- `market_context_high->fx_24h` score `0.1481` n `53` status `ready` deltaP `10.5261` edge `0.0468` maxDD `-2.506`
- `news_risk_high->metal_4h` score `0.1211` n `68` status `ready` deltaP `5.165` edge `0.0287` maxDD `-0.8085`
- `news_risk_high->crypto_alt_1h` score `0.0578` n `68` status `ready` deltaP `6.0321` edge `0.0354` maxDD `-3.1233`
- `news_risk_high->fx_4h` score `0.0507` n `68` status `ready` deltaP `11.5316` edge `0.0231` maxDD `-0.6604`
- `market_context_high->commodity_1h` score `-0.0028` n `53` status `ready` deltaP `5.0757` edge `0.0199` maxDD `-1.3282`
- `market_context_high->fx_1h` score `-0.0029` n `53` status `ready` deltaP `7.3523` edge `0.001` maxDD `-0.6874`
- `news_risk_high->index_1h` score `-0.0637` n `68` status `ready` deltaP `2.4657` edge `0.0077` maxDD `-0.5845`
- `news_risk_high->fx_1h` score `-0.1035` n `68` status `ready` deltaP `2.2191` edge `0.0042` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1224` n `68` status `ready` deltaP `2.7651` edge `0.0062` maxDD `-0.5599`
- `market_context_high->commodity_4h` score `-0.2224` n `53` status `ready` deltaP `3.4198` edge `0.0362` maxDD `-3.0005`
- `news_risk_high->crypto_major_1h` score `-0.2568` n `68` status `ready` deltaP `1.6203` edge `0.0283` maxDD `-3.762`
- `news_risk_high->commodity_1h` score `-0.6358` n `68` status `ready` deltaP `3.7161` edge `-0.0283` maxDD `-2.9058`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
