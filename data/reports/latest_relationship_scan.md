# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T00:22:14.329787+00:00`
- Price records: `672`
- Market context records: `1066`
- Flow alert records: `4972`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8669`

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

- `market_context_high->crypto_major_24h` score `15.4338` n `171` status `ready` deltaP `34.4855` edge `1.1026` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `5.189` n `171` status `ready` deltaP `11.853` edge `0.4768` maxDD `-9.5387`
- `market_context_high->equity_24h` score `4.2315` n `171` status `ready` deltaP `12.7433` edge `0.3215` maxDD `-3.6396`
- `market_context_high->index_24h` score `3.6691` n `171` status `ready` deltaP `13.2495` edge `0.2524` maxDD `-2.1308`
- `market_context_high->metal_24h` score `3.2228` n `171` status `ready` deltaP `-4.818` edge `0.4674` maxDD `-6.3373`
- `market_context_high->equity_4h` score `0.5005` n `173` status `ready` deltaP `4.2797` edge `0.1058` maxDD `-4.41`
- `market_context_high->index_4h` score `0.043` n `173` status `ready` deltaP `2.8823` edge `0.0609` maxDD `-2.7889`
- `market_context_high->fx_1h` score `-0.0276` n `173` status `ready` deltaP `6.2442` edge `0.0004` maxDD `-0.3124`
- `market_context_high->crypto_major_1h` score `-0.1765` n `173` status `ready` deltaP `7.8701` edge `0.0252` maxDD `-5.3898`
- `market_context_high->index_1h` score `-0.2527` n `173` status `ready` deltaP `4.5645` edge `0.0157` maxDD `-2.0417`
- `market_context_high->equity_1h` score `-0.3409` n `173` status `ready` deltaP `1.034` edge `0.0333` maxDD `-3.8217`
- `market_context_high->fx_4h` score `-0.682` n `173` status `ready` deltaP `1.4706` edge `0.0024` maxDD `-1.6381`
- `market_context_high->metal_1h` score `-0.7552` n `173` status `ready` deltaP `5.4126` edge `-0.0213` maxDD `-3.5505`
- `market_context_high->crypto_major_4h` score `-0.8141` n `173` status `ready` deltaP `9.4679` edge `0.104` maxDD `-11.7968`
- `market_context_high->crypto_alt_1h` score `-0.8943` n `173` status `ready` deltaP `2.0941` edge `0.0201` maxDD `-5.3538`
- `market_context_high->commodity_1h` score `-1.0171` n `173` status `ready` deltaP `-1.362` edge `0.0051` maxDD `-3.7959`
- `market_context_high->crypto_alt_4h` score `-1.7548` n `173` status `ready` deltaP `3.18` edge `0.083` maxDD `-13.0347`
- `market_context_high->metal_4h` score `-2.3754` n `173` status `ready` deltaP `1.2107` edge `-0.1172` maxDD `-9.2991`
- `market_context_high->commodity_4h` score `-2.6713` n `173` status `ready` deltaP `-7.8167` edge `0.0264` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-3.0615` n `171` status `ready` deltaP `5.3592` edge `-0.0206` maxDD `-19.2774`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
