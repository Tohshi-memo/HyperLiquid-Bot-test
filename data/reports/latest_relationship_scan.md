# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T07:52:30.931090+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9100`

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

- `market_context_high->unknown_4h` score `18.5564` n `124` status `ready` deltaP `-2.9553` edge `1.5996` maxDD `-1.016`
- `market_context_high->metal_24h` score `0.6076` n `113` status `ready` deltaP `28.4445` edge `0.1553` maxDD `-7.3625`
- `market_context_high->fx_24h` score `0.1726` n `113` status `ready` deltaP `22.2237` edge `0.0312` maxDD `-1.2451`
- `market_context_high->fx_4h` score `0.0404` n `124` status `ready` deltaP `8.2367` edge `0.0083` maxDD `-0.4545`
- `market_context_high->fx_1h` score `-0.0332` n `134` status `ready` deltaP `4.4798` edge `0.0017` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.3663` n `134` status `ready` deltaP `1.1909` edge `0.0116` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.3819` n `134` status `ready` deltaP `4.7882` edge `-0.0017` maxDD `-1.6682`
- `market_context_high->commodity_4h` score `-0.4969` n `124` status `ready` deltaP `2.1587` edge `0.0448` maxDD `-1.165`
- `market_context_high->index_24h` score `-0.6056` n `113` status `ready` deltaP `10.7824` edge `-0.0213` maxDD `-4.925`
- `market_context_high->index_1h` score `-0.6412` n `134` status `ready` deltaP `-1.7875` edge `-0.0051` maxDD `-1.2155`
- `market_context_high->metal_4h` score `-1.2893` n `124` status `ready` deltaP `3.4372` edge `-0.0172` maxDD `-5.3474`
- `market_context_high->crypto_major_1h` score `-1.4103` n `134` status `ready` deltaP `1.0457` edge `-0.0297` maxDD `-9.3126`
- `market_context_high->index_4h` score `-2.2475` n `124` status `ready` deltaP `-9.7217` edge `-0.0359` maxDD `-4.3282`
- `market_context_high->equity_1h` score `-2.4305` n `134` status `ready` deltaP `-1.3339` edge `-0.0741` maxDD `-12.2891`
- `market_context_high->crypto_alt_1h` score `-3.9019` n `134` status `ready` deltaP `-2.8198` edge `-0.0579` maxDD `-13.2099`
- `market_context_high->crypto_major_24h` score `-4.8855` n `113` status `ready` deltaP `-2.4198` edge `-0.1245` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-6.1812` n `124` status `ready` deltaP `-9.4168` edge `-0.2257` maxDD `-32.9851`
- `market_context_high->commodity_24h` score `-6.5485` n `113` status `ready` deltaP `-18.9927` edge `-0.154` maxDD `-24.0477`
- `market_context_high->equity_24h` score `-7.1258` n `113` status `ready` deltaP `-5.0747` edge `-0.3222` maxDD `-36.6024`
- `market_context_high->equity_4h` score `-8.8726` n `124` status `ready` deltaP `-8.2415` edge `-0.3564` maxDD `-45.7601`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
