# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T12:52:27.200328+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14754`

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

- `market_context_high->unknown_1h` score `0.9656` n `145` status `ready` deltaP `7.1981` edge `0.0552` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.2097` n `138` status `ready` deltaP `18.434` edge `-0.0615` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.0985` n `138` status `ready` deltaP `7.9335` edge `0.01` maxDD `-0.3539`
- `market_context_high->index_1h` score `0.0163` n `145` status `ready` deltaP `7.5728` edge `0.0047` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.0069` n `145` status `ready` deltaP `4.5148` edge `0.0049` maxDD `-0.2043`
- `market_context_high->metal_4h` score `-0.2621` n `138` status `ready` deltaP `6.7935` edge `-0.0173` maxDD `-1.5942`
- `market_context_high->metal_1h` score `-0.3304` n `145` status `ready` deltaP `0.6762` edge `-0.005` maxDD `-0.6822`
- `market_context_high->equity_1h` score `-0.3554` n `145` status `ready` deltaP `4.3382` edge `0.0325` maxDD `-5.2257`
- `market_context_high->index_4h` score `-0.4927` n `138` status `ready` deltaP `4.3478` edge `0.0114` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.7381` n `138` status `ready` deltaP `-1.9353` edge `0.0033` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.9231` n `145` status `ready` deltaP `-7.1185` edge `-0.0018` maxDD `-1.1941`
- `market_context_high->equity_4h` score `-1.7131` n `138` status `ready` deltaP `-1.2173` edge `0.069` maxDD `-16.1079`
- `market_context_high->fx_24h` score `-1.7859` n `124` status `ready` deltaP `0.4145` edge `0.0094` maxDD `-2.2121`
- `market_context_high->crypto_alt_4h` score `-1.8471` n `138` status `ready` deltaP `4.6262` edge `-0.056` maxDD `-5.6346`
- `market_context_high->commodity_24h` score `-2.042` n `124` status `ready` deltaP `-5.7068` edge `0.0512` maxDD `-4.666`
- `market_context_high->crypto_alt_1h` score `-2.4116` n `145` status `ready` deltaP `-2.3983` edge `-0.0355` maxDD `-7.9582`
- `market_context_high->crypto_major_1h` score `-3.445` n `145` status `ready` deltaP `-4.7718` edge `-0.1094` maxDD `-7.6697`
- `market_context_high->index_24h` score `-4.5085` n `124` status `ready` deltaP `-8.5238` edge `-0.045` maxDD `-20.7621`
- `market_context_high->crypto_major_4h` score `-5.4637` n `138` status `ready` deltaP `-0.866` edge `-0.3199` maxDD `-5.3711`
- `market_context_high->metal_24h` score `-5.464` n `124` status `ready` deltaP `-24.692` edge `-0.2051` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
