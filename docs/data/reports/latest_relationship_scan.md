# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T09:37:16.735823+00:00`
- Price records: `672`
- Market context records: `1618`
- Flow alert records: `6564`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8824`

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

- `market_context_high->metal_24h` score `11.1397` n `188` status `ready` deltaP `26.6327` edge `0.9446` maxDD `-9.8407`
- `market_context_high->index_24h` score `3.3317` n `188` status `ready` deltaP `18.787` edge `0.2777` maxDD `-5.3574`
- `market_context_high->equity_4h` score `1.3561` n `191` status `ready` deltaP `11.2294` edge `0.1476` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.3115` n `188` status `ready` deltaP `17.3537` edge `0.4095` maxDD `-28.2723`
- `market_context_high->crypto_major_24h` score `0.869` n `188` status `ready` deltaP `22.8021` edge `0.6195` maxDD `-50.5943`
- `market_context_high->crypto_alt_4h` score `0.4723` n `191` status `ready` deltaP `13.6557` edge `0.2963` maxDD `-19.4759`
- `market_context_high->crypto_major_4h` score `0.269` n `191` status `ready` deltaP `9.6859` edge `0.2408` maxDD `-13.3376`
- `market_context_high->crypto_alt_24h` score `-0.1089` n `188` status `ready` deltaP `22.9018` edge `0.8011` maxDD `-72.3614`
- `market_context_high->fx_24h` score `-0.2657` n `188` status `ready` deltaP `7.7201` edge `0.0313` maxDD `-1.3925`
- `market_context_high->crypto_alt_1h` score `-0.2859` n `192` status `ready` deltaP `0.5863` edge `0.0618` maxDD `-4.1892`
- `market_context_high->equity_1h` score `-0.4542` n `192` status `ready` deltaP `1.5906` edge `0.0324` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.6432` n `192` status `ready` deltaP `0.8359` edge `0.004` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.7912` n `192` status `ready` deltaP `0.0593` edge `-0.0031` maxDD `-0.3914`
- `market_context_high->index_4h` score `-0.8733` n `191` status `ready` deltaP `0.1684` edge `0.035` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `-0.9073` n `192` status `ready` deltaP `-1.4908` edge `0.0293` maxDD `-6.1883`
- `market_context_high->commodity_1h` score `-1.0596` n `192` status `ready` deltaP `0.3649` edge `0.0014` maxDD `-4.7041`
- `market_context_high->metal_1h` score `-1.2049` n `192` status `ready` deltaP `4.2259` edge `0.005` maxDD `-6.3532`
- `market_context_high->fx_4h` score `-1.3828` n `191` status `ready` deltaP `-10.5279` edge `-0.0142` maxDD `-1.4313`
- `market_context_high->metal_4h` score `-1.4337` n `191` status `ready` deltaP `8.5062` edge `0.093` maxDD `-12.5349`
- `market_context_high->commodity_4h` score `-5.2063` n `191` status `ready` deltaP `-14.1856` edge `-0.1102` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
