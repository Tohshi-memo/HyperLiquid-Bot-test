# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T13:37:25.984247+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13758`

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

- `market_context_high->equity_1h` score `0.2797` n `123` status `ready` deltaP `8.3248` edge `0.0493` maxDD `-3.1861`
- `market_context_high->index_1h` score `0.2562` n `123` status `ready` deltaP `11.404` edge `0.0057` maxDD `-0.5766`
- `market_context_high->fx_4h` score `0.2032` n `111` status `ready` deltaP `9.9306` edge `0.0101` maxDD `-0.3539`
- `market_context_high->fx_1h` score `-0.0735` n `123` status `ready` deltaP `3.2946` edge `0.0045` maxDD `-0.2043`
- `market_context_high->equity_4h` score `-0.1885` n `111` status `ready` deltaP `4.0692` edge `0.1201` maxDD `-8.3685`
- `market_context_high->index_4h` score `-0.3047` n `111` status `ready` deltaP `5.676` edge `0.0155` maxDD `-1.7252`
- `market_context_high->metal_1h` score `-0.406` n `123` status `ready` deltaP `1.4982` edge `-0.0042` maxDD `-0.503`
- `market_context_high->metal_4h` score `-0.4125` n `111` status `ready` deltaP `3.9442` edge `-0.0216` maxDD `-1.273`
- `market_context_high->commodity_24h` score `-0.4679` n `105` status `ready` deltaP `4.4147` edge `0.1149` maxDD `-4.666`
- `market_context_high->unknown_1h` score `-0.4716` n `123` status `ready` deltaP `10.0385` edge `-0.0835` maxDD `-0.4843`
- `market_context_high->commodity_4h` score `-0.6283` n `111` status `ready` deltaP `-0.9476` edge `0.0108` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.6408` n `123` status `ready` deltaP `-3.9993` edge `0.0011` maxDD `-1.1941`
- `market_context_high->crypto_alt_1h` score `-0.9543` n `123` status `ready` deltaP `-0.7448` edge `0.0056` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-1.4114` n `123` status `ready` deltaP `-3.1425` edge `-0.0575` maxDD `-4.1996`
- `market_context_high->crypto_alt_4h` score `-2.8039` n `111` status `ready` deltaP `-0.1153` edge `-0.1059` maxDD `-5.4926`
- `market_context_high->fx_24h` score `-3.0138` n `105` status `ready` deltaP `-12.4752` edge `-0.007` maxDD `-2.2121`
- `market_context_high->index_24h` score `-4.1759` n `105` status `ready` deltaP `-5.4217` edge `-0.049` maxDD `-18.6848`
- `market_context_high->crypto_major_4h` score `-4.359` n `111` status `ready` deltaP `-1.4186` edge `-0.2517` maxDD `-3.1677`
- `market_context_high->metal_24h` score `-4.4824` n `105` status `ready` deltaP `-16.7212` edge `-0.1324` maxDD `-11.4635`
- `market_context_high->unknown_24h` score `-5.0513` n `105` status `ready` deltaP `8.2937` edge `-0.4256` maxDD `-1.0505`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
