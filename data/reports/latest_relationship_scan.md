# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T14:07:34.493959+00:00`
- Price records: `672`
- Market context records: `6823`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11700`

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

- `market_context_high->unknown_24h` score `0.8874` n `176` status `ready` deltaP `-1.5467` edge `0.4993` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `0.298` n `176` status `ready` deltaP `10.7481` edge `0.14` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.1684` n `203` status `ready` deltaP `6.2933` edge `0.03` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.2999` n `203` status `ready` deltaP `3.8738` edge `0.0256` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.3685` n `203` status `ready` deltaP `0.1593` edge `0.0002` maxDD `-0.5468`
- `market_context_high->index_1h` score `-0.782` n `203` status `ready` deltaP `-3.2646` edge `-0.0037` maxDD `-0.9833`
- `market_context_high->metal_1h` score `-0.9221` n `203` status `ready` deltaP `-5.4962` edge `-0.0077` maxDD `-1.9098`
- `market_context_high->commodity_1h` score `-1.0886` n `203` status `ready` deltaP `-2.3856` edge `-0.0065` maxDD `-2.1314`
- `market_context_high->fx_4h` score `-1.2811` n `192` status `ready` deltaP `6.5295` edge `-0.0014` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.4415` n `192` status `ready` deltaP `-3.379` edge `-0.0133` maxDD `-5.5853`
- `market_context_high->index_4h` score `-1.6651` n `192` status `ready` deltaP `1.9944` edge `-0.0264` maxDD `-6.6968`
- `market_context_high->unknown_1h` score `-1.6724` n `203` status `ready` deltaP `-4.7041` edge `-0.0179` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.6864` n `203` status `ready` deltaP `0.5944` edge `-0.029` maxDD `-4.9061`
- `market_context_high->metal_4h` score `-2.7189` n `192` status `ready` deltaP `-3.6839` edge `-0.0257` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-3.0498` n `192` status `ready` deltaP `0.0635` edge `-0.0587` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.2215` n `192` status `ready` deltaP `-0.2795` edge `-0.0528` maxDD `-20.6678`
- `market_context_high->unknown_4h` score `-3.3523` n `192` status `ready` deltaP `-11.8649` edge `0.0363` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.4564` n `176` status `ready` deltaP `-9.7853` edge `-0.0025` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-5.0027` n `192` status `ready` deltaP `-0.4954` edge `-0.1709` maxDD `-30.3733`
- `market_context_high->metal_24h` score `-9.5738` n `176` status `ready` deltaP `-21.4489` edge `-0.2359` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
