# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T01:07:26.974362+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11618`

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

- `market_context_high->crypto_major_24h` score `2.3914` n `91` status `ready` deltaP `7.9461` edge `0.2671` maxDD `-4.9964`
- `market_context_high->equity_4h` score `1.5344` n `96` status `ready` deltaP `8.8668` edge `0.1576` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.5072` n `96` status `ready` deltaP `12.4564` edge `0.0727` maxDD `-0.4112`
- `market_context_high->commodity_24h` score `1.4459` n `91` status `ready` deltaP `16.8594` edge `0.2563` maxDD `-4.666`
- `market_context_high->metal_4h` score `1.1964` n `96` status `ready` deltaP `17.937` edge `0.0377` maxDD `-1.273`
- `market_context_high->crypto_major_4h` score `0.9389` n `96` status `ready` deltaP `11.001` edge `0.107` maxDD `-3.1677`
- `market_context_high->index_1h` score `0.7893` n `96` status `ready` deltaP `14.2652` edge `0.0094` maxDD `-0.0982`
- `market_context_high->crypto_alt_4h` score `0.5129` n `96` status `ready` deltaP `11.5854` edge `0.0925` maxDD `-5.4926`
- `market_context_high->unknown_1h` score `0.3595` n `96` status `ready` deltaP `9.3563` edge `-0.0097` maxDD `-0.4843`
- `market_context_high->unknown_24h` score `0.2574` n `91` status `ready` deltaP `16.039` edge `-0.0641` maxDD `-0.3771`
- `market_context_high->metal_1h` score `0.1069` n `96` status `ready` deltaP `5.5202` edge `0.0108` maxDD `-0.4291`
- `market_context_high->fx_4h` score `-0.0896` n `96` status `ready` deltaP `5.6656` edge `0.001` maxDD `-0.3539`
- `market_context_high->index_4h` score `-0.1498` n `96` status `ready` deltaP `5.0559` edge `0.0193` maxDD `-0.5728`
- `market_context_high->crypto_alt_1h` score `-0.3621` n `96` status `ready` deltaP `2.8256` edge `0.0149` maxDD `-2.413`
- `market_context_high->fx_1h` score `-0.4063` n `96` status `ready` deltaP `-2.6697` edge `0.0016` maxDD `-0.2043`
- `market_context_high->crypto_major_1h` score `-0.4359` n `96` status `ready` deltaP `1.9336` edge `0.0157` maxDD `-2.7581`
- `market_context_high->commodity_4h` score `-0.4565` n `96` status `ready` deltaP `2.5661` edge `0.0094` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.897` n `96` status `ready` deltaP `-7.8905` edge `-0.0058` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-1.6515` n `91` status `ready` deltaP `-1.7666` edge `0.0771` maxDD `-8.831`
- `market_context_high->fx_24h` score `-4.0451` n `91` status `ready` deltaP `-24.2617` edge `-0.0254` maxDD `-1.3293`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
