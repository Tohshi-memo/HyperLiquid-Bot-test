# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T04:07:27.560596+00:00`
- Price records: `672`
- Market context records: `3142`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8008`

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

- `market_context_high->commodity_24h` score `14.2898` n `108` status `ready` deltaP `47.5115` edge `0.9169` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `11.933` n `108` status `ready` deltaP `21.9328` edge `0.897` maxDD `-1.9039`
- `market_context_high->crypto_alt_24h` score `11.1969` n `108` status `ready` deltaP `11.4004` edge `2.3571` maxDD `-71.142`
- `market_context_high->index_24h` score `6.5344` n `108` status `ready` deltaP `31.0185` edge `0.8864` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.5361` n `108` status `ready` deltaP `11.9213` edge `1.3437` maxDD `-53.663`
- `market_context_high->commodity_4h` score `2.7868` n `145` status `ready` deltaP `18.0804` edge `0.1575` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `0.1534` n `146` status `ready` deltaP `4.1322` edge `0.0275` maxDD `-1.7142`
- `market_context_high->crypto_alt_1h` score `-0.3728` n `146` status `ready` deltaP `6.3551` edge `0.1228` maxDD `-14.7034`
- `market_context_high->fx_24h` score `-0.4234` n `108` status `ready` deltaP `5.787` edge `-0.0011` maxDD `-0.4876`
- `market_context_high->index_1h` score `-0.5249` n `146` status `ready` deltaP `3.4021` edge `0.0163` maxDD `-4.5023`
- `market_context_high->equity_1h` score `-0.8168` n `146` status `ready` deltaP `3.4882` edge `0.0206` maxDD `-8.8863`
- `market_context_high->crypto_major_1h` score `-0.95` n `146` status `ready` deltaP `3.5251` edge `0.081` maxDD `-15.1032`
- `market_context_high->index_4h` score `-1.122` n `145` status `ready` deltaP `12.069` edge `0.0666` maxDD `-17.6057`
- `market_context_high->fx_1h` score `-1.1275` n `146` status `ready` deltaP `-10.6185` edge `-0.0055` maxDD `-0.7941`
- `market_context_high->fx_4h` score `-1.5052` n `145` status `ready` deltaP `-14.385` edge `-0.0086` maxDD `-1.4115`
- `market_context_high->unknown_4h` score `-1.5914` n `145` status `ready` deltaP `5.7464` edge `0.0513` maxDD `-14.7778`
- `market_context_high->metal_1h` score `-2.0803` n `146` status `ready` deltaP `-4.4541` edge `-0.0043` maxDD `-7.4828`
- `market_context_high->equity_4h` score `-2.8104` n `145` status `ready` deltaP `13.6732` edge `0.0791` maxDD `-36.7784`
- `market_context_high->crypto_alt_4h` score `-2.8222` n `145` status `ready` deltaP `19.589` edge `0.4387` maxDD `-58.6918`
- `market_context_high->unknown_1h` score `-3.1669` n `146` status `ready` deltaP `1.6098` edge `-0.072` maxDD `-14.2111`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
