# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T13:37:26.724397+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11685`

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

- `risk_on_high->crypto_alt_24h` score `17.3782` n `61` status `ready` deltaP `41.0519` edge `1.3452` maxDD `-10.9887`
- `risk_on_and_context->crypto_alt_24h` score `17.3782` n `61` status `ready` deltaP `41.0519` edge `1.3452` maxDD `-10.9887`
- `risk_on_high->unknown_4h` score `8.1336` n `107` status `ready` deltaP `25.4032` edge `0.5701` maxDD `-2.266`
- `risk_on_and_context->unknown_4h` score `8.1336` n `107` status `ready` deltaP `25.4032` edge `0.5701` maxDD `-2.266`
- `market_context_high->unknown_4h` score `6.5876` n `159` status `ready` deltaP `22.0998` edge `0.471` maxDD `-2.5493`
- `risk_on_high->fx_24h` score `5.4214` n `61` status `ready` deltaP `65.3375` edge `0.0494` maxDD `-0.6561`
- `risk_on_and_context->fx_24h` score `5.4214` n `61` status `ready` deltaP `65.3375` edge `0.0494` maxDD `-0.6561`
- `risk_on_high->crypto_major_24h` score `4.4312` n `61` status `ready` deltaP `25.8538` edge `0.6888` maxDD `-19.1107`
- `risk_on_and_context->crypto_major_24h` score `4.4312` n `61` status `ready` deltaP `25.8538` edge `0.6888` maxDD `-19.1107`
- `market_context_high->metal_24h` score `3.986` n `103` status `ready` deltaP `31.7017` edge `0.2203` maxDD `-2.625`
- `market_context_high->crypto_alt_24h` score `3.8049` n `103` status `ready` deltaP `20.1861` edge `0.7722` maxDD `-27.517`
- `market_context_high->crypto_major_24h` score `3.3706` n `103` status `ready` deltaP `20.0445` edge `0.4587` maxDD `-20.2494`
- `risk_on_high->unknown_1h` score `2.4214` n `107` status `ready` deltaP `6.6652` edge `0.215` maxDD `-1.9453`
- `risk_on_and_context->unknown_1h` score `2.4214` n `107` status `ready` deltaP `6.6652` edge `0.215` maxDD `-1.9453`
- `market_context_high->unknown_1h` score `2.1988` n `159` status `ready` deltaP `6.0069` edge `0.2062` maxDD `-2.041`
- `risk_on_high->metal_24h` score `1.805` n `61` status `ready` deltaP `32.3542` edge `0.1098` maxDD `-2.527`
- `risk_on_and_context->metal_24h` score `1.805` n `61` status `ready` deltaP `32.3542` edge `0.1098` maxDD `-2.527`
- `news_risk_high->unknown_1h` score `1.5179` n `61` status `ready` deltaP `3.7695` edge `0.136` maxDD `-1.1043`
- `market_context_high->fx_24h` score `1.0426` n `103` status `ready` deltaP `37.3095` edge `0.0308` maxDD `-1.6688`
- `news_risk_high->commodity_24h` score `0.6342` n `44` status `ready` deltaP `7.7336` edge `0.0613` maxDD `-1.1904`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
