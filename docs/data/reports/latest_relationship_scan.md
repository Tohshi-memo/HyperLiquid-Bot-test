# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T17:22:18.908929+00:00`
- Price records: `672`
- Market context records: `2478`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9248`

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

- `market_context_high->unknown_24h` score `5.1621` n `122` status `ready` deltaP `19.7547` edge `0.3313` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `4.2039` n `136` status `ready` deltaP `21.198` edge `0.4769` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.9553` n `136` status `ready` deltaP `18.4809` edge `0.3874` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `1.9119` n `122` status `ready` deltaP `10.8863` edge `0.5618` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `1.5879` n `136` status `ready` deltaP `10.1507` edge `0.1667` maxDD `-3.4972`
- `market_context_high->crypto_major_1h` score `0.4877` n `141` status `ready` deltaP `7.4787` edge `0.1102` maxDD `-4.2199`
- `market_context_high->crypto_alt_1h` score `0.3376` n `141` status `ready` deltaP `5.8001` edge `0.1082` maxDD `-6.1656`
- `market_context_high->index_24h` score `-0.0152` n `122` status `ready` deltaP `3.9019` edge `0.0708` maxDD `-2.5127`
- `market_context_high->index_4h` score `-0.2103` n `136` status `ready` deltaP `5.4878` edge `0.0206` maxDD `-2.3986`
- `market_context_high->equity_24h` score `-0.2145` n `122` status `ready` deltaP `18.1837` edge `0.0136` maxDD `-6.8828`
- `market_context_high->crypto_alt_24h` score `-0.3332` n `122` status `ready` deltaP `0.6944` edge `0.6484` maxDD `-43.6595`
- `market_context_high->fx_1h` score `-0.35` n `141` status `ready` deltaP `0.6147` edge `0.0045` maxDD `-0.278`
- `market_context_high->unknown_1h` score `-0.3577` n `141` status `ready` deltaP `2.1829` edge `0.0276` maxDD `-3.0902`
- `market_context_high->metal_1h` score `-0.4706` n `141` status `ready` deltaP `1.2921` edge `0.007` maxDD `-3.0759`
- `market_context_high->fx_4h` score `-0.6374` n `136` status `ready` deltaP `-0.6367` edge `0.0085` maxDD `-0.8774`
- `market_context_high->commodity_1h` score `-0.6479` n `141` status `ready` deltaP `1.135` edge `-0.0028` maxDD `-4.3601`
- `market_context_high->index_1h` score `-0.664` n `141` status `ready` deltaP `-1.1891` edge `0.002` maxDD `-1.2855`
- `market_context_high->fx_24h` score `-0.8702` n `122` status `ready` deltaP `3.4438` edge `0.004` maxDD `-2.7484`
- `market_context_high->metal_4h` score `-0.9234` n `136` status `ready` deltaP `3.4343` edge `0.0389` maxDD `-4.7664`
- `market_context_high->equity_1h` score `-0.9457` n `141` status `ready` deltaP `-1.1328` edge `0.0126` maxDD `-2.7085`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
