# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T13:07:11.064593+00:00`
- Price records: `648`
- Market context records: `758`
- Flow alert records: `2137`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1117`

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

- `market_context_high->crypto_major_24h` score `13.3598` n `146` status `ready` deltaP `31.817` edge `0.9346` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.7474` n `146` status `ready` deltaP `7.4673` edge `0.5173` maxDD `-0.0508`
- `risk_on_high->metal_1h` score `1.2564` n `31` status `ready` deltaP `14.446` edge `0.0314` maxDD `-0.5074`
- `risk_on_and_context->metal_1h` score `1.2564` n `31` status `ready` deltaP `14.446` edge `0.0314` maxDD `-0.5074`
- `risk_on_high->fx_1h` score `0.8239` n `31` status `ready` deltaP `12.4294` edge `0.0043` maxDD `-0.147`
- `risk_on_and_context->fx_1h` score `0.8239` n `31` status `ready` deltaP `12.4294` edge `0.0043` maxDD `-0.147`
- `market_context_high->index_24h` score `0.5606` n `146` status `ready` deltaP `3.3047` edge `0.2242` maxDD `-5.9609`
- `risk_on_high->crypto_major_1h` score `0.5368` n `31` status `ready` deltaP `8.8058` edge `0.0101` maxDD `-0.5923`
- `risk_on_and_context->crypto_major_1h` score `0.5368` n `31` status `ready` deltaP `8.8058` edge `0.0101` maxDD `-0.5923`
- `risk_on_high->commodity_1h` score `0.1307` n `31` status `ready` deltaP `5.3629` edge `0.0186` maxDD `-0.6739`
- `risk_on_and_context->commodity_1h` score `0.1307` n `31` status `ready` deltaP `5.3629` edge `0.0186` maxDD `-0.6739`
- `market_context_high->equity_24h` score `0.0077` n `146` status `ready` deltaP `1.8024` edge `0.2491` maxDD `-10.5047`
- `risk_on_high->crypto_alt_1h` score `0.0071` n `31` status `ready` deltaP `5.6652` edge `-0.0119` maxDD `-0.6637`
- `risk_on_and_context->crypto_alt_1h` score `0.0071` n `31` status `ready` deltaP `5.6652` edge `-0.0119` maxDD `-0.6637`
- `market_context_high->fx_1h` score `-0.4462` n `174` status `ready` deltaP `2.7335` edge `0.0024` maxDD `-0.291`
- `market_context_high->fx_4h` score `-0.4625` n `162` status `ready` deltaP `5.8956` edge `0.0093` maxDD `-1.6381`
- `risk_on_high->index_1h` score `-0.4676` n `31` status `ready` deltaP `-2.7167` edge `0.0075` maxDD `-0.2687`
- `risk_on_and_context->index_1h` score `-0.4676` n `31` status `ready` deltaP `-2.7167` edge `0.0075` maxDD `-0.2687`
- `market_context_high->commodity_1h` score `-0.5985` n `174` status `ready` deltaP `1.4511` edge `0.0379` maxDD `-3.7959`
- `market_context_high->equity_1h` score `-0.6773` n `174` status `ready` deltaP `-1.0057` edge `0.0009` maxDD `-4.4826`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
