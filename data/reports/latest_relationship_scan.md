# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T07:37:15.545152+00:00`
- Price records: `672`
- Market context records: `990`
- Flow alert records: `4759`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1440`

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

- `market_context_high->crypto_major_24h` score `12.8094` n `211` status `ready` deltaP `31.3355` edge `0.9174` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.1204` n `211` status `ready` deltaP `10.7201` edge `0.3953` maxDD `-9.5387`
- `market_context_high->fx_1h` score `-0.3595` n `211` status `ready` deltaP `1.842` edge `-0.0003` maxDD `-0.3124`
- `market_context_high->commodity_1h` score `-0.4907` n `211` status `ready` deltaP `2.9236` edge `0.0204` maxDD `-3.7959`
- `market_context_high->equity_1h` score `-0.6656` n `211` status `ready` deltaP `0.8545` edge `0.0157` maxDD `-4.4826`
- `market_context_high->index_24h` score `-0.6981` n `211` status `ready` deltaP `2.9306` edge `0.1218` maxDD `-5.9609`
- `market_context_high->fx_4h` score `-0.7354` n `211` status `ready` deltaP `0.6848` edge `0.0008` maxDD `-1.6381`
- `market_context_high->index_1h` score `-0.7693` n `211` status `ready` deltaP `2.4962` edge `0.0046` maxDD `-2.8282`
- `market_context_high->equity_24h` score `-1.2085` n `211` status `ready` deltaP `4.4048` edge `0.1304` maxDD `-10.5047`
- `market_context_high->crypto_major_1h` score `-1.2241` n `211` status `ready` deltaP `4.6594` edge `-0.0157` maxDD `-11.4508`
- `market_context_high->equity_4h` score `-1.5312` n `211` status `ready` deltaP `1.6503` edge `0.0766` maxDD `-10.5498`
- `market_context_high->index_4h` score `-1.7631` n `211` status `ready` deltaP `-1.8688` edge `0.0178` maxDD `-6.5149`
- `market_context_high->metal_1h` score `-1.9066` n `211` status `ready` deltaP `-1.4416` edge `-0.0389` maxDD `-9.0076`
- `market_context_high->crypto_alt_1h` score `-2.0559` n `211` status `ready` deltaP `-0.7137` edge `-0.0226` maxDD `-8.1842`
- `market_context_high->crypto_major_4h` score `-2.953` n `211` status `ready` deltaP `6.9322` edge `0.0783` maxDD `-22.648`
- `market_context_high->commodity_4h` score `-3.3225` n `211` status `ready` deltaP `-2.2975` edge `0.0552` maxDD `-13.0076`
- `market_context_high->crypto_alt_4h` score `-3.3589` n `211` status `ready` deltaP `-2.2353` edge `0.0128` maxDD `-15.2248`
- `market_context_high->fx_24h` score `-3.5796` n `211` status `ready` deltaP `-1.3787` edge `-0.0218` maxDD `-20.2343`
- `market_context_high->metal_4h` score `-4.621` n `211` status `ready` deltaP `-5.0761` edge `-0.1629` maxDD `-24.9891`
- `market_context_high->commodity_24h` score `-8.321` n `211` status `ready` deltaP `2.4284` edge `0.3818` maxDD `-102.8492`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
